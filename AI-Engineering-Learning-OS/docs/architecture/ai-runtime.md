# Infraestrutura de IA (AI Runtime)

## Visão Geral

A Infraestrutura de IA (AI Runtime) é a camada responsável por centralizar a comunicação entre a aplicação e os modelos de Inteligência Artificial utilizados pelo projeto.

Seu objetivo é fornecer uma arquitetura desacoplada, permitindo que diferentes componentes do sistema utilizem capacidades de IA sem depender diretamente de um provedor específico de modelos.

Esta camada será a base para futuras funcionalidades como:

- Agentes inteligentes.
- Memória contextual.
- Sistemas de recuperação de conhecimento (RAG).
- Integração com ferramentas externas.
- Orquestração de múltiplos modelos.

---

# Objetivos

A Infraestrutura de IA possui os seguintes objetivos:

- Centralizar a comunicação com modelos de linguagem.
- Abstrair provedores de IA.
- Permitir troca de modelos sem impacto na aplicação.
- Facilitar testes e manutenção.
- Preparar a arquitetura para evolução futura.
- Garantir baixo acoplamento entre módulos.

---

# Arquitetura

A arquitetura segue um modelo baseado em camadas:

```text
                 Copilot
                     │
        ┌────────────┼────────────┐
        │            │            │
     Agentes      Memória       RAG
        │            │            │
        └────────────┼────────────┘
                     │
        Infraestrutura de IA
              (AI Runtime)
                     │
              Model Manager
                     │
        ┌────────────┼────────────┐
        │                         │
     Providers            Configuração
        │
   ┌────┴────┐
   │         │
 Ollama   Futuros Providers
   │
 Modelos LLM

 Componentes
Model Manager

Responsável pelo gerenciamento da comunicação entre a aplicação e os modelos de IA.

Responsabilidades:

Gerenciar solicitações aos modelos.
Controlar acesso aos Providers.
Abstrair detalhes de implementação.
Permitir troca de modelos.
Centralizar configurações de execução.
Providers

Representam as integrações com diferentes runtimes ou serviços de IA.

Responsabilidades:

Implementar comunicação com modelos.
Adaptar diferentes APIs.
Controlar detalhes específicos de cada provedor.
Retornar respostas padronizadas.

Provider inicial:

Ollama

Provedores futuros:

OpenAI
Azure OpenAI
LM Studio
Outros runtimes locais ou externos
Sistema de Configuração

Responsável por centralizar parâmetros relacionados à execução dos modelos.

Exemplos:

Modelo ativo.
Provider utilizado.
Parâmetros de geração.
Configurações do runtime.
Chat Service

Serviço responsável pela comunicação inicial entre a aplicação e o AI Runtime.

Responsabilidades:

Receber solicitações.
Encaminhar mensagens ao Model Manager.
Processar respostas.
Servir como base para futuras interfaces conversacionais.
Fluxo de Comunicação
Usuário
  │
  ▼
Aplicação
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
Integração com Outros Módulos
Agentes

Os agentes utilizarão o AI Runtime para acessar modelos de linguagem.

Os agentes não terão conhecimento sobre:

Modelo utilizado.
Provider.
Runtime de execução.
Memória

A camada de memória utilizará o AI Runtime para:

Resumo de informações.
Consolidação de conhecimento.
Recuperação contextual.
RAG

O sistema RAG utilizará o AI Runtime para:

Geração de respostas.
Interpretação de contexto.
Síntese de informações recuperadas.
Princípios Arquiteturais
Baixo Acoplamento

Nenhum componente deve depender diretamente de um modelo ou fornecedor específico.

Extensibilidade

Novos modelos e provedores devem ser adicionados sem alterar componentes existentes.

Separação de Responsabilidades

Cada componente deve possuir uma responsabilidade clara.

Testabilidade

Os componentes devem permitir testes isolados.

Evolução Futura

A Infraestrutura de IA será expandida para suportar:

Múltiplos modelos simultâneos.
Seleção dinâmica de modelos.
Memória de longo prazo.
Agentes especializados.
Ferramentas externas.
Avaliação automática de respostas.
Orquestração avançada de agentes.
Referências
ADR-001 — Arquitetura da Infraestrutura de IA (AI Runtime)
Milestone 3 — Fundação da Infraestrutura de IA