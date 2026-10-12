tasks = []


def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
    }
    tasks.append(task)
    return task

def list_tasks():
    """Return all tasks currently stored in memory."""
    return tasks

if __name__ == "__main__":
    add_task("Learn Git and GitHub")
    add_task("Create my first Pull Request")

    print(list_tasks())