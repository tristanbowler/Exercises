class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
        
def serializeHelper(node, array):
        if node is None:
            array.append(None)
            return
        
        array.append(node.val)
        serializeHelper(node.left, array)
        serializeHelper(node.right, array)
    
def serialize(node):
    array = []
    serializeHelper(node, array)
    serialized = ""
    for item in array:
        serialized = serialized + str(item) + ','
    serialized = serialized[:-1] # chop off extraneous comma
    return serialized

def deserializeHelper(index, array):
    if array[index] == 'None':
        return (None, index)
    
    node = Node(array[index])
    index = index + 1
    (node.left, index ) = deserializeHelper(index, array)
    index = index + 1
    (node.right, index) = deserializeHelper(index, array)
    return (node, index)

def deserialize(serialized):
    array = serialized.split(',')
    (node, index) = deserializeHelper(0, array)
    return node
    
node = Node('root', Node('left', Node('left.left', Node('left.left.left'), Node('left.left.right'))), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'