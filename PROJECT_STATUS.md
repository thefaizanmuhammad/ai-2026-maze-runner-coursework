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
- Status: Implemented and tested locally
- Last update: 14 October 2026
- Notes: Graph search with a Stack; maze_small and maze_medium match reference costs, steps, and expansion counts.

### Q3 — DLS
- Status: Implemented and tested locally
- Last update: 14 October 2026
- Notes: Recursive DFS with path cycle detection; distinguishes CUTOFF from failure and goal-tests the depth boundary without expanding it.

### Q4 — IDS
- Status: Implemented and tested locally
- Last update: 14 October 2026
- Notes: Calls DLS at increasing limits; stops on a solution or proven failure. maze_small: 50 steps, 1352 expansions.

### Q8 — Key Hunt Problem
- Status: Implemented and tested locally
- Last update: 14 October 2026
- Notes: State is (position, frozenset of remaining key positions). Independent BFS test oracle matches keys_tiny (26 steps, 490 expansions) and keys_small (54 steps, 1723 expansions). Integration with Hadia's BFS is pending.

---

## Hadia — Set B: Q2, Q5, Q6, Q7

### Q2 — BFS
- Status: Not started
- Last update:
- Notes:

### Q5 — UCS
- Status: Not started
- Last update:
- Notes:

### Q6 — Greedy Best-First Search + Heuristics
- Status: Not started
- Last update:
- Notes:

### Q7 — A*
- Status: Not started
- Last update:
- Notes:

---

## Shared — Faizan and Hadia

### Q9 — Key Hunt Heuristic
- Status: Not started
- Last update:
- Notes: The Q8 state stores remaining key positions in state[1]. The current heuristic is still the starter's trivial placeholder.

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

- Local verification: `python -m unittest discover -s tests -v` (11 tests passed).
- AI assistant used: OpenAI Codex helped implement and test Faizan's assigned questions and update project tracking. Include this assistance in the shared report disclosure.
- Q2, Q5, Q6, Q7 and Q9 remain pending; full `--compare` results require integration of that work.
- Tests are collaboration files; submit only `search.py`, `heuristics.py`, `griever_hole.py`, and `report.pdf` as required.
