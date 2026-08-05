from copilot.ai_runtime.model_manager import ModelManager
from copilot.ai_runtime.interfaces import AIProvider


class MockProvider(AIProvider):
    """
    Provider falso utilizado apenas para testes.
    """

    def generate(self, prompt: str) -> str:
        return f"Resposta simulada para: {prompt}"


def test_model_manager_calls_provider():
    """
    Valida que o Model Manager utiliza
    corretamente o provider configurado.
    """

    provider = MockProvider()

    manager = ModelManager(
        provider=provider
    )

    response = manager.generate(
        "Teste de integração"
    )

    assert response == "Resposta simulada para: Teste de integração"