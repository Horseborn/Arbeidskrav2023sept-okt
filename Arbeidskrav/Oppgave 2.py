# import random as rnd
#
#
# # Opprett og skriv ut en liste med 5 tilfeldig heltall mellom 1 og 100
# #Lest meg opp på list comprehension og prøvd meg på det
#
# random_list = [rnd.randint(1, 100) for _ in range(5)]
# print(random_list)
# #
# # Sorter og skriv ut den samme listen med tallene i stigende rekkefølge
# #Her bruker jeg "sort" funksjonen, om jeg ikke gir argumenter sorterer den automatisk listen i stigende rekkefølge
# random_list.sort()
# print(random_list)
#
# #
# #Opprett og skriv ut en liste med 100 tilfeldige heltall mellom 1 og 200
# #Her er konseptet det samme som oppgave 1, har og lært nå at variabel navnet i en for løkke ofte settes til "_"
# #om ikke variabelen skal brukes, slik som i dette tilfelle
# lrg_rndList = [rnd.randint(1, 200) for _ in range(100)]
# print(lrg_rndList)
#
#
#
# #I listen med 100 tilfeldig tall skal du nå fjerne alle tall som er større en 100
# #Oppgave fullført uten list comprehension. Synes den måten er lettere å forstå, men list comprehension er tydelig mer effektiv og konsis
# filtered_lrgList2 = []
# for x in lrg_rndList:
#     if x <= 100:
#         filtered_lrgList2.append(x)
# print('Uten list comprehension: ', filtered_lrgList2)
#
# #Oppgave fullført med list comprehension
# filtered_lrgList = [number for number in lrg_rndList if number <= 100]
# print('List comprehension: ', filtered_lrgList)
#
# #
# # I listen med tilfeldig tall skal du nå også fjerne alle tall som er delelig med tre, altså tall som er i 3 gangeren.
# #Her må man bruke modulo operator. Jeg prøver først uten list comprehension
# divided_lrgList = []
# for n in lrg_rndList:
#     if n % 3 != 0:
#         divided_lrgList.append(n)
# print(f'Uten list comprehension -> {divided_lrgList}')
# #Her skrev jeg samme kode men med bruk av list comprehension
# divided_lrgList2 = [number for number in lrg_rndList if number % 3 != 0]
# print(f'List comprehension -> {divided_lrgList2}')

'''Formatted online'''



import random as rnd


# Opprett og skriv ut en liste med 5 tilfeldig heltall mellom 1 og 100
# Lest meg opp på list comprehension og prøvd meg på det

random_list = [rnd.randint(1, 100) for _ in range(5)]
print(random_list)
#
# Sorter og skriv ut den samme listen med tallene i stigende rekkefølge
# Her bruker jeg "sort" funksjonen, om jeg ikke gir argumenter sorterer den automatisk listen i stigende rekkefølge
random_list.sort()
print(random_list)

#
# Opprett og skriv ut en liste med 100 tilfeldige heltall mellom 1 og 200
# Her er konseptet det samme som oppgave 1, har og lært nå at variabel navnet i en for løkke ofte settes til "_"
# om ikke variabelen skal brukes, slik som i dette tilfelle
lrg_rndList = [rnd.randint(1, 200) for _ in range(100)]
print(lrg_rndList)


# I listen med 100 tilfeldig tall skal du nå fjerne alle tall som er større en 100
# Oppgave fullført uten list comprehension. Synes den måten er lettere å forstå, men list comprehension er tydelig mer effektiv og konsis
filtered_lrgList2 = []
for x in lrg_rndList:
    if x <= 100:
        filtered_lrgList2.append(x)
print("Uten list comprehension: ", filtered_lrgList2)

# Oppgave fullført med list comprehension
filtered_lrgList = [number for number in lrg_rndList if number <= 100]
print("List comprehension: ", filtered_lrgList)

#
# I listen med tilfeldig tall skal du nå også fjerne alle tall som er delelig med tre, altså tall som er i 3 gangeren.
# Her må man bruke modulo operator. Jeg prøver først uten list comprehension
divided_lrgList = []
for n in lrg_rndList:
    if n % 3 != 0:
        divided_lrgList.append(n)
print(f"Uten list comprehension -> {divided_lrgList}")
# Her skrev jeg samme kode men med bruk av list comprehension
divided_lrgList2 = [number for number in lrg_rndList if number % 3 != 0]
print(f"List comprehension -> {divided_lrgList2}")
