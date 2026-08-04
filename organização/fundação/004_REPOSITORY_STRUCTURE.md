# AI Engineering Learning OS

# Official Repository Structure

## Estrutura Oficial do Repositório


---

# Document Control

| Campo | Valor |
|---|---|
| Documento | 004_REPOSITORY_STRUCTURE.md |
| Categoria | Engenharia do Sistema |
| Tipo | Repository Specification |
| Status | Official |
| Versão | 1.0 |
| Controle | Manual |
| Autor | Vagner Ferreira |
| Criado em | 2026-08-04 |


---

# Histórico de Versões

| Versão | Data | Descrição |
|---|---|---|
| 1.0 | 2026-08-04 | Primeira especificação oficial da estrutura do repositório |


---

# 1. Introdução


O AI Engineering Learning OS será construído seguindo uma arquitetura modular, onde cada componente possui uma responsabilidade claramente definida.


Este documento define a organização física do repositório e estabelece as regras para criação, manutenção e evolução da estrutura do projeto.


A estrutura do repositório não representa apenas uma organização de arquivos.


Ela representa a própria arquitetura do sistema.


---

# 2. Relação com a Arquitetura Oficial


O documento:


003_PROJECT_ARCHITECTURE.md


define:



Como o sistema funciona.



Este documento define:



Onde cada responsabilidade vive dentro do projeto.



A relação é:



Architecture

    ↓

Repository Structure

    ↓

Source Code

    ↓

Implementation



---

# 3. Filosofia do Repositório


O repositório segue quatro princípios fundamentais:


---

## 3.1 Architecture First


A estrutura deve nascer da arquitetura.


Nenhuma pasta deve existir apenas porque parece conveniente.


Toda área deve possuir uma responsabilidade definida.


---

## 3.2 Separation of Concerns


Cada componente deve permanecer isolado dentro do seu domínio.


Exemplo:



agents/

Responsável por comportamentos.

runtime/

Responsável por execução de modelos.

memory/

Responsável por persistência de contexto.



Misturar responsabilidades cria dependências difíceis de manter.


---

## 3.3 Explicit Over Implicit


A organização deve favorecer clareza.


Preferimos:



agents/documentation_agent/



ao invés de:



utils/

helpers/

misc/



Pastas genéricas devem ser evitadas.


---

## 3.4 Evolution Friendly


A estrutura deve permitir crescimento.


O projeto deve conseguir evoluir de:



Single Agent

    ↓

Multiple Agents

    ↓

Agent Platform

    ↓

Engineering OS



sem reconstrução completa.


---

# 4. Objetivo da Estrutura


A estrutura oficial deve permitir:


- localização rápida de componentes;
- desenvolvimento organizado;
- testes independentes;
- documentação próxima do código;
- evolução modular;
- manutenção de longo prazo.


---

# 5. Princípio Fundamental


## Repository Mirrors Architecture


A organização do repositório deve refletir a arquitetura definida.


Exemplo:


Arquitetura:



Memory System



Repositório:



memory/



Arquitetura:



Agent Architecture



Repositório:



agents/



Arquitetura:



Knowledge System



Repositório:



knowledge/



---

# 6. Regras Gerais de Organização


## Cada pasta deve possuir:


- propósito documentado;
- responsabilidade única;
- limites definidos;
- testes quando aplicável.


---

## Cada módulo deve possuir:


- código;
- documentação necessária;
- testes relacionados;
- configuração quando necessário.


---

## Evitar:



misc/

temp/

random/

old/

backup/



Essas estruturas indicam ausência de decisão arquitetural.


---

# 7. Visão Geral do Repositório


A estrutura inicial:



ai-engineering-learning-os/

│
├── app/
│
├── core/
│
├── runtime/
│
├── agents/
│
├── skills/
│
├── memory/
│
├── knowledge/
│
├── rag/
│
├── tools/
│
├── models/
│
├── workflows/
│
├── interfaces/
│
├── config/
│
├── tests/
│
├── docs/
│
├── logs/
│
├── scripts/
│
├── examples/
│
├── notebooks/
│
├── requirements/
│
├── README.md
│
└── LICENSE



