def romanToInt(self, s: str) -> int:
    res = 0
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(s)-1):
        if (table[s[i]] < table[s[i+1]]):
            res -= table[s[i]]
        else:
            res += table[s[i]]
    res += table[s[len(s)-1]]
    return res

romanToInt("III")
romanToInt("LVIII")
romanToInt("MCMXCIV")
romanToInt("MMMCDXC")