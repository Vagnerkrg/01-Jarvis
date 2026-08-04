from core.router import RequestRouter


def test_programming_route():
    router = RequestRouter()

    result = router.route(
        "Quero criar uma API usando Python"
    )

    assert result["category"] == "programming"
    assert result["target"] == "programmer_agent"


def test_architecture_route():
    router = RequestRouter()

    result = router.route(
        "Explique a arquitetura do sistema"
    )

    assert result["category"] == "architecture"
    assert result["target"] == "architect_agent"


def test_documentation_route():
    router = RequestRouter()

    result = router.route(
        "Criar documentação README"
    )

    assert result["category"] == "documentation"
    assert result["target"] == "documenter_agent"


def test_unknown_route():
    router = RequestRouter()

    result = router.route(
        "Qual a previsão do tempo?"
    )

    assert result["category"] == "general"
    assert result["target"] == "general_agent"