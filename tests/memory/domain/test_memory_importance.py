import pytest

from copilot.memory.domain.memory_importance import MemoryImportance


def test_memory_importance_contains_official_levels():
    assert MemoryImportance.LOW.value == "low"
    assert MemoryImportance.MEDIUM.value == "medium"
    assert MemoryImportance.HIGH.value == "high"
    assert MemoryImportance.CRITICAL.value == "critical"


def test_memory_importance_rejects_unknown_level():
    with pytest.raises(ValueError):
        MemoryImportance("unknown")