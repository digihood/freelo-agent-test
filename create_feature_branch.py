#!/usr/bin/env python3
"""
GitHub REST API script to create a feature branch.
Creates a new branch from main using the GitHub REST API.
"""

import os
import sys
import json
import requests
from typing import Optional

# Configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "digihood"
REPO_NAME = "freelo-agent-test"
BASE_BRANCH = "main"


def get_base_branch_sha(owner: str, repo: str, branch: str = "main") -> Optional[str]:
    """
    Get the SHA of the base branch (main).

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name (default: main)

    Returns:
        SHA of the branch or None if error
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/git/refs/heads/{branch}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["object"]["sha"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching base branch SHA: {e}")
        return None


def create_feature_branch(owner: str, repo: str, branch_name: str, base_sha: str) -> bool:
    """
    Create a new feature branch using the GitHub REST API.

    Args:
        owner: Repository owner
        repo: Repository name
        branch_name: Name of the feature branch to create
        base_sha: SHA of the commit to base the branch on

    Returns:
        True if successful, False otherwise
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/git/refs"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "ref": f"refs/heads/{branch_name}",
        "sha": base_sha
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"✓ Feature branch created successfully!")
        print(f"  Branch: {data['ref']}")
        print(f"  URL: {data['url']}")
        return True
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 422:
            print(f"✗ Error: Branch '{branch_name}' already exists")
        else:
            print(f"✗ HTTP Error {e.response.status_code}: {e.response.text}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Error creating feature branch: {e}")
        return False


def main():
    """Main entry point."""
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set")
        sys.exit(1)

    # Get feature branch name from command line or use default
    branch_name = sys.argv[1] if len(sys.argv) > 1 else "feature/test-branch"

    print(f"Creating feature branch '{branch_name}' from '{BASE_BRANCH}'...")
    print()

    # Get the SHA of the base branch
    print(f"Fetching SHA of base branch '{BASE_BRANCH}'...")
    base_sha = get_base_branch_sha(REPO_OWNER, REPO_NAME, BASE_BRANCH)

    if not base_sha:
        print("Failed to fetch base branch SHA")
        sys.exit(1)

    print(f"Base branch SHA: {base_sha}")
    print()

    # Create the feature branch
    print(f"Creating feature branch from base SHA...")
    success = create_feature_branch(REPO_OWNER, REPO_NAME, branch_name, base_sha)

    if success:
        print()
        print(f"Next steps:")
        print(f"  git fetch origin")
        print(f"  git checkout {branch_name}")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
