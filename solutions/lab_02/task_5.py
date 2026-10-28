import sys
import tracemalloc
import gc

def measure(name, factory, count):
    gc.collect()
    tracemalloc.start()
    try:
        obj = factory()
        current, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    return {
        "name": name,
        "count": count,
        "size": sys.getsizeof(obj),
        "current": current,
        "peak": peak,
    }


def create_list(count):
    numbers = []
    for i in range(count):
        numbers.append(i)
    return numbers


def collect_results():
    objects = [
        measure("Пустой список", lambda: [], 0),
        measure("Список из десяти чисел", lambda: list(range(10)), 10),
        measure("Кортеж из десяти чисел", lambda: tuple(range(10)), 10),
        measure("Строка из десяти символов", lambda: "abcdefghij", 10),
        measure("Целое число", lambda: 42, None),
        measure("None", lambda: None, None),
    ]

    numbers = []
    previous_size = sys.getsizeof(numbers)
    growth_counts = []

    for i in range(100):
        numbers.append(i)
        size = sys.getsizeof(numbers)

        if size != previous_size:
            growth_counts.append(len(numbers))
            previous_size = size

    growth = [
        measure("Рост списка", lambda n=n: create_list(n), n)
        for n in growth_counts
    ]

    comparison = [
        measure(
            "list(range(100_000))",
            lambda: list(range(100_000)),
            100_000,
        ),
        measure(
            "range(100_000)",
            lambda: range(100_000),
            100_000,
        ),
    ]

    return {
        "objects": objects,
        "growth": growth,
        "comparison": comparison,
        "ratio": comparison[0]["peak"] / comparison[1]["peak"],
    }


if __name__ == "__main__":
    results = collect_results()

    for row in results["objects"]:
        print(row["name"], row["size"])

    for row in results["growth"]:
        print(row["count"], row["size"])

    for row in results["comparison"]:
        print(
            row["name"],
            row["current"] / 1024,
            row["peak"] / 1024,
        )
