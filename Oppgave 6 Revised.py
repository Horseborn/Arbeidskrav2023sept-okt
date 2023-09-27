import math

math_dict = {
    1: lambda a, b: a + b,
    2: lambda a, b: a - b,
    3: lambda a, b: a * b,
    4: lambda a, b: a / b
}
print('Welcome to my calculator! \n 1. Addition.'
      ' \n 2. Subtraction. \n 3. Multiplication.'
      ' \n 4. Divide. \n 5. Exit the program'
      )
while True:
    try:
        user_input = int(input())
        if user_input == 5:
            print('Farewell')
            break  # exit the while loop
        if user_input not in math_dict:
            print(f'{user_input} is not a valid command. Try again.')
            continue

        num1 = float(input())
        num2 = float(input())

        if user_input == 4 and num2 == 0:
            print('Error: Dividing by zero.')
            continue
        else:
            result = math_dict[user_input](num1, num2)
            print(result)

    except ValueError:
        print('Enter a valid number.')
    except Exception as e:
        print(f'Unexpecterd error ocurred {e}')



