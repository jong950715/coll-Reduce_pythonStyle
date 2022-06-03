from reducers import *


class MyIter(list):
    def __init__(self, iterable):
        super().__init__()
        for x in iterable:
            if isinstance(x, Iterable):
                self.append(MyIter(x))
            else:
                self.append(x)

    def coll_reduce(self, reduceF, init):
        return internal_reduce(self, reduceF, init)

    def my_map(self, mapF):  # just for python style not clojure impl
        return my_map(mapF, self)

    def my_flatten(self):  # just for python style not clojure impl
        return my_flatten(self)
