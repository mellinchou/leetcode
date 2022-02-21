from typing import List
def letterCombinations(digits: str) -> List[str]:
    if digits=='': return []
    buttonCombo=[]
    res=[]
    myMap={ '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
    }
    
    def dfs2(pivot, options):
        if not options:
            res.append(pivot)
            return
        for i in range(0,len(options[0])):
            dfs2(pivot+options[0][i], options[1:])

    # dfs([], indexToMapValues(-1, buttonToValues(digits)))
    
    for char in digits:
        buttonCombo.append(myMap[char])
    dfs2('', buttonCombo)


    # def buttonToValues(buttons):
    #     values=[]
    #     for elem in buttons:
    #         values.append(myMap[elem])
    #     return values

    # def indexToMapValues(i, myList):
    #     rangeList=[*range(0,i), *range(i+1, len(myList))]
    #     optionsValues=[]
    #     for elem in rangeList:
    #         optionsValues.append(myList[elem])
    #     return optionsValues

    # def dfs(pivot, options):
    #     if not options:
    #         buttonCombo.append(pivot)
    #         return
        
    #     for i in range(len(options)):
    #         temp=pivot.copy()
    #         temp.append(options[i])
    #         dfs(temp, indexToMapValues(i, options))

letterCombinations('23')