class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={}
        indegree={}

        #initialising both dictionaries
        for i in range(numCourses):
            graph[i]=[]
            indegree[i]=0	

        #filling graph and indegree dictionaries
        for child,parent in prerequisites:
            graph[parent].append(child)
            indegree[child]+=1

        #initially storing keys in queue whose indegree is zero
        queue=deque()
        for key,value in indegree.items():
            if value==0:
                queue.append(key)

        #Main_Logic
        courseSequence=[]
        while queue:
            course=queue.popleft()
            courseSequence.append(course)
            for neighbour in graph[course]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)

        if len(courseSequence)==numCourses:
            return True 
        else:
            return False