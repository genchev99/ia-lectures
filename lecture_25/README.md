# Exercise

## Problem 01 - The Knight Santa

Given a two-dimensional space with width and height of `100` - `0` to `100` (`x and y axis`)

```
 (0, 100)            (100, 100)  
    --------------------
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    --------------------
 (0, 0)              (100, 0)
```

This year Santa is giving presents only to the kids that live in a `key positions` irrelevant of whether they were good
or bad. Starting from the position (`x`, `y`) Santa can only move as a chess Knight

- https://www.chess.com/terms/chess-knight

Due to the `crazy fuel prices` Santa has a limited hops as well - limits to the number `n`.

If we want to Santa we need to predict his movement. Create a program that will get the staring position (`x`
and `y`) and the hops limit `n` from the `standard input`. After that at the end of the program you need to `plot a map`
where all the places that will be visited by Santa are marked with `S` and all other places are marked with `_`. The
initial position should be marked with `$`.

For simplicity the example will use a chess board (`8x8`), starting position (`3, 3`) and `n=1`. The result should look
like:

```
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ S _ S _ _ _
_ S _ _ _ S _ _
_ _ _ $ _ _ _ _
_ S _ _ _ S _ _
_ _ S _ S _ _ _
_ _ _ _ _ _ _ _
```

> Hint #1: Use a Queue to store the potential positions
>
> Hint #2: Make sure that you don't exit the space (positions < 0 or greater than 100)

## Problem 02

Казваме, че `k` е число на Hamming, ако простите делители на `k` са сред `2`, `3`, и `5`, т.е. `k=2^x*3^y*5^z`
за `x, y, z >= 0`

Да се изведат в нарастващ ред всички числа на Hamming, които са по-малки от `n`.
(Направете функция `first_hamming(n)`, която да връща лист опашка от първите n числа)

## Problem 03

Да се имплементира `queue` посредством `Node`-ове

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Problem 04 - The secret Santa

Given a list of names create a program that will set up a `secret Christmas pairs`. Each person you need to match
with `a different` person `A -> B` where person `A` will give present to person `B`. Make sure that there is no person
without a present and also no one is giving a present to himself. Make the program in a way the results are always
randomized.

Example:

```python
names = ["Pesho", "Gosho", "Ivan"]

"""
Possible result:

Pesho -> Gosho
Gosho -> Ivan
Ivan -> Pesho
"""
```