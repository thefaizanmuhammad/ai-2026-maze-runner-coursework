"""Regression checks for Faizan's Q1, Q3, Q4 and Q8 implementations.

Run from the project root: python -m unittest discover -s tests -v
The BFS helper is a test oracle, independent of Hadia's search.py work.
"""

import unittest
from collections import deque

import maze
import runner
import search
from griever_hole import KeyHuntProblem
from problems import GraphProblem
from util import CUTOFF


def reference_bfs(problem):
    fringe = deque([(problem.getStartState(), [])])
    expanded = set()
    while fringe:
        state, actions = fringe.popleft()
        if problem.isGoalState(state):
            return actions
        if state in expanded:
            continue
        expanded.add(state)
        for successor, action, cost in problem.getSuccessors(state):
            fringe.append((successor, actions + [action]))
    return None


class SearchTests(unittest.TestCase):
    def test_assignment_reference_results(self):
        cases = [
            ('maze_small', 'dfs', None, 'escaped', 50, 82),
            ('maze_medium', 'dfs', None, 'escaped', 162, 233),
            ('maze_small', 'dls', 60, 'escaped', 50, 52),
            ('maze_small', 'dls', 30, 'cutoff', None, 32),
            ('maze_small', 'ids', None, 'escaped', 50, 1352),
        ]
        for name, algorithm, limit, status, steps, expanded in cases:
            with self.subTest(maze=name, algorithm=algorithm, limit=limit):
                result = runner.solve(maze.loadMaze(name), 'maze', algorithm,
                                      depth=limit, timeout=10)
                self.assertEqual(result['status'], status)
                self.assertEqual(result.get('steps'), steps)
                self.assertEqual(result.get('cost'), steps)
                self.assertEqual(result['expanded'], expanded)

    def test_start_is_goal_without_expansion(self):
        for algorithm in (search.dfs, lambda p: search.dls(p, 0), search.ids):
            problem = GraphProblem('G', ['G'], [])
            self.assertEqual(algorithm(problem), [])
            self.assertEqual(problem.expandedStates, [])

    def test_unreachable_cycle_terminates(self):
        for algorithm in (search.dfs, lambda p: search.dls(p, 10), search.ids):
            problem = GraphProblem('A', ['G'], [
                ('A', 'toB', 'B', 1), ('B', 'toA', 'A', 1)])
            self.assertIsNone(algorithm(problem))

    def test_dfs_order_and_single_expansion(self):
        problem = GraphProblem('A', ['G'], [
            ('A', 'toB', 'B', 1), ('A', 'toC', 'C', 1),
            ('C', 'toB', 'B', 1), ('B', 'toA', 'A', 1)])
        self.assertIsNone(search.dfs(problem))
        self.assertEqual(problem.expandedStates, ['A', 'C', 'B'])

    def test_depth_boundary_is_goal_tested_but_not_expanded(self):
        edges = [('A', 'toB', 'B', 1), ('B', 'toG', 'G', 1)]
        problem = GraphProblem('A', ['G'], edges)
        self.assertIs(search.dls(problem, 1), CUTOFF)
        self.assertEqual(problem.expandedStates, ['A'])
        problem = GraphProblem('A', ['G'], edges)
        self.assertEqual(search.dls(problem, 2), ['toB', 'toG'])
        self.assertEqual(problem.expandedStates, ['A', 'B'])

    def test_dls_revisits_state_on_shorter_path(self):
        problem = GraphProblem('A', ['G'], [
            ('A', 'toB', 'B', 1), ('A', 'toC', 'C', 1),
            ('B', 'toC', 'C', 1), ('C', 'toD', 'D', 1),
            ('D', 'toG', 'G', 1)])
        self.assertEqual(search.dls(problem, 3), ['toC', 'toD', 'toG'])
        self.assertEqual(problem.expandedStates.count('C'), 2)

    def test_ids_finds_shortest_path_and_respects_max_depth(self):
        edges = [('A', 'toB', 'B', 1), ('A', 'toG', 'G', 1),
                 ('B', 'toC', 'C', 1), ('C', 'toG', 'G', 1)]
        self.assertEqual(search.ids(GraphProblem('A', ['G'], edges)), ['toG'])
        self.assertIsNone(search.ids(GraphProblem('A', ['G'], edges), maxDepth=0))
        self.assertEqual(search.ids(GraphProblem('A', ['G'], edges), maxDepth=1),
                         ['toG'])


class KeyHuntTests(unittest.TestCase):
    def test_assignment_bfs_results(self):
        for name, steps, expanded in [('keys_tiny', 26, 490),
                                      ('keys_small', 54, 1723)]:
            with self.subTest(maze=name):
                layout = maze.loadMaze(name)
                problem = KeyHuntProblem(layout)
                actions = reference_bfs(problem)
                self.assertEqual(len(actions), steps)
                self.assertEqual(problem.getCostOfActions(actions), steps)
                self.assertEqual(problem._expanded, expanded)
                self.assertTrue(runner.checkSolution(layout, 'keys', actions)[0])

    def test_key_collection_exit_and_revisits(self):
        layout = maze.Maze(['%%%%%%%', '%SE K %', '%%%%%%%'])
        problem = KeyHuntProblem(layout)
        start = problem.getStartState()
        hash(start)
        before_key = problem.getSuccessors(start)[0][0]
        self.assertEqual(before_key[0], layout.exit)
        self.assertFalse(problem.isGoalState(before_key))
        actions = reference_bfs(problem)
        self.assertEqual(actions, ['East', 'East', 'East', 'West', 'West'])
        state = start
        for action in actions:
            state = next(s for s, a, c in problem.getSuccessors(state) if a == action)
        self.assertTrue(problem.isGoalState(state))
        self.assertEqual(state[1], frozenset())
        self.assertEqual(start[1], frozenset(layout.keys))

    def test_successor_order_terrain_costs_and_bookkeeping(self):
        layout = maze.Maze(['%%%%%', '% K %', '%~SG%', '% E %', '%%%%%'])
        problem = KeyHuntProblem(layout)
        successors = problem.getSuccessors(problem.getStartState())
        self.assertEqual([a for s, a, c in successors],
                         ['North', 'South', 'East', 'West'])
        self.assertEqual([c for s, a, c in successors], [1, 1, 10, 3])
        self.assertEqual(successors[0][0][1], frozenset())
        self.assertFalse(problem.isGoalState(successors[1][0]))
        for state, action, cost in successors:
            hash(state)
        self.assertEqual(problem._expanded, 1)
        self.assertEqual(problem.expandedPositions(), [layout.start])

    def test_no_keys_and_unreachable_key(self):
        problem = KeyHuntProblem(maze.Maze(['%%%%', '%SE%', '%%%%']))
        self.assertEqual(problem.getStartState()[1], frozenset())
        self.assertEqual(reference_bfs(problem), ['East'])
        problem = KeyHuntProblem(maze.Maze(['%%%%%%%', '%SE%K%%', '%%%%%%%']))
        self.assertIsNone(reference_bfs(problem))


if __name__ == '__main__':
    unittest.main()
