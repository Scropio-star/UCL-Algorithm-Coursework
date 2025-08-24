# UCL-Algorithm-Coursework

# Overview
simple implement about some basic sort algorithm and data structure


## 2-3 tree
### Features
- Insert keys
- Search for keys
- Visual tree structure printing

### Classes
#### `Node23` Class
Represents a node in the 2-3 tree.

##### Attributes:
`keys`: List of keys stored in the node (up to 2 keys)

`children`: List of child nodes (up to 3 children)

`is_leaf`: Boolean indicating whether the node is a leaf

### Tree23 Class
Main implementation of the 2-3 tree.

#### Methods:

`__init__()` : Initializes an empty tree

`insert(key)`: Inserts a key into the tree

`search(key)`: Searches for a key in the tree, returns a boolean

`print_tree(node, level)`: Prints the tree structure (for debugging)

## Circular List 