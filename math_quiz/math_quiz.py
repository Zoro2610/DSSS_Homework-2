import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min and max inclusive.
    
    Args:
        min_value (int): The minimum value for random integer
        max_value (int): The maximum value for random integer

    Returns:
        int: A random integer between min_value and max_value   
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Randomly select and return an arithmetic operator.

    Returns:
        str: An operator which can be '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem(num1, num2, operator):
    """
    Create a Math problem from two number and a operator.

    Args:
        num1 (int): First operand in maths problem.
        num2 (int): Second operand in maths problem.
        operator (str): Arithmetic operator which can be '+', '-', or '*'.
    
    Returns:
        tuple: A tuple containing:
            str: String representation of the math problem.
            int: Correct answer to the math problem.
    """
    problem = f"{num1} {operator} {num2}" # Format the string to show math expression (e.g. "4 + 5")

    # CAlculate answer based on the operator
    if operator == '+':
        ans = num1 + num2 
    elif operator == '-':
        ans = num1 - num2
    else:
        ans = num1 * num2
        
    return problem, ans # Return problem as string and correct answer

def math_quiz():
    """
    Run the maths quiz game where the user answers generated math questions.

    This function generates math questions using randomly selected numbers and operators.
    User is prompted to answer each question and feedback is provided whther the answer is correct or not.
    Final score is displayed in the end.

    Raises:
        ValueError: If the user input is not an integer.
    """
    score = 0 # Initialize the score
    total_questions = 3 # Total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through each question
    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10) # Generate first random number
        num2 = generate_random_integer(1, 5) # Generate second random number
        operator = generate_random_operator() # Generate random operator 

        # Create math problem and determine the correct answer
        problem, correct_answer = generate_math_problem (num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error Handling for input
        while True:
            try:
                user_answer = int(input("Your answer: ")) # Check if the user input is valid
                break # Exit loop if input is valid

            except ValueError:
                print("Invalid input! Enter an integer") # Display if the output is not an integer

        if user_answer == correct_answer: # Check if the user answer is correct
            print("Correct! You earned a point.")
            score += 1 # Increase score for correct answer
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}") # Display the final score

if __name__ == "__main__":
    math_quiz()
