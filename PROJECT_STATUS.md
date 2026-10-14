# AI Maze Runner — Project Status

## Overall Status

- [x] GitHub repository created
- [x] Starter code added
- [x] Branch structure created
- [x] Q1–Q8 implemented, merged, and tested on `main`
- [x] Q1–Q9 completed
- [x] Full integration testing (expected IDS timeouts recorded below)
- [x] Report completed
- [ ] Final submission prepared

---

## Faizan — Set A: Q1, Q3, Q4, Q8

### Q1 — DFS
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: DFS: maze_small cost 50, 50 steps, 82 expansions; maze_medium cost 162, 162 steps, 233 expansions.

### Q3 — DLS
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: DLS: maze_small limit 60 gives cost 50, 50 steps, 52 expansions; limit 30 gives CUTOFF, 32 expansions. Boundary and shorter-route checks passed.

### Q4 — IDS
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: IDS: maze_small cost 50, 50 steps, 1352 expansions. Start-goal, failure, and depth-bound checks passed before integration.

### Q8 — Key Hunt Problem
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: Key Hunt tested with the integrated BFS: keys_tiny cost 26, 26 steps, 490 expansions; keys_small cost 54, 54 steps, 1723 expansions. All keys collected before finishing at the exit. Q9 is also integrated and tested.

---

## Hadia — Set B: Q2, Q5, Q6, Q7

### Q2 — BFS
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: BFS: maze_tiny cost 8, 8 steps, 27 expansions; maze_medium cost 66, 66 steps, 407 expansions; open_glade cost 32, 32 steps, 344 expansions.

### Q5 — UCS
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: UCS: griever_alley cost 42, 28 steps, 50 expansions; ivy_maze cost 70, 64 steps, 418 expansions. Cheaper alternative-route check passed.

### Q6 — Greedy Best-First Search + Heuristics
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: Greedy with Manhattan: greedy_trap cost 52, 25 steps, 60 expansions; maze_medium cost 80, 80 steps, 81 expansions. Manhattan and Euclidean heuristics passed consistency checks on all provided mazes.

### Q7 — A*
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: A* with Manhattan: greedy_trap cost 25, 25 steps, 155 expansions; maze_big cost 124, 124 steps, 679 expansions.

---

## Shared — Faizan and Hadia

### Q9 — Key Hunt Heuristic
- Status: Completed, merged, and tested on `main`
- Last update: 14 October 2026
- Notes: Uses nearest-key distance + a minimum spanning tree over remaining keys + nearest-key-to-exit distance, with cached maze distances and tree costs. With no keys remaining, uses distance to the exit. `keys_medium`: start heuristic 83, optimal cost 94, 94 steps, 446 A* expansions versus 9695 UCS expansions. Consistency passed on all reachable states and transitions of keys_tiny, keys_small, keys_medium, a weighted-terrain test, and a no-key test. Goal heuristic is zero. A* costs matched UCS on all tested key layouts.

---

## Report

- [x] AI Assistant Used
- [x] Results tables
- [x] DFS vs BFS
- [x] IDS
- [x] Costs
- [x] Heuristics
- [x] Q9 heuristic explanation

---

## Integration / Testing

- [x] Faizan branch merged into main
- [x] Hadia branch merged into main
- [x] Q1–Q8 tested on `main` (16 reference cases plus edge checks)
- [x] Q1–Q9 tested on `main`
- [x] Q1–Q8 expected results checked
- [x] Q9 consistency and performance checked
- [x] `--compare` results collected for maze_medium, open_glade, and ivy_maze
- [x] Final code tested from `main`

---

## Important Notes

Q1–Q9 are integrated and tested on `main`. The completed four-page report is saved as `report.pdf` in the project root and includes the AI assistance disclosure. The four required submission files are verified; final ZIP packaging and upload remain pending.


## Final Integration Results — 14 October 2026

- Tested integrated code at commit `525fae4` on `main`.
- All 16 assignment reference cases passed exactly, plus graph boundary/cycle/failure checks.
- 77 additional search runs across all 11 provided mazes passed; A* with Manhattan, Euclidean, and null heuristics matched UCS optimal costs.
- Q9 consistency checked exhaustively on keys_tiny (496 states, 1088 transitions), keys_small (1728 states, 3784 transitions), and keys_medium (11004 states, 24206 transitions). Goal heuristic was zero.
- Q9 A*: keys_tiny cost 26, 93 expansions; keys_small cost 54, 149 expansions; keys_medium cost 94, 446 expansions. All costs matched UCS.
- Instructor support files and maze layouts match the original ZIP byte-for-byte.
- CLI comparison runs below used a 10-second timeout per algorithm. IDS timed out on open_glade and ivy_maze because path-based search repeatedly explores different routes. These are recorded performance limits, not invalid-path or missing-implementation errors. Time and timeout expansion counts vary by machine.

```text
Medium maze - with loops  (21x41, problem: maze)
Algorithm                           Path cost    Steps   Expanded  Time (s)
---------------------------------------------------------------------------
Depth-first search                        162      162        233     0.005
Breadth-first search                       66       66        407     0.002
Iterative deepening search                 66       66     437730     1.936
Uniform-cost search                        66       66        407     0.002
Greedy best-first search [manhattan]         80       80         81     0.000
A* search [manhattan]                      66       66        209     0.001


The Open Glade - lots of room to wander  (15x33, problem: maze)
Algorithm                           Path cost    Steps   Expanded  Time (s)
---------------------------------------------------------------------------
Depth-first search                        234      234        322     0.002
Breadth-first search                       32       32        344     0.002
Iterative deepening search                  -        -    2257183    10.000   (timed out after 10.0 seconds)
Uniform-cost search                        32       32        344     0.002
Greedy best-first search [manhattan]         36       36         39     0.000
A* search [manhattan]                      32       32        114     0.001


The Ivy Maze - thick ivy (3) and Griever territory (10)  (21x41, problem: maze)
Algorithm                           Path cost    Steps   Expanded  Time (s)
---------------------------------------------------------------------------
Depth-first search                        159       88        422     0.004
Breadth-first search                       80       60        439     0.003
Iterative deepening search                  -        -    2417801    10.000   (timed out after 10.0 seconds)
Uniform-cost search                        70       64        418     0.002
Greedy best-first search [manhattan]        130       82         85     0.000
A* search [manhattan]                      70       64        344     0.002
```

## Final Submission Check

- All 20 reference and report-result checks passed.
- Q9 consistency rechecked on all reachable states in the three supplied key mazes.
- Instructor support files and maze layouts remain unchanged.
- Submit only `search.py`, `heuristics.py`, `griever_hole.py`, and `report.pdf`.
