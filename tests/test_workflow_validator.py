"""Unit tests for WorkflowValidator class."""

import pytest
from src.workflow_validator import WorkflowValidator, WorkflowStep


class TestWorkflowValidator:
    """Test suite for WorkflowValidator."""

    def test_validate_task_spec_valid(self):
        """Test that a properly formatted TaskSpec JSON passes validation."""
        validator = WorkflowValidator()
        task_spec = {
            "task_id": "25686114",
            "description": "Validate multi-agent workflow",
            "acceptance_criteria": [
                "Analyzer creates TaskSpec",
                "Architect produces implementation plan"
            ]
        }

        result = validator.validate_task_spec(task_spec)

        assert result is True
        assert validator.get_workflow_status()[WorkflowStep.ANALYZER.value] is True
        assert len(validator.get_validation_errors()) == 0

    def test_validate_task_spec_missing_fields(self):
        """Test that TaskSpec with missing fields fails validation."""
        validator = WorkflowValidator()
        task_spec = {
            "task_id": "25686114",
            "description": "Incomplete task spec"
            # Missing acceptance_criteria
        }

        result = validator.validate_task_spec(task_spec)

        assert result is False
        assert "Missing required field: acceptance_criteria" in validator.get_validation_errors()

    def test_validate_design_spec_valid(self):
        """Test that a properly formatted design spec passes validation."""
        validator = WorkflowValidator()
        design_spec = {
            "component_changes": [
                {
                    "component_name": "src/workflow_validator.py",
                    "change_type": "new"
                }
            ],
            "data_flow": "Analyzer -> Architect -> Programmer"
        }

        result = validator.validate_design_spec(design_spec)

        assert result is True
        assert validator.get_workflow_status()[WorkflowStep.ARCHITECT.value] is True

    def test_validate_design_spec_invalid(self):
        """Test that invalid design spec fails validation."""
        validator = WorkflowValidator()
        design_spec = {
            "component_changes": []
            # Missing data_flow
        }

        result = validator.validate_design_spec(design_spec)

        assert result is False
        assert "Missing required field: data_flow" in validator.get_validation_errors()

    def test_workflow_status_tracking(self):
        """Test that workflow status is properly tracked through multiple steps."""
        validator = WorkflowValidator()

        # Initially all steps should be False
        status = validator.get_workflow_status()
        assert all(not completed for completed in status.values())

        # Mark steps complete
        validator.mark_step_complete(WorkflowStep.ANALYZER)
        validator.mark_step_complete(WorkflowStep.ARCHITECT)

        status = validator.get_workflow_status()
        assert status[WorkflowStep.ANALYZER.value] is True
        assert status[WorkflowStep.ARCHITECT.value] is True
        assert status[WorkflowStep.PROGRAMMER.value] is False
        assert status[WorkflowStep.GIT_WORKER.value] is False

    def test_validate_invalid_inputs(self):
        """Test that invalid or malformed inputs are properly rejected."""
        validator = WorkflowValidator()

        # Test with non-dict input
        result = validator.validate_task_spec("not a dict")
        assert result is False
        assert "TaskSpec must be a dictionary" in validator.get_validation_errors()

        validator.reset()

        # Test with None
        result = validator.validate_design_spec(None)
        assert result is False
        assert "DesignSpec must be a dictionary" in validator.get_validation_errors()

    def test_validate_implementation_plan_valid(self):
        """Test that a valid implementation plan passes validation."""
        validator = WorkflowValidator()
        impl_plan = {
            "files_to_change": [
                {
                    "file_path": "src/workflow_validator.py",
                    "change_type": "new"
                }
            ],
            "diffs_summary": "Create workflow validator module"
        }

        result = validator.validate_implementation_plan(impl_plan)

        assert result is True

    def test_reset_workflow(self):
        """Test that reset clears workflow status and errors."""
        validator = WorkflowValidator()

        # Add some status and errors
        validator.mark_step_complete(WorkflowStep.ANALYZER)
        validator.validation_errors.append("test error")

        # Reset
        validator.reset()

        status = validator.get_workflow_status()
        assert all(not completed for completed in status.values())
        assert len(validator.get_validation_errors()) == 0
