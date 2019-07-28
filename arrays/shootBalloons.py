from typing import List
from collections import Counter


"""
when you encounter a new ball, check if arrow
at same height exists. Then decrement count of
arrows at that height.
Else add new arrow at height (ball-1)
keep track of max number of active arrows
at any given point in time.
"""
def shoot(balls: List[int]) -> int:
    arrows = Counter([balls[0] - 1])
    ans = 1
    for ball in balls[1:]:
        if ball in arrows:
            arrows[ball] -= 1
            if arrows[ball] == 0:
                del arrows[ball]
        arrows[ball - 1] += 1
        ans = max(ans, sum(arrows.values()))
    return ans

if __name__ == "__main__":
    balls = [5, 4, 4, 3, 3]
    # balls = [5, 4, 3]
    # balls = [3, 4, 5, 6]
    # balls = [3, 3, 3]
    # balls = [0]
    # balls = [5, 4, 6, 3, 7]
    # balls = [7, 7, 7, 3, 3]
    # balls = [3, 3, 3, 3, 8, 8]
    print(f"Minimum number of arrows required = {shoot(balls)}")