---

# 8. Organização por Camadas


O repositório segue a mesma divisão definida na arquitetura:



Interface Layer

    ↓

Application Layer

    ↓

Orchestration Layer

    ↓

Agent Layer

    ↓

Knowledge Layer

    ↓

Runtime Layer

    ↓

Core Layer



---

# 9. Regra de Dependência


As dependências devem respeitar:



interfaces

    ↓

app

    ↓

workflows

    ↓

agents

    ↓

skills

    ↓

memory / knowledge / tools

    ↓

runtime

    ↓

core



Componentes inferiores nunca devem depender de componentes superiores.


---

# 10. Resultado Esperado


Ao seguir esta estrutura:


O desenvolvedor deve conseguir responder:



Onde está o comportamento?

agents/

Onde está o conhecimento?

knowledge/

Onde está a execução de modelos?

runtime/

Onde estão as regras fundamentais?

core/

Onde estão as ferramentas?

tools/



A estrutura do projeto deve tornar a arquitetura visível.

# 11. Estrutura Oficial de Diretórios

## Official Directory Structure


A estrutura do repositório deve representar diretamente os componentes definidos na arquitetura oficial.


Cada diretório possui uma finalidade específica e não deve assumir responsabilidades de outras áreas.


---

# 12. Diretório Principal


Estrutura:



ai-engineering-learning-os/



Representa o projeto completo.


Dentro dele estão:


- código fonte;
- configurações;
- documentação;
- testes;
- recursos auxiliares.


---

# 13. app/


## Application Layer


Responsabilidade:


A camada de aplicação representa o ponto de composição do sistema.


Ela conecta os componentes arquiteturais para formar uma aplicação funcional.


---

Contém:



app/

├── main.py

├── application.py

├── bootstrap.py



---

Responsabilidades:


- inicialização do sistema;
- carregamento de configurações;
- criação dos serviços;
- composição dos componentes.


---

Não deve conter:


- regras de negócio;
- lógica de agentes;
- implementação de modelos.


---

# 14. core/


## Core Foundation Layer


Responsabilidade:


O Core representa a fundação do sistema.


É a camada mais estável do projeto.


---

Contém:



core/

├── interfaces/

├── models/

├── exceptions/

├── contracts/



---

Responsabilidades:


- contratos;
- interfaces;
- entidades fundamentais;
- padrões internos.


---

Não deve conter:


- chamadas externas;
- dependências de frameworks;
- modelos de IA.


---

# 15. runtime/


## AI Runtime Layer


Responsabilidade:


Gerenciar a execução dos modelos de inteligência artificial.


---

Contém:



runtime/

├── model_manager/

├── inference/

├── embeddings/

├── context/



---

Responsabilidades:


- comunicação com modelos;
- gerenciamento de contexto;
- execução de inferência;
- controle de chamadas.


---

Não deve conter:


- regras de agentes;
- conhecimento;
- memória permanente.


---

# 16. agents/


## Agent Layer


Responsabilidade:


Armazenar agentes especializados do sistema.


---

Contém:



agents/

├── documentation_agent/

├── research_agent/

├── coding_agent/

├── data_agent/



---

Cada agente deve possuir:



agent/

├── definition.py

├── prompt.md

├── config.yaml

├── tests/



---

Responsabilidades:


- comportamento especializado;
- instruções;
- composição de skills.


---

Não deve conter:


- gerenciamento do runtime;
- armazenamento de conhecimento;
- infraestrutura.


---

# 17. skills/


## Skills Layer


Responsabilidade:


Armazenar capacidades reutilizáveis.


---

Contém:



skills/

├── document_generation/

├── data_analysis/

├── code_review/

├── research/



---

Responsabilidades:


- procedimentos;
- capacidades;
- operações reutilizáveis.


---

Não deve conter:


- identidade de agentes;
- controle de workflow.


---

# 18. memory/


