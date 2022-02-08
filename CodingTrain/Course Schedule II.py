class Solution:
    def isCyclic(self, graph, v, visited, lookup, order):
        visited[v] = True
        lookup[v] = True
        cycle = False
        for u in graph[v]:
            if lookup[u]:
                cycle = True
            elif not visited[u]:
                cycle = self.isCyclic(graph, u, visited, lookup, order)
            if cycle:
                break
        lookup[v] = False
        order.append(v)
        return cycle
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            courses[v].append(u)
        
        visited = [False] * numCourses
        lookup = [False] * numCourses
        order = []
        
        for v in range(numCourses):
            if not visited[v] and self.isCyclic(courses, v, visited, lookup, order):
                return []
        
        return order[::-1]