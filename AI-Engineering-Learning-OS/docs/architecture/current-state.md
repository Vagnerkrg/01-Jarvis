# Estado Atual da Arquitetura

## Introdução

Este documento registra o estado atual da arquitetura do Copilot durante seu desenvolvimento.

O objetivo é manter uma visão clara do que já foi definido, implementado e quais componentes ainda estão em evolução.

---

# Status Geral

## Fase Atual

Milestone:

```text
M3 — Fundação da Infraestrutura de IA

Status:

Em desenvolvimento
Arquitetura Atual

A arquitetura definida atualmente possui as seguintes camadas:

                    Copilot

                       │

              Application Layer

                       │

        ┌──────────────┼──────────────┐

        │              │              │

     Agents        Memory           RAG

        │              │              │

        └──────────────┼──────────────┘

                       │

                AI Runtime Layer

                       │

                Model Manager

                       │

                  Providers

                       │

                 Modelos LLM
Componentes Definidos
AI Runtime

Status:

Arquitetura definida

Responsabilidade:

Centralizar a comunicação entre a aplicação e modelos de Inteligência Artificial.

Model Manager

Status:

Planejado

Responsabilidade:

Gerenciar chamadas, seleção e comunicação com modelos.

Providers

Status:

Planejado

Provider inicial:

Ollama

Responsabilidade:

Abstrair diferentes runtimes de IA.

Chat Service

Status:

Planejado

Responsabilidade:

Controlar comunicação entre aplicação e infraestrutura de IA.

Componentes Futuros
Sistema de Agentes

Status:

Próxima evolução

Planejado:

Base de agentes.
Registro de agentes.
Pipeline de execução.
Ferramentas.
Sistema de Memória

Status:

Futuro

Planejado:

Memória contextual.
Persistência.
Recuperação de informações.
Sistema RAG

Status:

Futuro

Planejado:

Indexação.
Embeddings.
Busca semântica.
Recuperação de conhecimento.
Decisões Arquiteturais Atuais
ADR-001

Nome:

Arquitetura da Infraestrutura de IA

Status:

Aceita

Decisão principal:

Criar uma camada AI Runtime para impedir acoplamento direto entre componentes e modelos.

Princípios Ativos

A arquitetura segue:

Modularidade.
Baixo acoplamento.
Alta coesão.
Documentação contínua.
Testabilidade.
Evolução incremental.
Próximas Implementações

Ordem planejada:

Instalação do Ollama.
Escolha do modelo local inicial.
Implementação do Model Manager.
Implementação do Provider Ollama.
Implementação do Chat Service.
Testes de integração.
Critério de Evolução

Uma nova fase somente deve iniciar quando:

Arquitetura documentada.
Implementação validada.
Testes passando.
Decisões registradas.
Referências
overview.md
ai-runtime.md
architecture-roadmap.md
ADR-001-arquitetura-da-infraestrutura-de-ia.md