## Memory System Layer


Responsabilidade:


Gerenciar memória do sistema.


---

Contém:



memory/

├── short_term/

├── working/

├── long_term/

├── storage/

├── retrieval/



---

Responsabilidades:


- armazenamento de contexto;
- recuperação de memória;
- políticas de retenção.


---

Não deve conter:


- documentos externos;
- conhecimento geral.


---

# 19. knowledge/


## Knowledge Base Layer


Responsabilidade:


Armazenar fontes de conhecimento utilizadas pelo sistema.


---

Contém:



knowledge/

├── documents/

├── sources/

├── metadata/

├── indexes/



---

Responsabilidades:


- organização de conhecimento;
- gerenciamento de fontes;
- preparação para recuperação.


---

Não deve conter:


- histórico de conversas;
- preferências pessoais.


---

# 20. rag/


## Retrieval Augmented Generation Layer


Responsabilidade:


Gerenciar o pipeline de recuperação de conhecimento.


---

Contém:



rag/

├── loaders/

├── chunking/

├── embeddings/

├── retrievers/

├── pipelines/



---

Responsabilidades:


- processamento de documentos;
- geração de embeddings;
- busca semântica;
- montagem de contexto.


---

Não deve conter:


- memória pessoal;
- comportamento de agentes.


---

# 21. tools/


## Tools Layer


Responsabilidade:


Gerenciar ferramentas utilizadas pelos agentes.


---

Contém:



tools/

├── filesystem/

├── database/

├── api/

├── execution/



---

Responsabilidades:


- executar ações externas;
- integrar serviços;
- disponibilizar capacidades.


---

Não deve conter:


- planejamento;
- tomada de decisão.


---

# 22. models/


## Model Layer


Responsabilidade:


Gerenciar modelos utilizados pelo sistema.


---

Contém:



models/

├── language/

├── embeddings/

├── vision/

├── configurations/



---

Responsabilidades:


- configurações;
- referências;
- gerenciamento de modelos.


---

Não deve conter:


- lógica de agentes;
- prompts de comportamento.


---

# 23. workflows/


## Workflow Layer


Responsabilidade:


Gerenciar processos compostos.


---

Contém:



workflows/

├── definitions/

├── executions/

├── states/



---

Responsabilidades:


- sequência de tarefas;
- estados;
- controle de execução.


---

Não deve conter:


- inteligência específica;
- conhecimento.


---

# 24. interfaces/


## Interface Layer


Responsabilidade:


Representar os pontos de interação com usuários e sistemas externos.


---

Contém:



interfaces/

├── api/

├── cli/

├── ui/



---

Responsabilidades:


- receber entradas;
- apresentar resultados;
- disponibilizar integrações.


---

Não deve conter:


- regras internas do sistema.


---

# 25. config/


## Configuration Layer


Responsabilidade:


Centralizar configurações do sistema.


---

Contém:



config/

├── system.yaml

├── agents.yaml

├── models.yaml

├── runtime.yaml



---

Responsabilidades:


- ambientes;
- parâmetros;
- configurações.


---

Não deve conter:


- código de execução.


---

# 26. logs/


## Logging Layer


Responsabilidade:


Armazenar registros operacionais.


---

Contém:



logs/

├── system/

├── execution/

├── security/



---

Responsabilidades:


- auditoria;
- diagnóstico;
- observabilidade.


---

# 27. scripts/


## Automation Scripts


Responsabilidade:


Scripts auxiliares de desenvolvimento.


Exemplos:



scripts/

├── setup/

├── migration/

├── maintenance/



---

# 28. examples/


## Examples and Demonstrations


Responsabilidade:


Armazenar exemplos de utilização.


Exemplos:



examples/

├── simple_agent/

├── rag_example/

├── workflow_example/



---

# 29. notebooks/


## Experimental Area


Responsabilidade:


Ambiente para exploração e experimentação.


Não deve conter:


- código principal;
- componentes oficiais.


---

# 30. docs/


## Documentation Layer


Responsabilidade:


