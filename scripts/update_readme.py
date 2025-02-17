import os

README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')

def add_exercise_to_readme(exercise_number, exercise_name, difficulty):
    # Read existing README.md content
    if os.path.exists(README_PATH):
        with open(README_PATH, 'r') as readme_file:
            readme_content = readme_file.readlines()
    else:
        readme_content = [
            "# LeetCode Solutions\n\n",
            "This repository contains solutions to LeetCode problems.\n\n",
            "## Solutions\n\n",
            "| Exercise Number | Exercise Name | Difficulty |\n",
            "|-----------------|---------------|------------|\n"
        ]
    
    # Ensure the table header and separator are present
    if "| Exercise Number | Exercise Name | Difficulty |\n" not in readme_content:
        readme_content.append("| Exercise Number | Exercise Name | Difficulty |\n")
    if "|-----------------|---------------|------------|\n" not in readme_content:
        readme_content.append("|-----------------|---------------|------------|\n")
    
    # Find the index to insert the new exercise
    start_index = readme_content.index("|-----------------|---------------|------------|\n") + 1
    
    # Create the new exercise line
    new_exercise_line = f"| {exercise_number} | {exercise_name} | {difficulty} |\n"
    
    # Insert the new exercise line
    readme_content.insert(start_index, new_exercise_line)
    
    # Extract the table lines and sort them by exercise number
    table_lines = readme_content[start_index:]
    table_lines.sort(key=lambda x: int(x.split('|')[1].strip()))
    
    # Update the readme content with sorted table lines
    readme_content = readme_content[:start_index] + table_lines
    
    # Write the updated content back to README.md
    with open(README_PATH, 'w') as readme_file:
        readme_file.writelines(readme_content)
    
    print(f"Exercise {exercise_number} - {exercise_name} added to README.md")

if __name__ == "__main__":
    exercise_number = input("Enter the exercise number: ")
    exercise_name = input("Enter the exercise name: ")
    difficulty = input("Enter the difficulty (Easy, Medium, Hard): ")
    add_exercise_to_readme(exercise_number, exercise_name, difficulty)
