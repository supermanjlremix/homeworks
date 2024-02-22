import threading

def parallel_average(numbers: list, num_threads: int) -> float:
    sublist_size = len(numbers) // num_threads
    sublists = [numbers[i:i+sublist_size] for i in range(0, len(numbers), sublist_size)]
    results = []
    def calculate_average(sublist: list=[]) -> float:
        average = sum(sublist) / len(sublist)
        results.append(average)
    threads = []
    for sublist in sublists:
        thread = threading.Thread(target=calculate_average, args=(sublist,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    overall_average = sum(results) / len(results)
    return overall_average