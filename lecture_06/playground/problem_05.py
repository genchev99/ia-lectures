# def contains(list_of_numbers: list, number: int) -> bool:
#     for n in list_of_numbers:
#         if n == number:
#             return True
#
#     return False
#
#
# list_of_numbers = [-26, 46, 47, 5, -37, -12, 41, -8, -5, -4, -12, -34, -31, -6, 14, 19, 26, 28, 50, 45]
# number = 1
#
# print(contains(list_of_numbers, number))
def is_outside_circle(center_x: float, center_y: float, radius: float, point_x: float, point_y: float) -> bool:
    center_x = 2
    center_y = 3
    radius = 5
    m_x = 2
    m_y = 1

from math import f