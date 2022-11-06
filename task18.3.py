class TypeDecorator:
    @staticmethod
    def to_int(func):
        def wrapper(*args, **kwargs):
            try:
                result = int(func(*args, **kwargs))
                return result
            except:
                return TypeError("Cannot convert to int")
        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args, **kwargs):
            try:
                result = str(func(*args, **kwargs))
                return result
            except:
                return TypeError("Cannot convert to str")
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(value):
            try:
                result = bool(func(value))
                return result
            except:
                return TypeError("Cannot convert to bool")
        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args, **kwargs):
            try:
                result = float(func(*args, **kwargs))
                return result
            except:
                return TypeError("Cannot convert to float")
        return wrapper


@TypeDecorator.to_int
def to_do_int(string: str):
   return string

@TypeDecorator.to_str
def to_do_str(string: str):
   return string

@TypeDecorator.to_bool
def to_do_bool(string: str):
   return string

@TypeDecorator.to_float
def to_do_float(string: str):
   return string

print(type(to_do_int('25')))
print(to_do_int('25'))

print(type(to_do_str(55)))
print(to_do_str(55))

print(type(to_do_bool('4')))
print(to_do_bool('4'))

print(type(to_do_float('sf')))
print(to_do_float('-5'))

