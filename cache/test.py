# from typing import List


# def check(
#         row_start: int, row_end: int, column_start: int, column_end: int
#     ) -> List[List[int]]:
#     small_array = []
#     big_array = []
#     table = ""
#     for i in range(row_start, row_end + 1):
#         for j in range(column_start, column_end + 1):
#             table += str(j * i) + "  "
#             small_array.append(j * i)
#         big_array.append(small_array)
#         table += "\n\n"
#         small_array = []
#     return f"{big_array}\nthat is equal to the following multiplication table:\n\n{table}"

# print(check(row_start=2, row_end=4, column_start=3, column_end=7))
from bottle import *