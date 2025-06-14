
romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

class GoalDrivenAgent:
    def __init__(self, environment, start, goal):
        self.environment = environment
        self.current_city = start
        self.goal = goal
        self.path = [start]  # Keep track of the path taken

    def perceive(self):
        # Returns current city
        return self.current_city

    def decide_action(self):
        if self.current_city == self.goal:
            return None  # Goal reached

        # Simple decision: move to any connected city not yet visited,
        # or towards the goal if connected.
        neighbors = self.environment[self.current_city]

        # If goal is directly connected, move there
        if self.goal in neighbors:
            return self.goal

        # Otherwise, pick the next city not in path to avoid cycles
        for city in neighbors:
            if city not in self.path:
                return city

        # If all neighbors visited, just pick first neighbor (not optimal but works)
        return neighbors[0]

    def act(self, next_city):
        self.current_city = next_city
        self.path.append(next_city)

    def run(self):
        print(f"Starting at {self.current_city}, goal is {self.goal}")
        while self.current_city != self.goal:
            print(f"Current city: {self.current_city}")
            next_city = self.decide_action()
            if next_city is None:
                break
            print(f"Moving to: {next_city}")
            self.act(next_city)
        print(f"Goal {self.goal} reached!")
        print("Path taken:", " -> ".join(self.path))


# Example usage:
agent = GoalDrivenAgent(romania_map, start='Arad', goal='Bucharest')
agent.run()
