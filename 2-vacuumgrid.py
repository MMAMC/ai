#Create a simple reflex agent that navigates a 2*2 grid and cleans dirt in each spot.


import random

class ReflexAgent:
    def __init__(self):
        self.grid = [[random.choice([True, False]) for _ in range(2)] for _ in range(2)]  # Randomly generate dirt spots
        self.position = [0, 0]
    
    def sense(self):
        return self.grid[self.position[0]][self.position[1]]
    
    def clean(self):
        self.grid[self.position[0]][self.position[1]] = False
    
    def move_right(self):
        self.position[1] += 1
    
    def move_down(self):
        self.position[0] += 1
    
    def run(self):
        print("Initial grid state:")
        self.print_grid()

        while any(True in row for row in self.grid):
            print("\nAgent's position:", self.position)
            
            if self.sense():
                print("Sensing dirt at current location.")
                print("Cleaning...")
                self.clean()
                print("Location cleaned.")
            else:
                print("No dirt at current location.")
            
            if self.position[1] < 1:
                self.move_right()
            else:
                self.move_down()
            
            print("\nCurrent grid state:")
            self.print_grid()
        
        print("\nAll locations are clean now.")
    
    def print_grid(self):
        for row in self.grid:
            print(' '.join('1' if cell else '0' for cell in row))

if __name__ == "__main__":
    reflex_agent = ReflexAgent()
    reflex_agent.run()



""" Initial grid state:
0 1
0 0

Agent's position: [0, 0]
No dirt at current location.

Current grid state:
0 1
0 0

Agent's position: [0, 1]
Sensing dirt at current location.
Cleaning...
Location cleaned.

Current grid state:
0 0
0 0

All locations are clean now.


** Process exited - Return Code: 0 **
Press Enter to exit terminal """
