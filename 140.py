# Levenshtein Distance - It is the minimum number of single-character edits required to convert one string into another.

# allowed operations - insertion, deletion, update

"""
kitten → sitting

kitten → sitten (replace k → s)

sitten → sittin (replace e → i)

sittin → sitting (insert g)

👉 Distance = 3


we build a 2d table

      ""  s  i  t  t  i  n  g
""    0  1  2  3  4  5  6  7
k     1
i     2
t     3
t     4
e     5
n     6


each cell stores

min(
    deletion,
    insertion,
    substitution
)
"""

# implementaion
def levenshtein(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost  # substitution
            )

    return dp[m][n]


print(levenshtein("kitten", "sitting"))  # 3


# space optimized version
def levenshtein_optimized(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    previous = list(range(len(s2) + 1))

    for i, c1 in enumerate(s1):
        current = [i + 1]

        for j, c2 in enumerate(s2):
            insertions = previous[j + 1] + 1
            deletions = current[j] + 1
            substitutions = previous[j] + (c1 != c2)

            current.append(min(insertions, deletions, substitutions))

        previous = current

    return previous[-1]

# you can use pip install python-Levenshtein and import Levenshtein
