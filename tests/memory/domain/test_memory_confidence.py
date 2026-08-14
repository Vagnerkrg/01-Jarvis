import pytest

from copilot.memory.domain.memory_confidence import MemoryConfidence


def test_memory_confidence_contains_official_levels():
    assert MemoryConfidence.HIGH.value == "high"
    assert MemoryConfidence.MEDIUM.value == "medium"
    assert MemoryConfidence.LOW.value == "low"


def test_memory_confidence_rejects_unknown_level():
    with pytest.raises(ValueError):
        MemoryConfidence("unknown")