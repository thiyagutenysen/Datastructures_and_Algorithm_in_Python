# idea
# if (say)father=p;
# then left_son=(2*p)+1;
# and right_son=(2*p)+2;


# N = number of elements in a tree
N = 10
tree = [None]*N


def root(data):
    if tree[0]:
        print("Tree root already exist")
    else:
        tree[0] = data


def set_left(data, parent):
    if tree[parent] == None:
        print("No parent found")
    elif 2*parent+1 >= N:
        print("array is incapable to add this node to the tree")
    else:
        tree[2*parent+1] = data


def set_right(data, parent):
    if tree[parent] == None:
        print("No parent found")
    elif 2*parent+2 >= N:
        print("array is incapable to add this node to the tree")
    else:
        tree[2*parent+2] = data

# level order printing


def print_tree():
    for i in range(N):
        if tree[i]:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()


# output
root('A')
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()
