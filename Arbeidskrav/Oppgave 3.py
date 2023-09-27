# # Lag en liste som innholder fem valgfrie dyr (tekststrenger). Skriv så ut alle elementene på hver sin linje.
# #Her må jeg lese meg opp og lære hvordan å formattere det jeg skal printe til konsollen.
# animal_list = ['cat', 'tiger', 'pufferfish', 'crab', 'eagle']
# print(*animal_list, sep='\n')
# print('\n')
# # Deretter skal du gi dyrene navn. Navnene skal du legge i en ny liste.
# # Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Ola er en hund»
# animal_names = ['Nami', 'Torjus', 'Fishtula', 'Snapper', 'Bald']
# for i in range(len(animal_list)):
#     print(f'{animal_names[i]} er en {animal_list[i]}!')
# print('\n')
# #
# # Skriv ut det første og siste elementet i listen med dyr.
# print(f'Det første elementet i listen med dyr er {animal_list[0]}, og det siste elementet i listen er {animal_list[-1]}', '\n')
# #
# # Skriv ut listen med dyr i reversert alfabetisk rekkefølge.
# #Her reverserer jeg listen med en simpel innebygd funksjon. Ulempen med dette er at vi lager ikke en ny, reversert liste,
# #men vi reverserer hele listen, vi kan evt kjøre funksjonen en gang til for å få listen tilbake til opprinnelig rekkefølge.
# animal_list.reverse()
# print(animal_list)
# animal_list.reverse()
# print(animal_list, '\n')
# #Ett alternativt svar til dette kan være:
# reversed_animalList = []
# for i in animal_list:
#     reversed_animalList.insert(0, i)
# print(reversed_animalList, '\n')
# #Det som skjer i koden over er at jeg lager en ny liste kalt "reversed_animalList, jeg kjører en for løkke gjennom
# #listen med dyrenavn, "animal_list", så setter jeg inn variabelen "i" i den nye listen på index plassering 0, dette skaper
# #da i praksis en baklengs liste av animal_list
# #
# # Du skal nå lage en dictionary med disse fem dyrene med navn. Du kan bruke navn som key og hvilken type dyr som value.
# # Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Siri er en katt»
# #Her bruker jeg en ny, innebygd funksjon som heter "items()", den gir meg mulighet til å loope gjennom min dictionary
# #slik at jeg lett kan lese ut både key og dens value
# animal_dictionary = {
#     'Nami': 'katt',
#     'Torjus': 'tiger',
#     'Fishtula': 'pufferfish',
#     'Snapper': 'crab',
#     'Bald': 'eagle'
# }
# for name, species in animal_dictionary.items():
#     print(f'{name} er en {species}')
#
#
#
#
# # for i in animal_dictionary:
# #     print(f'{animal_dictionary[i]}')



# Lag en liste som innholder fem valgfrie dyr (tekststrenger). Skriv så ut alle elementene på hver sin linje.
# Her må jeg lese meg opp og lære hvordan å formattere det jeg skal printe til konsollen.
animal_list = ["cat", "tiger", "pufferfish", "crab", "eagle"]
print(*animal_list, sep='\n')
print("\n")

# Deretter skal du gi dyrene navn. Navnene skal du legge i en ny liste.
# Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Ola er en hund»
animal_names = ["Nami", "Torjus", "Fishtula", "Snapper", "Bald"]
for i in range(len(animal_list)):
    print(f"{animal_names[i]} er en {animal_list[i]}!")
print("\n")
#


# Skriv ut det første og siste elementet i listen med dyr.
print(
    f"Det første elementet i listen med dyr er {animal_list[0]}, og det siste elementet i listen er {animal_list[-1]}",
    "\n",
)
#

# Skriv ut listen med dyr i reversert alfabetisk rekkefølge.
# Her reverserer jeg listen med en simpel innebygd funksjon. Ulempen med dette er at vi lager ikke en ny, reversert liste,
# men vi reverserer hele listen, vi kan evt kjøre funksjonen en gang til for å få listen tilbake til opprinnelig rekkefølge.
animal_list.reverse()
print(animal_list)
animal_list.reverse()
print(animal_list, "\n")
# Ett alternativt svar til dette kan være:
reversed_animalList = []
for i in animal_list:
    reversed_animalList.insert(0, i)
print(reversed_animalList, "\n")
# Det som skjer i koden over er at jeg lager en ny liste kalt "reversed_animalList, jeg kjører en for løkke gjennom
# listen med dyrenavn, "animal_list", så setter jeg inn variabelen "i" i den nye listen på index plassering 0, dette skaper
# da i praksis en baklengs liste av animal_list


# Du skal nå lage en dictionary med disse fem dyrene med navn. Du kan bruke navn som key og hvilken type dyr som value.
# Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Siri er en katt»
# Her bruker jeg en ny, innebygd funksjon som heter "items()", den gir meg mulighet til å loope gjennom min dictionary
# slik at jeg lett kan lese ut både key og dens value
animal_dictionary = {
    "Nami": "katt",
    "Torjus": "tiger",
    "Fishtula": "pufferfish",
    "Snapper": "crab",
    "Bald": "eagle",
}
for name, species in animal_dictionary.items():
    print(f"{name} er en {species}")



