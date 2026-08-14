from dataclasses import dataclass, field

from copilot.memory.domain.memory_metadata import MemoryMetadata
from copilot.memory.domain.memory_relation import MemoryRelation


@dataclass
class Memory:
    """
    Representa uma unidade estruturada de memória do sistema.

    Uma Memory registra uma informação que pode ser reutilizada
    durante futuras execuções do AI Engineering Learning OS.
    """

    memory_id: str
    content: str
    context: str
    metadata: MemoryMetadata
    relations: list[MemoryRelation] = field(default_factory=list)