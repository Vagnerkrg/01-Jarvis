from unittest.mock import Mock, patch

from copilot.ai_runtime.model_manager import ModelManager
from copilot.ai_runtime.providers.ollama_provider import OllamaProvider


@patch("copilot.ai_runtime.providers.ollama_provider.requests.post")
def test_model_manager_with_ollama_provider(mock_post):
    """
    Valida integração entre Model Manager
    e Ollama Provider.
    """

    mock_response = Mock()

    mock_response.json.return_value = {
        "response": "Copilot funcionando"
    }

    mock_response.raise_for_status.return_value = None

    mock_post.return_value = mock_response

    provider = OllamaProvider()

    manager = ModelManager(
        provider=provider
    )

    response = manager.generate(
        "Qual sua função?"
    )

    assert response == "Copilot funcionando"

    mock_post.assert_called_once()