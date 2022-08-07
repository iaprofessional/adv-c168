 class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number

        
    def add_citizen(self):
            print("Name: " + self.citizen_name)   
            print("Age: " + str(self.citizen_age))   
            print("DOB: " + self.citizen_dob)
            print("Id: " + self.citizen_id)   
            print("Citizen Added")
            
            
            
 citizen1 = Citizen("Stephen Strange",25,"10 August 1995","01")
 citizen1.add_citizen()
 
 citizen2 = Citizen("Peter Parker",17,"15 May 1999","02")
 citizen2.add_citizen()
 
