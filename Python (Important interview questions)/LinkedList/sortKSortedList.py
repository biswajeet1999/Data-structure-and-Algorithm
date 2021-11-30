class Node:
   def __init__(self, key):
      self.data = key
      self.prev = None
      self.next = None

class DLL:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def insert(self, key):
      if self.head is None:
         self.head = self.tail = Node(key)
         return
      newNode = Node(key)
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
   
   def remove(self):
      if self.head is None:
         return None
      nodeToDelete = self.head
      self.head = nodeToDelete.next
      if self.head is None:
         self.tail = None
         return nodeToDelete
      self.head.prev = None
      nodeToDelete.next = None
      return nodeToDelete
      
   def display(self):
      curNode = self.head
      while curNode:
         print(curNode.data, end="  ")
         curNode = curNode.next
      print()

class MinHeap:
   def __init__(self):
      self.size = 0
      self.heap = []

   def isEmpty(self):
      return self.size == 0
   
   def insert(self, node: Node):
      self.heap.append(node)
      self.size += 1
      self.prelocateUp(self.size - 1)

   def delete(self):
      self.swap(0, self.size - 1)
      deletedNode = self.heap.pop()
      self.size -= 1
      self.prelocateDown(0)
      return deletedNode

   def prelocateDown(self, idx):
      leftChildIdx = idx * 2 + 1
      while leftChildIdx < self.size:
         rightChildIdx = idx * 2 + 2
         if rightChildIdx >= self.size or self.heap[rightChildIdx].data > self.heap[leftChildIdx].data:
            idxToSwap = leftChildIdx
         else:
            idxToSwap = rightChildIdx
         
         if self.heap[idx].data < self.heap[idxToSwap].data:
            return
         self.swap(idx, idxToSwap)
         idx = idxToSwap
         leftChildIdx = idx * 2 + 1

   def prelocateUp(self, idx):
      while idx != 0:
         parentIdx = (idx-1) // 2
         if self.heap[parentIdx].data < self.heap[idx].data:
            return   
         self.swap(parentIdx, idx)
         idx = parentIdx

   def swap(self, i, j):
      self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
   
# O(nlogk) time | O(k + 1) space
def sort(lst: DLL, k):
   minHeap = MinHeap()
   curNode = lst.head
   for _ in range(k + 1):
      if curNode is None:
         break
      nodeToInsert = curNode
      curNode = curNode.next
      minHeap.insert(nodeToInsert)
   newListHead = newListTail = None
   while not minHeap.isEmpty():
      node = minHeap.delete()
      node.next = node.prev = None
      if curNode:
         minHeap.insert(curNode)
         curNode = curNode.next
      if newListHead is None:
         newListHead = newListTail = node
      else:
         newListTail.next = node
         newListTail = node
   lst.head = newListHead
   lst.tail = newListTail


dll = DLL()
dll.insert(3)
dll.insert(6)
dll.insert(2)
dll.insert(12)
dll.insert(56)
dll.insert(8)
dll.display()
sort(dll, k = 2)
dll.display()