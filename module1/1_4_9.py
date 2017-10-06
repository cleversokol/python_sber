# namespaces is dict of pairs namespace:parent
namespaces = {}
# variables is dict of pairs namespace:[list of variables]
variables = {"global":[]}

def create(namespace, parent):
    namespaces.update({namespace:parent})
    variables.update({namespace:[]})

def add (namespace, var):
    variables[namespace].append(var)

def get(namespace, var):
    list = variables.get(namespace)
    if var in list:
        return namespace
    elif namespace == "global":
        return "None"
    else:
        namespace = namespaces.get(namespace)
        return get(namespace, var)

# First input value is number of pending commands
n = int(input())
for i in range(n):
    # var can be either parent namespace or variable name
    command, namespace, var = input().split()
    if command == "create":
        # create <namespace> <parent> –  создать новое пространство имен
        # с именем <namespace> внутри пространства <parent>
        create(namespace, var)
    elif command == "add":
        # add <namespace> <var> – добавить в пространство <namespace> переменную <var>
        add(namespace, var)
    elif command == "get":
        # get <namespace> <var> – получить имя пространства,
        # из которого будет взята переменная <var> при запросе из пространства <namespace>,
        # или None, если такого пространства не существует
        print(get(namespace, var))
    else:
        print("Unknown command")
