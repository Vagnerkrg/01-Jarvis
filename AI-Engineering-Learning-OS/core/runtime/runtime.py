"""
Agent Execution Runtime

Controls the lifecycle of agent executions.
"""

from .context import AgentContext


class AgentRuntime:
    """
    Basic execution runtime for Jarvis agents.
    """

    def create_context(self, task: str) -> AgentContext:
        """
        Create a new execution context.
        """
        return AgentContext(task=task)

    def execute(self, context: AgentContext):
        """
        Execute agent lifecycle.
        """

        context.start()

        # Future:
        # Agent invocation happens here.

        context.complete(
            result=f"Task completed: {context.task}"
        )

        return context