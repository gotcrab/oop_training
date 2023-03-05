class Task:
    def __init__(self, name , description, status=False):
        self.name = name
        self.description = description
        self.status = status

    def display(self):
        if self.status:
            return print(f'{self.name} (Сделана)')

        return print(f'{self.name} (Не сделана)')

    def __repr__(self) -> str:
        return f'''
        class Task,
        Name: {self.name},
        Discription: {self.description},
        Status: {self.status}
'''


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

class TaskManager:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def mark_done(self, task: Task):
        if task in self.task_list.tasks:
            task.status = True

    def mark_undone(self, task: Task):
        if task in self.task_list.tasks:
            task.status = False

    def show_tasks(self):
        for task in self.task_list.tasks:
            task.display()


if __name__ == '__main__':
    # Создаем список задач
    todo = TaskList()
    assert todo.tasks == []

    # Создаем несколько задач и добавляем их в список
    task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
    assert task1.name == 'Стирка'
    assert task1.description == 'Постирать трусы, носки, слюнявчики'
    assert task1.status is False

    task1.display()


    print('Wow')
    print(task1.description)

    todo.add_task(task1)
    assert len(todo.tasks) == 1


    task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
    assert task2.name == 'Продукты'
    assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
    assert task2.status is False
    print(task2.description)
    print(task2.status)

    todo.add_task(task2)
    assert len(todo.tasks) == 2

    # Создаем менеджер задач и показываем список задач
    manager = TaskManager(todo)
    assert isinstance(manager.task_list, TaskList)
    print('-----Список дел-----')
    manager.show_tasks()

    # Отмечаем первую задачу выполненной и показываем список задач
    manager.mark_done(task1)

    # Проверяем изменился ли статус 2мя способами
    assert task1.status is True
    assert manager.task_list.tasks[0].status is True
    print(task1.status)
    print(task2.status)

    # print(manager.task_list.tasks)
    print('-----Список дел-----')
    manager.show_tasks()

    # Удаляем вторую задачу и показываем список задач
    # todo.remove_task(task2)
    #
    # assert len(todo.tasks) == 1
    # assert len(manager.task_list.tasks) == 1
    # print('Wow')
    #
    # print('-----Список дел-----')
    # manager.show_tasks()
    # print('Wow')
