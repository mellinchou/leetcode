import collections
def deleteAndEarn(nums):
    sortedNums=collections.Counter(sorted(nums))
    take, notake = 0,0
    for i in sortedNums.keys():
        take, notake = max(notake + i*sortedNums[i], take - (i-1)*sortedNums[i-1] + i*sortedNums[i]), take
    return max(take, notake)

print(deleteAndEarn([3,4,2]))
print(deleteAndEarn([2,2,3,3,3,4]))