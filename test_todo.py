import pytest
from todo import TodoList


def test_add_task():
    todos = TodoList()
    todos.add("Buy milk")
    assert todos.list_open() == ["Buy milk"]


def test_add_empty_task_raises():
    todos = TodoList()
    with pytest.raises(ValueError):
        todos.add("   ")


def test_complete_task():
    todos = TodoList()
    todos.add("Buy milk")
    todos.complete(0)
    assert todos.list_open() == []


def test_remove_task():
    todos = TodoList()
    todos.add("Buy milk")
    todos.add("Walk dog")
    todos.remove(0)
    assert todos.list_open() == ["Walk dog"]


def test_list_all_shows_status():
    todos = TodoList()
    todos.add("Buy milk")
    todos.complete(0)
    assert todos.list_all() == [{"task": "Buy milk", "done": True}]
