def calculate_sums_and_compress_list(lst):
    odd_sum = 0
    negative_sum = 0
    first_negative_index = -1
    last_negative_index = -1

    for i, num in enumerate(lst):
        if num % 2 != 0:
            odd_sum += num

        if num < 0:
            if first_negative_index == -1:
                first_negative_index = i
            last_negative_index = i
            negative_sum += num

    compressed_list = [num for num in lst if abs(num) <= 1]
    compressed_list.extend([0] * (len(lst) - len(compressed_list)))

    return odd_sum, negative_sum, compressed_list


# Example usage:
my_list = [1, 2, -3, 4, 5, -6, 7, -8]
odd_sum_result, negative_sum_result, compressed_list_result = calculate_sums_and_compress_list(my_list)

print("Sum of list items with odd numbers:", odd_sum_result)
print("Sum of list items between first and last negative elements:", negative_sum_result)
print("Compressed list:", compressed_list_result)