# Fluxo de Comunicação da Arquitetura

## Introdução

Este documento descreve como os componentes do sistema se comunicam durante a execução de uma solicitação.

O objetivo é definir responsabilidades, limites de comunicação e evitar dependências diretas entre componentes.

---

# Princípio Geral

A comunicação do sistema segue uma arquitetura em camadas.

Nenhum componente deve acessar diretamente implementações internas de outro componente.

O fluxo deve sempre utilizar interfaces e serviços definidos.

---

# Fluxo Principal

```text
Usuário
   │
   ▼
Interface
   │
   ▼
Application Layer
   │
   ▼
Chat Service
   │
   ▼
Model Manager
   │
   ▼
Provider
   │
   ▼
Modelo LLM

Descrição do Fluxo
1. Usuário

O usuário envia uma solicitação através da interface disponível.

Exemplos:

Pergunta.
Solicitação de tarefa.
Consulta de conhecimento.
2. Interface

A interface recebe a entrada do usuário e encaminha para a camada de aplicação.

Responsabilidades:

Capturar entrada.
Exibir resultado.
Gerenciar interação.

A interface não possui conhecimento sobre:

Modelos LLM.
Providers.
Agentes internos.
3. Application Layer

A camada de aplicação controla o fluxo da solicitação.

Responsabilidades:

Identificar o tipo de solicitação.
Acionar serviços necessários.
Coordenar componentes.
4. Chat Service

O Chat Service funciona como ponto de entrada para comunicação com a infraestrutura de IA.

Responsabilidades:

Receber mensagens.
Preparar requisições.
Encaminhar ao Model Manager.
5. Model Manager

O Model Manager é o controlador central da comunicação com modelos.

Responsabilidades:

Receber solicitações.
Selecionar configuração adequada.
Acionar Provider.
Retornar resposta padronizada.
6. Provider

O Provider realiza a comunicação específica com o runtime ou serviço de IA.

Exemplo inicial:

Provider Ollama

Responsabilidade:

Converter chamadas para formato esperado pelo modelo.
Executar requisição.
Retornar resultado.
7. Modelo LLM

O modelo executa o processamento da solicitação.

Responsabilidades:

Interpretar entrada.
Gerar resposta.
Retornar resultado.
Fluxo com Agentes

Quando agentes estiverem implementados, o fluxo será:

Usuário
   │
   ▼
Agent Controller
   │
   ▼
Agent
   │
   ▼
AI Runtime
   │
   ▼
Model Manager
   │
   ▼
Modelo LLM

Os agentes não acessam modelos diretamente.

Fluxo com RAG

Quando uma solicitação precisar de conhecimento externo:

Usuário
   │
   ▼
RAG Engine
   │
   ├───────────────┐
   │               │
   ▼               ▼
Vector Store    AI Runtime
                   │
                   ▼
                Modelo LLM

O RAG fornece contexto adicional antes da geração da resposta.

Fluxo com Memória

Quando existir memória contextual:

Usuário
   │
   ▼
Memory System
   │
   ▼
Context Builder
   │
   ▼
AI Runtime
   │
   ▼
Modelo LLM

A memória auxilia o modelo fornecendo informações relevantes.

Regras de Comunicação
Regra 1 — Sem acesso direto ao modelo

Nenhum componente deve chamar diretamente um modelo LLM.

Regra 2 — AI Runtime como único gateway

Toda comunicação com modelos deve passar pelo AI Runtime.

Regra 3 — Interfaces estáveis

Alterações internas não devem impactar consumidores externos.

Regra 4 — Componentes independentes

Cada módulo deve evoluir sem depender de detalhes internos dos demais.

Evolução Futura

O fluxo poderá evoluir para suportar:

Múltiplos agentes.
Orquestração inteligente.
Seleção automática de modelos.
Execução paralela de tarefas.
Avaliação de respostas.
Referências
overview.md
components.md
ai-runtime.md
ADR-001-arquitetura-da-infraestrutura-de-ia.md