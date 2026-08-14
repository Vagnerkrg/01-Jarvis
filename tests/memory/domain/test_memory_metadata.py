from datetime import datetime

from copilot.memory.domain.memory_confidence import MemoryConfidence
from copilot.memory.domain.memory_importance import MemoryImportance
from copilot.memory.domain.memory_metadata import MemoryMetadata
from copilot.memory.domain.memory_source import MemorySource
from copilot.memory.domain.memory_type import MemoryType


def test_memory_metadata_creation():
    created_at = datetime.now()

    metadata = MemoryMetadata(
        type=MemoryType.ENGINEERING,
        created_at=created_at,
        updated_at=created_at,
        source=MemorySource.ENGINEERING_DECISION,
        importance=MemoryImportance.HIGH,
        confidence=MemoryConfidence.HIGH,
        tags=["architecture", "runtime"],
    )

    assert metadata.type == MemoryType.ENGINEERING
    assert metadata.created_at == created_at
    assert metadata.updated_at == created_at
    assert metadata.source == MemorySource.ENGINEERING_DECISION
    assert metadata.importance == MemoryImportance.HIGH
    assert metadata.confidence == MemoryConfidence.HIGH
    assert metadata.tags == ["architecture", "runtime"]