def fib_bottom_up(n):
    # Check if n is 0 or 1 (base cases), 
    # if so, return n immediately as the Fibonacci of 0 is 0 and of 1 is 1.
    if n <= 1:
        return n
    
    # Initialize a table (list) to store the computed Fibonacci numbers up to n.
    # The list has (n + 1) elements, all initialized to 0.
    table = [0] * (n + 1)
    
    # Manually set the Fibonacci of 1 as 1, 
    # as we already know this value, and it serves as a starting point for the loop.
    table[1] = 1
    
    # Loop through numbers from 2 to n (inclusive) to fill the table.
    # For each number i, compute the Fibonacci number as the sum of the two preceding Fibonacci numbers.
    # Store the computed Fibonacci number in the table at index i.
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    
    # After the loop, the table is filled with Fibonacci numbers up to n.
    # Return the Fibonacci number at index n from the table.
    return table[n]

# Example Usage:
n = 10  # Define the term number of the Fibonacci sequence you want to compute.
# Call the fib_bottom_up function with n and print the resulting Fibonacci number.
print(f"Fibonacci({n}) =", fib_bottom_up(n))