from abc import ABCMeta, abstractmethod
from typing import Iterable


def internal_reduce(coll, func, init):
    res = init
    for s in coll:
        res = func(res, s)

    return res


class CollReduce(metaclass=ABCMeta):  # abstract class
    @abstractmethod
    def coll_reduce(self, f1, init):  # abstract method must be override
        pass


def make_reducer(reducible, transformF):
    class AnonClass(CollReduce):
        def __init__(self):
            pass

        def coll_reduce(self, f1, init):
            return reducible.coll_reduce(transformF(f1), init)

        def my_reduce(coll, reduceF, init):
            return coll.coll_reduce(reduceF, init)

    return AnonClass()


def my_reduce(reduceF, init, coll):
    return coll.coll_reduce(reduceF, init)


def my_map(mapF, reducible):
    def reducingStrategy(reduceF):
        # when acc, v is given
        def _mapWithReduce(acc, v):
            return reduceF(acc, mapF(v))

        return _mapWithReduce

    # return make_reducer(reducible, lambda reduceF: lambda acc, v: reduceF(acc, mapF(v)))
    return make_reducer(reducible, reducingStrategy)


def my_flatten(reducible):
    def reducingStrategy(reduceF):
        def _flattenWithReduce(acc, v):
            if isinstance(v, Iterable):
                return my_flatten(v).coll_reduce(reduceF, acc)
            else:
                return reduceF(acc, v)

        return _flattenWithReduce

    # return make_reducer(reducible, lambda reduceF: lambda acc, v: reduceF(acc, mapF(v)))
    return make_reducer(reducible, reducingStrategy)