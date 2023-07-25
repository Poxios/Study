# JS Promise.all equivalent in Python
```python
with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = {executor.submit(function_A), executor.submit(function_B), executor.submit(function_C)}
    
    for future in concurrent.futures.as_completed(futures):
        print(future.result())  # or store the result, handle exceptions, etc.

    # all futures are done here
    some_function()
```