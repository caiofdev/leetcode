import os

VALID_CATEGORIES = ['algorithms', 'database', 'scripts']

def create_solution(category, problem_name):
    if category not in VALID_CATEGORIES:
        print(f"Invalid category. Choose from: {', '.join(VALID_CATEGORIES)}")
        return
    
    # Create the directory if it doesn't exist
    base_path = os.path.dirname(os.path.dirname(__file__))
    category_path = os.path.join(base_path, category, problem_name)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    
    # Path to the solution file
    solution_file = os.path.join(category_path, f"{problem_name}.py")
    
    # Basic template for the solution file
    template = f'''"""
Solution for {problem_name}
"""

def solution():
    # Write your solution here
    pass
'''

    # Create the solution file with the template
    with open(solution_file, 'w') as file:
        file.write(template)
    
    print(f"Solution created at: {solution_file}")

if __name__ == "__main__":
    category = input("Enter the category of the problem (algorithms, database, scripts): ")
    problem_name = input("Enter the name of the problem: ")
    create_solution(category, problem_name)
