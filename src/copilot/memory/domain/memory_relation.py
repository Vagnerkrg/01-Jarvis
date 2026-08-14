from enum import Enum


class MemoryRelation(str, Enum):
    """
    Tipos oficiais de relacionamento entre memórias.
    """

    DERIVED_FROM = "derived_from"
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    UPDATES = "updates"
    REFERENCES = "references"