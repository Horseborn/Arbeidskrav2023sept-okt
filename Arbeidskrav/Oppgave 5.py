
print('Tast inn ønsket oppgave')
task_choice = int(input())

# Skriv en funksjon som tar en lengde i meter som input og returnerer lengden i fot.
# Tallet som skal testes skal leses inn fra tastaturet.

if task_choice == 1:
    def meter_convertion():
        print('Tast inn antall meter du ønsker å konvertere til fot: ')
        meter = int(input())
        converted_meter = meter * 3.28084
        print(f'{meter} meter konvertert til fot er {converted_meter}')

    meter_convertion()

    def meter_converter(user_input):
        converted_meter1 = user_input * 3.28084
        return converted_meter1

    print('Tast inn ønsket meter som du vil konvertere til fot: ')
    user_input = float(input())


    result = meter_converter(user_input)

    print(f'{user_input} meter konvertert til fot er {result}')





#
# Lag en funksjon som og konverterer temperatur i Celsius til Fahrenheit. Tallet skal testes skal leses inn fra tastaturet.
#Har prøvd to variasjoner av begge oppgavene.
elif task_choice == 2:
    def celsius_converter():
        print('Tast inn ønsket temperatur som du vil konvertere: ')
        celcius = float(input())
        converted_celcius = (celcius * 9/5) + 32
        print(f'{celcius} konvertert til fahrenheit er {converted_celcius}')

    celsius_converter()

    def celcius_converter2(num_input):
        converted_celcius = (num_input * 9/5) + 32
        return converted_celcius

    print('Tast inn ønsket temperatur du vil konvertere: ')
    num_input = float(input())
    result = celcius_converter2(num_input)
    print(result)