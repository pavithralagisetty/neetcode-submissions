class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        d=defaultdict(list)
        indegree=defaultdict(int)
        for word in words:
            for ch in word:
                indegree[ch]=0
        
        for i in range(1,len(words)):
            word1=words[i-1]
            word2=words[i]
            if len(word1)>len(word2) and word1[:len(word2)]==word2:
                return ""
            for j in range(min(len(word1),len(word2))):
                if word1[j]==word2[j]:
                    continue
                else:
                    d[word1[j]].append(word2[j])
                    indegree[word2[j]]+=1                        
                    break
        print(indegree)

        q=deque()
        for key in indegree:
            if indegree[key]==0:
                q.append(key)
        ans=''
        while q:
            node=q.popleft()
            ans+=node
            for nei in d[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return ans if len(ans) == len(indegree) else ""
