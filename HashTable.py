from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

  def create_arr(self, size): # creates array and fills elements with a ll object
    arr = []

    for i in range(size):
      ll = LinkedList()
      arr.append(ll)

    return arr

  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored.

  def hash_func(self, key): # creates keys into index values were it can decide were to store key value pairs
    word = key.lower()
    hashNum = ord(word[0])
    index = hashNum % self.size

    return index

  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

  def insert(self, key, value): # generates a hashed key, assings to a touple, checks for duplicates, if found it will place in a ll, then we run replace to remove the past duplicate
    hashKey = self.hash_func(key)
    bit = (key, value)
    newBit = self.arr[hashKey].find(key)

    if newBit != -1:
      new_item = self.arr[hashKey].append(newBit)
      self.arr[hashKey].replace(new_item)

    else:
        self.arr[hashKey].append(bit)

  # Traverse through the every Linked List in the table and print the key value pairs.

  def print_key_values(self): # goes throughout all the table and prints all data to the command line
    for i in range(self.size):
      self.arr[i].print_nodes()
