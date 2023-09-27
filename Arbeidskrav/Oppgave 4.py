print('Tast inn ønsket oppgave ut av 4:  ')
task_choice = int(input())
task_list = [3, 5, 9, 10, 11]

# For hver av verdiene i lisnte [3, 5, 9, 10, 11] skriv ut om verdien er:
# Større eller lik 10, mindre eller lik 5 eller ett sted mellom 5 og 10
if task_choice == 1:

    for i in task_list:
        if i >= 10:
            print(f'{i} er større eller lik 10')
        elif i <= 5:
            print(f'{i} er mindre eller lik 5.')
        else:
            print(f'{i} er ett sted mellom 5 og 10.')

# Lag en for-løkke hvor du skriver ut både index og verdi for denne listen på en egen linje.
# Eks: «Index=0, Verdi=3»
# Her lærte jeg "enumerate" funksjonen som gir meg mulighet til å loope gjennom en list og lese ut både index og verdi,
# det at jeg skaper to variabler inne i for løkka separert med komma gir meg mulighet til å bruke begge i print
elif task_choice == 2:

    for index, value in enumerate(task_list):
        print(f'Index = {index}, verdi = {value}')

# Gjør det samme som i oppgave B. men nå gjør med en while-løkke
# Her setter jeg index til 0, så setter jeg opp en while loop til å kjøre så lenge index er mindre enn lengden til
# listen, så lager jeg en ny variabel
elif task_choice == 3:
    index = 0
    while index < len(task_list):
        value = task_list[index]
        print(f'Index = {index}, verdi = {value}')
        index += 1


# Lag et program som regner ut summen av alle tallene i listen.
elif task_choice == 4:
    i = 0
    for n in task_list:
        n = n * 2
        print(n)

list1 = [1, 5, 7, 10, 11]

# Step 1: Find the sum of the elements in list1
sum_of_elements = sum(list1)

# Step 2: Double the sum
doubled_sum = sum_of_elements + sum_of_elements

# Step 3: Print the doubled sum
print(f"The doubled sum of the elements in list1 is: {doubled_sum}")
