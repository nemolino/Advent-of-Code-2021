from math import ceil
from binarytree import Node
from copy import deepcopy

def build_tree(s, root):

    root.left = Node(-1)
    root.left.parent = root
    root.right = Node(-1)
    root.right.parent = root
    
    if isinstance(s[0], int): root.left = Node(s[0])
    else: root.left = build_tree(s[0], root.left)
    
    if isinstance(s[1], int): root.right = Node(s[1])
    else: root.right = build_tree(s[1], root.right)

    return root
                
def reduce_tree(root):

    flag = True
    while flag:
        flag = False

        ### explode operation 
        if root.max_leaf_depth == 5:
            
            flag, prec, succ, right, node_exploded = True, None, False, None, False
            
            def explode(root, level):

                nonlocal prec, succ, right, node_exploded
                
                if root is None or (node_exploded == True and succ == False): return

                if root.value != -1 and succ:
                    root.value += right
                    succ = False
                    return
                
                if level == 4 and root.value == -1 and node_exploded == False:
                    right = root.right.value
                    if prec is not None:
                        prec.value += root.left.value
                    root.value = 0
                    root.left = None
                    root.right = None
                    succ = True
                    node_exploded = True
                    return

                if root.value != -1 and not succ: prec = root
                
                explode(root.left, level+1)
                explode(root.right, level+1)

            explode(root, 0)
        
        ### split operation       
        if root.max_node_value >= 10 and flag == False:

            flag, node_splitted = True, False

            def split(root):

                nonlocal node_splitted
                
                if root is None or node_splitted == True: return
                
                if root.value >= 10:
                    root.left = Node(root.value//2)
                    root.left.parent = root
                    root.right = Node(ceil(root.value/2))
                    root.right.parent = root
                    root.value = -1
                    node_splitted = True
                    return

                split(root.left)
                split(root.right)

            split(root)

    return root
    
def get_magnitude(root):
    
    levels = root.levels
    while len(levels) > 1:
        tmp = [Node(levels[-1][i].value*3 + levels[-1][i+1].value*2) for i in range(0, len(levels[-1]), 2)]
        levels = levels[:-1]
        levels[-1][:len(tmp)] = tmp
        
    return levels[0][0].value
                   
def day18_a():

    # a snailfish number is represented by a binary tree
    
    with open('in.txt') as f: num = f.read().split('\n')

    root1 = Node(-1)
    root1.parent = Node(-1)
    root1 = build_tree(eval(num[0]), root1)

    for i in range(1, len(num)):

        root2 = Node(-1)
        root2.parent = Node(-1)
        root2 = build_tree(eval(num[i]), root2)

        root = Node(-1)
        root.parent = Node(-1)
        root.left = root1
        root.right = root2

        root = reduce_tree(root)
        root1 = root
        
    return get_magnitude(root)

def day18_b():

    with open('in.txt') as f: num = f.read().split('\n')

    num_roots = []

    for el in num:
        num_roots.append(Node(-1))
        num_roots[-1].parent = Node(-1)
        num_roots[-1] = build_tree(eval(el), num_roots[-1])

    max_mag = 0

    for a in num_roots:
        
        root = Node(-1)
        root.parent = Node(-1)
        
        for b in num_roots:

            root.left = deepcopy(a)
            root.right = deepcopy(b)

            mag = get_magnitude(reduce_tree(root))
            if mag > max_mag: max_mag = mag
                
            root.left, root.right = root.right, root.left

            mag = get_magnitude(reduce_tree(root))
            if mag > max_mag: max_mag = mag

    return max_mag

if __name__ == "__main__":
    print(day18_a())
    print(day18_b())