Centralizar documentação técnica.


Inclui:



docs/

├── architecture/

├── decisions/

├── guides/

├── references/



---

# 31. tests/


## Testing Layer


Responsabilidade:


Garantir qualidade do sistema.


Estrutura:



tests/

├── unit/

├── integration/

├── e2e/

├── evaluation/



---

# 32. Resumo das Responsabilidades


| Pasta | Responsabilidade |
|---|---|
| app | Composição da aplicação |
| core | Fundamentos e contratos |
| runtime | Execução de modelos |
| agents | Comportamentos especializados |
| skills | Capacidades reutilizáveis |
| memory | Continuidade e contexto |
| knowledge | Informação externa |
| rag | Recuperação de conhecimento |
| tools | Execução de ações |
| models | Gerenciamento de modelos |
| workflows | Processos compostos |
| interfaces | Interação |
| config | Configuração |
| tests | Validação |
| docs | Documentação |
| logs | Observabilidade |


---

# 33. Resultado Esperado


Seguindo esta estrutura:



Arquitetura

    +

Organização Física

    +

Responsabilidades Claras

=

Base Sustentável de Desenvolvimento

# 34. Code Organization Rules

## Regras de Organização de Código


O AI Engineering Learning OS seguirá padrões consistentes de organização de código para garantir:


- legibilidade;
- manutenção;
- evolução;
- colaboração;
- redução de complexidade.


---

# 35. Princípio Fundamental


O código deve seguir:



Clareza

Responsabilidade Única

Baixo Acoplamento

Alta Coesão



---

# 36. Single Responsibility Principle


Cada módulo deve possuir uma única responsabilidade principal.


Exemplo:


Correto:



memory/retrieval.py

Responsável por:

Recuperação de memória.



Incorreto:



memory/utils.py

Responsável por:

Memória

Logs

Configuração

Banco de dados



---

# 37. Module Design


Um módulo deve:


- possuir propósito claro;
- possuir interface definida;
- evitar dependências desnecessárias;
- possuir testes quando aplicável.


---

# 38. Estrutura Interna de Módulos


Um componente deve seguir:



component/

├── init.py

├── component.py

├── config.py

├── exceptions.py

├── schemas.py

├── tests/

└── README.md



Nem todos os arquivos são obrigatórios.


A estrutura deve crescer conforme a necessidade.


---

# 39. Regra de Crescimento de Módulos


Um módulo começa simples.


Exemplo:



agents/

└── coding_agent.py



Somente quando crescer:



agents/

└── coding_agent/

├── agent.py

├── prompts/

├── tools/

├── tests/


A complexidade deve ser criada quando necessária.


---

# 40. Naming Conventions


## Convenções de Nomenclatura


O projeto seguirá padrões consistentes de nomes.


---

# 41. Arquivos Python


Arquivos devem utilizar:



snake_case



Exemplo:


Correto:



memory_manager.py

document_loader.py

agent_router.py



Incorreto:



MemoryManager.py

DocumentLoader.py

AgentRouter.py



---

# 42. Classes


Classes devem utilizar:



PascalCase



Exemplo:


```python
class MemoryManager:
    pass


class AgentRouter:
    pass
``` id="g6p3mv"


---

# 43. Funções e Métodos


Funções devem utilizar:



snake_case



Exemplo:


```python
def retrieve_memory():
    pass


def load_document():
    pass
``` id="d3v9kh"


---

# 44. Constantes


Constantes devem utilizar:



UPPER_CASE



Exemplo:


```python
MAX_TOKEN_LIMIT = 4096

DEFAULT_TIMEOUT = 30

``` id="b7k4ps"


---

# 45. Diretórios


Pastas devem utilizar:



snake_case



Exemplo:



documentation_agent/

vector_storage/

model_manager/



---

# 46. Nomes Devem Representar Responsabilidade


Evitar nomes genéricos.


Não utilizar:



utils/

helpers/

common/

misc/



Preferir:



document_processing/

memory_management/

model_adapters/



---

# 47. Organização de Imports


