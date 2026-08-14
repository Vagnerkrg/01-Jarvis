import pytest

from copilot.memory.domain.memory_type import MemoryType


def test_memory_type_contains_official_categories():
    assert MemoryType.SHORT_TERM.value == "short_term"
    assert MemoryType.WORKING.value == "working"
    assert MemoryType.LONG_TERM.value == "long_term"
    assert MemoryType.SEMANTIC.value == "semantic"
    assert MemoryType.EPISODIC.value == "episodic"
    assert MemoryType.ENGINEERING.value == "engineering"


def test_memory_type_rejects_unknown_category():
    with pytest.raises(ValueError):
        MemoryType("unknown")