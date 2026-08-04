from core.runtime import AgentContext, AgentRuntime


def test_create_agent_context():
    context = AgentContext(
        task="Test Jarvis runtime"
    )

    assert context.status == "created"
    assert context.task == "Test Jarvis runtime"


def test_runtime_execution():

    runtime = AgentRuntime()

    context = runtime.create_context(
        "Execute test task"
    )

    result = runtime.execute(context)

    assert result.status == "completed"
    assert result.result == (
        "Task completed: Execute test task"
    )


def test_context_lifecycle():

    context = AgentContext(
        task="Lifecycle test"
    )

    context.start()

    assert context.status == "running"

    context.complete(
        "Finished"
    )

    assert context.status == "completed"
    assert context.result == "Finished"