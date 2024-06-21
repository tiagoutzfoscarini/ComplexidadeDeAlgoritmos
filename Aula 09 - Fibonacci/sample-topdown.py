def fib_top_down(n, memo={}):
    # Base case: If n is 0 or 1, return n as the Fibonacci number for these two cases is the number itself.
    if n <= 1:
        return n
    
    # Check if the Fibonacci number for n is already computed (present in memo).
    # If not, compute it using the recursive formula: F(n) = F(n - 1) + F(n - 2).
    if n not in memo:
        # Recursively call fib_top_down for (n - 1) and (n - 2) and store the result in memo[n].
        # The memo dictionary is used to store already computed Fibonacci numbers to avoid redundant calculations.
        memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    
    # Return the computed Fibonacci number for n from the memo dictionary.
    return memo[n]

# Example Usage:
n = 10  # Define the term number of the Fibonacci sequence you want to compute.
# Call the fib_top_down function with n and print the resulting Fibonacci number to the console.
print(f"Fibonacci({n}) =", fib_top_down(n))