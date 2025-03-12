import os
import sys

# README path
README_PATH = "README.md"

def count_solved_problems():
    # counting .py files
    problem_count = 0
    for root, dirs, files in os.walk("."):
        if "2024" in root:
            problem_count += len([f for f in files if f.endswith(".py")])
    return problem_count

def update_readme(push_date):
    problem_count = count_solved_problems()

    with open(README_PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(README_PATH, "w", encoding="utf-8") as file:
        for line in lines:
            if "Total Problems Solved" in line:
                file.write(f"- **Total Problems Solved**: `{problem_count} problems`\n")
            elif "Latest Submission" in line:
                file.write(f"- **Latest Submission**: `{push_date}`\n")
            else:
                file.write(line)

if __name__ == "__main__":
    # Receive the pushed date from GitHub Actions
    push_date = sys.argv[1] if len(sys.argv) > 1 else "YYYY-MM-DD"
    update_readme(push_date)
