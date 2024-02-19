# F7rSt-CLaSS FUnCt7ons：
# "A Programming language is said to have first-class functions if it treats functions as first-class citizens."
# First-Class Citizen (Programming:
# "A first-class citizen (sometimes called first-class obiects) in a programming language is an entity which supports all the
# operations generally available to other entities.
# These operations typically include
# being passed as an argument, returned from a
# function, and assigned to a variable


# def square(x):
#     return x*x

# print(square(3))




# def square(x):
#     return x * x


# def my_map(func, args_list):
#     result = []
#     for i in args_list:
#         result.append(func(i))
#     return result


# squares = my_map(square , [1,2,3,4,5])

# print(squares)


#Loading...
def log_msg(msg):

    def logger_message():
        print("Log:" , msg)
    return logger_message

log_hi= log_msg("babe")
log_hi()
