"""
Planning Engine

Responsible for creating and organizing execution plans.
"""

from dataclasses import dataclass, field


@dataclass
class Plan:
    """
    Represents a structured execution plan.
    """

    goal: str
    steps: list[str] = field(default_factory=list)

    def add_step(self, step: str):
        """
        Add a new step to the plan.
        """
        self.steps.append(step)


class Planner:
    """
    Basic planning engine for Jarvis.
    """

    def create_plan(self, goal: str) -> Plan:
        """
        Create an initial plan from a goal.
        """

        return Plan(
            goal=goal
        )

    def add_task(self, plan: Plan, task: str):
        """
        Add a task to an existing plan.
        """

        plan.add_step(task)

        return plan