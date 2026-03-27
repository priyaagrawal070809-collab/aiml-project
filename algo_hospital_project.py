name - priya agrawal(25bai10987)
import numpy as np
import matplotlib.pyplot as plt
import heapq

def heuristic(a, b):
    """Manhattan distance (admissible for grid paths)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    """A* pathfinder: cost = distance + 2 * infection_risk per cell."""
    rows, cols = grid.shape
    open_set = []  # Priority queue: (f_score, g_score, position)
    heapq.heappush(open_set, (heuristic(start, goal), 0, start))
    
    came_from = {}
    g_score = np.full((rows, cols), np.inf)
    g_score[start] = 0
    f_score = np.full((rows, cols), np.inf)
    f_score[start] = heuristic(start, goal)
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        if current == goal:
            # Backtrack to get path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Neighbors: up, down, left, right
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dr, current[1] + dc)
            nr, nc = neighbor
            if 0 <= nr < rows and 0 <= nc < cols and grid[neighbor] != 1:  # Valid, not wall
                # Movement cost: 1 (distance) + penalty for risk
                move_cost = 1 + grid[neighbor] * 2
                tentative_g = current_g + move_cost
                
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], tentative_g, neighbor))
    
    return []  # No path found

# Hospital grid: 0=safe floor, 0.5=medium risk (e.g., crowded hall), 1=wall/obstacle, 2=high risk (isolation)
grid = np.zeros((15, 20))
grid[3:8, 5:8] = 1      # Walls (rooms/corridors)
grid[10:12, 2:5] = 1    # More walls
grid[5:7, 12:15] = 2    # High infection zone (red)
grid[1:3, 16:19] = 0.5  # Medium risk (orange)

start = (1, 1)  # Nurse station (green)
goal = (13, 18) # Patient room (red)

path = astar(grid, start, goal)

# Visualization
fig, ax = plt.subplots(figsize=(12, 9))
im = ax.imshow(grid, cmap='Reds', alpha=0.7, vmin=0, vmax=2)
if path:
    path_array = np.array(path)
    ax.plot(path_array[:, 1], path_array[:, 0], 'b-', linewidth=5, label='Optimal Path (Low Exposure)')
ax.plot(start[1], start[0], 'go', markersize=20, label='Start: Nurse Station', markeredgecolor='black', markeredgewidth=2)
ax.plot(goal[1], goal[0], 'ro', markersize=20, label='Goal: Patient Room', markeredgecolor='black', markeredgewidth=2)
ax.set_title('Hospital A* Pathfinding: Minimize Infection Exposure\n(Grid: Risk Levels; Path Avoids High-Risk Zones)', fontsize=14, pad=20)
ax.set_xlabel('Columns (X)')
ax.set_ylabel('Rows (Y)')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3, linestyle='--')
plt.colorbar(im, ax=ax, label='Infection Risk (0=Safe, 1=Wall, 2=High Risk)', shrink=0.8)
plt.tight_layout()
plt.savefig('hospital_path_astar.png', dpi=150, bbox_inches='tight')
plt.show()

# Stats
if path:
    total_cost = sum(1 + grid[pos] * 2 for pos in path[1:])  # Exclude start
    print(f"Path found: {len(path)-1} steps, total exposure cost: {total_cost:.1f}")
    print("Path coordinates:", path)
else:
    print("No path found.")
