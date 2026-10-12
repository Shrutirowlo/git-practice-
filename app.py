tasks = []


def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
    }
    tasks.append(task)
    return task


if __name__ == "__main__":
    print(add_task("Learn Git and GitHub"))
    print(tasks)