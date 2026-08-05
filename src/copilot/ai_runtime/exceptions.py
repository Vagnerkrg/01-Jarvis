"""
Exceções da camada AI Runtime.

Centraliza todas as exceções relacionadas à comunicação
com provedores de Inteligência Artificial.
"""


class AIRuntimeError(Exception):
    """
    Exceção base da camada AI Runtime.
    """

    pass


class ProviderConnectionError(AIRuntimeError):
    """
    Erro ao conectar com o Provider.
    """

    pass


class ProviderTimeoutError(AIRuntimeError):
    """
    Timeout durante comunicação com o Provider.
    """

    pass


class ProviderResponseError(AIRuntimeError):
    """
    Provider retornou uma resposta inválida.
    """

    pass