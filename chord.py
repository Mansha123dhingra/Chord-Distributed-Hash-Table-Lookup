class Node:
    def __init__(self, node_id, m):
        self.id = node_id
        self.m = m
        self.finger = [None] * m
        self.successor = None

    def __repr__(self):
        return f"Node({self.id})"


def create_ring(node_ids, m):
    nodes = [Node(i, m) for i in sorted(node_ids)]
    
    for i in range(len(nodes)):
        nodes[i].successor = nodes[(i + 1) % len(nodes)]
    
    return nodes


def build_finger_tables(nodes, m):
    max_id = 2 ** m
    
    for node in nodes:
        for i in range(m):
            target = (node.id + 2 ** i) % max_id
            
            for n in nodes:
                if n.id >= target:
                    node.finger[i] = n
                    break
            else:
                node.finger[i] = nodes[0]


def lookup(start_node, key):
    path = [start_node.id]
    current = start_node

    while True:
        if current.id < key <= current.successor.id:
            path.append(current.successor.id)
            break
        
        for finger in reversed(current.finger):
            if finger and current.id < finger.id < key:
                current = finger
                path.append(current.id)
                break
        else:
            current = current.successor
            path.append(current.id)

    return path


if __name__ == "__main__":
    print("Program started...")   # 👈 IMPORTANT
    
    m = 4
    node_ids = [1, 3, 7, 8, 12]
    
    nodes = create_ring(node_ids, m)
    build_finger_tables(nodes, m)
    
    start = nodes[0]
    key = 10
    
    path = lookup(start, key)
    print("Lookup Path:", path)