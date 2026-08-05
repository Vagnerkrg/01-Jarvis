"""
Testes unitários do ChatService.
"""

from copilot.ai_runtime.interfaces import AIProvider
from copilot.ai_runtime.model_manager import ModelManager
from copilot.services.chat_service import ChatService


class MockProvider(AIProvider):
    """
    Provider falso utilizado apenas para testes.
    """

    def generate(self, prompt: str) -> str:
        return f"Resposta simulada: {prompt}"


def test_chat_service_send_message():
    """
    Valida que o ChatService envia mensagens
    corretamente utilizando o ModelManager.
    """

    provider = MockProvider()

    model_manager = ModelManager(
        provider=provider
    )

    chat_service = ChatService(
        model_manager=model_manager
    )

    response = chat_service.send_message(
        "Olá Jarvis"
    )

    assert response == "Resposta simulada: Olá Jarvis"