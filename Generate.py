import random
from pathlib import Path

def ExitOnError():
	print ("Le programme se termine maintenant. Appuyez sur Entrée pour continuer...")
	input()
	sys.exit(0)

def CheckFiles(file):
	characterFile = Path(file)
	if characterFile.is_file() == False:
		print ("Fatal error : Le fichier \"character.txt\" est introuvable !")
		ExitOnError()

def LoadCharacters(file):
	fileReader = open(file, "r")
	string = ""
	for char in fileReader:
		string += char
	if string == "":
		print ("Fatal error : Il n'y a pas de caractères à charger. !")
		ExitOnError()
	else:
		return string

def CheckUserInput():
	userInput = 0
	while True:
		try:
			userInput = int(input("Nombre de caractères désirés (5 à 50) : "))
		except ValueError:
			print("Error : Veuillez taper le nombre de caractères souhaitez (exemple: 10).")
			print("-------------------------")
			#continue
		else:
			if userInput >= 5 and userInput <= 50:
				return userInput
			else:
				print("Error : Un mot de passe doit contenir entre 5 et 50 caractères.")
				print("-------------------------")

def BuildPassword(password_length, data):
	output = ""
	for x in range (0, password_length):
		output += str(random.choice(data))
	return output

def WritePasswordIntoFile(file, text):
	with open(file, 'a') as textWriter:
		textWriter.write("\n" + text)

CheckFiles("character.txt")
characters = LoadCharacters("character.txt")
print ("Vos mots de passe seront créés aléatoirement en utilisant ces caractères :\n" + characters)
print("-------------------------")

while True:
	chosenLength = CheckUserInput()
	password = BuildPassword(chosenLength, characters)
	WritePasswordIntoFile("résultat.txt", password)
	print ("Password : " + password)
	print("-------------------------")