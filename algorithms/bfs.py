from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.result import SearchResult
from puzzle.state import State


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:

        frontier = deque([initial])
        visited = set([initial])

        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:

            current = frontier.popleft()
            nodes_expanded += 1

            if current.is_goal:
                return SearchResult(
                    solution=current,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=current.cost
                )

            for neighbor in current.neighbors():

                if neighbor not in visited:
                    frontier.append(neighbor)
                    visited.add(neighbor)
                    nodes_generated += 1

            max_frontier_size = max(max_frontier_size, len(frontier))

        return SearchResult(solution=None)