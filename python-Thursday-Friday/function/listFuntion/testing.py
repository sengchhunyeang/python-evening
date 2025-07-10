# Lambda function to check even numbers
get_even_numbers = lambda x: x % 2 == 0

# Function to filter even numbers using the lambda
def get_even_number(numbers):
    return list(filter(get_even_numbers, numbers))

# Sample list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the result
print(get_even_number(sample_list))
