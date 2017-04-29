import sys
import functools


def takes(*type_args):
    def sub_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            for i in range(min(len(type_args), len(args))):
                if not isinstance(args[i], type_args[i]):
                    raise TypeError
            return func(*args)
        return wrapper
    return sub_decorator

exec(sys.stdin.read())


@takes(int, str, )
def f(a, b):
    print(a, b)
