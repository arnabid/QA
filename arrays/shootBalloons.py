from typing import List
from collections import Counter


"""
Arrows are only shot from left to right.
when you encounter a new balloon, check if arrow
at same height exists. If yes, then decrement count of
arrows at that height.
Else add new arrow at height (balloon-1)
keep track of max number of active arrows
at any given point in time.

Insight: You have to shoot an arrow at the height of
the first balloon. If that does not hit some balloon at height h,
then you have to shoot another arrow at height h and so on.

TODO: what if you can shoot arrows from both ends?
"""
def shoot(balloons: List[int]) -> int:
    arrows = Counter([balloons[0] - 1])
    ans = 1
    for balloon in balloons[1:]:
        if balloon in arrows:
            arrows[balloon] -= 1
            if arrows[balloon] == 0:
                del arrows[balloon]
        arrows[balloon - 1] += 1
        ans = max(ans, sum(arrows.values()))
    return ans

if __name__ == "__main__":
    # balloons = [5, 4, 4, 3, 3]
    # balloons = [5, 4, 3]
    # balloons = [3, 4, 5, 6]
    # balloons = [3, 3, 3]
    # balloons = [0]
    # balloons = [5, 4, 6, 3, 7]
    # balloons = [7, 7, 7, 3, 3]
    balloons = [3, 3, 3, 3, 8, 8]
    print(f"Minimum number of arrows required = {shoot(balloons)}")
