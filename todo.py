"""A tiny in-memory to-do list app. Simple on purpose — this exists to
give a CI/CD pipeline something real to build and test."""


class TodoList:
    def __init__(self):
        self.items = []

    def add(self, task: str) -> None:
        if not task or not task.strip():
            raise ValueError("Task cannot be empty")
        self.items.append({"task": task.strip(), "done": False})

    def complete(self, index: int) -> None:
        self.items[index]["done"] = True

    def remove(self, index: int) -> None:
        self.items.pop(index)

    def list_open(self) -> list:
        return [item["task"] for item in self.items if not item["done"]]

    def list_all(self) -> list:
        return self.items


def main():
    todos = TodoList()
    todos.add("Prep BCG Platinion case interview")
    todos.add("Set up CI/CD pipeline")
    todos.complete(0)

    print("All tasks:")
    for item in todos.list_all():
        status = "✓" if item["done"] else " "
        print(f"[{status}] {item['task']}")


if __name__ == "__main__":
    main()
