import random
from timeit import default_timer as timer

global ordered
ordered= []
#Class- holds a number,
class Node():
    def __init__(self,value,parent = None):
        self.parent = parent
        self.value = value
        self.child = False
        self.lc = None
        self.rc = None

##  function to sort- is given a number, if number is bigger
##  create a rightside child, if smaller, left side child.
##  if there is already a child where it should go, then pass it to that node      
    def createChild(self, num1):
        if num1 < self.value:
            if self.lc == None:
                self.lc = Node(num1,self)
            else:
                self.lc.createChild(num1)
        else:
            if self.rc == None:
                self.rc = Node(num1,self)
            else:
                self.rc.createChild(num1)
        self.child = True

##function to traverse the tree with recursion
def traverse(node):
    global ordered
    if not node.child:
        ordered.append(node.value)
    else:
        if node.lc != None:
            traverse(node.lc)
        ordered.append(node.value)
        if node.rc != None:
            traverse(node.rc)
    return

#BubbleSort
def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
    return(arr)

#my sorting function - build a tree then traverse it
def treeSort(arr):
    root = Node(arr[0])
    for x in arr:
        if x != root.value:
            root.createChild(x)
    return(traverse(root))

##create a random array
arr = []
for x in range(10000):
    arr.append(random.randint(0,100))

## Output unordered array
print('unordered array:')
print(arr)
print("\ntree sorted array: ")

##output sorted arrays and time it took each function to order
s = timer()
treeSort(arr)
print(ordered)
e = timer()

print("time for tree sort: ",e-s)
print("\nBubble sorted array: ")
s = timer()
print(BubbleSort(arr))
e = timer()
print("time for bubble sort: ",e-s)


