from task_5 import collect_results


def print_report(results):
    rows = (
        results["objects"]
        + results["growth"]
        + results["comparison"]
    )

    print(
        "Сценарий | Число элементов | Размер внешнего объекта, байт | "
        "Текущий объём, КБ | Пиковый объём, КБ"
    )

    for row in rows:
        count = "—" if row["count"] is None else row["count"]

        print(
            f'{row["name"]} | {count} | {row["size"]} | '
            f'{row["current"] / 1024:.3f} | '
            f'{row["peak"] / 1024:.3f}'
        )

    print(
        "Отношение пикового объёма list / range:",
        results["ratio"],
    )


if __name__ == "__main__":
    results = collect_results()
    print_report(results)