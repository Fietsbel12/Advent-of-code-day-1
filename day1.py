# dit stukt zorgt er voor dat het dataset.txt kan worden ingelezen
calorieFile = open("dataset.txt", "r", encoding="UTF-8")
calorieList = calorieFile.read().splitlines()

# Bereken de calorieën gedragen door elke elf
currentElfCalories = 0 # Calorieën voor de huidige elf
maxElfCalories = 0 # Maximaal aantal calorieën gedragen door een elf
maxElfNumber = 0 # Nummer van de elf met de meeste calorieën

# Loop door elke regel in calorieList om de calorieën per elf te berekenen 
for line in calorieList:
    if line.strip(): # Dit stuk word uitgevoerd als de regel niet leeg is
        currentElfCalories += int(line.strip()) # Voeg calorieën toe aan de huidige elf
    else:
        # Als de regel leeg is, check of de huidige elf de meeste calorieën heeft
        if currentElfCalories > maxElfCalories:
            maxElfCalories = currentElfCalories
            maxElfNumber += 1  # Verhoogt het elfnummer voor de volgende elf
        currentElfCalories = 0  # reset calorieën voor de volgende elf

# Controleer de calorieën van de laatste elf
if currentElfCalories > maxElfCalories:
    maxElfCalories = currentElfCalories # Update het maximale aantal calorieën
    maxElfNumber += 1  # Verhoogt het elfnummer voor de laaste elf

# Geef het totale aantal calorieën van de elf met de meeste calorieën terug
print(f"De Elf met elfnummer {maxElfNumber} draagt de meeste calorieën: {maxElfCalories}")

calorieFile.close() # Sluit het bestand