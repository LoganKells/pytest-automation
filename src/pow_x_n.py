def power(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n *= -1

    def fast_power(x: float, n: int) -> float:
        # Recursive, fast
        if int(n) == 0:
            return 1.0
        half_power_result = fast_power(x, int(n / 2))

        if abs(half_power_result) < 1e-5:
            return 0.0
        elif n % 2 == 0:
            return half_power_result * half_power_result
        else:
            return half_power_result * half_power_result * x

    return fast_power(x, n)