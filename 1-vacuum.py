# To simulate a vacuum cleaner agent that moves linearly is a space of two locations: A and B. Each location can be clean or dirty. 

class VacuumCleaner:  

    def __init__(self):  

        self.location = 'A'  

        self.locations = {'A': 'clean', 'B': 'dirty'}  

  

    def clean(self):   

        print(f"Location {self.location} is {self.locations[self.location]}")  

        if self.locations[self.location] == 'dirty':  

            print("Cleaning...") 

            self.locations[self.location] = 'clean'  

            print(f"Location {self.location} is now clean") 

 

    def move(self):  

        if self.location == 'A':  

            self.location = 'B'  

        else:  

            self.location = 'A'  

        print(f"Moving to location {self.location}")  

  

    def run(self):  

        print("Starting vacuum cleaner simulation...")  

        print("-----------------------------")  

        self.clean()  

        while any(status == 'dirty' for status in self.locations.values()):  

            self.move()  

            self.clean()  

        print("-----------------------------")  

        print("Simulation complete. Both locations are clean.") 

   

  

if __name__ == "__main__":  

     vacuum = VacuumCleaner()  

     vacuum.run() 

""" Starting vacuum cleaner simulation...
-----------------------------
Location A is clean
Moving to location B
Location B is dirty
Cleaning...
Location B is now clean
-----------------------------
Simulation complete. Both locations are clean.


** Process exited - Return Code: 0 **
Press Enter to exit terminal """
