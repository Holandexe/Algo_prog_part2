import os

def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "in.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

if len(lines) >= 2:
    w1 = lines[0]
    w2 = lines[1]
    result = min_distance(w1, w2)
    print(f"Кількість операцій для перетворення '{w2}' в '{w1}': {result}")
else:
    print("Помилка: у файлі 'in.txt' має бути мінімум два слова.")