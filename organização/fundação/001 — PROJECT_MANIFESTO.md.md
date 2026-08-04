Documento............. PROJECT_MANIFESTO.md
Categoria............. Fundação
Status................ Documento Constitucional
Autor................. Vagner Ferreira
Controle.............. Manual
Versão................ 1.0
Criado em............. 2026-08-04


# AI Engineering Learning OS

# Documento Fundador

## A Ideia Inicial do Projeto

### Versão 0.1

---

# Introdução

O AI Engineering Learning OS nasceu da necessidade de criar um assistente de inteligência artificial que fosse muito além de um chatbot.

A ideia nunca foi desenvolver apenas mais um sistema baseado em LLMs.

O objetivo sempre foi construir um companheiro de engenharia capaz de acompanhar continuamente o usuário durante seus estudos, projetos e desenvolvimento de software.

O projeto nasce como uma jornada de aprendizado em Engenharia de IA, onde cada componente será compreendido, desenvolvido e evoluído gradualmente.

Mais do que construir uma ferramenta, o objetivo é compreender profundamente como um verdadeiro assistente inteligente pode ser criado.

---

# A Inspiração

A inspiração do projeto vem do conceito representado pelo JARVIS.

Não no sentido fictício de uma inteligência artificial perfeita, mas na ideia de um assistente pessoal que:

* acompanha o usuário continuamente;
* compreende seus projetos;
* lembra decisões importantes;
* aprende com o tempo;
* auxilia durante o desenvolvimento;
* evolui junto com seu criador.

O assistente deve se tornar uma extensão da capacidade técnica do usuário.

---

# A Filosofia

O projeto parte de um princípio simples.

Uma IA poderosa não é apenas um modelo de linguagem.

Ela é o resultado da integração entre diversos componentes trabalhando juntos.

O modelo LLM será apenas uma parte do sistema.

A verdadeira inteligência surgirá da combinação entre:

* memória persistente;
* recuperação de conhecimento;
* contexto dos projetos;
* ferramentas;
* histórico;
* arquitetura modular;
* especializações.

O objetivo não é possuir o maior modelo.

O objetivo é possuir o melhor assistente.

---

# O Primeiro Passo

O projeto começará de forma simples.

A primeira versão terá apenas uma missão:

Construir um Assistente Pessoal de IA Local.

Todo o desenvolvimento inicial acontecerá utilizando modelos executados localmente.

Essa decisão foi tomada para permitir compreender profundamente toda a infraestrutura necessária para sistemas baseados em LLMs, mantendo privacidade, controle e independência tecnológica.

---

# O Papel do Modelo Local

O modelo local não será considerado a inteligência definitiva do sistema.

Ele será o mecanismo responsável pela linguagem e pelo raciocínio.

A evolução do assistente acontecerá principalmente através da arquitetura construída ao redor do modelo.

Por esse motivo, limitações naturais dos modelos locais não representam um problema.

O conhecimento será expandido continuamente por outros componentes da plataforma.

---

# Como o Assistente Aprenderá

O assistente não será treinado novamente sempre que novas informações forem adicionadas.

Seu crescimento acontecerá através de memória externa.

Documentos, livros, artigos, PDFs e documentações serão processados em uma Base de Conhecimento.

Esse processo deverá seguir uma arquitetura semelhante a:

Documento

↓

Extração de conteúdo

↓

Divisão em partes (Chunks)

↓

Embeddings

↓

Banco Vetorial

↓

Resumo Inteligente

↓

Memória Persistente

Em vez de modificar os pesos do modelo, o sistema aprenderá recuperando conhecimento relevante sempre que necessário.

---

# Memória Inteligente

Nem toda informação deve ser armazenada.

O assistente deverá ser capaz de decidir o que representa conhecimento permanente e o que deve permanecer apenas como contexto temporário.

Informações importantes poderão se transformar em memória.

Exemplos:

* decisões arquiteturais;
* preferências do usuário;
* padrões de desenvolvimento;
* aprendizados importantes;
* documentação criada.

Conversas comuns não deverão aumentar indefinidamente a memória do sistema.

A qualidade da memória será mais importante que sua quantidade.

---

# Base de Conhecimento

A Base de Conhecimento será construída continuamente.

Cada documento poderá gerar:

* representação vetorial;
* resumo estruturado;
* palavras-chave;
* relacionamentos;
* contexto.

No futuro, o assistente poderá consultar milhares de documentos sem depender exclusivamente da memória do modelo.

---

# Especializações

Além da memória, o assistente deverá possuir capacidades especializadas.

Essas capacidades poderão ser implementadas através de Skills.

As Skills representam conhecimentos procedurais especializados.

Cada Skill ensinará ao assistente como resolver determinado tipo de problema.

Exemplos:

* Python;
* Arquitetura;
* Engenharia de Software;
* Data Science;
* Machine Learning;
* Git;
* Documentação;
* Testes;
* Prompt Engineering.

Inicialmente poderão ser utilizadas Skills públicas como referência.

