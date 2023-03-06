import concurrent.futures

# Define a function to execute asynchronously
def my_function(arg):
    # Do some work here...
    result = arg * 2
    return result

# Create a thread pool with 4 worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit multiple tasks to the thread pool
    futures = [executor.submit(my_function, i) for i in range(10)]

    # Wait for all tasks to complete and get their results
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# Print the results
print(results)