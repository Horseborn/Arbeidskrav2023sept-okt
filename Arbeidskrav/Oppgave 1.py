# # Oppgave 1
# #
# # Skriv et program som leser inn et navn og skriver ut en hilsen til brukeren.Eks «Hei, Ola» 
# name = input("Hva heter du? ")
# print(f'Hei {name}! Hyggelig å møte deg.')
# #
# # Skriv et program som leser inn et tall og skriver ut om tallet er positivt, negativt eller null 
# num_input = int(input("Tast ett tall. :"))
# if num_input > 0:
#     print(f'Ditt tall positivt {num_input}')
# elif num_input < 0:
#     print(f'Ditt tall er negativt {num_input}')
# else:
#     print(f'Ditt tall er null {num_input}')
# #
# # Skriv et program som leser inn et tall og skriver ut det dobbelte. 
# dbl_num = float(input("Tast inn ett tall så skal jeg doble det! : "))
# doubled_num = dbl_num + dbl_num
# print(f'{dbl_num} + {dbl_num} = {doubled_num}')
# #
# # Skriv et program som leser inn en tekst og skriver ut teksten baklengs.
# txt = input()
# rev_txt = txt[:: -1]
# print(rev_txt)

'''Formatted Online '''

# Oppgave 1
#
# Skriv et program som leser inn et navn og skriver ut en hilsen til brukeren.Eks «Hei, Ola»
name = input("Hva heter du? ")
print(f"Hei {name}! Hyggelig å møte deg.")
#
# Skriv et program som leser inn et tall og skriver ut om tallet er positivt, negativt eller null
num_input = int(input("Tast ett tall. :"))
if num_input > 0:
    print(f"Ditt tall positivt {num_input}")
elif num_input < 0:
    print(f"Ditt tall er negativt {num_input}")
else:
    print(f"Ditt tall er null {num_input}")
#
# Skriv et program som leser inn et tall og skriver ut det dobbelte.
dbl_num = float(input("Tast inn ett tall så skal jeg doble det! : "))
doubled_num = dbl_num + dbl_num
print(f"{dbl_num} + {dbl_num} = {doubled_num}")
#
# Skriv et program som leser inn en tekst og skriver ut teksten baklengs.
print('Tast inn en string, så skal jeg printe stringen ut baklengs!')
txt = input()
rev_txt = txt[::-1]
print(rev_txt)
