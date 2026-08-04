"""
Request Router

Responsible for classifying user requests
and selecting the execution target.
"""


class RequestRouter:
    """
    Basic rule-based request router.

    Future versions may replace this
    implementation with embeddings or LLM routing.
    """

    def __init__(self):
        self.rules = {
            "programming": {
                "keywords": [
                    "python",
                    "code",
                    "codigo",
                    "programar",
                    "api",
                    "bug",
                    "erro",
                    "software",
                ],
                "target": "programmer_agent",
            },
            "architecture": {
                "keywords": [
                    "architecture",
                    "arquitetura",
                    "design",
                    "estrutura",
                    "sistema",
                ],
                "target": "architect_agent",
            },
            "documentation": {
                "keywords": [
                    "document",
                    "documentacao",
                    "documentação",
                    "readme",
                    "markdown",
                ],
                "target": "documenter_agent",
            },
        }

    def route(self, request: str) -> dict:
        """
        Classify a request and return execution target.

        Args:
            request:
                User input text.

        Returns:
            Dictionary containing category and target.
        """

        text = request.lower()

        for category, rule in self.rules.items():
            for keyword in rule["keywords"]:
                if keyword in text:
                    return {
                        "category": category,
                        "target": rule["target"],
                    }

        return {
            "category": "general",
            "target": "general_agent",
        }