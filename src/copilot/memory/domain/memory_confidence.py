from enum import Enum


class MemoryConfidence(str, Enum):
    """
    Níveis oficiais de confiança de uma memória.
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"