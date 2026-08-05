from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Interface base para provedores de modelos de IA.

    Todo provider deve implementar esta interface.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Executa uma chamada ao modelo de IA.

        Args:
            prompt:
                Texto enviado ao modelo.

        Returns:
            Resposta gerada pelo modelo.
        """
        pass