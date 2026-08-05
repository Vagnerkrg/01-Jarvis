import requests

from ..interfaces import AIProvider


class OllamaProvider(AIProvider):
    """
    Provider de integração com o Ollama Runtime.

    Responsável por enviar prompts para modelos
    executados localmente pelo Ollama.
    """

    def __init__(
        self,
        model: str = "llama3.1:8b",
        base_url: str = "http://localhost:11434"
    ):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str) -> str:
        """
        Envia um prompt para o modelo Ollama.

        Args:
            prompt:
                Texto enviado ao modelo.

        Returns:
            Resposta gerada pelo modelo.
        """

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["response"]