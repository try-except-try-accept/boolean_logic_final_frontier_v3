from random import randint, choice, randrange, shuffle

class Node:
    def __init__(self, label, negated):

        self.text = label
        self.left = None
        self.right = None
        self.negated = negated
        
    def __repr__(self):

        return self.text

    def __len__(self):
        return len(self.text)

    def add_child(self, child, branch, negated):
        

        
        if self.text in TERMS:
            raise ValueError(f"Can't add child to node {self.text}")

        child = Node(child, negated)
        
        if branch:
            self.right = child
        else:
            self.left = child

        return child

    def childless(self):
        return self.left == None == self.right

##########################        

class BoolExpTree:

    def __init__(self, terms, gates, gates_left, nots_left, test_mode=False):
        
        self.terms = terms
        self.gates = gates
        self.gates_left = gates_left
        self.nots_left = nots_left
        if not test_mode:
            self.generate()

    def test_display(self, node=None, depth=0):

        
        print("\t"*depth, node)
        print("\t"*depth, "is connected on left to", node.left)
        print("\t"*depth, "is connected on right to", node.right)

        if node.left:
            self.test_display(node.left, depth+1)
        if node.right:
            self.test_display(node.right, depth+1)

    
    def negate(self, node):

        if self.nots_left and randint(0, 1):
            self.nots_left -= 1
            return node.add_child("NOT", 0)
        else:
            return node

    def decide_negation(self):
        negated = False
        if randint(0, 1) and self.nots_left > 0:
            self.nots_left -= 1
            negated = True
        return negated
        
        
    def generate(self):
            
        self.root = Node(choice(self.gates), self.decide_negation())
        self.new_branch(self.root)
        input("Generated")
        
    def new_branch(self, node):


        # are there gates left?

        # are there enough terms for the new gate?

        # if not - term as leaf.

        branch_order = [0, 1]
        shuffle(branch_order)



    
        

        for branch in branch_order:
            if randint(0, 1) and self.gates_left and len(self.terms) > 2:
                new_label = choice(self.gates)
                self.gates_left -= 1
            else:
                new_label = self.terms.pop(0)
                print("Terms left are", self.terms)
                        
            new_node = node.add_child(new_label, branch, self.decide_negation())

            if new_label in self.gates:
                self.new_branch(new_node)
                

        

    def print(self, node=None, direction=None):
            
        if node is None:
            node = self.root


        
        if node.negated and len(node) > 1:
            print("NOT", end=" ")

        if node.childless() and direction == 0 or str(node.left) in self.gates:
            print("(", end="")

        


        if node.left is not None:            
            self.print(node.left, 0)

        if node.negated and len(node) == 1:
            print("NOT", end=" ")

        print(" " + node.text, end=" ")

        if node.right is not None:            
            self.print(node.right, 1)
        
        if node.childless() and direction == 1 or str(node.right) in self.gates:
            print(")", end="")
        

        
GATES = ["AND", "OR"]
TERMS = ["A", "B", "C"]
        
def create_expression(stage, level):

    nots = 0

    t = list(TERMS) * 5
    g = list(GATES)

    if stage == 1:
        t.pop(0)
        
    if stage > 5:
        g.append("NAND")
    if stage > 6:
        g.append("NOR")
    if stage > 7:
        g.append("XOR")

    t.sort()          

    if stage == 3:
        nots = 1
    elif stage == 4 or stage == 10:
        nots = 2
    elif stage == 5 or stage == 11:
        nots = 3
    elif stage > 11:
        nots += stage-11

    TEST = False

    tree = BoolExpTree(t, g, level, 1, TEST)

    if TEST:

        tree.root = Node("AND")
        tree.root.left = Node("B")
        tree.root.right = Node("AND")
        tree.root.right.left = Node("B")
        tree.root.right.right = Node("OR")
        tree.root.right.right.left = Node("A")
        tree.root.right.right.right = Node("OR")
        tree.root.right.right.right.left = Node("OR")
        tree.root.right.right.right.right = Node("A")
        tree.root.right.right.right.left.left = Node("A")
        tree.root.right.right.right.left.right = Node("A")
        

    
    
    tree.test_display(tree.root)
    tree.print()
    input()




for stage in range(1, 12):

    for level in range(1, 6):

        create_expression(stage, level)



        

    
