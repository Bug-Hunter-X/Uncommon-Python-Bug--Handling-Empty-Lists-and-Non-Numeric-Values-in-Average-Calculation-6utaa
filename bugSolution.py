def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after removing non-numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}")

my_list_with_string = [10, 20, 'a', 40, 50]
average = calculate_average(my_list_with_string)
print(f"The average is: {average}")

my_list_with_mixed_types = [10, 20, 30.5, 40, 50]
average = calculate_average(my_list_with_mixed_types)
print(f"The average is: {average}")
