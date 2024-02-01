import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from the start node to this node
        self.h = h  # Heuristic cost from this node to the goal node
    
    def f(self):
        return self.g + self.h
    
    # Define comparison methods for heapq
    def __lt__(self, other):
        return self.f() < other.f()
    
    def __eq__(self, other):
        return self.state == other.state

def astar(start_state, goal_state, successors, heuristic):
    start_node = Node(state=start_state, g=0, h=heuristic(start_state, goal_state))
    open_set = [(start_node.f(), start_node)]
    closed_set = set()

    while open_set:
        _, current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for successor, cost in successors(current_node.state):
            if successor in closed_set:
                continue
            
            g = current_node.g + cost
            h = heuristic(successor, goal_state)
            new_node = Node(state=successor, parent=current_node, g=g, h=h)
            heapq.heappush(open_set, (new_node.f(), new_node))

    return None

# Example usage:
# Define a simple grid world and implement A* algorithm

def successors(state):
    x, y = state
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_successors = [(x, y) for x, y in candidates if 0 <= x < 5 and 0 <= y < 5]
    return [(successor, 1) for successor in valid_successors]

def heuristic(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

start_state = (0, 0)
goal_state = (4, 4)
path = astar(start_state, goal_state, successors, heuristic)
print("Path found by A* algorithm:", path)
