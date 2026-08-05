# Convenções de Nomenclatura da Arquitetura

## Introdução

Este documento define os padrões de nomenclatura utilizados na arquitetura do sistema.

O objetivo é manter consistência entre componentes, arquivos, módulos e documentações, facilitando manutenção e evolução do projeto.

---

# Princípios

As nomenclaturas devem seguir:

- Clareza.
- Consistência.
- Facilidade de entendimento.
- Padronização entre módulos.

---

# Arquivos

Arquivos de documentação devem utilizar:

```text
kebab-case.md

Exemplos:

ai-runtime.md

communication-flow.md

testing-strategy.md
Diretórios

Diretórios devem utilizar:

lowercase

Exemplos:

architecture/

agents/

memory/

providers/
Componentes

Componentes principais devem utilizar nomes descritivos.

Exemplos:

ModelManager

ChatService

AgentRegistry

MemoryManager
Classes

Classes devem utilizar:

PascalCase

Exemplos:

class ModelManager:
    pass

class OllamaProvider:
    pass
Funções e Métodos

Funções devem utilizar:

snake_case

Exemplos:

load_model()

generate_response()

register_agent()
Variáveis

Variáveis devem utilizar:

snake_case

Exemplos:

model_name

provider_config

agent_registry
Providers

Providers devem seguir o padrão:

NomeDoProvedor + Provider

Exemplos:

OllamaProvider

OpenAIProvider

AzureProvider
Serviços

Serviços devem seguir o padrão:

NomeDaResponsabilidade + Service

Exemplos:

ChatService

MemoryService

AgentService
Gerenciadores

Gerenciadores devem seguir:

NomeDoComponente + Manager

Exemplos:

ModelManager

MemoryManager

ConfigurationManager
Agentes

Agentes devem possuir nomes baseados em sua responsabilidade.

Exemplos:

ResearchAgent

CodingAgent

DataAnalysisAgent
ADRs

Architecture Decision Records devem seguir:

ADR-NNN-nome-da-decisao.md

Exemplo:

ADR-001-arquitetura-da-infraestrutura-de-ia.md
Branches Git

Branches devem seguir:

tipo/nome-da-entrega

Exemplos:

feature/m3-infraestrutura-ia

fix/model-manager-error

docs/update-architecture
Commits

Commits devem seguir:

tipo: descrição

Tipos utilizados:

feat
fix
docs
test
refactor
chore

Exemplos:

feat: implementa model manager

docs: adiciona arquitetura do AI Runtime

test: adiciona testes do provider ollama
Referências
development-guidelines.md
components.md
ai-runtime.md
ADR-001-arquitetura-da-infraestrutura-de-ia.md