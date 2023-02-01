def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@decorator
def hello():
    name = input("Введите имя: ")
    return name


print("Привет, ", hello())
