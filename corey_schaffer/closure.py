
#inner func has access to its local scope variable even when outer func is executed

# def outer_func():
#     message = "hi"

#     def inner_func():
#         print(message)
#         return message

#     return inner_func()

# my_func = outer_func()

# print(my_func)


# hi_func = outer_func("HI")
# hello_func = outer_func("Hello")


# def sorting(arr, parameter=""):
#     func(arr)

#     def _sorting():
    
#     return _sortin(arr)

def outer_func():
    message = "Hi"

    def inner_func():
        return message

    return inner_func()

my_func = outer_func()

print(my_func)


def logger(func):
    def inner_logger(*args):
        logging.info()