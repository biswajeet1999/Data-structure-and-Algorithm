# ternary search tree is used to store strings in more efficient way
# string operations are also more efficient
# Ternary search tree = trie + binary search tree
# Author:- Biswajeet padhi
# Date:- 19/1/2019
# 3rd sem

class Node():
    
    def __init__(self,data=''):
        self.data = data
        self.left = None
        self.middle = None
        self.right = None
        self.is_leaf = False

    def displayAllWords(self, word, index,prefix=''):  # prefix is used only for correct function otherwise not required
        global corrected_word_found
        if self.is_leaf == True:
            word = word[:len(word)-1]+self.data
            corrected_word_found = True # it is used for correct function otherwise not required
            print(prefix+word)
            
        if self.left is not None:
            self.left.displayAllWords(word,index,prefix)

        if self.middle is not None:  
            word = word[:len(word)-1]+self.data+' '  # extra spaces are added for adjustment purpose
            self.middle.displayAllWords(word, index+1,prefix)
            word = word[:index]+' ' # extra spaces are added for adjustment purpose
        
        if self.right is not None:
            self.right.displayAllWords(word,index,prefix)

class TernarySearchTree():
    
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        length = len(data)

        if(self.root == None):
            self.root = Node(data[0])
            if len(data) == 1:
                self.root.is_leaf = True

        # if root is leaf node then start from index 1 else start from index 0
        start_index = 1 if(self.root.left == None and self.root.right == None and self.root.middle == None) else 0
        temp = self.root
        
        for i in range(start_index,length):
            # find node
            while True :
                if i>0 and data[i-1] == temp.data:
                    if temp.middle == None:
                        temp.middle = Node(data[i])
                        temp = temp.middle
                        if i == len(data)-1:
                            temp.is_leaf = True
                        break
                    temp = temp.middle
                elif data[i] < temp.data:
                    if temp.left is None:
                        temp.left = Node(data[i])
                        temp = temp.left
                        if i == len(data)-1:
                            temp.is_leaf = True
                        break
                    temp = temp.left
                elif data[i] > temp.data: 
                    if temp.right is None:
                        temp.right = Node(data[i])
                        temp = temp.right
                        if i == len(data)-1:
                            temp.is_leaf = True
                        break
                    temp = temp.right
                elif data[i] == temp.data:
                    if i == len(data)-1:
                            temp.is_leaf = True
                    break
                    
    def displayAllWords(self):
        if self.root == None:
            print("No string exists")
        else:
            self.root.displayAllWords(' ',0) 

    def correct(self,parent,prefix):
        parent.displayAllWords(' ',0,prefix) # prifix should be add at the first of all searched words
        
    def search(self,word):
        if self.root == None:
            print("not found")
            return
        temp = self.root
        parent = None  # parent is used only for correction purpose like google search engine. for normal search operation parent is not required
        for i in range(0,len(word)):
            while temp is not None:
                if word[i] == temp.data:
                    if i == len(word)-1 and temp.is_leaf == True:
                        print('found')
                        return
                    parent = temp
                    temp = temp.middle
                    break
                elif word[i] > temp.data:
                    parent = temp
                    temp = temp.right
                elif word[i] < temp.data:
                    parent = temp
                    temp = temp.left
            if temp is None:
                print('Not found')
                print("Are you searching for: ")
                self.correct(parent,word[:i])
                if corrected_word_found == False:
                    print("No results found")
                return

        print('Not found')
        print("Are you searching for: ")
        self.correct(temp,word)

        if corrected_word_found == False:
                    print("No results found")
        

            

corrected_word_found = False

root = TernarySearchTree()
root.insert('apple')
root.insert('air')
root.insert('bal')
root.insert('cat')
root.insert('rat')
root.insert('elephant')
root.insert('dog')
root.insert('cow')
root.insert('god')
#root.displayAllWords()
s = input("Enter word to search: ")
while s != 'exit':
    root.search(s)
    s = input("Enter word to search: ")