Os imports devem seguir:



Standard Library

    ↓

Third Party Libraries

    ↓

Internal Modules



Exemplo:


```python
import os
from pathlib import Path


import numpy as np
from pydantic import BaseModel


from core.interfaces import Agent
from memory.manager import MemoryManager

``` id="c7v5nz"


---

# 48. Dependency Management


Dependências externas devem:


- ser declaradas;
- possuir versão controlada;
- evitar duplicação;
- possuir justificativa quando adicionadas.


---

# 49. Framework Independence


Sempre que possível:


O código interno não deve depender diretamente de frameworks externos.


Exemplo:


Evitar:



Agent

depende diretamente de:

LangChain



Preferir:



Agent Interface

    ↓

Framework Adapter

    ↓

LangChain



---

# 50. Configuration Rules


Configurações nunca devem ficar espalhadas pelo código.


Evitar:


```python
temperature = 0.7
``` id="v5n8rx"


Dentro de vários arquivos.


Preferir:


```yaml
models.yaml

temperature: 0.7

``` id="m7q2kp"


---

# 51. Environment Variables


Informações sensíveis devem utilizar variáveis de ambiente.


Exemplo:



API_KEY

DATABASE_URL

MODEL_TOKEN



Nunca:


```python
API_KEY = "secret_value"

``` id="k6x3qs"


---

# 52. Documentation Near Code


Componentes importantes devem possuir documentação próxima.


Exemplo:



agents/

└── research_agent/

├── agent.py

├── README.md

└── tests/


---

# 53. Code Review Principles


Toda alteração importante deve avaliar:



Esta mudança:

Mantém responsabilidade clara?

Reduz ou aumenta acoplamento?

Respeita arquitetura?

Possui testes?

Atualiza documentação?



---

# 54. Regra de Ouro


Antes de criar qualquer arquivo novo:


A pergunta obrigatória é:



Qual responsabilidade arquitetural este arquivo representa?



Se não existir uma resposta clara:


O arquivo não deve ser criado.


---

# 55. Resultado Esperado


Com estas regras:



Arquitetura

    +

Organização

    +

Padrões

    +

Disciplina

=

Sistema Evolutivo



O código do AI Engineering Learning OS deve permanecer compreensível mesmo após anos de evolução.

# 56. Development Workflow

## Processo Oficial de Desenvolvimento


O desenvolvimento do AI Engineering Learning OS seguirá um processo estruturado baseado em:



Documentation First

Architecture First

Test Driven Development

Incremental Evolution



---

# 57. Princípio de Desenvolvimento


Nenhuma grande implementação deve começar diretamente pelo código.


O fluxo oficial é:



Idea

↓

Documentation

↓

Architecture Review

↓

Implementation

↓

Testing

↓

Integration

↓

Documentation Update



---

# 58. Documentation First


A documentação deve preceder mudanças importantes.


Antes de implementar:


Deve existir:


- objetivo definido;
- responsabilidade identificada;
- impacto analisado;
- arquitetura validada.


---

# 59. Architecture First


Toda nova funcionalidade deve responder:



Onde esta capacidade pertence?



Exemplos:


Nova capacidade de memória:



memory/



Novo agente:



agents/



Nova integração:



tools/



---

# 60. Development Cycle


O ciclo oficial:


Planejar
Documentar
Implementar
Testar
Revisar
Registrar aprendizado


---

# 61. Git Strategy


## Estratégia de Controle de Versão


O projeto utilizará Git como mecanismo oficial de controle de evolução.


---

# 62. Branch Strategy


Estratégia:



main

↓

feature branches



---

# 63. Main Branch


A branch principal representa:



Versão estável do sistema



A main deve sempre possuir:


- código funcional;
- testes passando;
- documentação atualizada.


---

# 64. Feature Branches


Novas capacidades devem ser desenvolvidas em branches específicas.


Formato:



feature/nome-da-capacidade



Exemplos:



feature/memory-system

feature/rag-pipeline

feature/planner-agent

feature/tool-framework



