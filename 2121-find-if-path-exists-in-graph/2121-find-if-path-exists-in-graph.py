class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        G = defaultdict(list)

        for src, dest in edges: # transforma no formato padrão dict(mais ez mexer)
            G[src].append(dest)
            G[dest].append(src)
            
        def dfs(node): 
            seen.add(node)
            if node == destination:
                return True

            for neighbor in G[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            
            return False
        
        return dfs(source)