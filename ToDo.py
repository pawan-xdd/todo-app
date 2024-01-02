# todos = []
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
text = """
Principles of Productivity:
Managing your inflow.
Systemizing everything that repeats.
"""

while True:
    # Get User input and strip space characters from it
    user_action = input("Type Add, Show , Edit, Complete or Exit: ")
    user_action = user_action.strip()
    # match user_action:

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith('add'):

        # todo = input("Enter A ToDo: ") + "\n"
        todo = user_action[4:] + '\n'
        # file = open('files/subfiles/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = get_todos()
        # with open('files/subfiles/todos.txt', 'r') as file:
        #   todos = file.readlines()

        todos.append(todo)

        # file = open('files/subfiles/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        # with open('files/subfiles/todos.txt', 'w') as file:
        #    file.writelines(todos)
        write_todos(todos)

    # elif 'show' in user_action:
    elif user_action.startswith('show'):
        # file = open('files/subfiles/todos.txt', 'r')
        # todos = file.readlines()
        #  file.close()
        # with open('files/subfiles/todos.txt', 'r') as file:
        #  todos = file.readlines()

        # new_todos = []

        # for item in todos:
        # new_item = item.strip('\n')
        # new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item.title()}")
        # print(f"Length is ,{index + 1}")

    # elif 'edit' in user_action:
    elif user_action.startswith('edit'):
        try:
            # number = int(input("Number of the todo to edit: "))
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            # with open('files/subfiles/todos.txt', 'r') as file:
            #   todos = file.readlines()

            # print('Here is existing todos: ', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            # print('Here is how it will be: ', todos)

            # with open('files/subfiles/todos.txt', 'w') as file:
            #    file.writelines(todos)
            write_todos(todos)
            # existing_todo = todos[number]
            # print(new_todo)
        except ValueError:
            print("Your command is not valid.")
            continue

    # elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        try:
            # number = int(input("Number of the todo to complete: "))
            number = int(user_action[9:])

            todos = get_todos()

            # with open('files/subfiles/todos.txt', 'r') as file:
            #    todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # with open('files/subfiles/todos.txt', 'w') as file:
            #  file.writelines(todos)
            write_todos(todos)

            message = f"Todo : {todo_to_remove.capitalize()} was removed from the list."
            print(message)
        except IndexError:
            print(f"There is no item with that number.")
            continue

    # elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not Valid.")
        # case _:
        # print("Hey, You Entered An unknown Command.")
# print(todos)
print("Bye!")

# print(todo)
# print("next..")
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3, 'hello']
# print(todos)

# print(type(todos))
