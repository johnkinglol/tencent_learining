#!/usr/bin/env python
# coding=utf-8
import math

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


def power(x, n=2):
    s, i = 1, 0
    while i < n:
        s = s * x
        i = i + 1

    return s

def prime(x):
    i = 2
    while i < int(math.sqrt(x) + 1):
        if x % i == 0:
            return False
        i = i + 1

    return True


if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d.get('a'))
    L = {'Hello', 'World', 18, 'Apple', 'Watch', None}
    s = ""
    for l in L:
        if isinstance(l, str):
            s = s + l.lower() + " "
    print(s)

    gen = fib(10)
    for x in gen:
        print(x)
    o = odd()
    print(o.next())

    list = [1, 2, 3, 4, 5]
    result = map(str, list)
    print(result)
    list = range(2, 100)
    result = filter(prime, list)
    print(result)
