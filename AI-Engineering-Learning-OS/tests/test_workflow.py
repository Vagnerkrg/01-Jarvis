from core.workflow import Workflow, WorkflowStep


def test_create_workflow_step():

    step = WorkflowStep(
        "Collect data"
    )

    assert step.name == "Collect data"
    assert step.status == "pending"


def test_execute_step():

    step = WorkflowStep(
        "Process data"
    )

    result = step.execute()

    assert result["status"] == "completed"
    assert step.status == "completed"


def test_workflow_execution():

    workflow = Workflow(
        "Data Analysis"
    )

    workflow.add_step(
        "Collect data"
    )

    workflow.add_step(
        "Generate report"
    )

    result = workflow.execute()

    assert result["workflow"] == "Data Analysis"
    assert len(result["steps"]) == 2
    assert result["status"] == "completed"