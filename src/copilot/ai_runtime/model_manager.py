from .interfaces import AIProvider


class ModelManager:
    """
    Gerenciador central de modelos de IA.

    Responsável por abstrair a comunicação
    entre a aplicação e os providers.
    """

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        """
        Envia uma solicitação para o provider ativo.
        """

        return self.provider.generate(prompt)