def lengthOfLongestSubstring(s: str) -> int:
    if len(s)<1: return 0
    elif len(s)==1: return 1

    uniqueSubstrings=[]

    for i in range(0,len(s)):
        current=s[i]
        for char in range(i+1,len(s)):
            if s[char] in current:
                uniqueSubstrings.append(current)
                break
            else:
                current+=s[char]
        uniqueSubstrings.append(current)
    
    return(len(max(uniqueSubstrings, key=len)))

print(lengthOfLongestSubstring("abcabcbb")) #3
print(lengthOfLongestSubstring("bbbbb")) #1
print(lengthOfLongestSubstring("pwwkew")) #3
print(lengthOfLongestSubstring("hkcpmprxxxqw")) #5
print(lengthOfLongestSubstring("ggububgvfk")) #6
print(lengthOfLongestSubstring("au")) #2
print(lengthOfLongestSubstring("")) #0
print(lengthOfLongestSubstring(" ")) #1