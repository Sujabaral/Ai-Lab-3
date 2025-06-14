# Simple Romania map neighbors
romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Timisoara': ['Arad'],
    'Bucharest': []
}

# Simple heuristic (distance to Bucharest)
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Fagaras': 176,
    'Timisoara': 329,
    'Bucharest': 0
}

class SimpleUtilityAgent:
    def __init__(self, environment, heuristic, start, goal):
        self.env = environment
        self.heuristic = heuristic
        self.current = start
        self.goal = goal
        self.path = [start]

    def next_move(self):
        if self.current == self.goal:
            return None
        neighbors = self.env[self.current]
        # Pick neighbor with smallest heuristic (closest to goal)
        next_city = min(neighbors, key=lambda city: self.heuristic[city])
        return next_city

    def move(self):
        next_city = self.next_move()
        if next_city:
            self.current = next_city
            self.path.append(next_city)

    def run(self):
        print(f"Starting at {self.current}, goal is {self.goal}")
        while self.current != self.goal:
            print(f"At {self.current}, moving to next best city...")
            self.move()
        print(f"Reached {self.goal}!")
        print("Path:", " -> ".join(self.path))

# Run example
agent = SimpleUtilityAgent(romania_map, heuristic, start='Arad', goal='Bucharest')
agent.run()
