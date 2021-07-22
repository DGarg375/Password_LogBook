def clear():
	_ = call('clear' if os.name == 'posix' else 'cls')

def Add():
	f = open("Homework.txt", "a")
	Organization = input("Organization: ")
	Username = input("Username: ")
	Password = input("Password: ")
	sentence = "Username: " + Username + "     Password: " + Password + "\n"
	f.write(Organization)
	f.write("\n")
	f.write(sentence)
	f.close()
	print("\n")

def count_lines():
	f =  open("Homework.txt", "r")
	Counter=0
	Content = f.read()
	f.close()
	CoList = Content.split("\n")
	for i in CoList:
		if i:
			Counter+=1
	return Counter
	
def Search():
	f = open("Homework.txt", "r")
	pass_list = f.readlines()
	f.close()
	some = int(count_lines())
	count = 0
	Orga = input("Enter the organization for it's credentials: ")
	for i in range(some-1):
		wow = pass_list[i]
		wow = wow.rstrip("\n")
		if wow == Orga:
			print("\n", pass_list[i], "\n", pass_list[i+1])
			i=some
		else:	
			count += 1;
	if count == some-1:
		print("\n", "No organization like that in database")
	print("\n")

choice = "something"

def Load():
	f = open("Homework.txt")
	text = f.read()
	print(text, "\n")

def clear():
		import os
		import time
		os.system("ls")
		time.sleep(0)
		os.system('clear')
	
while choice != "Exit":
	clear()
	choice = input("Enter the operation (Add/Search/Load File/Exit): ")
	print("\n")
	if choice == "Add":	
		Add()
		call = input("Back?(yes/no): ")
		if call == "no":
			choice = "Exit"
			clear()
	elif choice == "Search":
		Search()
		call = input("Back?(yes/no): ")
		if call == "no":
			choice = "Exit"
			clear()
	elif choice == "Load File":
		Load()
		call = input("Back?(yes/no): ")
		if call == "no":
			choice = "Exit"
			clear()
	elif choice == "Exit":
		choice = "Exit"
		clear()
