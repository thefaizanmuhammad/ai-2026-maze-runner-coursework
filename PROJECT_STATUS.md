# AI Maze Runner — Project Status

## Overall Status

- [x] GitHub repository created
- [x] Starter code added
- [x] Branch structure created
- [ ] Q1–Q9 completed
- [ ] Full integration testing
- [ ] Report completed
- [ ] Final submission prepared

---

## Faizan — Set A: Q1, Q3, Q4, Q8

### Q1 — DFS
- Status: Not started
- Last update:
- Notes:

### Q3 — DLS
- Status: Not started
- Last update:
- Notes:

### Q4 — IDS
- Status: Not started
- Last update:
- Notes:

### Q8 — Key Hunt Problem
- Status: Not started
- Last update:
- Notes:

---

## Hadia — Set B: Q2, Q5, Q6, Q7

### Q2 — BFS
- **Status:** Completed and tested successfully.
- **Last update:** Implemented Breadth-First Search using a FIFO queue and an expanded set to prevent repeated state expansion.
- **Notes:**
  - Uses graph search and returns the sequence of actions leading to the exit.
  - Tested successfully on `maze_medium`: path cost 66, 66 steps, 407 nodes expanded.
  - Tested successfully on `open_glade`: path cost 32, 32 steps, 344 nodes expanded.
  - Both tests matched the expected assignment results.

### Q5 — UCS
- **Status:** Completed and tested successfully.
- **Last update:** Implemented Uniform-Cost Search using a priority queue ordered by cumulative path cost, `g(n)`.
- **Notes:**
  - Accounts for different terrain costs to find the minimum-cost route.
  - Uses an expanded set to avoid expanding the same state more than once.
  - Tested successfully on `griever_alley`: path cost 42, 28 steps, 50 nodes expanded.
  - Tested successfully on `ivy_maze`: path cost 70, 64 steps, 418 nodes expanded.
  - Both tests matched the expected assignment results.

### Q6 — Greedy Best-First Search + Heuristics
- **Status:** Implemented; final test verification in progress.
- **Last update:** Implemented Greedy Best-First Search in `search.py` and Manhattan and Euclidean distance heuristics in `heuristics.py`.
- **Notes:**
  - Greedy uses a priority queue ordered by heuristic value, `h(n)`.
  - Manhattan distance calculates the sum of absolute row and column differences.
  - Euclidean distance calculates straight-line distance to the goal.
  - Initial testing produced a `Method not implemented` error, which was resolved after updating and saving the correct files.
  - The algorithm subsequently returned `ESCAPED!`. Final path cost, steps, and expanded-node counts still need to be recorded.

### Q7 — A*
- **Status:** Implemented; final test verification in progress.
- **Last update:** Implemented A* Search using a priority queue ordered by `f(n) = g(n) + h(n)`.
- **Notes:**
  - Combines actual accumulated path cost with the heuristic estimate.
  - Uses graph search and an expanded set to prevent repeated expansions.
  - Supports Manhattan and Euclidean heuristics.
  - The initial `Method not implemented` error was addressed by updating `search.py`.
  - Final local testing and confirmation of path cost, steps, and expanded-node counts are pending.

---
---

## Shared — Faizan and Hadia

### Q9 — Key Hunt Heuristic
- Status: Not started
- Last update:
- Notes:

---

## Report

- [ ] AI Assistant Used
- [ ] Results tables
- [ ] DFS vs BFS
- [ ] IDS
- [ ] Costs
- [ ] Heuristics
- [ ] Q9 heuristic explanation

---

## Integration / Testing

- [ ] Faizan branch merged into main
- [ ] Hadia branch merged into main
- [ ] Q1–Q9 tested
- [ ] Expected results checked
- [ ] `--compare` results collected
- [ ] Final code tested from `main`

---

## Important Notes

Add any shared issues, bugs, decisions, or things the other person should know here.
