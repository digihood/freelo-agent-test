#!/bin/bash
# GitHub REST API script to create a feature branch
# This script creates a new branch from main using the GitHub REST API

set -e

# Configuration
GITHUB_TOKEN="${GITHUB_TOKEN}"
REPO_OWNER="digihood"
REPO_NAME="freelo-agent-test"
BASE_BRANCH="main"
FEATURE_BRANCH="${1:-feature/test-branch}"

# Validate GITHUB_TOKEN
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GITHUB_TOKEN environment variable not set"
    exit 1
fi

echo "Creating feature branch '$FEATURE_BRANCH' from '$BASE_BRANCH'..."
echo

# Fetch the SHA of the base branch
echo "Fetching SHA of base branch '$BASE_BRANCH'..."
BASE_SHA=$(curl -s \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -H "Accept: application/vnd.github+json" \
    "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/git/refs/heads/$BASE_BRANCH" \
    | grep -o '"sha":"[^"]*' | cut -d'"' -f4)

if [ -z "$BASE_SHA" ]; then
    echo "Error: Failed to fetch base branch SHA"
    exit 1
fi

echo "Base branch SHA: $BASE_SHA"
echo

# Create the feature branch
echo "Creating feature branch from base SHA..."
RESPONSE=$(curl -s -X POST \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -H "Accept: application/vnd.github+json" \
    -d "{\"ref\":\"refs/heads/$FEATURE_BRANCH\",\"sha\":\"$BASE_SHA\"}" \
    "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/git/refs")

# Check if the request was successful
if echo "$RESPONSE" | grep -q '"ref":"refs/heads'; then
    echo "✓ Feature branch created successfully!"
    echo "$RESPONSE" | grep -o '"ref":"[^"]*' | head -1
    echo
    echo "Next steps:"
    echo "  git fetch origin"
    echo "  git checkout $FEATURE_BRANCH"
    exit 0
else
    echo "✗ Error creating feature branch:"
    echo "$RESPONSE" | grep -o '"message":"[^"]*' || echo "$RESPONSE"
    exit 1
fi
