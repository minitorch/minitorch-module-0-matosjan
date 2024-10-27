"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x: float, y: float) -> float:
    """$f(x, y) = x * y$"""
    return x * y


def id(x: float) -> float:
    """$f(x) = x$"""
    return x


def add(x: float, y: float) -> float:
    """$f(x, y) = x + y$"""
    return x + y


def neg(x: float) -> float:
    """$f(x) = -x$"""
    return -x


def lt(x: float, y: float) -> float:
    """$f(x, y) =$ 1.0 if x is less than y, else 0.0"""
    return float(x < y)


def eq(x: float, y: float) -> float:
    """$f(x, y) =$ 1.0 if x is equal to y, else 0.0"""
    return float(x == y)


def max(x: float, y: float) -> float:
    """$f(x, y) =$ x if x is greater than y, else y"""
    if x > y:
        return x
    return y


def is_close(x: float, y: float) -> float:
    """$f(x, y) = |x - y| < 1e-2$"""
    return float(abs(x - y) < 1e-2)


def sigmoid(x: float) -> float:
    r"""$f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$"""
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    return math.exp(x) / (1 + math.exp(x))


def relu(x: float) -> float:
    """$f(x) =$ x if x is greater than 0, else 0"""
    return max(x, 0)


def log(x: float) -> float:
    """$f(x) = log(x)$"""
    return math.log(x + 1e-6)


def exp(x: float) -> float:
    """$f(x) = e^{x}$"""
    return math.exp(x)


def inv(x: float) -> float:
    """$f(x) = 1/x$"""
    return 1 / x


def log_back(x: float, d: float) -> float:
    """$f(x, d) =$ derivative of log times d"""
    return d / x


def inv_back(x: float, d: float) -> float:
    """$f(x, d) =$ derivative of reciprocal times d"""
    return -(d / x**2)


def relu_back(x: float, d: float) -> float:
    """$f(x, d) =$ derivative of relu times d"""
    if relu(x) == 0:
        return 0
    return d


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.


def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """Higher-order map.

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
    ----
        fn: Function from one value to one value.

    Returns:
    -------
         A function that takes a list, applies `fn` to each element, and returns a
         new list

    """
    return lambda x: [fn(y) for y in x]


def zipWith(
    fn: Callable[[float, float], float],
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """Higher-order zipwith (or map2).

    See https://en.wikipedia.org/wiki/Map_(higher-order_function)

    Args:
    ----
        fn: combine two values

    Returns:
    -------
         Function that takes two equally sized lists `ls1` and `ls2`, produce a new list by
         applying fn(x, y) on each pair of elements.

    """
    return lambda x, y: [fn(a, b) for a, b in zip(x, y)]


def reduce(
    fn: Callable[[float, float], float], start: float
) -> Callable[[Iterable[float]], float]:
    r"""Higher-order reduce.

    Args:
    ----
        fn: combine two values
        start: start value $x_0$

    Returns:
    -------
         Function that takes a list `ls` of elements
         $x_1 \ldots x_n$ and computes the reduction :math:`fn(x_3, fn(x_2,
         fn(x_1, x_0)))`

    """

    def helper_fn(ls: Iterable[float]) -> float:
        res = start
        for val in ls:
            res = fn(res, val)
        return res

    return helper_fn


def negList(ls: Iterable[float]) -> Iterable[float]:
    """Use `map` and `neg` to negate each element in `ls`"""
    return map(neg)(ls)


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    """Add the elements of `ls1` and `ls2` using `zipWith` and `add`"""
    return zipWith(add)(ls1, ls2)


def sum(ls: Iterable[float]) -> float:
    """Sum up a list using `reduce` and `add`."""
    return reduce(add, 0)(ls)


def prod(ls: Iterable[float]) -> float:
    """Product of a list using `reduce` and `mul`."""
    return reduce(mul, 1)(ls)
