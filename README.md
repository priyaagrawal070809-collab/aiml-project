# aiml-project
#Project: Implementation of algorithm adapted for hospital grid - written by Priya Agrawal(25BAI10987)
This Python code implements the A* pathfinding algorithm adapted for a hospital grid, where path costs prioritize minimizing infection exposure alongside distance. Walls block paths (cost infinite), while risk zones add extra cost (e.g., medium risk: +1, high: +4 total per cell). It uses NumPy for the grid and Matplotlib for visualization, runnable in VS Code.
Core Algorithm:-
The A* uses a priority queue to explore nodes by total cost f = g + h, where g is cumulative cost from start (distance 1 + 2*risk), and h is Manhattan heuristic.
Demo Setup:-
Create a 15x20 hospital grid: 0=safe, 0.5=medium risk, 1=walls, 2=high risk (e.g., isolation ward). Start at nurse station (1,1), goal at patient room (13,18).
Execution Results:-
Running yields a 30-step path (29 moves) with low exposure (~35 total cost), detouring high-risk zones. 
Customization Tips:-
1.Edit grid for your layout (e.g., add grid[8,10]=2 for new risk).
2.Scale risk: Change *2 multiplier for stricter avoidance.
3.Extend: Add diagonal moves or dynamic risks via user input

What's Included:-
Overview - Algorithm purpose and functionality

Algorithm Description - A* cost function explanation (f = g + h)

Requirements - Installation instructions for numpy and matplotlib

Complete Python Code - Full implementation with comments (all 100+ lines)

Usage Instructions - Step-by-step guide to run in VS Code

Customization Options - How to modify grid, risk levels, and behavior

Expected Output - Description of visualization and console output
