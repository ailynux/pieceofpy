<h1 align="center">🚀 Python Data Structures and Algorithms 🚀</h1>

<p align="center">
  <img src="https://giffiles.alphacoders.com/360/36000.gif" alt="Animated" width="500px" />
</p>

<p align="center">
  <a href="https://github.com/ailynux/pieceofpy/actions">
    <img src="https://img.shields.io/github/workflow/status/ailynux/pieceofpy/Python%20CI?style=for-the-badge&logo=github-actions&logoColor=white&color=blueviolet" alt="GitHub Actions CI">
  </a>
  <a href="https://codecov.io/gh/ailynux/pieceofpy">
    <img src="https://img.shields.io/codecov/c/github/ailynux/pieceofpy?style=for-the-badge&logo=codecov&logoColor=white&color=ff69b4" alt="Codecov Coverage">
  </a>
  <a href="https://github.com/ailynux/pieceofpy/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/ailynux/pieceofpy?style=for-the-badge&color=yellowgreen" alt="License">
  </a>
   <a href="https://github.com/ailynux/pieceofpy/stargazers">
    <img src="https://img.shields.io/github/stars/ailynux/pieceofpy?style=for-the-badge&logo=github&color=orange" alt="GitHub Stars">
  </a>
</p>

<p align="center">
  <strong>Welcome to the ultimate guide on Python Data Structures and Algorithms!</strong><br>
  This repository is designed as an interactive tutorial and comprehensive reference to master the core elements of Python programming, essential for solving complex coding challenges and enhancing algorithmic thinking.
</p>


## Table of Contents

- [Introduction](#introduction)
- [Data Structures](#data-structures)
  - [Arrays](#arrays)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Linked Lists](#linked-lists)
  - [Trees](#trees)
  - [Graphs](#graphs)
- [Algorithms](#algorithms)
  - [Sorting Algorithms](#sorting-algorithms)
  - [Searching Algorithms](#searching-algorithms)
  - [Recursion](#recursion)
  - [Dynamic Programming](#dynamic-programming)
- [Contributing](#contributing)

## Introduction

Understanding data structures and algorithms is crucial for solving complex problems efficiently. This guide aims to introduce these concepts using Python, making them accessible to both beginners and experienced programmers.
<p align="center">
  <img src="https://threadwaiting.com/wp-content/uploads/2018/01/TechnicalFeaturesofPython.gif" alt="Animated" width=500px />
</p>

## Data Structures

### Arrays
- Arrays in Python can be implemented using lists. They allow storing elements in a contiguous block of memory, providing efficient access.
**Example:**
```python
# Creating an array
array = [1, 2, 3, 4, 5]
```
### Stacks
- A stack follows the Last In First Out (LIFO) principle. It can be implemented using Python's built-in list.
**Example:**
```python
stack = []
# Push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
# Pop an item off the stack
stack.pop()
```
### Queues
- A queue follows the First In First Out (FIFO) principle. The collections.deque is efficient for this purpose.
**Example:**
```python
from collections import deque
queue = deque()
# Enqueue items
queue.appendleft(1)
queue.appendleft(2)
# Dequeue an item
queue.pop()
```
### Linked Lists
- A linked list consists of nodes that contain a data field and a reference to the next node in the list.

**Example:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A simple linked list
a = Node(1)
b = Node(2)
a.next = b
```
### Trees
- Trees are hierarchical data structures. The binary tree is a type of tree where each node has at most two children.
**Example:**
```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```
### Graphs
- Graphs consist of nodes (vertices) and edges. They can represent various real-world relationships.
**Example:**

```python
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C']}
```
## Algorithms

### Sorting Algorithms
Sorting algorithms include bubble sort, quicksort, and merge sort. They organize data in a specific order.

### Searching Algorithms
Searching algorithms like linear search and binary search are used to find elements within data structures.

### Recursion
Recursion involves functions calling themselves to solve subproblems of a larger problem.

### Dynamic Programming
Dynamic programming techniques are used to solve problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid computing the same results multiple times.

----

## Contributing 

🌟🚀 **We love your inputs!** We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug 🐛
- Discussing the current state of the code 📝
- Submitting a fix 🔧
- Proposing new features 💡
- Becoming a maintainer 🙌

### Questions?

Feel free to contact me at `adiaz@ai-lyn.com`, or open an issue in the repository if you need any help or have questions.

## Happy Coding! 🎉
Your contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

