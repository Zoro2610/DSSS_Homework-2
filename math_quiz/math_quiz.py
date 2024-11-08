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
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    else:
        ans = num1 * num2
    return problem, ans 

def math_quiz():
    score = 0
    total_questions = 3 # Total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        PROBLEM, ANSWER = generate_math_problem (num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
