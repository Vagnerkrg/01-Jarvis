from core.planner import Plan, Planner


def test_create_plan():

    planner = Planner()

    plan = planner.create_plan(
        "Construir agente de pesquisa"
    )

    assert isinstance(plan, Plan)
    assert plan.goal == "Construir agente de pesquisa"


def test_add_tasks_to_plan():

    planner = Planner()

    plan = planner.create_plan(
        "Criar agente"
    )

    planner.add_task(
        plan,
        "Criar ferramentas"
    )

    planner.add_task(
        plan,
        "Implementar agente"
    )

    assert len(plan.steps) == 2
    assert plan.steps[0] == "Criar ferramentas"
    assert plan.steps[1] == "Implementar agente"