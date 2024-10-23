class Phonebook:
    def __init__(self,name,surname,number):
        self.name = name
        self.surname = surname
        self.number = number
        if name is not None and surname is not None and number is not None: 
            self.save(name,surname,number)
       

    def save(self,name,surname,number):
        try:
            file = open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","a")
            file.write(f"{self.name},{self.surname},{self.number}\n")
            file.close()
        except IOError as e : 
             print(f"An error occured while saving the phonebook: {e}")

    def add_person(self):
        try:
            name = input("Enter te person's name: ")
            surname = input("Enter the person's surname: ")
            number  = input("Enter the person's number : ")
            
            person=Phonebook(name,surname,number)
            person.save()
            print("Person added.")
        except Exception as e:
            print(f"An error occured while adding the person: {e}" )



    def control_number(self, number):
  
        if len(number) != 11:
           return False
    
  
        if not number.isdigit():
           return False
    
    
        if number.startswith("05") and len(number) == 11 :
          return True
        else:
          return False

    
    def delete_person(self,name):
        try:
            with open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","r") as file:
                lines =file.readlines()

            with open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","w") as file:
                for line in lines:
                   if name not in line :
                        file.write(line)
            print(f"{name} deleted .")
        except IOError as e:
            print(f"An error occured while deleting {name}: {e}")

    def find_person_by_name(self,name):
        try:
            with open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","r") as file:
                for line in file:
                    if name in line:
                        print(line.strip())
                        return
            print(f"{name} is not found in the phonebook.")
        except IOError as e :
            print(f"An error occured while searching for {name}: {e}")

    def find_person_by_surname(self,surname):
        try:
            with open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","r") as file:
                found = False 
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) >= 2 and parts[1] == surname:
                        print(line.strip())
                        found = True
                if not found :
                    print(f"'{surname}' no person matching last name was found.")
        except IOError as e :
            print(f"{surname} an error occured while searching for the surname")

    def update_person(self,old_person,new_person):
        try:
            with open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","r") as file:
                lines = file.readlines() 

            with open(r"C:\Users\İNTO\Desktop\DOSYALAR\myphonebook.txt","w") as file:
                for line in lines: 
                    if old_person in line:
                        updated_line =line.replace(old_person, new_person)
                        file.write(updated_line)
                    else:
                        file.write(line)

            print(f"{old_person} updated to {new_person}.")
        except IOError as e:
            print(f"An error occured while updating {old_person}: {e}")






                     
        