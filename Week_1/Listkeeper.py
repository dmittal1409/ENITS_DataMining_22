
class Listkeeper:
  try: 
    def __init__(self):
      #The init function in any class works as self declaration function , ref constructor all

      self.list_names = dict([('Subjects',['Data Mining','Software Security','Applid cryptanalysis']),
                        ('Credits',[6,6,6]),
                        ('Sem',[1,1,1]),
                        ('Country',['Germany','India','Canada'])])
      
    def show(self):
      #The show is udfunction , declared for showing the names of list in the Dictonary and also if you to see value enter 2

      print("1. To show the list key wise")
      print("2 To show the list value wise")
      choice = int(input("enter your choice:"))
      if(choice ==1):
        return(self.list_names.keys())
      elif(choice == 2):
        print(self.list_names)
      else:
        print("please enter correct value")

    def add(self,index,value):
      #The add is udfunction , declared for adding the passed value to passed index

      self.list_names[index]=value
      
    def delete(self,index):
      #The delete is udfunction , declared for deleting the passed index value 

      self.list_names.pop(index)
      #self.list_names.popitem()
      #del(list_names[index])

    def sort(self):
      #The sort is udfunction , declared for sorting the dictonary key wise or value wise

      print("1. To sort the list key wise")
      print("2 To sort the list value wise")
      choice = int(input("enter your choice:"))
      if(choice ==1):
        list_keys = self.list_names.keys()
        #print(list_keys)
        new_sorted_list = sorted(list_keys)
        print(new_sorted_list)
        for i in new_sorted_list:
          print(f"{i}:{self.list_names[i]}")
      elif(choice ==2):
        list_value = self.list_names.items()
        print(list_value)
        new_sorted_list = sorted(list_value)
        print(new_sorted_list)
      else:
        print("please enter vaild input")
      
    def append(self):

      print("1. To append a new list to exsiting index")
      print("2 To append a new value in the exsiting list to exsiting index")
      choice = int(input("enter your choice:"))
      if(choice ==1):
        index = str(input("enter the index value : "))
        value = input("enter the value of : ")
        self.list_names[index].append(value)
      elif(choice ==2):
        index = str(input("enter the index value : "))
        list_index_value = int(input("enter the value of list index"))
        value = input("enter the value of : ")
        self.list_names[index][list_index_value]=(value)
      else:
        print("Please enter vaild input")
                
  except Exception as exe:
    #Exception block
    
    print(f"Error---->{exe}")

