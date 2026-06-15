puzzle = input("Paste raw text: ")

rows = [puzzle[i:i+9] for i in range(0, 81, 9)]
formatted = ",\n                    ".join(", ".join(c for c in row) for row in rows)
print(f"[{formatted}]")
