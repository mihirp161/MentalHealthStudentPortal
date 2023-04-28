
# Refrences: https://iq.opengenus.org/b-tree-in-cpp/
# Reference: https://pythonexamples.org/python-list-of-dictionaries/

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, order):
        self.root = BTreeNode(True)
        #'order' is order of B Tree
        self.order = order
        
    """Get Keys' value-value at the key 'k', value 'v'.

    Returns 'None' if 'k' is not found.
    Otherwise return k's tuple value at which the value was found.

    Arguments:
            k -- key to be searched
            v -- key's value-key to be searched
    """     
    
    def get_keys_value(self, k, v):
        K = self.search(hash(k))
        if K != None:
            (x, i) = K
            dict = x.keys[i][2]
            return dict.get(v)


    """Update Keys value at the key 'k'.

    Returns 'None' if 'k' is not found.
    Otherwise go to k's tuple value at which the value was found.

    Arguments:
            k -- key to be searched
            v -- key's value-key to be searched
            uv -- new value to be inserted
    """     
    
    def update_keys(self, k, v, uv):
        K = self.search(hash(k))
        if K != None:
            (x, i) = K
            dict = x.keys[i][2]
            dict.update({v: uv})
            tpl = list(x.keys[i])
            tpl[2] = dict
            x.keys[i] = tuple(tpl)

    """Pull Node Info for key 'k'.

    Returns 'None' if 'k' is not found.
    Otherwise returns a dictionary information at which the key was found.

    Arguments:
            k -- key to be searched
    """      
    def pull_node_info(self, k):
        K = self.search(hash(k))
        if K != None:
            (x, i) = K
            print("The studentID has following: ", x.keys[i][2])
         
            
    """Search for key 'k' at position 'x'.
    If 'x' is not specified, then search occurs from root.

    Returns 'None' if 'k' is not found.
    Otherwise returns a tuple of node and index at which the key was found.

    Arguments:
            k -- key to be searched
            x -- position to search from
    """        
    def search(self, k, x=None):

        if x != None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                # Search in children
                return self.search(k, x.child[i])
        else:
            # Search entire tree as node not provided
            return self.search(k, self.root)


    """Insert key 'k' at position 'x' in a non-full node

    Arguments:
            x -- Position of node
            k -- key to be inserted
    """
    def insert_nonfull(self, x, k):

        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.order) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_nonfull(x.child[i], k)
            
    """Splits the child of node at 'x' from index 'i'

    Arguments:
            x -- parent node of the node to be split
            i -- index value of the child
    """
    def split_child(self, x, i):

        order = self.order
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[order - 1])
        z.keys = y.keys[order : (2 * order) - 1]
        y.keys = y.keys[0 : order - 1]
        if not y.leaf:
            z.child = y.child[order : 2 * order]
            y.child = y.child[0 : order - 1]
    
    
    """Insert key 'k' in the B-Tree

    Arguments:
            k -- key to be inserted
    """
    def insert(self, k):

        root = self.root
        # Keys are full, hence we must split child
        if len(root.keys) == (2 * self.order) - 1:
            temp = BTreeNode()
            self.root = temp
            # Former root becomes 0th child of new root 'temp'
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_nonfull(temp, k)
        else:
            self.insert_nonfull(root, k)
    
    
    
    """Deletes internal node

    Arguments:
            x -- internal node in which key 'k' is present
            k -- key to be deleted
            i -- index position of key in the list

    """
    def delete_internal_node(self, x, k, i):

        order = self.order
        # Deleting the key if the node is a leaf
        if x.leaf:
            if x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
            return

        # Replacing the key with its predecessor and deleting predecessor
        if len(x.child[i].keys) >= order:
            x.keys[i] = self.delete_predecessor_node(x.child[i])
            return
        # Replacing the key with its successor and deleting successor
        elif len(x.child[i + 1].keys) >= order:
            x.keys[i] = self._delete_successor(x.child[i + 1])
            return
        # Merging the child, its left sibling and the key 'k'
        else:
            self.delete_merge(x, i, i + 1)
            self.delete_internal_node(x.child[i], k, self.order - 1)
    
    
    """Returns and deletes predecessor of key 'k' which is to be deleted

    Arguments:
            x -- node
    """
    def delete_predecessor_node(self, x):

        if x.leaf:
            return x.pop()
        n = len(x.keys) - 1
        if len(x.child[n].keys) >= self.order:
            self.delete_sibling(x, n + 1, n)
        else:
            self.delete_merge(x, n, n + 1)
        self.delete_predecessor_node_node(x.child[n])
    
    
    """Returns and deletes successor of key 'k' which is to be deleted

    Arguments:
            x -- node
    """
    def delete_successor_node(self, x):

        if x.leaf:
            return x.keys.pop(0)
        if len(x.child[1].keys) >= self.order:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        self.delete_successor_node(x.child[0])
    
    
    """Merges the children of x and one of its own keys

    Arguments:
            x -- parent node
            i -- index of one of the children
            j -- index of one of the children
    """
    def delete_merge(self, x, i, j):

        cnode = x.child[i]

        # Merging the x.child[i], x.child[j] and x.keys[i]
        if j > i:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            # Assigning keys of right sibling node to child node
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.child) > 0:
                    cnode.child.append(rsnode.child[k])
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child.pop())
            new = cnode
            x.keys.pop(i)
            x.child.pop(j)
        # Merging the x.child[i], x.child[j] and x.keys[i]
        else:
            lsnode = x.child[j]
            lsnode.keys.append(x.keys[j])
            # Assigning keys of left sibling node to child node
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.child) > 0:
                    lsnode.child.append(cnode.child[i])
            if len(lsnode.child) > 0:
                lsnode.child.append(cnode.child.pop())
            new = lsnode
            x.keys.pop(j)
            x.child.pop(i)

        # If x is root and is empty, then re-assign root
        if x == self.root and len(x.keys) == 0:
            self.root = new
            
    """Borrows a key from jth child of x and appends it to ith child of x

    Arguments:
            x -- parent node
            i -- index of one of the children
            j -- index of one of the children
    """
    def delete_sibling(self, x, i, j):

        cnode = x.child[i]
        if i < j:
            # Borrowing key from right sibling of the child
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            x.keys[i] = rsnode.keys[0]
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child[0])
                rsnode.child.pop(0)
            rsnode.keys.pop(0)
        else:
            # Borrowing key from left sibling of the child
            lsnode = x.child[j]
            cnode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.child) > 0:
                cnode.child.insert(0, lsnode.child.pop())


    """Calls helper functions to delete key 'k' after searching from node 'x'

    Arguments:
            x -- node, according to whose relative position, helper functions are called
            k -- key to be deleted
    """
    def delete(self, x, k):

        order = self.order
        i = 0
        while i < len(x.keys) and k > x.keys[i][0]:
            i += 1
        # Deleting the key if the node is a leaf
        if x.leaf:
            if i < len(x.keys) and x.keys[i][0] == k:
                x.keys.pop(i)
                return
            return

        # Calling 'delete_internal_node' when x is an internal node and contains the key 'k'
        if i < len(x.keys) and x.keys[i][0] == k:
            return self.delete_internal_node(x, k, i)
        # Recursively calling 'delete' on x's child
        elif len(x.child[i].keys) >= order:
            self.delete(x.child[i], k)
        # Ensuring that a child always has atleast 'order' keys
        else:
            if i != 0 and i + 2 < len(x.child):
                if len(x.child[i - 1].keys) >= order:
                    self.delete_sibling(x, i, i - 1)
                elif len(x.child[i + 1].keys) >= order:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i == 0:
                if len(x.child[i + 1].keys) >= order:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i + 1 == len(x.child):
                if len(x.child[i - 1].keys) >= order:
                    self.delete_sibling(x, i, i - 1)
                else:
                    self.delete_merge(x, i, i - 1)
            self.delete(x.child[i], k)
