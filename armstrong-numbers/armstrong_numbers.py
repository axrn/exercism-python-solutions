def is_armstrong(number: int) -> bool:
    num_str = str(number)
    return number == sum(int(x) ** len(num_str) for x in num_str)
