def find_sum_of_negative_elements():
    # Initialize an empty list
    A = []

    # Get 10 elements from the user
    for i in range(10):
        element = float(input(f"Введите элемент № {i + 1}: "))
        A.append(element)

    # Find the sum of negative elements
    negative_sum = sum([x for x in A if x < 0])

    # Display the sum of negative elements
    print(f"Sum of negative elements: {negative_sum}")

find_sum_of_negative_elements()
