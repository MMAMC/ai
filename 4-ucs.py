#Implement uniform cost search to find the least cost path in weighted graph. 

import heapq 

  

class Graph: 

    def __init__(self): 

        self.graph = {} 

  

    def add_edge(self, node1, node2, cost): 

        if node1 not in self.graph: 

            self.graph[node1] = [] 

        self.graph[node1].append((node2, cost)) 

  

    def uniform_cost_search(self, start, goal): 

        visited = set() 

        priority_queue = [(0, start, [])]  # (cost, node, path) 

         

        while priority_queue: 

            cost, current_node, path = heapq.heappop(priority_queue) 

             

            if current_node in visited: 

                continue 

             

            path = path + [current_node] 

            if current_node == goal: 

                return path, cost 

             

            visited.add(current_node) 

             

            if current_node in self.graph: 

                for neighbor, neighbor_cost in self.graph[current_node]: 

                    if neighbor not in visited: 

                        heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor, path)) 

         

        return None, None 

  

# Example usage: 

  

# Creating a graph 

graph = Graph() 

graph.add_edge('A', 'B', 1) 

graph.add_edge('A', 'C', 4) 

graph.add_edge('B', 'C', 2) 

graph.add_edge('B', 'D', 5) 

graph.add_edge('C', 'D', 1) 

  

# Running uniform cost search 

start_node = 'A' 

goal_node = 'D' 

path, cost = graph.uniform_cost_search(start_node, goal_node) 

  

if path: 

    print(f"Least cost path from {start_node} to {goal_node}:", ' -> '.join(path)) 

    print(f"Total cost: {cost}") 

else: 

    print("No path found.") 

""" Least cost path from A to D: A -> B -> C -> D
Total cost: 4


** Process exited - Return Code: 0 **
Press Enter to exit terminal """
