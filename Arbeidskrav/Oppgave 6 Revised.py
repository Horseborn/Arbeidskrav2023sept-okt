import math

math_dict = {
    1: lambda a, b: a + b,
    2: lambda a, b: a - b,
    3: lambda a, b: a * b,
    4: lambda a, b: a / b
}
# Put math meny inside a variable so that it can more easily be reused
math_meny = ('Welcome to my calculator! \n 1. Addition.'
             ' \n 2. Subtraction. \n 3. Multiplication.'
             ' \n 4. Divide. \n 5. Exit the program'
             )

while True:
    print(math_meny)
    try:
        user_input = int(input())

        if user_input == 5:
            print('Farewell')
            break  # exit the while loop
        if user_input not in math_dict:
            print(f'{user_input} is not a valid command. Try again.')
            continue

        # Here I declare two variables and set up an if statement to make the code in general more user-friendly
        math_symbol = ''
        ans = ''
        if user_input == 1:
            ans = 'Addition:'
            math_symbol = '+'
        elif user_input == 2:
            ans = 'Subtraction:'
            math_symbol = '-'
        elif user_input == 3:
            ans = 'Multiplication:'
            math_symbol = '*'
        elif user_input == 4:
            ans = 'Division:'
            math_symbol = '/'

        num1 = float(input(f'{ans} Enter first number: '))
        num2 = float(input(f'{ans} Enter second number: '))

        if user_input == 4 and num2 == 0:
            print('Error: Dividing by zero.')
            continue
        else:
            result = math_dict[user_input](num1, num2)
            print(f'{num1} {math_symbol} {num2} = {result}\n')


    # Here I try to catch errors, not used it before so unsure if they work optimally
    except ValueError:
        print('Enter a valid number.')
    except Exception as error:
        print(f'Unexpected error occurred {error}')
