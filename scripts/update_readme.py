import os

README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
VALID_CATEGORIES = ['algorithms', 'database', 'shell']

def add_exercise_to_readme(category, exercise_number, exercise_name, difficulty, exercise_link):
    # Read existing README.md content
    if os.path.exists(README_PATH):
        with open(README_PATH, 'r') as readme_file:
            readme_content = readme_file.readlines()
    else:
        readme_content = [
            "# LeetCode Solutions\n\n",
            "This repository contains solutions to LeetCode problems.\n\n"
        ]
    
    # Ensure the category section and table header are present
    category_header = f"### {category.capitalize()}\n"
    table_header = "| Exercise Number | Exercise Name | Difficulty | Solution |\n"
    table_separator = "|-----------------|---------------|------------|----------|\n"
    
    if category_header not in readme_content:
        readme_content.append("\n")
        readme_content.append(category_header)
        readme_content.append(table_header)
        readme_content.append(table_separator)
    
    # Find the index to insert the new exercise
    category_index = readme_content.index(category_header) + 4  # Skip header and table header
    while category_index < len(readme_content) and readme_content[category_index].startswith("|"):
        category_index += 1
    
    # Create the new exercise line with a link
    exercise_name_with_link = f"[{exercise_name}]({exercise_link})"
    solution_link = f"[Here](./{category}/{exercise_name})"
    new_exercise_line = f"| {exercise_number} | {exercise_name_with_link} | {difficulty} | {solution_link} |\n"
    
    # Insert the new exercise line
    readme_content.insert(category_index, new_exercise_line)
    
    # Extract the table lines and sort them by exercise number
    table_start_index = readme_content.index(category_header) + 4
    table_end_index = category_index + 1
    table_lines = readme_content[table_start_index:table_end_index]
    table_lines.sort(key=lambda x: int(x.split('|')[1].strip()))
    
    # Update the readme content with sorted table lines
    readme_content = readme_content[:table_start_index] + table_lines + readme_content[table_end_index:]
    
    # Write the updated content back to README.md
    with open(README_PATH, 'w') as readme_file:
        readme_file.writelines(readme_content)
    
    print(f"Exercise {exercise_number} - {exercise_name} added to {category} section in README.md")

if __name__ == "__main__":
    category = input("Enter the category of the problem (algorithms, database, shell): ")
    if category not in VALID_CATEGORIES:
        print(f"Invalid category. Choose from: {', '.join(VALID_CATEGORIES)}")
    else:
        exercise_number = input("Enter the exercise number: ")
        exercise_name = input("Enter the exercise name: ")
        difficulty = input("Enter the difficulty (Easy, Medium, Hard): ")
        exercise_link = input("Enter the link to the exercise: ")
        add_exercise_to_readme(category, exercise_number, exercise_name, difficulty, exercise_link)
