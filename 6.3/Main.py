
def cached(func):
    def wrapper(arg):
        if not hasattr(cached, 'prev_arg'):
            cached.prev_arg = arg

        if cached.prev_arg == arg and hasattr(cached, 'prev_val'):
            return cached.prev_val
        else:
            cached.prev_arg = arg
            cached.prev_val = func(arg)
            return cached.prev_val

    return wrapper


@cached
def inc(i):
    print(i + 1)
    return i + 1

inc(2)
inc(3)
inc(2)
inc(2)
