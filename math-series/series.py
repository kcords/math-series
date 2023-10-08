
def sum_series(nth, first=0, second=1):
    """Creates a sequence of numbers.

    Args:
        nth (int): Number to retrieve from the generated sequence.
        first (int, optional): Manually sets the first value of the sequence. Defaults to 0.
        second (int, optional): Manually sets the second value of the sequence. Defaults to 1.

    Returns:
        int: The nth value of the generated sequence.
    """
    values = [first, second]
    for idx in range(2, nth):
        values.append(values[idx - 1] + values[idx - 2])
    return values[nth - 1]


if __name__ == "__main__":
    print(
        "sum_series fib seq",
        sum_series(1),
        sum_series(2),
        sum_series(3),
        sum_series(4),
        sum_series(5)
    )
    print(
        "sum_series lucas nums",
        sum_series(1, 2, 1),
        sum_series(2, 2, 1),
        sum_series(3, 2, 1),
        sum_series(4, 2, 1),
        sum_series(5, 2, 1)
    )