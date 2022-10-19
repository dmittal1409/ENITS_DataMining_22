from Listkeeper import Listkeeper
#Importing ListKeeper module from Listkeeper file which has 5 functions
if __name__ == "__main__":

    obj = Listkeeper()
    print(obj.show())
    obj.add('qualification',(['school,','school','school'],['college','college','college'],['Bachelors','Bachelors',None]))
    print(obj.show())
    obj.delete('qualification')
    print(obj.show())
    obj.sort()
    obj.append()
    print(obj.show())
    obj.append()
    print(obj.show())
    
    
    
