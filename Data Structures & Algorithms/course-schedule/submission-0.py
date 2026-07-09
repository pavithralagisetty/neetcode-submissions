class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        g=defaultdict(list)
        for pre,course in prerequisites:
            g[course].append(pre)
            indegree[pre]+=1
        q=deque()
        c=0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            c+=1
            for nei in g[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        print(c)
        if c==numCourses:
            return True
        return False
        
