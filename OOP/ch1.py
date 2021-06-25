def edureka():
    def local_func():
        name = "Python"
    def non_local():
        nonlocal name
        name = "Python programming"
    def global_func():
        global name
        name = "Data Science"
    name = "edureka"
    print(name)
    local_func()
    print(name)
    non_local()
    print(name)
    global_func()
    print(name)

edureka()
print(name)