---

# 65. Bug Fix Branches


Correções devem utilizar:



fix/nome-do-problema



Exemplo:



fix/runtime-timeout



---

# 66. Commit Strategy


Commits devem representar mudanças significativas.


Evitar:



update

changes

test

fix



---

Preferir:



Add memory retrieval system

Implement agent router

Create RAG pipeline tests

Update architecture documentation



---

# 67. Commit Principles


Um bom commit deve:


- possuir propósito claro;
- representar uma mudança lógica;
- facilitar rastreamento;
- permitir rollback.


---

# 68. Testing Before Integration


Antes de integrar qualquer mudança:


Deve existir:



Code

Tests

Documentation



---

# 69. Pull Request / Review Concept


Mesmo sendo um projeto individual, alterações importantes devem passar por revisão conceitual.


A revisão deve verificar:



Arquitetura

Código

Testes

Documentação

Impacto



---

# 70. Documentation Management


A documentação será tratada como parte oficial do sistema.


Estrutura:



docs/

├── architecture/

├── decisions/

├── guides/

├── tutorials/

├── references/



---

# 71. Architecture Documentation


Documentos arquiteturais:



001_PROJECT_MANIFESTO.md

002_PROJECT_ROADMAP.md

003_PROJECT_ARCHITECTURE.md

004_REPOSITORY_STRUCTURE.md



representam a Fundação oficial.


---

# 72. Decision Documentation


Decisões importantes devem ser registradas:



docs/decisions/



Formato:



ADR-001-title.md

ADR-002-title.md



---

# 73. Engineering Journal


O projeto deve manter um histórico de aprendizado:



docs/engineering-journal/



Registrando:


- descobertas;
- problemas;
- soluções;
- melhorias.


---

# 74. Experimentation Rules


Experimentos devem ser isolados.


Local:



experiments/



Não devem contaminar:



core/

runtime/

agents/



---

# 75. Prototype to Production Flow


Novas ideias seguem:



Experiment

↓

Validation

↓

Documentation

↓

Architecture Decision

↓

Production Component



---

# 76. Knowledge Preservation


Todo aprendizado relevante deve permanecer no projeto.


A regra:



Se foi importante para entender o sistema,

deve ser documentado.



---

# 77. Engineering Discipline


O projeto seguirá:



Código pode mudar.

Tecnologia pode mudar.

Modelos podem mudar.

Mas o conhecimento acumulado deve permanecer.



---

# 78. Resultado Esperado


Com este processo:



Desenvolvimento

Documentação

Testes

Histórico

Arquitetura

=

Sistema Sustentável



O AI Engineering Learning OS será desenvolvido como um projeto profissional de engenharia, mantendo rastreabilidade e consistência durante toda sua evolução.

# 79. Testing Structure

## Estrutura Oficial de Testes


Os testes fazem parte da arquitetura do sistema.


Eles não são uma etapa posterior.


São mecanismos de proteção da evolução do projeto.


---

# 80. Princípio de Qualidade


O projeto segue:



Every Feature Must Be Tested



Toda nova capacidade relevante deve possuir validação correspondente.


---

# 81. Organização da Pasta tests/


Estrutura:



tests/

├── unit/

├── component/

├── integration/

├── e2e/

├── evaluation/

└── fixtures/



---

# 82. Unit Tests


Local:



tests/unit/



Responsabilidade:


Validar pequenas unidades isoladas.


Exemplos:



MemoryManager

PromptParser

ConfigLoader

Router



---

# 83. Component Tests


Local:



tests/component/



Responsabilidade:


Validar componentes completos.


Exemplos:



Agent

RAG Pipeline

Tool Execution

Workflow



---

# 84. Integration Tests


Local:



tests/integration/



Responsabilidade:


Validar comunicação entre camadas.


Exemplo:



Agent

↓

Runtime

↓

Model

↓

Response



---

# 85. End-to-End Tests


Local:



tests/e2e/



Responsabilidade:


Validar o fluxo completo do usuário.


Exemplo:



