from enum import Enum


class MemorySource(Enum):
    USER_INPUT = "user_input"
    AGENT_DECISION = "agent_decision"
    SYSTEM_EVENT = "system_event"
    ENGINEERING_DECISION = "engineering_decision"
    EXTERNAL_KNOWLEDGE = "external_knowledge"