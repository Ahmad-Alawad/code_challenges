class BNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        assert left is None or isinstance(left, BNode)
        assert right is None or isinstance(right, BNode)

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BNode %s>" % self.data

    def find(self, sought):
        """Return node with this data.

        Start here. Return None if not found.
        """

        node = self

        while node:

            print "checking ", node.data

            if node.data == sought:
                return node

            elif sought < node.data:
                node = node.left

            elif sought > node.data:
                node = node.right


    def print_in_order(self):

        if self.left:
            self.left.print_in_order()

        print self.data, "\t",

        if self.right:
            self.right.print_in_order()

class BTree(object):
    """ Binary Tree Class """
    def __init__(self):
        self.root = None


    def create_tree_from_list(self,data_list):
        global counter
        counter = 0
        if len(data_list) < 1:
            "No enough to create"
        elif len(data_list) == 1:
            node = BNode(data_list[0])
            self.root = node
        else:
            def subtree_from_list(sub_data_list):
                global counter
                counter += 1
                print "recursive call #%i data= %s" %(counter,sub_data_list)
                if len(sub_data_list) <= 0:
                    return None
                elif len(sub_data_list) == 1:
                    node = BNode(sub_data_list[0])
                    return node
                elif len(sub_data_list) == 2:
                    left_node = BNode(sub_data_list[0])
                    node = BNode(sub_data_list[1],left_node)
                    return node
                elif len(sub_data_list) == 3:
                    left_node = BNode(sub_data_list[0])
                    right_node = BNode(sub_data_list[2])
                    node = BNode(sub_data_list[1],left_node, right_node)
                    return node
                else:
                    root_index = len(sub_data_list) / 2
                    left_node = subtree_from_list(sub_data_list[:root_index])
                    right_node = subtree_from_list(sub_data_list[root_index+1:])
                    node = BNode(sub_data_list[root_index],left_node, right_node)

                    return node 
            # import pdb; pdb.set_trace()
            root_index = len(data_list) / 2
            self.root = BNode(data_list[root_index])
            min_index = root_index
            if min_index < 0:
                min_index = 0
            self.root.left = subtree_from_list(data_list[0:min_index])
            self.root.right = subtree_from_list(data_list[root_index+1:])
            

if __name__ == '__main__':

    numbers = [2,5,6,7,10,12,15,17,20,23,25,27,30,32,34,35,40]

    tree = BTree()
    tree.create_tree_from_list(numbers)
    root = tree.root
    print "\n\nPrinting the data in order \n"
    root.print_in_order()
    print
