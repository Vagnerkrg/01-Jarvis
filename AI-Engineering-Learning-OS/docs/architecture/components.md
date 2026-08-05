# Componentes da Arquitetura

## Introdução

Este documento descreve os principais componentes arquiteturais do sistema, suas responsabilidades e a relação entre eles.

A separação dos componentes permite evolução independente, manutenção simplificada e expansão futura do Copilot.

---

# Visão Geral dos Componentes

A arquitetura é composta pelos seguintes componentes principais:

- Interface
- Application Layer
- AI Runtime
- Agents
- Memory
- RAG
- Tools

---

# Interface

## Responsabilidade

Camada responsável pela interação entre usuário e sistema.

## Funções

- Receber entradas do usuário.
- Exibir respostas.
- Controlar experiência de interação.

## Não deve

- Conhecer detalhes dos modelos de IA.
- Acessar provedores diretamente.
- Controlar lógica interna dos agentes.

---

# Application Layer

## Responsabilidade

Camada responsável pela coordenação das funcionalidades do sistema.

## Funções

- Gerenciar fluxo de execução.
- Coordenar serviços.
- Integrar componentes.

## Não deve

- Implementar lógica específica de modelos.
- Gerenciar diretamente infraestrutura de IA.

---

# AI Runtime

## Responsabilidade

Camada responsável pela comunicação com modelos de Inteligência Artificial.

## Componentes

### Model Manager

Responsável por:

- Gerenciar chamadas aos modelos.
- Controlar execução.
- Padronizar comunicação.

---

### Providers

Responsáveis por:

- Integrar diferentes runtimes.
- Adaptar APIs.
- Encapsular detalhes externos.

Provider inicial:

- Ollama

---

### Configuration System

Responsável por:

- Gerenciar configurações.
- Definir modelos ativos.
- Controlar parâmetros de execução.

---

### Chat Service

Responsável por:

- Receber solicitações.
- Encaminhar mensagens.
- Retornar respostas.

---

# Agents

## Responsabilidade

Executar tarefas especializadas utilizando capacidades de IA.

## Funções

- Planejamento.
- Execução.
- Uso de ferramentas.
- Tomada de decisão.

## Dependências

Os agentes utilizam o AI Runtime para acessar modelos.

---

# Memory

## Responsabilidade

Gerenciar informações persistentes e contexto.

## Funções

- Armazenamento de conhecimento.
- Recuperação contextual.
- Histórico de interações.

---

# RAG

## Responsabilidade

Aumentar a capacidade de resposta através de recuperação de conhecimento.

## Funções

- Indexação de documentos.
- Busca semântica.
- Recuperação de contexto.
- Geração baseada em conhecimento.

---

# Tools

## Responsabilidade

Permitir interação com recursos externos.

Exemplos futuros:

- APIs.
- Sistemas locais.
- Arquivos.
- Bancos de dados.
- Serviços externos.

---

# Relação Entre Componentes

Fluxo principal:

```text
Usuário
   │
   ▼
Interface
   │
   ▼
Application Layer
   │
   ├───────────────┐
   │               │
   ▼               ▼
Agents          RAG
   │               │
   └───────┬───────┘
           │
           ▼
     AI Runtime
           │
           ▼
      Modelos LLM

      Regras Arquiteturais
Componentes devem possuir responsabilidades únicas.
Comunicação deve ocorrer através de interfaces definidas.
Dependências diretas entre módulos devem ser evitadas.
Novos componentes devem ser documentados antes da implementação.
Referências
overview.md
ai-runtime.md
ADR-001-arquitetura-da-infraestrutura-de-ia.md