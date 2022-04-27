"""
Object Oriented Programming

1. Lists
2. Dictionaries
3. Tuples
4. Object
"""


"""
Create a class Student which contains attributes name, age, grade
Printing the student should generate "Student(Yacoub Lambaz, 18, A+)"
"""
class Student(object):
    def __init__(self, name, age, grade):
        assert type(name) == str and type(age) == int and type(grade) == str, "Return message"
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        ans = "Student(" + self.name +", " + str(self.age) + ", " + self.grade + ")"
        return ans

    def __add__(self,other):
        assert type(other) == Student, "Type must be student"
        return self.age + other.age

    def isGoodStudent(self):
        if self.grade == "A+":
            return True
        else:
            return False

"""
Create a class SuperStudent which, in addition to all the attributes
and methods in the Student class, also has an attribute "superpower".
Printing the SuperStudent should generate "SuperStudent(Jacob Lampej, 18, A+, Telephathy)"
(Inheritance)
"""
class SuperStudent(Student):
    def __init__(self,name,age,grade,superpower):
        Student.__init__(self,name,age,grade)
        self.superpower = superpower

    def __str__(self):
        ans = "Student(" + self.name +", " + str(self.age) + ", " + self.grade + ", " + self.superpower + ")"
        return ans


"""
Create a class Teacher which contains attributes name, age, students
Printing the Teacher should generate "Teacher(Aizawa, 28, [Yacoub Lambaz, Jacob Lampej])"
"""
class Teacher(object):
    def __init__(self,name,age,students):
        assert type(name) == str and type(age) == int and type(students) == list, "Type problem"
        for student in students:
            assert type(student) == Student or type(student) == SuperStudent, "Type problem 2"

        self.name = name
        self.age = age
        self.students = students

    def __str__(self):
        ans = "Teacher(" + self.name + ", " + str(self.age) + ", " + "["
        for student in self.students:
            ans = ans + student.name + ", "
        ans = ans[:-2]
        ans = ans + "])"
        return ans

SS1 = SuperStudent("Tamara", 18, "A+", "Super Speed")
S1 = Student("Yacoub",18,"A+")
Maya = Teacher("Maya",18,[SS1, S1])
print(Maya)

"""
What is a linked list?
1. Create class node
2. Create class LinkedList


"""
class Node:
    def __init__(self,val,next = None):
        assert type(val) == int
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self,startingNode = None):
        assert type(startingNode) == Node or type(startingNode) == None, "Starting node must be a node"
        self.startingNode = startingNode

def printLinkedList(linkedList):
    assert type(linkedList) == LinkedList, "Type error"
    currentNode = linkedList.startingNode
    while currentNode.next != None:
        print(currentNode.val)
        currentNode = currentNode.next
    print(currentNode.val)


N5 = Node(5)
N4 = Node(4)
N3 = Node(3)
N2 = Node(2)
N1 = Node(1)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5
LL1 = LinkedList(N1)
# printLinkedList(LL1)


"""
What is a binary tree?
1. Create class node
2. Create class BTree
Write a function traverse(BTree) which prints out all the items in the binary tree
"""
class BNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
B1 = BNode(1)
B2 = BNode(2)
B3 = BNode(3)
B4 = BNode(4)
B5 = BNode(5)
B6 = BNode(6)
B1.left = B2
B2.right = B4
B1.right = B3
B3.right = B5
B3.left = B6

def printAllChildren(startingNode):
    assert type(startingNode) == BNode, "Type Error"
    def trav(node):
        if node == None:
            return
        trav(node.left)
        trav(node.right)
        print(node.val)
    trav(startingNode)

# printAllChildren(B1)
"""
What is a graph?
Directed vs Undirected
AUB Representation of a graph: Using dictionaries with key:value being {node: [listofneighbors]}



"""
import copy
class GNode:
    def __init__(self,val, next = []):
        assert type(val) == int and type(next) == list, "Type error"
        for item in next:
            assert type(item) == GNode, "Type Error 2"
        self.val = val
        self.next = next

    def __str__(self):
        return "G"+str(self.val)

    def connect(self,other):
        assert type(other) == GNode, "Type Error 3"
        newNext = copy.deepcopy(self.next)
        newNext.append(other)
        self.next = newNext

def printAllNodes(startingNode):
    assert type(startingNode) == GNode, "Type Error 4"
    L = [] #list of values that I've seen
    def trav(Node):
        if Node.val in L:
            return
        L.append(Node.val)
        for item in Node.next:
            trav(item)
    trav(startingNode)
    print(L)

G1 = GNode(1)
G2 = GNode(2)
G3 = GNode(3)
G4 = GNode(4)
G1.connect(G4)
G2.connect(G1)
G2.connect(G4)
G3.connect(G1)
G4.connect(G3)
G4.connect(G2)

printAllNodes(G1)


class DiGraph:
    def __init__(self):
        self.map = {}

def connect(diGraph, GNode1,GNode2):
    if str(GNode1) not in diGraph.map:
        diGraph.map[str(GNode1)] = []
    if str(GNode2) not in diGraph.map:
        diGraph.map[str(GNode2)] = []
    diGraph.map[str(GNode1)].append(GNode2)
    diGraph.map[str(GNode2)].append(GNode1)

    print(diGraph.map)

DiG1 = DiGraph()

connect(DiG1, G1, G2)



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        ans = "(" + str(self.x) + ", " + str(self.y) + ")"
        return ans

    def __add__(self,other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Point(newx,newy)