User Request

↓

Interface

↓

Orchestrator

↓

Agent

↓

Tools

↓

Result



---

# 86. AI Evaluation Tests


Local:



tests/evaluation/



Sistemas de IA precisam de avaliações além de testes tradicionais.


Avaliar:


- qualidade da resposta;
- comportamento esperado;
- consistência;
- utilização correta de ferramentas;
- recuperação de conhecimento.


---

# 87. Test Fixtures


Local:



tests/fixtures/



Responsabilidade:


Armazenar:


- dados de teste;
- exemplos;
- respostas esperadas;
- configurações temporárias.


---

# 88. Quality Gates


## Portões de Qualidade


Uma alteração só pode avançar quando cumprir critérios mínimos.


---

# 89. Gate 1 — Code Quality


Verificações:



Código organizado

Padrões respeitados

Sem erros críticos



---

# 90. Gate 2 — Testing


Verificações:



Testes executados

Testes passando

Novos testes adicionados quando necessário



---

# 91. Gate 3 — Architecture Compliance


Verificações:



Responsabilidade correta

Dependências corretas

Arquitetura preservada



---

# 92. Gate 4 — Documentation


Verificações:



Documentação atualizada

Decisões registradas

Exemplos atualizados



---

# 93. Continuous Integration


## CI Pipeline


O projeto utilizará integração contínua para validar mudanças automaticamente.


Fluxo:



Commit

↓

CI Trigger

↓

Install Dependencies

↓

Run Tests

↓

Validate Quality

↓

Generate Report



---

# 94. CI Responsibilities


A integração contínua deve verificar:


- instalação correta;
- testes automatizados;
- erros de código;
- compatibilidade;
- regressões.


---

# 95. Release Management


## Gestão de Versões


O projeto seguirá versionamento controlado.


Formato:



MAJOR.MINOR.PATCH



Exemplo:



1.0.0



---

# 96. Versionamento


## Major


Mudanças grandes:



Alteração arquitetural

Breaking changes

Nova geração do sistema



---

## Minor


Novas capacidades:



Novo agente

Nova skill

Nova integração



---

## Patch


Correções:



Bug fix

Melhoria pequena

Correção documental



---

# 97. Release Checklist


Antes de uma versão oficial:



✓ Testes passando

✓ Documentação atualizada

✓ ADRs revisados

✓ Changelog criado

✓ Arquitetura validada



---

# 98. Changelog


O projeto deve manter histórico de versões:



CHANGELOG.md



Registrando:


- novas funcionalidades;
- correções;
- mudanças importantes.


---

# 99. Repository Maturity Model


A evolução do repositório segue:


## Level 1 — Organized


Possui:



Estrutura definida

Documentação inicial

Testes básicos



---

## Level 2 — Professional


Possui:



CI

Quality Gates

Automação

ADR



---

## Level 3 — Engineering Platform


Possui:



Multi-Agent System

Observability

Automation

Evaluation Framework



---

# 100. Final Repository Principle


O repositório do AI Engineering Learning OS deve ser tratado como:



Código

Arquitetura

Conhecimento

Histórico

Processo



Não é apenas um local para armazenar arquivos.


É a representação física do sistema.


---

# 101. Conclusão do Documento


A estrutura oficial do repositório estabelece a base para uma construção organizada, modular e sustentável.


A arquitetura define responsabilidades.


O repositório organiza essas responsabilidades.


O processo garante evolução segura.


---

# Documento Finalizado


Documento:



004_REPOSITORY_STRUCTURE.md



Status:



Official Repository Specification

Version 1.0



Categoria:



Engenharia do Sistema



---

A partir deste documento, o AI Engineering Learning OS possui:



001_PROJECT_MANIFESTO.md

    ↓

Identidade

002_PROJECT_ROADMAP.md

    ↓

Planejamento

003_PROJECT_ARCHITECTURE.md

    ↓

Arquitetura Oficial

004_REPOSITORY_STRUCTURE.md

    ↓

Organização Física do Sistema


---
