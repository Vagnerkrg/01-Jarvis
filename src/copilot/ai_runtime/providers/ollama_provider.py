"""
Provider responsável pela comunicação com o Ollama.

Encapsula toda a comunicação HTTP entre o Copilot
e o runtime Ollama.
"""

import requests

from requests.exceptions import (
    ConnectionError,
    HTTPError,
    RequestException,
    Timeout,
)

from ..exceptions import (
    ProviderConnectionError,
    ProviderResponseError,
    ProviderTimeoutError,
)
from ..interfaces import AIProvider


class OllamaProvider(AIProvider):
    """
    Provider responsável pela comunicação
    com o runtime Ollama.
    """

    def __init__(
        self,
        model: str = "llama3.1:8b",
        base_url: str = "http://localhost:11434",
        timeout: int = 120,
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def generate(self, prompt: str) -> str:
        """
        Envia um prompt para o Ollama.

        Args:
            prompt:
                Texto enviado ao modelo.

        Returns:
            Resposta gerada pelo modelo.

        Raises:
            ProviderConnectionError:
                Quando não for possível conectar ao Ollama.

            ProviderTimeoutError:
                Quando a requisição exceder o tempo limite.

            ProviderResponseError:
                Quando a resposta do Ollama for inválida.
        """

        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=self.timeout,
            )

            response.raise_for_status()

            data = response.json()

            if "response" not in data:
                raise ProviderResponseError(
                    "Resposta inválida recebida do Ollama."
                )

            return data["response"]

        except ConnectionError as exc:
            raise ProviderConnectionError(
                "Não foi possível conectar ao Ollama."
            ) from exc

        except Timeout as exc:
            raise ProviderTimeoutError(
                "Tempo limite excedido durante a comunicação com o Ollama."
            ) from exc

        except HTTPError as exc:
            raise ProviderResponseError(
                f"O Ollama retornou erro HTTP: {exc}"
            ) from exc

        except RequestException as exc:
            raise ProviderResponseError(
                "Erro inesperado durante a comunicação com o Ollama."
            ) from exc

        except ValueError as exc:
            raise ProviderResponseError(
                "O Ollama retornou uma resposta JSON inválida."
            ) from exc