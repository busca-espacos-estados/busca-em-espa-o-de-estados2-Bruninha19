import heapq

from puzzle.base_search import BaseSearch
from puzzle.result import SearchResult
from puzzle.state import State


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        """
        Heurística admissível:
        Distância de Manhattan
        """

        distance = 0

        for i, value in enumerate(state.tiles):

            if value == 0:
                continue

            goal_row, goal_col = divmod(value - 1, 3)
            current_row, current_col = divmod(i, 3)

            distance += abs(goal_row - current_row)
            distance += abs(goal_col - current_col)

        return distance

    def search(self, initial: State) -> SearchResult:

        frontier = []
        heapq.heappush(frontier, (0, initial))

        visited = {}

        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while frontier:

            _, current = heapq.heappop(frontier)
            nodes_expanded += 1

            if current.is_goal:
                return SearchResult(
                    solution=current,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=current.cost
                )

            visited[current] = current.cost

            for neighbor in current.neighbors():

                if neighbor not in visited or neighbor.cost < visited[neighbor]:

                    g = neighbor.cost
                    h = self.heuristic(neighbor)
                    f = g + h

                    heapq.heappush(frontier, (f, neighbor))
                    nodes_generated += 1

            max_frontier_size = max(max_frontier_size, len(frontier))

        return SearchResult(solution=None)