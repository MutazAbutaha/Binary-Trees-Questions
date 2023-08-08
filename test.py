def swap_without_extra_space(a, b):
    a , b = b , a
    return a, b

# Example usage:
x = 20
y = 10
x, y = swap_without_extra_space(x, y)
print("x:", x)  # Output: 10
print("y:", y)  # Output: 5
