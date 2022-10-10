"""Recordes to tree nodes.

Web-forums have a tree layout, so posts are presented as a tree.
However the posts are typically stored in a database as an unsorted
set of records. Thus when presenting the posts to the user the tree
structure has to be reconstructed.

The records only contain an ID number and a parent ID number.
The ID number is always between 0 (inclusive) and the length of the
record list (exclusive). All records have a parent ID lower than their
own ID, except for the root record, which has a parent ID that's equal
to its own ID.
"""


class Record:
    """DB record."""
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """Tree node."""
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    records.sort(key=lambda x: x.record_id)
    if records[-1].record_id != len(records) - 1 or records[0].record_id != 0:
        raise ValueError("Record id is invalid or out of order.")
    trees = []
    for rec in records:
        if rec.record_id < rec.parent_id:
            raise ValueError("Node record_id should be smaller than it's parent_id.")
        if rec.record_id == rec.parent_id != 0:
            raise ValueError("Only root should have equal record and parent id.")
        trees.append(Node(rec.record_id))
    for tree in trees:
        #tree.children = [record.record_id for record in records if record.parent_id == tree.node_id and record.record_id != 0]
        tree.children = [trees[record.record_id] for record in records if record.parent_id == tree.node_id and record.record_id != 0]
        #tree.children = [t for t in trees if records[t.node_id].parent_id == tree.node_id and t.node_id != 0]
    return trees[0]
