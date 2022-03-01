from heapq import heappush


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a,b in tickets:
            heappush(graph[a],b)
        route=[]
        def dfs(a):
            while graph[a]:
                dfs(heappop(graph[a]))
            route.append(a)
        dfs('JFK')
        return route[::-1]