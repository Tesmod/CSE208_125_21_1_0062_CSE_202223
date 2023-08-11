#Fibonacci Series
def generate_fibonacci_series(n):
    series = [0, 1]
    counter = 2
    
    while counter < n:
        new_number  = series[-1] + series[-2]
        series.append(new_number)
        counter += 1
    
    return series
fibonacci_series = generate_fibonacci_series(15)
print(fibonacci_series)