class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for ast in asteroids:
            st.append(ast)
            while len(st)>1 and st[-2]>0 and st[-1]<0:
                t=st.pop()
                if(abs(t)==st[-1]):
                    st.pop()
                elif(abs(t)>st[-1]):
                    st.pop()
                    st.append(t)
        return st