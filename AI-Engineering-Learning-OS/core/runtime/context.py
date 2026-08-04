"""
Agent Execution Context

Stores information about an agent execution lifecycle.
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class AgentContext:
    """
    Represents the execution context of an agent task.
    """

    task: str
    session_id: str = field(default_factory=lambda: str(uuid4()))
    status: str = "created"
    created_at: datetime = field(default_factory=datetime.now)
    result: str | None = None

    def start(self):
        """Start execution."""
        self.status = "running"

    def complete(self, result: str):
        """Complete execution with result."""
        self.status = "completed"
        self.result = result