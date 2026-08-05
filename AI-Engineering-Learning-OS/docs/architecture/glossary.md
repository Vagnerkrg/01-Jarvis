# Glossário da Arquitetura

## Introdução

Este documento define os principais termos utilizados na arquitetura do sistema.

O objetivo é manter uma linguagem comum entre desenvolvimento, documentação e evolução do projeto.

---

# AI Runtime

Camada responsável por abstrair a comunicação entre a aplicação e os modelos de Inteligência Artificial.

Responsabilidades:

- Gerenciar modelos.
- Controlar providers.
- Padronizar comunicação.
- Isolar dependências externas.

---

# Model Manager

Componente central responsável pelo gerenciamento da comunicação com modelos de IA.

Responsabilidades:

- Selecionar modelo.
- Controlar chamadas.
- Gerenciar configurações.
- Padronizar respostas.

---

# Provider

Camada responsável por integrar um serviço ou runtime específico de Inteligência Artificial.

Exemplos:

- Ollama.
- OpenAI.
- Outros provedores futuros.

---

# LLM (Large Language Model)

Modelo de linguagem capaz de interpretar e gerar texto utilizando técnicas de Inteligência Artificial.

Exemplos de capacidades:

- Conversação.
- Geração de código.
- Análise de informações.
- Raciocínio.

---

# Modelo Local

Modelo de Inteligência Artificial executado no ambiente do usuário sem depender obrigatoriamente de serviços externos.

Benefícios:

- Privacidade.
- Controle.
- Disponibilidade local.
- Personalização.

---

# Ollama

Runtime utilizado para executar modelos de linguagem localmente.

No projeto, será o primeiro provider oficial da infraestrutura de IA.

Responsabilidades:

- Executar modelos locais.
- Gerenciar modelos instalados.
- Disponibilizar comunicação com a aplicação.

---

# Agente (Agent)

Componente especializado capaz de executar tarefas utilizando modelos de IA.

Um agente possui:

- Objetivo.
- Contexto.
- Capacidade de raciocínio.
- Ferramentas.
- Processo de execução.

---

# Agent Registry

Sistema responsável pelo registro e gerenciamento dos agentes disponíveis.

Responsabilidades:

- Registrar agentes.
- Localizar agentes.
- Controlar informações dos agentes.

---

# Agent Runtime

Ambiente responsável pela execução dos agentes.

Responsabilidades:

- Gerenciar ciclo de vida.
- Controlar execução.
- Monitorar resultados.

---

# Memória (Memory)

Sistema responsável por armazenar e recuperar informações relevantes para o funcionamento do Copilot.

Tipos possíveis:

## Memória de Curto Prazo

Informações da interação atual.

---

## Memória de Longo Prazo

Informações persistentes entre diferentes sessões.

---

# RAG (Retrieval Augmented Generation)

Arquitetura que combina recuperação de conhecimento com geração através de modelos de linguagem.

Fluxo:

```text
Documento
    │
    ▼
Indexação
    │
    ▼
Busca
    │
    ▼
Contexto
    │
    ▼
LLM

Embedding

Representação numérica de um texto ou informação.

Permite:

Comparação semântica.
Busca por similaridade.
Recuperação de conhecimento.
Vector Database

Banco especializado em armazenar representações vetoriais.

Utilizado para:

Busca semântica.
Armazenamento de embeddings.
Recuperação eficiente.
Context Window

Quantidade máxima de informação que um modelo consegue processar em uma interação.

Prompt

Instrução enviada ao modelo de IA para orientar sua resposta.

Pode conter:

Objetivo.
Contexto.
Regras.
Exemplos.
Prompt Management

Sistema responsável pelo controle e organização dos prompts utilizados pelos componentes.

Tool

Recurso externo utilizado por agentes para executar ações.

Exemplos:

APIs.
Arquivos.
Banco de dados.
Sistemas externos.
Orquestração

Processo responsável por coordenar múltiplos componentes ou agentes para realizar uma tarefa.

Provider Abstraction

Princípio arquitetural que permite trocar provedores de IA sem alterar componentes internos.

Low Coupling (Baixo Acoplamento)

Princípio onde componentes possuem pouca dependência direta entre si.

Benefícios:

Facilidade de manutenção.
Maior flexibilidade.
Evolução independente.
ADR (Architecture Decision Record)

Documento utilizado para registrar decisões arquiteturais importantes.

Contém:

Contexto.
Problema.
Alternativas.
Decisão.
Consequências.
Referências
overview.md
components.md
ai-runtime.md
ADR-001-arquitetura-da-infraestrutura-de-ia.md