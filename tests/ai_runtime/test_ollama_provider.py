from unittest.mock import Mock, patch

from copilot.ai_runtime.providers.ollama_provider import OllamaProvider


def test_ollama_provider_initialization():
    """
    Valida a criação do provider com configurações padrão.
    """

    provider = OllamaProvider()

    assert provider.model == "llama3.1:8b"
    assert provider.base_url == "http://localhost:11434"


@patch("copilot.ai_runtime.providers.ollama_provider.requests.post")
def test_ollama_provider_generate(mock_post):
    """
    Valida o envio de prompt para o Ollama.
    """

    mock_response = Mock()

    mock_response.json.return_value = {
        "response": "Resposta simulada do Ollama"
    }

    mock_response.raise_for_status.return_value = None

    mock_post.return_value = mock_response

    provider = OllamaProvider()

    result = provider.generate(
        "Explique sua função."
    )

    assert result == "Resposta simulada do Ollama"

    mock_post.assert_called_once()