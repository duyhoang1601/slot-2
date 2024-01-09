def find_nearest_to_average(arr):
    # Calculate the average of the array
    average = sum(arr) / len(arr)

    # Find the element closest to the average
    closest_element = min(arr, key=lambda x: abs(x - average))

    # Find the position of the closest element
    position = arr.index(closest_element)

    return position

# Take user input for the array
try:
    n = int(input("Enter the number of elements in the array: "))
    arr = [float(input(f"Enter element {i + 1}: ")) for i in range(n)]

    # Call the function to find and display the position of the closest element
    result_position = find_nearest_to_average(arr)

    print(f"The position of the element closest to the average is: {result_position + 1}")

except ValueError:
    print("Please enter a valid number.")

except Exception as e:
    print(f"An error occurred: {e}")
