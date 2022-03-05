import collections
def deleteAndEarn(self, nums):
    points = collections.Counter(nums)
    prev = curr = 0
    for value in range(10001):
        prev, curr = curr, max(prev + value * points[value], curr)
    return curr