import pytest

from copilot.memory.domain.memory_relation import MemoryRelation


def test_memory_relation_contains_official_types():
    assert MemoryRelation.DERIVED_FROM.value == "derived_from"
    assert MemoryRelation.SUPPORTS.value == "supports"
    assert MemoryRelation.CONTRADICTS.value == "contradicts"
    assert MemoryRelation.UPDATES.value == "updates"
    assert MemoryRelation.REFERENCES.value == "references"


def test_memory_relation_rejects_unknown_type():
    with pytest.raises(ValueError):
        MemoryRelation("unknown")