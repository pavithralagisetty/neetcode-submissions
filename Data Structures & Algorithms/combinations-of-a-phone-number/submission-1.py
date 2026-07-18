class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        subset=[]
        res=[]
        if not digits:
            return []
        d={
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        def dfs(level):
            if len(subset)==len(digits):
                res.append(''.join(subset))
                return
            
            for i in d[int(digits[level])]:
             
                subset.append(i)
                dfs(level+1)
                subset.pop()
        dfs(0)
        return res