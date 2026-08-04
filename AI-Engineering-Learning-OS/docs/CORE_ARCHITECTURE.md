# Core System Architecture

## Overview

The Core System represents the execution foundation of the Jarvis AI Engineering Learning OS.

Its responsibility is to coordinate requests, planning, execution, and interaction between agents, tools, memory systems, and workflows.

The Core does not contain domain knowledge.
It provides the execution infrastructure that enables intelligent behavior.

---

# Core Responsibilities

The Core System is responsible for:

- Request routing
- Task planning
- Execution orchestration
- Runtime context management
- Workflow coordination
- Internal scheduling

---

# Core Architecture

User Request

  |
  v

Router

  |
  v

Planner

  |
  v

Orchestrator

  |
  +----------------+
  |                |
  v                v

Runtime Workflow

  |
  v

Agents / Tools

  |
  v

Result


---

# Core Modules

## Router

Location:


core/router


Responsibility:

Determine the correct execution path for incoming requests.

Responsibilities:

- classify requests
- identify required capability
- select execution strategy

The Router does not execute tasks.

---

## Planner

Location:


core/planner


Responsibility:

Transform complex requests into structured execution plans.

Responsibilities:

- task decomposition
- step generation
- dependency identification

---

## Orchestrator

Location:


core/orchestrator


Responsibility:

Coordinate execution between system components.

Responsibilities:

- manage execution flow
- invoke agents
- coordinate tools
- collect results

---

## Runtime

Location:


core/runtime


Responsibility:

Maintain execution context.

Responsibilities:

- session state
- execution metadata
- temporary context
- lifecycle management

---

## Workflow

Location:


core/workflow


Responsibility:

Define reusable execution processes.

Examples:

- software development workflow
- documentation workflow
- research workflow

---

## Scheduler

Location:


core/scheduler


Responsibility:

Manage scheduled internal operations.

Examples:

- periodic tasks
- automated routines
- background processes

---

# Architectural Principles

## Separation of Responsibilities

Each module must have a single clear responsibility.

---

## Modular Evolution

Components should evolve independently.

---

## Test First

Every core component must include automated tests.

---

## Documentation First

Architectural decisions must be documented before implementation.

---

# Initial Execution Flow

Example:

Input:


Create a Python API project


Flow:


Request

↓

Router

↓

Planner

↓

Orchestrator

↓

Programming Agent

↓

Runtime

↓

Result


---

# Future Extensions

The Core System will later integrate:

- Memory System
- Knowledge System
- Agent Framework
- Tool Registry
- LLM Providers

