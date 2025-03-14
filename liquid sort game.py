class Container:
    def __init__(self, colors):
        self.colors = colors

    def is_full(self):
        return len(self.colors) >= 4

    def is_empty(self):
        return len(self.colors) == 0

    def top_color(self):
        if not self.is_empty():
            return self.colors[-1]
        return None

    def can_pour_into(self, other):
        if self.is_empty() or other.is_full():
            return False
        return other.is_empty() or self.top_color() == other.top_color()

    def pour_into(self, other):
        if self.can_pour_into(other):
            while self.colors and not other.is_full() and (other.is_empty() or self.top_color() == other.top_color()):
                other.colors.append(self.colors.pop())

    def __str__(self):
        return " | ".join(self.colors) if self.colors else "Empty"

def display_containers(containers):
    for i, container in enumerate(containers):
        print(f"Container {i + 1}: {container}")

def is_game_won(containers):
    return all(len(set(container.colors)) == 1 for container in containers if not container.is_empty())

def liquid_sort_game():
    # Initializing containers with liquids
    containers = [
        Container(['Red', 'Blue', 'Green', 'Red']),
        Container(['Blue', 'Green', 'Red', 'Blue']),
        Container(['Green', 'Red', 'Blue', 'Green']),
        Container([]),
        Container([]),
    ]

    while not is_game_won(containers):
        display_containers(containers)
        try:
            from_container = int(input("Select the container to pour from (1-5): ")) - 1
            to_container = int(input("Select the container to pour into (1-5): ")) - 1

            if 0 <= from_container < len(containers) and 0 <= to_container < len(containers):
                containers[from_container].pour_into(containers[to_container])
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Invalid input, please enter numbers.")

    print("Congratulations! You've sorted all the liquids!")
    display_containers(containers)

# Run the game
liquid_sort_game()
