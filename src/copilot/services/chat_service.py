"""
Serviço responsável pela comunicação com modelos de IA.

Esta camada abstrai o uso do Model Manager e será a porta
de entrada para futuras integrações com Memória, RAG,
Ferramentas e Agentes.
"""

from copilot.ai_runtime.model_manager import ModelManager


class ChatService:
    """
    Serviço responsável pelo envio de mensagens
    para o modelo de IA.
    """

    def __init__(self, model_manager: ModelManager):
        self._model_manager = model_manager

    def send_message(self, message: str) -> str:
        """
        Envia uma mensagem para o modelo de IA.

        Args:
            message:
                Prompt enviado ao modelo.

        Returns:
            Resposta gerada pelo modelo.
        """

        return self._model_manager.generate(message)