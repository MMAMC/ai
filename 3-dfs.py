#Implement Depth First Search to find an item in a simple tree structure. 

class TreeNode: 

    def __init__(self, value): 

        self.value = value 

        self.children = [] 

  

    def add_child(self, child_node): 

        self.children.append(child_node) 

  

  

def dfs_search(root, target): 

    if root is None: 

        return None 

     

    # Stack to keep track of nodes and their paths 

    stack = [(root, [root.value])] 

     

    while stack: 

        node, path = stack.pop() 

         

        # If target found, return the path 

        if node.value == target: 

            return path 

         

        # Add children to stack with updated paths 

        for child in reversed(node.children): 

            stack.append((child, path + [child.value])) 

     

    # If target not found, return None 

    return None 

  

  

# Example usage: 

  

# Creating a simple tree structure 

root = TreeNode('A') 

B = TreeNode('B') 

C = TreeNode('C') 

D = TreeNode('D') 

E = TreeNode('E') 

F = TreeNode('F') 

G = TreeNode('G') 

  

root.add_child(B) 

root.add_child(C) 

B.add_child(D) 

B.add_child(E) 

C.add_child(F) 

C.add_child(G) 

  

# Searching for item 'G' 

target_item = 'G' 

path = dfs_search(root, target_item) 

  

if path: 

    print(f"Item '{target_item}' found at path: {' -> '.join(path)}") 

else: 

    print(f"Item '{target_item}' not found.") 

""" Item 'G' found at path: A -> C -> G


** Process exited - Return Code: 0 **
Press Enter to exit terminal """
