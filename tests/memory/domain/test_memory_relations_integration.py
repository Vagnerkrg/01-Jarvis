from datetime import datetime

from copilot.memory.domain.memory import Memory
from copilot.memory.domain.memory_confidence import MemoryConfidence
from copilot.memory.domain.memory_importance import MemoryImportance
from copilot.memory.domain.memory_metadata import MemoryMetadata
from copilot.memory.domain.memory_relation import MemoryRelation
from copilot.memory.domain.memory_source import MemorySource
from copilot.memory.domain.memory_type import MemoryType


def test_memory_accepts_typed_relations():
    timestamp = datetime.now()

    metadata = MemoryMetadata(
        type=MemoryType.ENGINEERING,
        created_at=timestamp,
        updated_at=timestamp,
        source=MemorySource.ENGINEERING_DECISION,
        importance=MemoryImportance.HIGH,
        confidence=MemoryConfidence.HIGH,
        tags=["architecture"],
    )

    memory = Memory(
        memory_id="mem_001",
        content="Runtime deve ser independente de modelos.",
        context="Architecture Decision",
        metadata=metadata,
        relations=[MemoryRelation.SUPPORTS],
    )

    assert memory.relations == [MemoryRelation.SUPPORTS]