"""

	@author: Gökhan Özeloğlu

"""


import sys
from operator import itemgetter


film_list = []
try:
    fs = open(sys.argv[1],"r")
    for i in fs.readlines():
        film_list.append(i.rstrip(";\n").split(","))
    f = open("dvdStore.txt","a+")
except IndexError:
    print("You did not enter any argument! So, program created 'dvdStore.txt' automatically!")
    print("Your all operations will be saved on this file!")
    print("You must press 'Q' to save all operations before exist!\n ")
    f = open("dvdStore.txt","w")
except FileNotFoundError:
    print(sys.argv[1],"could not find on the machine! So, dvdStore.txt is created!")
    print("Your all operations will be saved on this file!")
    print("You must press 'Q' to save all operations before exist!\n ")
    f = open("dvdStore.txt","w")


print(" ---HUBM DVD----")
print("A:   Add new dvd")
print("R:   Remove dvd")
print("S:   Search dvd")
print("L:   List dvd")
print("E:   Edit dvd")
print("H:   Hire dvd")
print("Q:   Quit")
print("Enter Command: ",end="")


for line in film_list:
    temp = []
    counter = 0
    indis = film_list.index(line)
    for i in line:
        if i == [""]:
            continue
        else:
            i =i.strip()
            temp.append(i)
            counter += 1
            if counter == 6:
                del film_list[indis]
                film_list.insert(indis,temp)

