## Problem 01

Implement the function `is_prime(x: int) -> bool:` that takes the number `x` and returns `True` if it's prime. Otherwise returns `False`. 

`1 and 0` are `NOT prime`!

##### Example

> Prime: 2, 3, 5, 7, 11, 13, 17, 19
> Not prime: 0, 1, 4, 6, 8, 9, 10

## Problem 02

Implement the function `first_n_primes(n: int) -> list` that takes `n` and returns a list with the first `n` prime numbers. Make sure that `n` is a non-negative integer.

###### Example

> first_n_primes(6) => 2, 3, 5, 7, 11, 13, 17, 19
>
> first_n_primes(0) => []
>
> first_n_primes(2) => 2, 3

## Problem 03

Implement the function `is_prod_of_primes(x: int) -> bool` that takes `x` (a positive integer) and returns true if `x` is a product of `ONLY prime numbers`.

##### Example

> 15 = 3 * 5
>
> 30 = 2 * 3 * 5
> 
> 105 = 3 * 5 * 7

## Problem 04

Implement the function `is_magic_number(x: int) -> bool` that takes `x` (a positive integer) and returns `True` if `x` is a product of `2, 3, 5, 7` that can be used multiple times.

> x = 2^a * 3^b * 5^c * 7^d where a, b, c, d >= 0

You can use recursion if you want.

## Problem 05

- Да се реализира клас служител. Той трябва да съдържа информация за име, адрес, ЕГН, отдел в който работи служителят и заплата му.
- Да се реализира клас специалист, който наследява служител, но притежава като допълнение описание на специалността си.
- Да се реализира клас ръководител на отдел, който наследява специалист и притежава информация на отдела, който ръководи, и указатели към всички служители в този отдел.
- Да се реализира клас секретарка, за която имаме списък от езици които говори.
- Да се реализира клас директор, който да има секретарка и указатели към всички служители във фирмата.
- Да се реализира програма, която да дава възможност да се въведе информация за една фирма. По указател към директор на дадена фирма да се изчислява необходимата за заплатите сума.

