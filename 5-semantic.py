#Create a Semantic Network for a family tree and determine relationships between members. 

class Person: 

    def __init__(self, name, gender): 

        self.name = name 

        self.gender = gender 

        self.parents = [] 

  

    def add_parent(self, parent): 

        self.parents.append(parent) 

  

    def is_parent_of(self, person): 

        return person in self.parents 

  

    def __str__(self): 

        return f"{self.name} ({self.gender})" 

  

  

class FamilyTree: 

    def __init__(self): 

        self.people = {} 

  

    def add_person(self, name, gender): 

        if name not in self.people: 

            self.people[name] = Person(name, gender) 

  

    def add_relationship(self, child_name, parent_name): 

        if child_name in self.people and parent_name in self.people: 

            child = self.people[child_name] 

            parent = self.people[parent_name] 

            child.add_parent(parent) 

  

    def find_relationship(self, person1_name, person2_name): 

        if person1_name not in self.people or person2_name not in self.people: 

            return "Unknown" 

  

        person1 = self.people[person1_name] 

        person2 = self.people[person2_name] 

  

        if person1.is_parent_of(person2): 

            return f"{person1} is a parent of {person2}" 

        elif person2.is_parent_of(person1): 

            return f"{person2} is a parent of {person1}" 

        elif person1 == person2: 

            return f"They are the same person: {person1}" 

        else: 

            return f"No direct relationship found between {person1} and {person2}" 

  

  

# Example usage: 

  

# Creating a family tree 

family = FamilyTree() 

family.add_person("John", "Male") 

family.add_person("Alice", "Female") 

family.add_person("Bob", "Male") 

family.add_person("Mary", "Female") 

  

family.add_relationship("John", "Bob") 

family.add_relationship("Alice", "Bob") 

family.add_relationship("Alice", "Mary") 

  

# Finding relationships 

print(family.find_relationship("John", "Bob")) 

print(family.find_relationship("Alice", "Mary")) 

print(family.find_relationship("Bob", "Mary")) 

print(family.find_relationship("John", "Alice")) 

print(family.find_relationship("John", "John")) 

print(family.find_relationship("John", "Lucy"))  # Unknown person


""" John (Male) is a parent of Bob (Male)
Alice (Female) is a parent of Mary (Female)
No direct relationship found between Bob (Male) and Mary (Female)
No direct relationship found between John (Male) and Alice (Female)
They are the same person: John (Male)
Unknown


** Process exited - Return Code: 0 **
Press Enter to exit terminal """