No futuro, o próprio projeto possuirá sua própria biblioteca de Skills, construída ao longo de sua evolução.

---

# O Papel do Visual Studio Code

Durante a primeira versão, o Visual Studio Code será o ambiente principal do assistente.

Ele deverá compreender:

* projetos;
* arquivos;
* documentação;
* código;
* histórico de desenvolvimento.

O VS Code representa apenas a primeira interface do sistema.

---

# Evolução Futura

O objetivo final não é permanecer restrito ao Visual Studio Code.

No futuro, o assistente poderá evoluir para uma aplicação instalada no próprio sistema operacional.

Esse aplicativo poderá permanecer ativo continuamente, funcionando como um serviço local.

Nesse estágio, o assistente poderá auxiliar não apenas no desenvolvimento de software, mas também em tarefas pessoais e profissionais, como organização de documentos, gerenciamento de tarefas, integração com ferramentas, automações e outras capacidades.

Independentemente da interface utilizada, o núcleo do sistema permanecerá o mesmo.

---

# O Verdadeiro Objetivo

O AI Engineering Learning OS não busca construir apenas uma inteligência artificial.

Seu objetivo é criar um companheiro técnico permanente.

Um sistema que acompanhe seu criador durante anos, evoluindo junto com seus conhecimentos, seus projetos e sua experiência.

Cada projeto desenvolvido, cada documento estudado e cada decisão importante contribuirão para tornar o assistente mais útil.

A evolução acontecerá através da arquitetura, da memória, do conhecimento acumulado e das capacidades adicionadas ao longo do tempo.

O projeto nasce pequeno.

Mas sua visão é de longo prazo.

Não será apenas um software.

Será uma plataforma pessoal de inteligência construída continuamente junto com seu criador.


Estrutura que vamos seguir
Esse é o desenho que vamos seguir da estrutura das pastas e arquivos. 


AI-Engineering-Learning-OS/

│

├── app/
│   ├── api/
│   ├── frontend/
│   ├── cli/
│   └── vscode/
│
├── core/
│   ├── orchestrator/
│   ├── workflow/
│   ├── router/
│   ├── planner/
│   ├── scheduler/
│   └── runtime/
│
├── agents/
│   ├── teacher/
│   ├── reviewer/
│   ├── architect/
│   ├── programmer/
│   ├── debugger/
│   ├── documenter/
│   ├── researcher/
│   ├── git/
│   ├── python/
│   ├── sql/
│   ├── docker/
│   ├── ai/
│   └── custom/
│
├── rag/
│   ├── ingestion/
│   ├── chunking/
│   ├── indexing/
│   ├── retrieval/
│   ├── reranking/
│   ├── routing/
│   ├── query_translation/
│   ├── hybrid_search/
│   └── generation/
│
├── memory/
│   ├── conversation/
│   ├── learning/
│   ├── profile/
│   ├── projects/
│   ├── long_term/
│   └── cache/
│
├── knowledge/
│   ├── python/
│   ├── git/
│   ├── docker/
│   ├── sql/
│   ├── ai/
│   ├── projects/
│   ├── docs/
│   └── personal/
│
├── databases/
│   ├── postgres/
│   ├── chroma/
│   ├── graph/
│   ├── cache/
│   └── metadata/
│
├── models/
│   ├── llm/
│   ├── embedding/
│   ├── reranker/
│   ├── vision/
│   └── tokenizer/
│
├── prompts/
│   ├── system/
│   ├── agents/
│   ├── tasks/
│   ├── workflows/
│   └── templates/
│
├── tools/
│   ├── filesystem/
│   ├── terminal/
│   ├── git/
│   ├── browser/
│   ├── python/
│   ├── database/
│   └── vscode/
│
├── skills/
│   ├── programming/
│   ├── learning/
│   ├── writing/
│   ├── architecture/
│   └── custom/
│
├── workspace/
│
├── config/
│
├── docs/
│
├── tests/
│
└── logs/


# Governança do Documento

Este documento representa a visão fundadora do AI Engineering Learning OS.

Ele registra a motivação original, os princípios e a direção estratégica definidos pelo criador do projeto.

## Regras Permanentes

1. Este documento é considerado um Documento Constitucional do projeto.

2. Seu conteúdo nunca deverá ser reescrito, resumido ou substituído automaticamente por qualquer ferramenta de IA.

3. Novas informações poderão ser adicionadas apenas como complementos, preservando integralmente o histórico existente.

4. Nenhuma seção deverá ser removida sem autorização explícita do proprietário do projeto.

5. Alterações estruturais somente poderão ser realizadas mediante solicitação direta do proprietário.

6. Assistentes de IA poderão utilizar este documento como referência, mas nunca deverão modificar seu conteúdo por iniciativa própria.

7. Em caso de conflito entre este documento e documentos mais recentes, este documento deverá ser tratado como a referência histórica da visão original do projeto.

Status:
Documento Protegido

Autor 
vagner Ferreira 