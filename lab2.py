import math

def min_eating_speed(piles, h):
    def can_finish(k):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours <= h

    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    print(min_eating_speed([1, 8, 5, 4], 8))
    print(min_eating_speed([4, 5, 8, 12], 5))
    print(min_eating_speed([1, 3, 9, 17], 6))
