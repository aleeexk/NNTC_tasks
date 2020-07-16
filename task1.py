print([i if (i % 5 != 0) and (i % 3 != 0) else 'buzz' if (i % 3 != 0) else 'fizz' if (i % 5 != 0) else 'fizzbuzz' for i in range(1, 101)])
