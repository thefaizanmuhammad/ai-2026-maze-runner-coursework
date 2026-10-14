# AI Maze Runner — Project Status

## Overall Status

- [x] GitHub repository created
- [x] Starter code added
- [x] Branch structure created
- [x] Q1–Q8 implemented, merged, and tested on `main`
- [ ] Q1–Q9 completed
- [ ] Full integration testing
- [ ] Report completed
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
- Notes: Key Hunt tested with the integrated BFS: keys_tiny cost 26, 26 steps, 490 expansions; keys_small cost 54, 54 steps, 1723 expansions. All keys collected before finishing at the exit. Q9 remains pending.

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
- Status: Completed and tested on `faizan`; merge into `main` pending
- Last update: 14 October 2026
- Notes: Uses nearest-key distance + a minimum spanning tree over remaining keys + nearest-key-to-exit distance, with cached maze distances and tree costs. With no keys remaining, uses distance to the exit. `keys_medium`: start heuristic 83, optimal cost 94, 94 steps, 446 A* expansions versus 9695 UCS expansions. Consistency passed on all reachable states and transitions of keys_tiny, keys_small, keys_medium, a weighted-terrain test, and a no-key test. Goal heuristic is zero. A* costs matched UCS on all tested key layouts.

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

- [x] Faizan branch merged into main
- [x] Hadia branch merged into main
- [x] Q1–Q8 tested on `main` (16 reference cases plus edge checks)
- [ ] Q1–Q9 tested
- [x] Q1–Q8 expected results checked
- [ ] Q9 consistency and performance checked
- [ ] `--compare` results collected
- [ ] Final code tested from `main`

---

## Important Notes

Q1–Q8 are integrated on `main`. Q9 is implemented and tested on `faizan`; its merge and full final testing remain pending, along with report preparation and submission. AI assistance must be disclosed in the report.
