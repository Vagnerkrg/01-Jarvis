from enum import Enum


class MemoryImportance(str, Enum):
    """
    Níveis oficiais de importância de uma memória.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"