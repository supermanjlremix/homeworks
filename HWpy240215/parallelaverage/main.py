from parallelaverage import parallel_average

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        num_threads = int(input("На сколько частей разделить список и вычислить среднее значение каждого? "))
        num_threads / num_threads
    except Exception as error:
        print(error)
        exit()
    average = parallel_average(numbers, num_threads)
    print(f"Average: {average}")
