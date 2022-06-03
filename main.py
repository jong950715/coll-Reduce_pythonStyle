from typing import Iterable
from MyIter import *
from my_operator import *

from reducers import *


def reduceExample():
    coll = MyIter([1, 2, 3, 4, 5, 6])
    res1 = my_reduce(add, 5, coll)

    print("\nreduce example")
    print("reduce res1 :", res1)


def mapExample():
    coll = MyIter([1, 2, 3, 4, 5, 6])
    res1 = my_reduce(conj, [], my_map(add1, coll))
    res2 = my_reduce(add, 0, my_map(add1, coll))

    print("\nmap example")
    print("map res1 : ", res1)
    print("map res2 : ", res2)


def flattenExample():
    coll = MyIter([1, 2, [3, [4, [5]], 6]])
    res1 = my_reduce(conj, [], my_flatten(coll))
    res2 = my_reduce(add, 0, my_flatten(coll))

    print("\nflatten example")
    print("flatten res1 : ", res1)
    print("flatten res2 : ", res2)


def methodLinkStype():
    coll = MyIter([1, 2, [3, [4, 5], 6]])
    res = coll.my_flatten().my_reduce(conj, MyIter([])).my_map(add1).my_reduce(conj, [])  # python style

    print("\npretty example")
    print("link style res : ", res)


def main():
    reduceExample()
    mapExample()
    flattenExample()
    methodLinkStype()


if __name__ == '__main__':
    main()
