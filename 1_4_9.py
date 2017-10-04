# namespaces is dict of pairs namespace:parent
namespaces = {"_":"global"}
# variables is dict of pairs variable:namespace
variables = {}

def create(namespace, parent):
    namespaces.update({namespace:parent})
    if namespaces.get(namespace) == None:
        namespaces[parent].append(namespace)
        namespaces[namespace].append("")

def add (namespace, var):
    variables.update({namespace})

def get(namespace, var):
    name = namespaces.get(namespace)
    if name == None && namespace == "global":
        print("None")


# First input value is number of pending commands
n = input()
for i in n():
    # var can be either parent namespace or variable name
    command, namespace, var = input('Enter 3 variables: ').split()
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
        get(namespace, var)
    else:
        print("Unknown command")
