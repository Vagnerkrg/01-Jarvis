from dataclasses import dataclass
from datetime import datetime

from copilot.memory.domain.memory_confidence import MemoryConfidence
from copilot.memory.domain.memory_importance import MemoryImportance
from copilot.memory.domain.memory_source import MemorySource
from copilot.memory.domain.memory_type import MemoryType


@dataclass
class MemoryMetadata:
    type: MemoryType
    created_at: datetime
    updated_at: datetime
    source: MemorySource
    importance: MemoryImportance
    confidence: MemoryConfidence
    tags: list[str]