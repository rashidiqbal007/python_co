def outer_func(msg):
    def inner_func():
        print(msg)
        # lets remove execution () in inner_func(), now outer_func() executes and waits for inner_func to execute.
        # it cant execute without (), so neeche we would make outer_func() = my_func and execute inner_func by my_func()
    return inner_func



# decorator function below
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("see")
        return original_function(*args, **kwargs)
    return wrapper_function


# @means decorator_function will take display func as an argument.
@decorator_function  
def display_info(name, age):
    print("This is the display info function. ({}, {})".format(name, age))

display_info("cute",2)

@decorator_function
def display():
    print("this is the display func wrapped in decorator func.")

display()
# decorator_function_display = decorator_function(display) same as @decorator_function
# decorator_function_display()





# hi_func = outer_func("hi babe")
# hello_func = outer_func("hello babe")
# hi_func()

