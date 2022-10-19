"""Binary Search Tree."""


class TreeNode:
    """Manage tree node that can be a subtree."""

    def __init__(self, data: str, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

    def add(self, data: str):
        """Add new data into the proper place of sub subtree."""
        if int(data) <= int(self.data):
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add(data)

    def get_sub_tree_data(self) -> list[str]:
        """Return sorted data from this subtree."""
        all_data = [] if self.left is None else self.left.get_sub_tree_data()
        all_data += [self.data]
        all_data += [] if self.right is None else self.right.get_sub_tree_data()
        return all_data


class BinarySearchTree:
    """Build and manage access to a binary-search-tree."""

    def __init__(self, tree_data: list[str]):
        self.root = tree_data

    @property
    def root(self):
        """Return root node."""
        return self._root

    @root.setter
    def root(self, tree_data: list[str]):
        """Build binary-tree and set its root node.

        :param tree_data: list of data (numbers) to build the tree with.
        :return: None
        """
        self._root = TreeNode(tree_data[0])
        for data in tree_data[1:]:
            self.root.add(data)

    def data(self) -> TreeNode:
        """Return root node of binary tree."""
        return self.root

    def sorted_data(self) -> list[str]:
        """Return sorted data of binary tree nodes."""
        return self.root.get_sub_tree_data()
