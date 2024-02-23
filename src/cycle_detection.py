"""
Cycle Detection
---------------

Cycle detection or cycle finding is the algorithmic problem of finding a cycle
in a sequence of iterated function values.

    For any function f that maps a finite set S to itself, and any initial
    value x0 in S, the sequence of iterated function values must eventually use
    the same value twice. Furthermore, there must be some pair of distinct
    indices i and j such that xi = xj. Once this happens, the sequence must
    continue periodically, by repeating the same sequence of values from xi to
    xj − 1. Cycle detection is the problem of finding i and j, given f and x0.

Question:

    Why must the sequence of iterated function values eventually use the same
    value twice?

Answer:

    This is a consequence of the Pigeonhole Principle, which essentially states
    that if you have more pigeons than pigeonholes, at least one pigeonhole
    must contain more than one pigeon. Applied to this scenario, the "pigeons"
    are the iterated function values, and the "pigeonholes" are the elements of
    the finite set S.

    Because S is finite and you are continually generating new values from
    within S, you can only generate at most n unique values before you have to
    "reuse" a value, due to the finiteness of S. Once a value is reused, the
    sequence will enter a cycle because applying f to that value will produce
    the same sequence of values that followed the first occurrence of the
    value.

Formally, the task of a cycle detection algorithm is finding μ and λ (defined
as follows):

    Let S be any finite set, f be any function that maps S to itself, and x0 be
    any element of S. For any i > 0, let xi = f(xi − 1). Let μ be the smallest
    index such that the value xμ reappears infinitely often within the sequence
    of values xi, and let λ (the loop length) be the smallest positive integer
    such that xμ = xλ + μ.

In practice, however, cycle detection can be as simple as identifying if a
cycle exists.

Several algorithms are known for finding cycles quickly and with little memory.
Two of note are Robert W. Floyd's tortoise and hare algorithm and Richard P.
Brent's algorithm based on the idea of exponential search. Here, we will focus
only on Floyd's cycle-finding algorithm.
"""

from typing import Any, Callable, Tuple


def floyd(f: Callable[[Any], Any], x0: Any) -> Tuple[int, int]:
    """
    Floyd's cycle-finding algorithm (Floyd's tortoise and hare)

    The algorithm maintains two pointers into the given sequence, one (the
    tortoise) at xi, and the other (the hare) at x2i. At each step of the
    algorithm, it increases i by one, moving the tortoise one step forward and
    the hare two steps forward in the sequence, and then compares the sequence
    values at these two pointers. The smallest value of i > 0 for which the
    tortoise and hare point to equal values is the desired value ν.

    The interesting insight in Floyd's tortoise and hare algorithm is that once
    the two pointers enter the loop, they will inevitably meet (period ν of a
    repetition) from which μ (the index of the first element of the cycle) and
    λ (the length of the loop) can be found.
    """
    # Find ν (a period of a repetition).
    #
    # The main phase of the algorithm consists of finding a repetition such
    # that xi = x2i.
    #
    # The hare moves twice as quickly as the tortoise and the distance between
    # them increases by 1 at each step. Eventually, they will both be inside
    # the cycle and then, at some point, they will meet (ν). The distance
    # between them will be divisible by the period λ.
    tortoise, hare = f(x0), f(f(x0))
    while tortoise != hare:
        tortoise, hare = f(tortoise), f(f(hare))

    # Find μ (the index of the first element of the cycle).
    #
    # At this point the tortoise position, ν, which is also equal to the
    # distance between hare and tortoise, is divisible by the period λ. The
    # hare moving in the cycle one step at a time, and the tortoise (reset to
    # x0) moving towards the cycle, will intersect at the beginning of the
    # cycle. Because the distance between them is constant at 2ν, a multiple of
    # λ, they will meet as soon as the tortoise reaches index μ.
    mu, tortoise = 0, x0
    while tortoise != hare:
        # NOTE: Here, the tortoise and hare move at the same speed.
        tortoise, hare = f(tortoise), f(hare)
        mu += 1

    # Find λ (the loop length or the shortest cycle starting from xμ)
    #
    # Finally, once the value of μ is known it is trivial to find the length λ
    # of the shortest repeating cycle by searching for the first position μ + λ
    # for which xμ + λ = xμ.
    lam, hare = 1, f(tortoise)
    while tortoise != hare:
        # NOTE: The hare moves one step at a time while tortoise (xμ) is still.
        hare = f(hare)
        lam += 1

    return mu, lam
