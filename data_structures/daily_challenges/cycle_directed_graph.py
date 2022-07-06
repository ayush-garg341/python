def cycleInGraph(edges):
    # Write your code here.
    visited = [0] * len(edges)
    dfs_visited = [0] * len(edges)
    for i in range(len(edges)):
        if not visited[i]:
            if check_cycle_dfs(i, visited, dfs_visited, edges):
                return True
    return False


def check_cycle_dfs(i, dfs_visited, visited, edges):
    visited[i] = 1
    dfs_visited[i] = 1
    for adj in edges[i]:
        if dfs_visited[adj] == 1:
            return True
        else:
            if not visited[adj]:
                if check_cycle_dfs(adj, dfs_visited, visited, edges):
                    return True
    dfs_visited[i] = 0


print(cycleInGraph([[1, 3], [2, 3, 4], [0], [], [2, 5], []]))
