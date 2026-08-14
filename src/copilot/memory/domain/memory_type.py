from enum import Enum


class MemoryType(str, Enum):
    """
    Categorias oficiais de memória definidas pelo Memory System.
    """

    SHORT_TERM = "short_term"
    WORKING = "working"
    LONG_TERM = "long_term"
    SEMANTIC = "semantic"
    EPISODIC = "episodic"
    ENGINEERING = "engineering"