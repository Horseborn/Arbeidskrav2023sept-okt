print('Velkommen til min kalkulator! ')
print('\nBruk menyen og tast inn det du ønsker.\n1. + (Addisjon)\n2. - (Subtraksjon)\n3. * (Multiplikasjono)\n4. / (Divisjon)\nTast 5 om du ønsker avslutte. ')
while True:

    user_input = int(input())
    if user_input == 1:
        print('Tast inn to tall du ønsker addere: ')
        num1 = int(input())
        num2 = int(input())
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
        print('Tast 0 om du  ønsker menyen på nytt. Trykk Enter for å fortsette...')
    elif user_input == 2:
        print('Tast inn to tall du ønsker subtrahere: ')
        num1 = int(input())
        num2 = int(input())
        result = num1 - num2
        print(f'{num1} - {num2} = {result}')
        print('Tast 0 om du  ønsker menyen på nytt. Trykk Enter for å fortsette...')
    elif user_input == 3:
        print('Tast inn to tall du ønsker å multiplisere: ')
        num1 = int(input())
        num2 = int(input())
        result = num1 * num2
        print(f'{num1} * {num2} = {result}')
        print('Tast 0 om du  ønsker menyen på nytt. Trykk Enter for å fortsette...')
    elif user_input == 4:
        print('Tast inn to tall du ønsker å dividere: ')
        num1 = int(input())
        num2 = int(input())
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
        print('Tast 0 om du ønsker menyen på nytt. Trykk Enter for å fortsette...')
    elif user_input == 0:
        print('\nBruk menyen og tast inn det du ønsker.\n1. + (Addisjon)\n2. - (Subtraksjon)\n3. * (Multiplikasjon)\n4. / (Divisjon)\nTast 5 om du ønsker avslutte.')
    elif user_input == 5:
        print('Farvel')
        break
    elif user_input != 1 and 2 and 3 and 4 and 5:
        print('Vennligst tast inn ett gyldig tall.')
        continue

