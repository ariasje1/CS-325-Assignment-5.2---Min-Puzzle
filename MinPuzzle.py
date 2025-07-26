def minEffort(puzzle):
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


