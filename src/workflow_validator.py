"""Workflow Validator for Multi-Agent Orchestration.

This module provides validation utilities for agent outputs and workflow tracking
in a multi-agent system. It validates TaskSpec, DesignSpec, and ImplementationPlan
artifacts produced by different agents.
"""

from typing import Any, Dict, List, Optional
from enum import Enum


class WorkflowStep(Enum):
    """Workflow step enumeration."""
    ANALYZER = "analyzer"
    ARCHITECT = "architect"
    PROGRAMMER = "programmer"
    GIT_WORKER = "git_worker"


class WorkflowValidator:
    """Validates agent outputs and tracks workflow progress."""

    def __init__(self):
        """Initialize the workflow validator."""
        self.workflow_status: Dict[str, bool] = {
            step.value: False for step in WorkflowStep
        }
        self.validation_errors: List[str] = []

    def validate_task_spec(self, task_spec: Dict[str, Any]) -> bool:
        """Validate TaskSpec JSON from Analyzer agent.

        Args:
            task_spec: TaskSpec dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ["task_id", "description", "acceptance_criteria"]

        if not isinstance(task_spec, dict):
            self.validation_errors.append("TaskSpec must be a dictionary")
            return False

        for field in required_fields:
            if field not in task_spec:
                self.validation_errors.append(f"Missing required field: {field}")
                return False

        self.workflow_status[WorkflowStep.ANALYZER.value] = True
        return True

    def validate_design_spec(self, design_spec: Dict[str, Any]) -> bool:
        """Validate DesignSpec from Architect agent.

        Args:
            design_spec: DesignSpec dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ["component_changes", "data_flow"]

        if not isinstance(design_spec, dict):
            self.validation_errors.append("DesignSpec must be a dictionary")
            return False

        for field in required_fields:
            if field not in design_spec:
                self.validation_errors.append(f"Missing required field: {field}")
                return False

        self.workflow_status[WorkflowStep.ARCHITECT.value] = True
        return True

    def validate_implementation_plan(self, impl_plan: Dict[str, Any]) -> bool:
        """Validate ImplementationPlan from Architect agent.

        Args:
            impl_plan: ImplementationPlan dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ["files_to_change", "diffs_summary"]

        if not isinstance(impl_plan, dict):
            self.validation_errors.append("ImplementationPlan must be a dictionary")
            return False

        for field in required_fields:
            if field not in impl_plan:
                self.validation_errors.append(f"Missing required field: {field}")
                return False

        return True

    def mark_step_complete(self, step: WorkflowStep) -> None:
        """Mark a workflow step as complete.

        Args:
            step: The workflow step to mark complete
        """
        self.workflow_status[step.value] = True

    def get_workflow_status(self) -> Dict[str, bool]:
        """Get current workflow status.

        Returns:
            Dictionary mapping workflow steps to completion status
        """
        return self.workflow_status.copy()

    def get_validation_errors(self) -> List[str]:
        """Get accumulated validation errors.

        Returns:
            List of validation error messages
        """
        return self.validation_errors.copy()

    def reset(self) -> None:
        """Reset workflow status and clear validation errors."""
        self.workflow_status = {
            step.value: False for step in WorkflowStep
        }
        self.validation_errors = []
