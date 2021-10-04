"""
Write a program that reads from the console an integer n and draws a rectangle with size n with two asterisks is its
center as in the examples below.

Sample input and output

Input #1
> 2

Output #1
```
%%%%
%**%
%%%%
```

Input #2
> 3

Output #2
```
%%%%%%
%    %
% ** %
%    %
%%%%%%
```

Input #3
> 4

Output #3
```
%%%%%%%%
%      %
%  **  %
%      %
%%%%%%%%
```

Input #4
> 5

Output #4
```
%%%%%%%%%%
%        %
%        %
%   **   %
%        %
%        %
%%%%%%%%%%
```
"""

n = int(input("Please provide positive integer n in [2, 1000]: "))

number_of_rows_in_between = n
if number_of_rows_in_between % 2 == 0:
    number_of_rows_in_between -= 1

# first row
print("%" * n * 2)

for i in range(number_of_rows_in_between):
    print("%", end='')

    # find the middle row
    if i == (number_of_rows_in_between - 1) / 2:
        print(" " * (n - 2), end='')
        print("**", end='')
        print(" " * (n - 2), end='')
    else:
        print(" " * (n * 2 - 2), end='')

    print("%")

# last row
print("%" * n * 2)
