def climbStairs(self, n: int) -> int:
    # Botton Up DP

    # Index: [0, 1, 2, ..., one, two]
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
            
    return one
