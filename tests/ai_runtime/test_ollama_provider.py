from unittest.mock import Mock, patch

import pytest
from requests.exceptions import ConnectionError, HTTPError, Timeout

from copilot.ai_runtime.exceptions import (
    ProviderConnectionError,
    ProviderResponseError,
    ProviderTimeoutError,
)
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


@patch("copilot.ai_runtime.providers.ollama_provider.requests.post")
def test_connection_error(mock_post):
    """
    Deve lançar ProviderConnectionError
    quando não conseguir conectar ao Ollama.
    """

    mock_post.side_effect = ConnectionError()

    provider = OllamaProvider()

    with pytest.raises(ProviderConnectionError):
        provider.generate("teste")


@patch("copilot.ai_runtime.providers.ollama_provider.requests.post")
def test_timeout_error(mock_post):
    """
    Deve lançar ProviderTimeoutError
    quando ocorrer timeout.
    """

    mock_post.side_effect = Timeout()

    provider = OllamaProvider()

    with pytest.raises(ProviderTimeoutError):
        provider.generate("teste")


@patch("copilot.ai_runtime.providers.ollama_provider.requests.post")
def test_http_error(mock_post):
    """
    Deve lançar ProviderResponseError
    quando o Ollama retornar erro HTTP.
    """

    response = Mock()
    response.raise_for_status.side_effect = HTTPError()

    mock_post.return_value = response

    provider = OllamaProvider()

    with pytest.raises(ProviderResponseError):
        provider.generate("teste")


@patch("copilot.ai_runtime.providers.ollama_provider.requests.post")
def test_invalid_response(mock_post):
    """
    Deve lançar ProviderResponseError
    quando o JSON não possuir o campo response.
    """

    response = Mock()

    response.raise_for_status.return_value = None
    response.json.return_value = {}

    mock_post.return_value = response

    provider = OllamaProvider()

    with pytest.raises(ProviderResponseError):
        provider.generate("teste")