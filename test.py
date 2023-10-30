# Sample data (two lists)
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]

# Adding two lists element-wise
result_list = [x + y for x, y in zip(list_1, list_2)]

# Print the final value
print("Result after adding two lists:", result_list)
