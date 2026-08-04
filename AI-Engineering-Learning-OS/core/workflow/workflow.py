"""
Workflow Orchestration

Responsible for organizing and executing
sequential task flows.
"""


class WorkflowStep:
    """
    Represents a single workflow step.
    """

    def __init__(self, name: str):
        self.name = name
        self.status = "pending"

    def execute(self):
        """
        Execute workflow step.
        """

        self.status = "completed"

        return {
            "step": self.name,
            "status": self.status,
        }


class Workflow:
    """
    Basic sequential workflow engine.
    """

    def __init__(self, name: str):
        self.name = name
        self.steps = []

    def add_step(self, name: str):
        """
        Add a new execution step.
        """

        step = WorkflowStep(name)

        self.steps.append(step)

        return step

    def execute(self):
        """
        Execute all steps sequentially.
        """

        results = []

        for step in self.steps:
            results.append(
                step.execute()
            )

        return {
            "workflow": self.name,
            "steps": results,
            "status": "completed",
        }