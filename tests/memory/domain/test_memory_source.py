from copilot.memory.domain.memory_source import MemorySource


def test_memory_source_values():
    assert MemorySource.USER_INPUT.value == "user_input"
    assert MemorySource.AGENT_DECISION.value == "agent_decision"
    assert MemorySource.SYSTEM_EVENT.value == "system_event"
    assert MemorySource.ENGINEERING_DECISION.value == "engineering_decision"
    assert MemorySource.EXTERNAL_KNOWLEDGE.value == "external_knowledge"