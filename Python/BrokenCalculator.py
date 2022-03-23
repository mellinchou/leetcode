def brokenCalc(startValue: int, target: int) -> int:
        res = 0
        while startValue < target:
            res += target % 2 + 1
            target = int((target + 1) / 2)
        return res + startValue - target