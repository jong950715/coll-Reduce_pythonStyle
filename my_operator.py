from MyIter import MyIter


def partial(func, *args):
    def res(*_args):
        nArgs = list(_args)
        nArgs.extend(args)
        return func(*nArgs)

    return res


def add(a, b):
    return a + b


def add1(a):
    return add(a, 1)
# add1 = partial(add, 1)


def conj(a, b):
    a = MyIter(a)
    a.append(b)
    return a
