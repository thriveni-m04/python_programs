
# Q41. Find All Words in Grid

def find_words(board, words):
    # Build a Trie from the given words
    trie = {}

    for word in words:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = word

    rows = len(board)
    cols = len(board[0])
    found = []

    def dfs(r, c, node):
        ch = board[r][c]

        if ch not in node:
            return

        next_node = node[ch]

        # Check whether a complete word is found
        if "$" in next_node:
            found.append(next_node["$"])
            del next_node["$"]

        # Mark the current cell as visited
        board[r][c] = "#"

        # Move in four directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

        # Restore the original character
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie)

    return found


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]

words = ["oath", "pea", "eat", "rain"]

print("Found Words:", find_words(board, words))

