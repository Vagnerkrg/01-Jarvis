# ADR-001 — Arquitetura da Infraestrutura de IA (AI Runtime)

- **Status:** Aceita
- **Data:** 04/08/2026
- **Autor:** Vagner Ferreira
- **Versão:** 1.0

---

# Contexto

O projeto tem como objetivo desenvolver um Copilot pessoal baseado em Inteligência Artificial, capaz de evoluir para um sistema composto por agentes especializados, memória contextual, recuperação de conhecimento (RAG), integração com ferramentas externas e suporte a múltiplos modelos de linguagem (LLMs).

Para garantir uma arquitetura escalável, modular e de baixo acoplamento, tornou-se necessário definir uma camada responsável por centralizar toda a comunicação entre a aplicação e os modelos de IA.

Sem essa abstração, componentes como Agentes, Memória, RAG, Interface e Serviços de Aplicação dependeriam diretamente da implementação de um provedor específico, aumentando o acoplamento e dificultando a manutenção e evolução do sistema.

---

# Problema

Como permitir que diferentes componentes do sistema utilizem modelos de IA sem depender diretamente de um provedor específico?

A solução deve permitir que novos provedores sejam adicionados futuramente com o menor impacto possível na arquitetura existente.

---

# Decisão

Será criada uma camada denominada **AI Runtime**, responsável por abstrair completamente a comunicação entre a aplicação e os modelos de Inteligência Artificial.

Essa camada será o único ponto autorizado para interação com provedores de modelos.

Inicialmente, a arquitetura será composta pelos seguintes componentes:

- Model Manager
- Providers
- Sistema de Configuração
- Chat Service

O primeiro provedor oficial será o **Ollama**, responsável pela execução de modelos locais durante a fase inicial do projeto.

Toda comunicação entre os demais módulos e os modelos de IA deverá ocorrer exclusivamente através do **Model Manager**.

---

# Arquitetura

```text
                 Copilot
                     │
        ┌────────────┼────────────┐
        │            │            │
     Agentes      Memória       RAG
        │            │            │
        └────────────┼────────────┘
                     │
              AI Runtime Layer
                     │
              Model Manager
                     │
        ┌────────────┼────────────┐
        │            │            │
     Ollama     Futuros Providers
                     │
                 Modelos LLM
```

---

# Consequências

## Positivas

- Baixo acoplamento entre aplicação e provedores.
- Facilidade para adicionar novos provedores.
- Facilidade para troca de modelos.
- Arquitetura preparada para evolução.
- Maior facilidade para testes.
- Reutilização da infraestrutura pelos agentes.
- Reutilização pelo sistema de memória.
- Reutilização pelo mecanismo de RAG.
- Centralização da comunicação com IA.

## Negativas

- Introdução de uma camada adicional na arquitetura.
- Pequeno aumento da complexidade inicial.
- Necessidade de manutenção da camada de abstração.

---

# Alternativas Consideradas

## Comunicação direta com o Ollama

**Rejeitada.**

Criaria forte acoplamento entre a aplicação e um único provedor.

---

## Comunicação independente em cada módulo

**Rejeitada.**

Cada componente implementaria sua própria integração com o modelo, aumentando duplicação de código e dificultando manutenção.

---

## Camada centralizada de IA

**Aceita.**

Centraliza responsabilidades, reduz acoplamento e facilita futuras expansões da arquitetura.

---

# Impacto na Arquitetura

A partir desta decisão:

- Agentes não conhecerão provedores.
- Memória não conhecerá provedores.
- RAG não conhecerá provedores.
- Interface não conhecerá provedores.
- Serviços da aplicação utilizarão apenas o Model Manager.

Toda comunicação com modelos de IA será centralizada na camada AI Runtime.

---

# Próximos Passos

Esta decisão habilita o desenvolvimento das próximas etapas da Milestone 3:

1. Instalação do Ollama.
2. Seleção do primeiro modelo oficial.
3. Implementação do Model Manager.
4. Implementação do Provider Ollama.
5. Implementação do Chat Service.
6. Testes de integração.

---

# Referências

- Roadmap do Projeto
- Documentação da Arquitetura
- Milestone 3 — Infraestrutura de IA