command = list(input().strip().split(","))
command = [i.strip() for i in command]
#(command)
while command[0] != "Q":
    if command[0] == "A":
        serial_numbers = [i[0] for i in film_list]
        temp = []
        try:
            name = command[3].strip()
            genre = command[4].strip()
            director = command[5].strip()
            state = command[6].strip()
            if len(command) > 7:
                print("You entered more than 7 attributes. You must enter 7 attributes!")
            elif '"' in command[1]:
                print("Serial number must be integer")
            elif command[1] in serial_numbers:
                print("Serial number is already exists!")
            elif '"' in command[2]:
                print("Price must be integer!")
            elif name == '""':
                print("You must enter a film name!")
            elif '"' != command[3][0] or '"' != command[3][-1]:
                print("Film name must be entered in string type!")
            elif genre == '""':
                print("You must enter genre!")
            elif '"' != command[4][0] or '"' != command[4][-1]:
                print("Genre must be entered in string type!")
            elif director == '""':
                print("You must enter a director!")
            elif '"' != command[5][0] or '"' != command[5][-1]:
                print("Director must be entered in string type!")
            elif state == '""':
                print("You must enter a state")
            elif '"' != command[6][0] or '"' != command[6][-1]:
                print("State must be entered in string type!")
            elif command[6] != '"Inv"':
                print("New DVD must be Inv!")
            else:
                command[3] = command[3].strip().strip('"')
                command[4] = command[4].strip().strip('"')
                command[5] = command[5].strip().strip('"')
                command[6] = command[6].strip().strip('"')
                temp.append(command[1])
                temp.append(command[2])
                temp.append(command[3].strip())
                temp.append(command[4].strip())
                temp.append(command[5].strip())
                temp.append(command[6].strip())
                film_list.append(temp)
        except IndexError:
            print("You entered less than 7 attributes. You must enter 7 attributes!")

    if command[0] == "R":
        try:
            command[0] = command[0].strip()
            serial_numbers = [i[0] for i in film_list]
            command[1] = command[1].strip()
            if len(command) > 2 or len(command) < 2:
                print("You must enter 2 command")
            elif '"' in command[1]:
                print("Serial number must be integer!")
            elif command[1] not in serial_numbers:
                print("Film is not in the inventory")
            else:
                attribute = ["Serial:\t","Price:\t","Name:\t","Genre:\t","Director:","State:\t"]
                counter = 0
                print("\n")
                for i in film_list:
                    if i == [""]:
                        continue
                    elif i[0] == command[1]:
                        if i[-1] == "Inv":
                            for j in i:
                                print(attribute[counter],end=" ")
                                print(j)
                                counter += 1
                                if counter == 6:
                                    break
                            print("")

                            command = input("Are you sure to delete? Yes or No?: ")
                            if command == "No" or command == "NO" or command == "nO" or command == "N" or command == "n" or command == "no" :
                                continue
                            elif command == "Yes" or command == "YES" or command == "YEs" or command == "YeS" or command == "yEs" or command == "Y" or command == "y":
                                film_list.remove(i)
                            elif command != "Yes" or command != "No":
                                print("You must write 'Yes' or 'No'!")
                                break
                        else:
                            print("This film is hired. You cannot remove!")
                            break
        except IndexError:
            print("You entered less than 2 entry! You must enter 2 command!")
    if command[0].strip() == "S":
        try:
            command[1] = command[1].rstrip().lstrip()
            if len(command) < 2 or len(command) > 2:
                print("You must enter 2 commands!")
            elif '"' != command[1][0] or '"' != command[1][-1]:
                print("Name must be string type!")
            else:
                attribute = ["Serial:\t","Price:\t","Name:\t","Genre:\t","Director:","State:\t"]
                counter = 0
                command[1] = command[1].strip().strip('"')
                command[1] = command[1].strip()
                print(command[1])
                counter = 0
                if len(command[1]) < 3:
                        print("You must enter minimum 3 letters for searching!")
                for i in range(len(film_list)):
                    if film_list[i] == [""]:
                        continue

                    elif len(command[1]) >= 3 and command[1] in film_list[i][2]:
                        for j in film_list[i]:
                            print(attribute[counter],end=" ")
                            print(j)
                            counter += 1
                            if counter == 6:
                                break
                        #print("")
                        break
                counter = 0
                for j in film_list:
                    if j == [""]:
                        counter += 1
                        continue

                    elif command[1] not in j[2]:
                        counter += 1
                        if counter == len(film_list):
                            print("Entry could not found!")
        except IndexError:
            print("You entered less than 2 entry!Search mode has take 2 argument! You must enter 2 commands.")

    if command[0] == "E":   ###Bu if'in altında bazı kısımlar mantıksız saçma gelebilir. Son anda yaptığım değişikliklerden ötürü öyle oldu. Neyin olup olmadığını da biliyorum.
        try:
            E_Command = []
            serial_numbers = [i[0] for i in film_list]
            if '"' in command[1]:
                print("Serial number must be integer!")
            elif command[1] not in serial_numbers:
                print("There is no this serial number in the inventory!")
            else:
                counter = 0
                sayac = 0

                for i in command:
                    temp = []
                    if "{" in i:
                        temp.append(i.lstrip('{').rstrip('}').strip('"').strip().split("=")[0].strip('"').strip())
                        temp.append(i.lstrip('{').rstrip('}').strip('"').strip().split("=")[1].strip('"').strip())
                        E_Command.append(temp)
                    else:
                        E_Command.append(i)
                for i in range(len(E_Command)):
                   if "Name" in E_Command[i]:
                        new_name = E_Command[i][1]
                        for j in range(len(film_list)):
                            if E_Command[1] in film_list[j][0]:
                                temp = film_list[j]
                                del temp[2]
                                del film_list[j]
                                temp.insert(2,new_name.strip().lstrip('"'))
                                film_list.insert(j,temp)

                   elif "Price" in E_Command[i]:
                        new_price = E_Command[i][1]
                        for j in range(len(film_list)):
                            if E_Command[1] in film_list[j][0]:
                                temp = film_list[j]
                                del temp[1]
                                del film_list[j]
                                temp.insert(1,new_price.strip().lstrip('"'))
                                film_list.insert(j,temp)
                   elif "Genre" in E_Command[i]:
                        new_genre = E_Command[i][1]
                        for j in range(len(film_list)):
                            if E_Command[1] in film_list[j][0]:
                                temp = film_list[j]
                                del temp[3]
                                del film_list[j]
                                temp.insert(3,new_genre.strip().lstrip('"'))
                                film_list.insert(j,temp)
                   elif "Director" in E_Command[i]:
                        new_director = E_Command[i][1]
                        for j in range(len(film_list)):
                            if E_Command[1] in film_list[j][0]:
                                temp = film_list[j]
                                del temp[4]
                                del film_list[j]
                                temp.insert(4,new_director.strip().lstrip('"'))
                                film_list.insert(j,temp)
        except IndexError:
            print("You entered less than 3 entry! Edit mode take at least 3 argument!")
    if command[0] == "H":
        try:
            serial_numbers = [i[0] for i in film_list]
            if '"' in command[1]:
                print("Serial number must be integer!")
            elif len(command) < 2:
                print("You entered less than 2 command. You must enter 2 command!")
            elif len(command) > 2:
                print("You entered more than 2 commands. You must enter 2 commands!")
            elif command[1] not in serial_numbers:
                print("Serial number does not exists!")
            else:
                attribute = ["Serial:\t","Price:\t","Name:\t","Genre:\t","Director:","State:\t"]
                counter = 0
                for i in range(len(film_list)):
                    if film_list[i][0] == command[1]:
                        for j in film_list[i]:
                            print(attribute[counter],end=" ")
                            print(j)
                            counter += 1
                            if counter == 6:
                                print("DVD's state was changed to as hired!")
                                break
                        if film_list[i][-1] == "Inv":
                            temp = film_list[i]
                            del temp[-1]
                            temp.insert(5,"Hired")
                            del film_list[i]
                            film_list.insert(i,temp)
                        elif film_list[i][-1] == "Hired":
                            print("Hired dvd's state cannot be change!")
        except IndexError:
            print("You entered less than 2 entry! Hire mode take 2 argument! You must enter 2 commands!")
    if command[0] == "L":
        if len(command) > 1:
            print("List mode can have just one command!")
        elif film_list == []:
            print("DVD Store is empty! There is nothing to show!")
        else:
            command[0] = command[0].strip()
            counter = 0
            ListMode = []
            for i in film_list:
                if i != [""]:
                    ListMode.append(i)
            ListMode = sorted(ListMode,key=itemgetter(2))
            print("---INVENTORY ITEMS---")
            for i in film_list:
                if i != [""]:
                    print("\nSerial\tPrice\tName\tGenre\tDirector\tState\n")
                    print("-----\t-----\t----\t-----\t--------\t-----\n")
                    for j in i:
                        print(j,end=" ")
                    command = list(input("\n\nPress Enter to continue...").split())
                    if command == []:
                        continue


    print(" ---HUBM DVD----")
    print("A:   Add new dvd")
    print("R:   Remove dvd")
    print("S:   Search dvd")
    print("L:   List dvd")
    print("E:   Edit dvd")
    print("H:   Hire dvd")
    print("Q:   Quit")
    print("Enter Command: ",end="")

    command = list(input().split(","))
    command[0] = command[0].strip()

f = open("dvdStore.txt","w")
counter = 0
while len(film_list) != counter:
    for i in film_list:
        if i != [""]:
            f.write("%s,%s,%s,%s,%s,%s;\n" %(i[0],i[1],i[2],i[3],i[4],i[5]))
            counter += 1
        elif i == [""]:
            f.write("\n")
            counter += 1

f.close()
