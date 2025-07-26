#Author: Jesus Arias
#GitHub username: ariasje1
#Date: 07/25/2025
#Description: Finds the path with the minimal maximum height difference in a grid.
def minEffort(puzzle):
    """
        Finds the minimum effort required to travel from the top-left corner
        to the bottom-right corner of a 2D puzzle grid.

        This function returns the minimum possible effort among all valid
        paths from the starting cell [0][0] to the destination [m-1][n-1].

        Parameters:
            puzzle (list of list of int): A 2D grid where puzzle[i][j]
            represents the height of the cell at row i and column j.

        Returns:
            int: The minimum effort required to reach the bottom-right cell.
        """
    if not puzzle or not puzzle[0]:
        return 0

    rows = len(puzzle)
    cols = len(puzzle[0])

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize the effort matrix with infinity values
    effort = [[float('inf') for j in range(cols)] for i in range(rows)]
    effort[0][0] = 0

    # Priority queue: each element is (effort, row, col)
    pq = [(0, 0, 0)]

    while pq:
        # Sort to simulate a priority queue (lowest effort first)
        pq.sort()
        curr_effort, x, y = pq.pop(0)

        # If we reached the bottom-right cell, return the effort
        if x == rows - 1 and y == cols - 1:
            return curr_effort

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                # Calculate height difference
                diff = abs(puzzle[nx][ny] - puzzle[x][y])
                max_effort = max(curr_effort, diff)

                # If a better path is found, update and add to queue
                if effort[nx][ny] > max_effort:
                    effort[nx][ny] = max_effort
                    pq.append((max_effort, nx, ny))


