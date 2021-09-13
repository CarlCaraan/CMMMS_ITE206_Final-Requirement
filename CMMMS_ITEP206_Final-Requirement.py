print("Group Name: CMMMS")
print("Group Members: Caraan, Carl Aaron D.\n               Malaga, Aron Dominic A.\n               Martin, Liam Cassiel L.\n               Megino, Robin Andrew C.\n               Sorromero, Paolo M.")
print("ITEP 206 Integrated Programming\nBSIT 2-A \nAcademic Year 2020-2021, 2nd Semester\n")
name = input("Hello! Please enter your name: ")
print("Welcome to our python objects guide, " +name +"!\n")

def mainMenu():
    print("\n")
out = ("Output: ")
print("Choose a Python Object")
print("1) Set")
print("2) Tuple")
print("3) Dictionary")
print("4) List")
print("5) String")
print("6) Built-in Functions")
print("7) File Method")
print("8) Keywords")
selection= int(input("Enter your choice: "))
#set method
if selection ==1:
    print("You have selected Python Object: Set")
    print("Input 5 elements to be added to the Set")
    in1 = input("Enter 1st Element: ")
    in2 = input("Enter 2nd Element: ")
    in3 = input("Enter 3rd Element: ")
    in4 = input("Enter 4th Element: ")
    in5 = input("Enter 5th Element: ")
    print("Please choose on how you want to search the method")
    print("1) Select Set Method")
    print("2) Select all Set Method")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) add method")
        print("2) clear method")
        print("3) copy method")
        print("4) difference method")
        print("5) difference_update method")
        print("6) discard method")
        print("7) intersection method")
        print("8) intersection_update method")
        print("9) isdisjoint method")
        print("10) issubset method")
        print("11) issuperset method")
        print("12) pop method")
        print("13) remove method")
        print("14) symetric_difference method")
        print("15) symetric_difference_update method")
        print("16) union method")
        print("17) update method")
        selection= int(input("Enter your choice: "))
        if selection == 1:
            addset = ("add() Set \n The add() method adds an element or item to the set. \n Code: \n x = {in1,in2,in3} \n x.add(in4,in5) \n")
            print (addset)
            x = {in1, in2, in3, in4}
            x.add(in5)
            print(out)
            print(x)
        elif selection ==2:
            print("You have chosen the clear() method")
            clearset = ("clear() Set \n The clear() method removes all elements or items in a set. \n Code: \n x = {in1,in2,in3,in4,in5} \n y = x.clear() \n")
            print (clearset)
            x = [in1, in2, in3, in4, in5]
            x.clear()
            print(out)
            print(x)
        elif selection ==3:
            print("You have chosen the copy() method")
            copyset = ("copy() Set \n The copy() method copies the set. \n Code: \n x = {in1, in2, in3,in4,in5} \n y = x.copy() \n")
            print (copyset)
            x = {in1,in2,in3,in4,in5}
            x.copy()
            print(out)
            print(x)
        elif selection ==4:
            print("You have chosen the difference() method")
            differenceset = ("difference() Set \n The difference() method returns a set that contains the difference between two sets. \n Code: \n x = {in1,in2, in3} \n y = {in4,in5} () \n z = x.difference(y) \n")
            print (differenceset)
            x = {in1, in2, in3}
            y = {in4,in5}
            z = x.difference(y)
            print(out)
            print(z)
        elif selection ==5:
            print("You have chosen the difference_update() method")
            differenceupdateset = ("difference_update() Set \n The difference() method remove the items that exist in both sets.\n Code: \n x = {in1, in2, in3} \n y = {in4,in5} () \n z = x.difference_update(y) \n")
            print (differenceupdateset)
            x = {in1, in2, in3}
            y = {in4, in5}
            z = x.difference_update(y)
            print(out)
            print(z)            
        elif selection ==6:
            print("You have chosen the discard() method")
            discardset = ("discard() Set \n The discard() method removes the specified item from the set. \n Code: \n x = {in1, in2, in3} \n x.discard()\n")
            print (discardset)
            x = {in1, in2, in3, in4, in5}
            x.discard(in4)
            print(out)
            print(x)
        elif selection ==7:
            print("You have chosen the intersection() method")
            intersectionset = ("intersection() Set\n The intersection() method returns a set that contains the similarity between two or more sets. \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} () \n z = x.intersection (y) \n")
            print (intersectionset)
            x = {in1, in2, in3}
            y = {in4, in5}
            z = x.intersection(y)
            print(out)
            print(z)
        elif selection ==8:
            print("You have chosen the intersection_update() method")
            intersectionupdateset = ("intersection_update() Set \n The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets). \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} () \n z = x.intersection_update (y) \n")
            print (intersectionupdateset)
            x = {in1, in2, in3}
            y = {in4, in5}
            x.intersection_update(y)
            print(out)
            print(x)
        elif selection ==9:
            print("You have chosen the isdisjoint() method")
            isdisjointset = ("isdisjoint() Set \n The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False. \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} () \n z = x.isdisjoint (y) \n")
            print (isdisjointset)
            x = {in1, in2, in3}
            y = {in4, in5}
            z = x.isdisjoint(y)
            print(out)
            print(z)
        elif selection ==10:
            print("You have chosen the issubset() method")
            issubsetset = ("issubset() Set \n The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False. \n Code: \n x = {in1, in2, in3} \n y = {in3, in4, in5} () \n z = x.issubset (y) \n")
            print (issubsetset)
            x = {in1, in2, in3}
            y = {in4, in5, in3}
            z = x.issubset(y)
            print(out)
            print(z)
        elif selection ==11:
            print("You have chosen the issuperset() method")
            issupersetset = ("issuperset() Set \n The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False. \n Code: \n x = {in4, in5} \n y = {in1, in2, in3, in4, in5} () \n z = x.issuperset (y) \n")
            print (issupersetset)
            x = {in4, in5}
            y = {in1, in2, in3, in4, in5}
            z = x.issuperset(y)
            print(out)
            print(z)
        elif selection ==12:
            print("You have chosen the pop() method")
            popset = ("pop() Set \n The pop() method removes a random item from the set. This method returns the removed item.  \n Code: \n x = {in1, in2, in3, in4, in5} \n x.pop () \n")
            print (popset)
            x = {in1, in2, in3, in4, in5}
            x.pop ()
            print(out)
            print(x)
        elif selection ==13:
            print("You have chosen the remove() method")
            removeset = ("remove() Set \n The remove() method removes the specified element from the set.  \n Code: \n x = {in1, in2, in3, in4, in5} \n x.remove (in3) \n")
            x = {in1, in2, in3, in4, in5}
            print (removeset)
            x.remove (in3)
            print(out)
            print(x)
        elif selection ==14:
            print("You have chosen the symmetric_difference() method")
            symmetricdifferenceset = ("symmetric_difference() Set \n The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.   \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} \n z = x.symmetric_diffrence(y) \n")
            x = {in1, in2, in3}
            y = {in4, in5}
            z = x.symmetric_difference(y)
            print(out)
            print(z)
        elif selection ==15:
            print("You have chosen the symetric_difference_update() method")
            symmetricdifferenceupdateset = ("symmetric_difference_update() Set \n The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.   \n Code: \n x = {in1, in2, in3, in4, in5} \n y = {in4, in5} \n x.symmetric_diffrence_update(y) \n")
            print (symmetricdifferenceupdateset)
            x = {in1, in2, in3, in4, in5}
            y = {in4, in5}
            x.symmetric_difference(y)
            print(out)
            print(x)
        elif selection ==16:
            print("You have chosen the union() method")
            unionset = ("union() Set \n The union() method returns a set that contains all items from the original set, and all items from the specified sets. \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} \n z=x.union(y) \n")
            print(unionset)
            x = {in1, in2, in3}
            y = {in4, in5}
            z= x.union(y)
            print(out)
            print(z)
        elif selection ==17:
            print("You have chosen the update() method")
            updateset = ("update() Set \n The update() method updates the current set, by adding items from another set. \n Code: \n x = {in1, in2, in3} \n y = {in4,in5} \n z= x.update(y) \n")
            print(updateset)
            x = {in1, in2, in3}
            y = {in3,in4,in5}
            x.update(y)
            print(out)
            print(x)
    elif choice ==2:
        addset = ("add() Set \n The add() method adds an element or item to the set. \n Code: \n x = {in1,in2,in3} \n x.add(in4,in5) \n")
        print (addset)
        x = {in1, in2, in3, in4}
        x.add(in5)
        print(out)
        print(x)
        
        clearset = ("clear() Set \n The clear() method removes all elements or items in a set. \n Code: \n x = {in1,in2,in3,in4,in5} \n y = x.clear() \n")
        print (clearset)
        x = [in1, in2, in3, in4, in5]
        x.clear()
        print(out)
        print(x)
        
        copyset = ("copy() Set \n The copy() method copies the set. \n Code: \n x = {in1, in2, in3,in4,in5} \n y = x.copy() \n")
        print (copyset)
        x = {in1,in2,in3,in4,in5}
        x.copy()
        print(out)
        print(x)
        
        differenceset = ("difference() Set \n The difference() method returns a set that contains the difference between two sets. \n Code: \n x = {in1,in2, in3} \n y = {in4,in5} () \n z = x.difference(y) \n")
        print (differenceset)
        x = {in1, in2, in3}
        y = {in4,in5}
        z = x.difference(y)
        print(out)
        print(z)
        
        differenceupdateset = ("difference_update() Set \n The difference() method remove the items that exist in both sets.\n Code: \n x = {in1, in2, in3} \n y = {in4,in5} () \n z = x.difference_update(y) \n")
        print (differenceupdateset)
        x = {in1, in2, in3}
        y = {in4, in5}
        z = x.difference_update(y)
        print(out)
        print(z)
        
        discardset = ("discard() Set \n The discard() method removes the specified item from the set. \n Code: \n x = {in1, in2, in3} \n x.discard()\n")
        print (discardset)
        x = {in1, in2, in3, in4, in5}
        x.discard(in4)
        print(out)
        print(x)
         
        intersectionset = ("intersection() Set\n The intersection() method returns a set that contains the similarity between two or more sets. \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} () \n z = x.intersection (y) \n")
        print (intersectionset)
        x = {in1, in2, in3}
        y = {in4, in5}
        z = x.intersection(y)
        print(out)
        print(z)
         
        intersectionupdateset = ("intersection_update() Set \n The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets). \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} () \n z = x.intersection_update (y) \n")
        print (intersectionupdateset)
        x = {in1, in2, in3}
        y = {in4, in5}
        x.intersection_update(y)
        print(out)
        print(x)
        
        isdisjointset = ("isdisjoint() Set \n The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False. \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} () \n z = x.isdisjoint (y) \n")
        print (isdisjointset)
        x = {in1, in2, in3}
        y = {in4, in5}
        z = x.isdisjoint(y)
        print(out)
        print(z)
        
        issubsetset = ("issubset() Set \n The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False. \n Code: \n x = {in1, in2, in3} \n y = {in3, in4, in5} () \n z = x.issubset (y) \n")
        print (issubsetset)
        x = {in1, in2, in3}
        y = {in4, in5, in3}
        z = x.issubset(y)
        print(out)
        print(z)
        
        issupersetset = ("issuperset() Set \n The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False. \n Code: \n x = {in4, in5} \n y = {in1, in2, in3, in4, in5} () \n z = x.issuperset (y) \n")
        print (issupersetset)
        x = {in4, in5}
        y = {in1, in2, in3, in4, in5}
        z = x.issuperset(y)
        print(out)
        print(z)
        
        popset = ("pop() Set \n The pop() method removes a random item from the set. This method returns the removed item.  \n Code: \n x = {in1, in2, in3, in4, in5} \n x.pop () \n")
        print (popset)
        x = {in1, in2, in3, in4, in5}
        x.pop ()
        print(out)
        print(x)
        
        removeset = ("remove() Set \n The remove() method removes the specified element from the set.  \n Code: \n x = {in1, in2, in3, in4, in5} \n x.remove (in3) \n")
        x = {in1, in2, in3, in4, in5}
        print (removeset)
        x.remove (in3)
        print(out)
        print(x)
        
        symmetricdifferenceset = ("symmetric_difference() Set \n The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.   \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} \n z = x.symmetric_diffrence(y) \n")
        x = {in1, in2, in3}
        y = {in4, in5}
        z = x.symmetric_difference(y)
        print(out)
        print(z)
        
        symmetricdifferenceupdateset = ("symmetric_difference_update() Set \n The symmetric_difference_update() method updates the original set by removing items that are present in both sets, and inserting the other items.   \n Code: \n x = {in1, in2, in3, in4, in5} \n y = {in4, in5} \n x.symmetric_diffrence_update(y) \n")
        print (symmetricdifferenceupdateset)
        x = {in1, in2, in3, in4, in5}
        y = {in4, in5}
        x.symmetric_difference(y)
        print(out)
        print(x)
        
        unionset = ("union() Set \n The union() method returns a set that contains all items from the original set, and all items from the specified sets. \n Code: \n x = {in1, in2, in3} \n y = {in4, in5} \n z=x.union(y) \n")
        print(unionset)
        x = {in1, in2, in3}
        y = {in4, in5}
        z= x.union(y)
        print(out)
        print(z)
        
        updateset = ("update() Set \n The update() method updates the current set, by adding items from another set. \n Code: \n x = {in1, in2, in3} \n y = {in4,in5} \n z= x.update(y) \n")
        print(updateset)
        x = {in1, in2, in3}
        y = {in3,in4,in5}
        x.update(y)
        print(out)
        print(x)              
#tuple method       
elif selection ==2:
    print("You have selected Python Object: Tuple")
    print("Input 5 elements to be added to the tuple")
    in1 = input("Enter 1st Element: ")
    in2 = input("Enter 2nd Element: ")
    in3 = input("Enter 3rd Element: ")
    in4 = input("Enter 4th Element: ")
    in5 = input("Enter 5th Element: ")
    print("Please choose on how you want to search the method")
    print("1) Select tuple Method")
    print("2) Select all Set Method")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) count method")
        print("2) index method")
        selection= int(input("Enter your choice: "))
        if selection == 1:
            print("You have chosen the count() method")
            counttuple = ("count() Set \n The count() method returns the number of times a specified value appears in the tuple. \n Code: \n thistuple = {in1, in2, in3, in4, in5} \n x = thistuple.count (in3) \n")
            print(counttuple)
            thistuple = (in1, in2, in3, in4, in5,in3)
            x = thistuple.count(in3)
            print(out)
            print(x)
        elif selection ==2:
            print("You have chosen the index() method")
            indextuple = ("index() Set \n The index() method finds the first occurrence of the specified value. The index() method raises an exception if the value is not found. \n Code: \n thistuple = {in1, in2, in3, in4, in5} \n x = thistuple.index (in4) \n")
            print(indextuple)
            thistuple = (in1, in2, in3, in4, in5)
            x = thistuple.index(in3)
            print(out)
            print(x)
    elif choice ==2:
        counttuple = ("count() Set \n The count() method returns the number of times a specified value appears in the tuple. \n Code: \n thistuple = {in1, in2, in3, in4, in5} \n x = thistuple.count (in3) \n")
        print(counttuple)
        thistuple = (in1, in2, in3, in4, in5,in3)
        x = thistuple.count(in3)
        print(out)
        print(x)
        
        indextuple = ("index() Set \n The index() method finds the first occurrence of the specified value. The index() method raises an exception if the value is not found. \n Code: \n thistuple = {in1, in2, in3, in4, in5} \n x = thistuple.index (in4) \n")
        print(indextuple)
        thistuple = (in1, in2, in3, in4, in5)
        x = thistuple.index(in4)
        print(out)
        print(x)
#dictionary method        
elif selection ==3:
    print("You have selected Python Object: Dictionary")
    print("Input 5 elements to be added to the Dictionary")
    in1 = input("Enter 1st Element: ")
    in2 = input("Enter 2nd Element: ")
    in3 = input("Enter 3rd Element: ")
    in4 = input("Enter 4th Element: ")
    in5 = input("Enter 5th Element: ")
    print("Please choose on how you want to search method")
    print("1) Select Dictionary Method")
    print("2) Select all Dictionary Method")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) clear method")
        print("2) copy method")
        print("3) fromkeys method")
        print("4) get method")
        print("5) items method")
        print("6) keys method")
        print("7) pop method")
        print("8) popitem method")
        print("9) setdefault method")
        print("10) update method")
        print("11) values method")
        selection= int(input("Enter your choice: "))
        if selection == 1:
            print("You have chosen the Clear() method")
            cleardic=("clear() Method\nThe clear() method removes all the elements from a dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.clear()\nprint(x)")
            print(cleardic)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            x.clear()
            print(out)
            print(x)
        elif selection ==2:
            print("You have chosen the Copy() method")
            copydic=("copy() Method\nThe copy() method returns a copy of the specified dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.copy()\nprint(y)")
            print(copydic)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.copy()
            print(out)
            print(y)
        elif selection ==3:
            print("You have chosen the Fromkeys() method")
            fkeysdic=("fromkeys() Method\nThe fromkeys() method returns a dictionary with the specified keys and the specified value.\nCODE:\nx = (“‘key1’”,”’key2’”,”’key3’”,”’key4’”,”’key5’”)\ny = 0\nthisdict = dict.fromkeys(x, y)\nprint(thisdict)")
            print(fkeysdic)
            x = ('key1','key2','key3','key4','key5')
            y = 0
            thisdict = dict.fromkeys(x, y)
            print(out)
            print(thisdict)
        elif selection ==4:
            print("You have chosen the Get() method")
            getdic=("get() Method\nThe get() method returns the value of the item with the specified key\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.get(“key3”)\nprint(y)")
            print(getdic)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.get("key3")
            print(out)
            print(y)
        elif selection ==5:
            print("You have chosen the Items() method")
            itemsdic1=("items() Method\nThe items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. The view object will reflect any changes done to the dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.items()\nprint(y)")
            print(itemsdic1)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.items()
            print(out)
            print(y)            
            itemsdic2=("x = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.items()\nx[""key3""] = 3rd Element\nprint(y)")
            print(itemsdic2)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.items()
            x["key3"] = "3rd Element"
            print(out)
            print(y)
        elif selection ==6:
            print("You have chosen the Keys() method")
            keydic1=("keys() Method\nThe keys() method returns a view object. The view object contains the keys of the dictionary, as a list. The view object will reflect any changes done to the dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,:""key5"":in5}\ny = x.keys()\nprint(y)")
            print(keydic1)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.keys()
            print(out)
            print(y)
            keydic2=("x = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.items()\nx[""key6""] = ""6th Element""\nprint(y)")
            print(keydic2)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.items()
            x["key6"] = "6th Element"
            print(out)
            print(y)
        elif selection ==7:
            print("You have chosen the Pop() method")
            popdic1=("pop() Method\nThe pop() method removes the specified item from the dictionary. The value of the removed item is the return value of the pop() method.\nCODE:\nRemoving specified item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.pop(""key2"")\nprint(x)")
            print(popdic1)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            x.pop("key2")
            print(out)
            print(x)
            popdic2=("Returning the removed item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.pop(""key2"")\nprint(y)")
            print(popdic2)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.pop("key2")
            print(out)
            print(y)
        elif selection ==8:
            print("You have chosen the Popitem() method")
            popidic1=("popitem() Method\nThe popitem() method removes the item that was last inserted into the dictionary.\nCODE:\nRemoving specified item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.popitem()\nprint(x)")
            print(popidic1)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            x.popitem()
            print(out)
            print(x)
            popidic2=("Returning the removed item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.popitem()\nprint(out)\nprint(y)")
            print(popidic2)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.popitem()
            print(out)
            print(y)
        elif selection ==9:
            print("You have chosen the setdefault() method")
            defdic1=("setdefault() Method \nThe setdefault() method returns the value of the item with the specified key.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.setdefault(""key3"",""3rd Element"")\nprint(y)\nprint(x)")
            print(defdic1)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.setdefault("key3","3rd Element")
            print(out)
            print(y)
            print(x)
            defdic2=("If the key does not exist, insert the key, with the specified value.\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.setdefault(""key6"",""6th Element"")\nprint(y)\nprint(x)")
            print(defdic2)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.setdefault("key6","6th Element")
            print(out)
            print(y)
            print(x)
        elif selection ==10:
            print("You have chosen the update() method")
            updic=("update() Method\nThe update() method inserts the specified items to the dictionary. The specified items can be a dictionary, or an iterable object.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.update({""key3"":""3rdElement""})\nprint(x)")
            print(updic)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            x.update({"key3":"3rdElement"})
            print(out)
            print(x)
        elif selection ==11:
            print("You have chosen the values() method")
            valdic1=("values() Method The values() method returns a view object. The view object contains the values of the dictionary, as a list. The view object will reflect any changes done to the dictionary.\nCODE:\nGetting and returning the value of item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.values()\nprint(y)")
            print(valdic1)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.values()
            print(out)
            print(y)
            valdic2=("Making some changes\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.values()\nx[““key5””] = “”5th Element””\nprint (y)")
            print(valdic2)
            x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
            y = x.values()
            x["key5"] = "5th Element"
            print(out)
            print(y)
    elif choice ==2:
        print("\n")
        
        cleardic=("clear() Method\nThe clear() method removes all the elements from a dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.clear()\nprint(x)")
        print(cleardic)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        x.clear()
        print(out)
        print(x)
        print("\n")
        
        copydic=("copy() Method\nThe copy() method returns a copy of the specified dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.copy()\nprint(y)")
        print(copydic)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.copy()
        print(out)
        print(y)
        print("\n")
        
        fkeysdic=("fromkeys() Method\nThe fromkeys() method returns a dictionary with the specified keys and the specified value.\nCODE:\nx = (“‘key1’”,”’key2’”,”’key3’”,”’key4’”,”’key5’”)\ny = 0\nthisdict = dict.fromkeys(x, y)\nprint(thisdict)")
        print(fkeysdic)
        x = ('key1','key2','key3','key4','key5')
        y = 0
        thisdict = dict.fromkeys(x, y)
        print(out)
        print(thisdict)
        print("\n")
        
        getdic=("get() Method\nThe get() method returns the value of the item with the specified key\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.get(“key3”)\nprint(y)")
        print(getdic)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.get("key3")
        print(out)
        print(y)
        print("\n")
        
        itemsdic1=("items() Method\nThe items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list. The view object will reflect any changes done to the dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.items()\nprint(y)")
        print(itemsdic1)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.items()
        print(out)
        print(y)
        itemsdic2=("x = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.items()\nx[""key3""] = 3rd Element\nprint(y)")
        print(itemsdic2)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.items()
        x["key3"] = "3rd Element"
        print(out)
        print(y)
        print("\n")
        
        keydic1=("keys() Method\nThe keys() method returns a view object. The view object contains the keys of the dictionary, as a list. The view object will reflect any changes done to the dictionary.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,:""key5"":in5}\ny = x.keys()\nprint(y)")
        print(keydic1)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.keys()
        print(out)
        print(y)
        keydic2=("x = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.items()\nx[""key6""] = ""6th Element""\nprint(y)")
        print(keydic2)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.items()
        x["key6"] = "6th Element"
        print(out)
        print(y)
        print("\n")
        
        popdic1=("pop() Method\nThe pop() method removes the specified item from the dictionary. The value of the removed item is the return value of the pop() method.\nCODE:\nRemoving specified item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.pop(""key2"")\nprint(x)")
        print(popdic1)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        x.pop("key2")
        print(out)
        print(x)
        popdic2=("Returning the removed item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.pop(""key2"")\nprint(y)")
        print(popdic2)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.pop("key2")
        print(out)
        print(y)
        print("\n")
        
        popidic1=("popitem() Method\nThe popitem() method removes the item that was last inserted into the dictionary.\nCODE:\nRemoving specified item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.popitem()\nprint(x)")
        print(popidic1)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        x.popitem()
        print(out)
        print(x)
        popidic2=("Returning the removed item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.popitem()\nprint(out)\nprint(y)")
        print(popidic2)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.popitem()
        print(out)
        print(y)
        print("\n")
        
        defdic1=("setdefault() Method \nThe setdefault() method returns the value of the item with the specified key.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.setdefault(""key3"",""3rd Element"")\nprint(y)\nprint(x)")
        print(defdic1)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.setdefault("key3","3rd Element")
        print(out)
        print(y)
        print(x)
        defdic2=("If the key does not exist, insert the key, with the specified value.\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.setdefault(""key6"",""6th Element"")\nprint(y)\nprint(x)")
        print(defdic2)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.setdefault("key6","6th Element")
        print(out)
        print(y)
        print(x)
        print("\n")
        
        updic=("update() Method\nThe update() method inserts the specified items to the dictionary. The specified items can be a dictionary, or an iterable object.\nCODE:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\nx.update({""key3"":""3rdElement""})\nprint(x)")
        print(updic)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        x.update({"key3":"3rdElement"})
        print(out)
        print(x)
        print("\n")
        
        valdic1=("values() Method The values() method returns a view object. The view object contains the values of the dictionary, as a list. The view object will reflect any changes done to the dictionary.\nCODE:\nGetting and returning the value of item:\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.values()\nprint(y)")
        print(valdic1)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.values()
        print(out)
        print(y)
        valdic2=("Making some changes\nx = {""key1"":in1,""key2"":in2,""key3"":in3,""key4"":in4,""key5"":in5}\ny = x.values()\nx[““key5””] = “”5th Element””\nprint (y)")
        print(valdic2)
        x = {"key1":in1,"key2":in2,"key3":in3,"key4":in4,"key5":in5}
        y = x.values()
        x["key5"] = "5th Element"
        print(out)
        print(y)
#list method        
elif selection == 4:
    print("You have selected Python Object: List")
    print("Input 5 elements to be added to the List")
    in1 = input("Enter 1st Element: ")
    in2 = input("Enter 2nd Element: ")
    in3 = input("Enter 3rd Element: ")
    in4 = input("Enter 4th Element: ")
    in5 = input("Enter 5th Element: ")
    print("Please choose on how you want to search method")
    print("1) Select List Method")
    print("2) Select all List Method")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) append method")
        print("2) clear method")
        print("3) copy method")
        print("4) count method")
        print("5) extend method")
        print("6) index method")
        print("7) insert method")
        print("8) pop method")
        print("9) remove method")
        print("10) reverse method")
        print("11) sort method")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen the Append() method")
            appendlist = ("append() Method\n The append() method appends an element to the end of the list. \n Code: \n x = [in1, in2, in3, in4, in5] \n x.append(“6th Element“)")
            print (appendlist)
            x = [in1,in2,in3,in4,in5]
            x.append("6th element")
            print(out)
            print(x)
        elif selection ==2:
            print("You have chosen the Clear() method")
            clearlist = ("clear() Method \nThe clear() method removes all the elements from a list \nCode: \nx = [in1, in2, in3, in4, in5] \nx.clear() \nprint(x)")
            print (clearlist)
            x = [in1, in2, in3, in4, in5]
            x.clear()
            print(out)
            print(x) 
        elif selection ==3:
            print("You have chosen the Copy() method")
            copylist = ("copy() Method \nThe copy() method returns a copy of the specified list.\nCode:\nx = [in1, in2, in3, in4, in5]\ny = x.copy()\nprint(y)")
            print(copylist)
            x = [in1, in2, in3, in4, in5]
            y = x.copy()
            print(out)
            print(y) 
        elif selection ==4:
            print("You have chosen the Count() method")
            countlist = ("count() Method\nThe count() method returns the number of elements with the specified value.\nCode:\nx = [in1, in2, in3, in4, in5]\ny = x.count(in3)\nprint(y)")
            print(countlist)
            x = [in1, in2, in3, in4, in5]
            y = x.count(in5)
            print(out)
            print(y)
        elif selection ==5:
            print("You have chosen the Extend() method")
            extendlist=("extend() Method\nThe extend() method adds the specified list elements (or any iterable) to the end of the current list.\nCode:\nx = [in1, in2, in3]\ny = [in4,in5]\nx.extend(y)\nprint(x)")
            print (extendlist)
            x = [in1, in2, in3]
            y = [in4, in5]
            x.extend(y)
            print(out)
            print(x)
        elif selection ==6:
            print("You have chosen the Index() method")
            indexlist=("index() Method\nThe index() method returns the position at the first occurrence of the specified value.\nCode:\nx = [in1, in2, in3, in4, in5]\ny = x.index(in3)\nprint(y)")
            print(indexlist)
            x = [in1, in2, in3, in4, in5]
            y = x.index(in3)
            print(out)
            print(y) 
        elif selection ==7:
            print("You have chosen the Insert() method")
            insertlist=("insert() Method\nThe insert() method inserts the specified value at the specified position.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.insert(1, in1)\nprint(x)")
            print(inserlist)
            x = [in1, in2, in3, in4, in5]
            x.insert(1, in1)
            print(out)
            print(x) 
        elif selection ==8:
            print("You have chosen the Pop() method")
            poplist=("pop() method\nThe pop() method removes the element at the specified position.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.pop(1)\nprint(x)")
            print(poplist)
            x = [in1, in2, in3, in4, in5]
            x.pop(1)
            print(out)
            print(x) 
        elif selection ==9:
            print("You have chosen the Remove() method")
            removelist=("remove() method\nThe remove() method removes the first occurrence of the element with the specified value.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.remove(in3)\nprint(x)")
            print(removelist)
            x = [in1, in2, in3, in4, in5]
            x.remove(in2)
            print(out)
            print(x) 
        elif selection ==10:
            reverselist=("reverse() Method\nThe reverse() method reverses the sorting order of the elements.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.reverse()\nprint(x)")
            print(reverselist)
            x = [in1, in2, in3, in4, in5]
            x.reverse()
            print(out)
            print(x) 
        elif selection ==11:
            print("You have chosen the Sort() method")
            sortlist1=("sort() Method\nThe sort() method sorts the list ascending by default.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.sort()\nprint(x)")
            print(sortlist1)
            x = [in1, in2, in3, in4, in5]
            x.sort()
            print(out)
            print(x)
            sortlist2=("x = [in1, in2, in3, in4, in5]\nx.sort(reverse=True)\nprint(x)")
            print(sortlist2)
            x = [in1, in2, in3, in4, in5]
            x.sort(reverse=True)
            print(out)
            print(x)
            sortlist3=("x = [in1, in2, in3, in4, in5]\nx.sort(key=len)\nprint(x)")
            print(sortlist3)
            x = [in1, in2, in3, in4, in5]
            x.sort(key=len)
            print(out)
            print(x)      
    elif choice ==2:
        print("\n")
        
        appendlist = ("append() Method\n The append() method appends an element to the end of the list. \n Code: \n x = [in1, in2, in3, in4, in5] \n x.append(“6th Element“)")
        print (appendlist)
        x = [in1,in2,in3,in4,in5]
        x.append("6th element")
        print(out)
        print(x)
        print("\n")
        
        clearlist = ("clear() Method \nThe clear() method removes all the elements from a list \nCode: \nx = [in1, in2, in3, in4, in5] \nx.clear() \nprint(x)")
        print (clearlist)
        x = [in1, in2, in3, in4, in5]
        x.clear()
        print(out)
        print(x) 
        print("\n")
        
        copylist = ("copy() Method \nThe copy() method returns a copy of the specified list.\nCode:\nx = [in1, in2, in3, in4, in5]\ny = x.copy()\nprint(y)")
        print(copylist)
        x = [in1, in2, in3, in4, in5]
        y = x.copy()
        print(out)
        print(y) 
        print("\n")
        
        countlist = ("count() Method\nThe count() method returns the number of elements with the specified value.\nCode:\nx = [in1, in2, in3, in4, in5]\ny = x.count(in3)\nprint(y)")
        print(countlist)
        x = [in1, in2, in3, in4, in5]
        y = x.count(in5)
        print(out)
        print(y)
        print("\n")
        
        extendlist=("extend() Method\nThe extend() method adds the specified list elements (or any iterable) to the end of the current list.\nCode:\nx = [in1, in2, in3]\ny = [in4,in5]\nx.extend(y)\nprint(x)")
        print (extendlist)
        x = [in1, in2, in3]
        y = [in4, in5]
        x.extend(y)
        print(out)
        print(x)
        print("\n")
        
        indexlist=("index() Method\nThe index() method returns the position at the first occurrence of the specified value.\nCode:\nx = [in1, in2, in3, in4, in5]\ny = x.index(in3)\nprint(y)")
        print(indexlist)
        x = [in1, in2, in3, in4, in5]
        y = x.index(in3)
        print(out)
        print(y) 
        print("\n")
        
        insertlist=("insert() Method\nThe insert() method inserts the specified value at the specified position.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.insert(1, in1)\nprint(x)")
        print(insertlist)
        x = [in1, in2, in3, in4, in5]
        x.insert(1, in1)
        print(out)
        print(x)
        print("\n")
        
        poplist=("pop() method\nThe pop() method removes the element at the specified position.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.pop(1)\nprint(x)")
        print(poplist)
        x = [in1, in2, in3, in4, in5]
        x.pop(1)
        print(out)
        print(x) 
        print("\n")
        
        removelist=("remove() method\nThe remove() method removes the first occurrence of the element with the specified value.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.remove(in3)\nprint(x)")
        print(removelist)
        x = [in1, in2, in3, in4, in5]
        x.remove(in2)
        print(out)
        print("\n")
        
        reverselist=("reverse() Method\nThe reverse() method reverses the sorting order of the elements.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.reverse()\nprint(x)")
        print(reverselist)
        x = [in1, in2, in3, in4, in5]
        x.reverse()
        print(out)
        print(x) 
        print("\n")
        
        sortlist1=("sort() Method\nThe sort() method sorts the list ascending by default.\nCode:\nx = [in1, in2, in3, in4, in5]\nx.sort()\nprint(x)")
        print(sortlist1)
        x = [in1, in2, in3, in4, in5]
        x.sort()
        print(out)
        print(x)
        sortlist2=("x = [in1, in2, in3, in4, in5]\nx.sort(reverse=True)\nprint(x)")
        print(sortlist2)
        x = [in1, in2, in3, in4, in5]
        x.sort(reverse=True)
        print(out)
        print(x)
        sortlist3=("x = [in1, in2, in3, in4, in5]\nx.sort(key=len)\nprint(x)")
        print(sortlist3)
        x = [in1, in2, in3, in4, in5]
        x.sort(key=len)
        print(out)
        print(x)
#string method       
elif selection == 5:
    print("You have selected Python Object: String")
    print("Input 5 elements to be added to the String")
    in1 = input("Enter 1st Element: ")
    in2 = input("Enter 2nd Element: ")
    in3 = input("Enter 3rd Element: ")
    in4 = input("Enter 4th Element: ")
    in5 = input("Enter 5th Element: ")
    print("Please choose on how you want to search method")
    print("1) Select String Method")
    print("2) Select all String Method")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) capitalize method")
        print("2) casefold method")
        print("3) center method")
        print("4) count method")
        print("5) encode method")
        print("6) endswith method")
        print("7) expandtabs method")
        print("8) kind method")
        print("9) format method")
        print("10) index method")
        print("11) isalnum method")
        print("12) isalpha method")
        print("13) isdecimal method")
        print("14) isdigit method")
        print("15) isidentifier method")
        print("16) islower method")
        print("17) isnumeric method")
        print("18) isprintable method")
        print("19) isspace method")
        print("20) istitle method")
        print("21) isupper method")
        print("22) join method")
        print("23) lower method")
        print("24) lstrip method")
        print("25) partition method")
        print("26) replace method")
        print("27) rfind method")
        print("28) rindex method")
        print("29) rjust method")
        print("30) rpartition method")
        print("31) rsplit method")
        print("32) rstrip method")
        print("33) split method")
        print("34) startswith method")
        print("35) strip method")
        print("36) swapcase method")
        print("37) title method")
        print("38) upper method")
        print("39) zfill method")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen the capitalize() method")
            capst = ("capitalize() Method\nThe capitalize() method returns a string where the first character is upper case.\nCode:\ntext = ”hello there.”\nx = text.capitalize()\nprint(x)")
            print(capst)
            text = "hello there."
            x = text.capitalize()
            print(out)
            print(x)
        elif selection ==2:
            print("You have chosen the casefold() method")
            casest = ("casefold() Method\nThe casefold() method returns a string where all the characters are lower case.\nCode:\ntext = ”Hello There.”\nx = text.casefold()\nprint(x)")
            print(casest)
            text = "Hello There."
            x = text.casefold()
            print(out)
            print(x)
        elif selection ==3:
            print("You have chosen the center() method")
            centerst1=("center() Method\nThe center() method will center align the string, using a specified character (space is default) as the fill character.\nCode:\nDefault\ntext = ”CMMMS”\nx = text.center(15)\nprint(x)")
            print(centerst1)
            text = "CMMMS"
            x = text.center(15)
            print(out)
            print(x)
            
            centerst2=("Character as Padding\nCode:\ntext = ”CMMMS”\ny = text.center(15, “*”)\nprint(y)")
            print(centerst2)
            text = "CMMMS"
            y = text.center(15, "*")
            print(out)
            print(y)
        elif selection ==4:
            print("You have chosen the count() method")
            countst=("count() Method\nThe count() method returns the number of times a specified value appears in the string.\nCode:\ntext = ”Hello. Hello there, we are CMMMS.”\nx = text.count(“Hello”)\nprint(x)")
            print(countst)
            text = "Hello. Hello there, we are CMMMS."
            x = text.count("Hello")
            print(out)
            print(x)
        elif selection ==5:
            print("You have chosen the encode() method")
            encodest1=("encode() Method\nThe encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.\nCode:\ntext = “We are CMMMS.”\nx = text.encode()\nprint(x)")
            print(encodest1)
            text = "We are CMMMS."
            x = text.encode()
            print(out)
            print(x)
            
            encodest2=("Backslash Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""backslashreplace""))")
            print(encodest2)
            print(out)
            print(text.encode(encoding = "ascii", \
                              errors = "backslashreplace"))
            
            encodest3=("Ignore\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""ignore""))")
            print(encodest3)
            print(out)
            print(text.encode(encoding = "ascii", \
                              errors = "ignore"))
            
            encodest4=("Name Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""namereplace""))")
            print(encodest4)
            print(out)
            print(text.encode(encoding = "ascii", \
                              errors = "namereplace"))
            encodest5=("Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""replace""))")
            print(encodest5)
            print(out)
            print(text.encode(encoding = "ascii", \
                              errors = "replace"))
            
            encodest6=("XML Character Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""xmlcharrefreplace""))")
            print(encodest6)
            print(out)
            print(text.encode(encoding = "ascii", \
                              errors = "xmlcharrefreplace"))
            
            encodest7=("Strict\nCode:\nprint(text.encode(encoding = ""utf-8"", \ \n                  errors = ""utf-8""))")
            print(encodest7)
            print(out)
            print(text.encode(encoding = "utf-8", \
                              errors = "strict"))
        elif selection ==6:
            print("You have chosen the endswith() method")
            endst=("endswith() Method\nThe endswith() method returns True if the string ends with the specified value, otherwise False.\nCode:\ntext = “Hello There.”\nx = text.endswith(“.”)\nprint(x)")
            print(endst)
            text = "Hello There."
            x = text.endswith(".")
            print(out)
            print(x)
        elif selection ==7:
            print("You have chosen the expandtabs() method")
            expst1=("expandtabs() Method The expandtabs() method sets the tab size to the specified number of whitespaces.\nDefault\nCode:\ntext = “H\te\tl\tl\to“\nprint(text)")
            print(expst1)
            text = "H\te\tl\tl\to"
            print(out)
            print(text)
            
            expst2=("Sample\nCode:\nprint(text.expandtabs(5))")
            print(expst2)
            print(out)
            print(text.expandtabs(5))
        elif selection ==8:
            print("You have chosen the kind() method")
            findst=("find() Method\nThe find() method finds the first occurrence of the specified value.\nCode:\ntext = ”Hello there.”\nx = text.find(”there”)\nprint(x)")
            print(findst)
            text = "Hello there."
            x = text.find("there")
            print(out)
            print(x)
        elif selection ==9:
            print("You have chosen the format() method")
            formst=("format() Method\nThe format() method formats the specified value(s) and insert them inside the string's placeholder.\nCode:\ntext1 = ""We are {name}, we consist of {no} members"". format \ \n        (name = ""CMMMS"", no = 5)\ntext2 = ""We are {0}, we consist of {1} members"". format(""CMMMS"", 5)\ntext3 = ""We are {}, we consist of {} members"". format(""CMMMS"", 5)\nprint(text1)\nprint(text2)\nprint(text3)")
            print(formst)
            text1 = "We are {name}, we consist of {no} members". format \
                    (name = "CMMMS", no = 5)
            text2 = "We are {0}, we consist of {1} members". format("CMMMS", 5)
            text3 = "We are {}, we consist of {} members". format("CMMMS", 5)
            print(out)
            print(text1)
            print(text2)
            print(text3)
        elif selection ==10:
            print("You have chosen the index() method")
            indst=("index() Method\nThe index() method finds the first occurrence of the specified value.\nCode:\ntext = ”Hello there, we are CMMMS.”\nx = text.index(""we"")\nprint(x)")
            print(indst)
            text = "Hello there, we are CMMMS."
            x = text.index("we")
            print(out)
            print(x)
        elif selection ==11:
            print("You have chosen the isalnum() method")
            isast=("isalnum() Method\nThe isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).\nCode:\ntext = ”CMMMS”\nx = text.isalnum()\nprint(x)")
            print(isast)
            text = "CMMMS"
            x = text.isalnum()
            print(out)
            print(x)
        elif selection ==12:
            print("You have chosen the isalpha() method")
            alphast = ("isalpha() Method\nThe isalpha() method returns True if all the characters are alphabet letters (a-z).\nCode:\ntext = ”CMMMS”\nx = text.isalpha()\nprint(x)")
            print(alphast)
            text = "CMMMS"
            x = text.isalpha()
            print(out)
            print(x)
        elif selection ==13:
            print("You have chosen the isdecimal() method")
            decst=("isdecimal() Method\nThe isdecimal() method returns True if all the characters are decimals (0-9). This method is used on unicode objects.\nCode:\ntext1 = ""\u0030""\ntext2 = ""\u0047""\nx = text1.isdecimal()\ny = text1.isdecimal()\nprint(x)\nprint(y)")
            print(decst)
            text1 = "\u0030"
            text2 = "\u0047"
            x = text1.isdecimal()
            y = text1.isdecimal()
            print(out)
            print(x)
            print(y)
        elif selection ==14:
            print("You have chosen the isdigit() method")
            isdig=("isdigit() Method\n The idsigit() method returns True if all the characters are digits, otherwise False. Exponents like ², are also considered to be digit. \nCode:\ntext = “19”\nx = text.isdigit()\nprint(x)")
            print(isdig)
            text = "19"
            x = text.isdigit()
            print(out)
            print(x)
        elif selection ==15:
            print("You have chosen the isidentifier() method")
            isid=("isidentifier() Method\n The ididentifier() method returns True if the string is a valid identifier, otherwise False. \n A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces. \nCode:\ntext =""Sample""\nx = text.isidentifier()\nprint(x)")
            print(isid)
            text ="Sample"
            x = text.isidentifier()
            print(out)
            print(x) 
        elif selection ==16:
            print("You have chosen the islower() method")
            islo=("islower() Method\n The islower() method returns True if all the characters are in lower case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.\nCode:\ntext=""hello there""\nx = text.islower()\nprint(x)")
            print(islo)
            text="hello there"
            x = text.islower()
            print(out)
            print(x)
        elif selection ==17:
            print("You have chosen the isnumeric() method")
            isnu=("isnumeric() Method\n The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False. Exponents, like ² and ¾ are also considered to be numeric values. \nCode:\ntext= ""54321""\nx = text.isnumeric()\nprint(x)")
            print(isnu)
            text= "54321"
            x = text.isnumeric()
            print(out)
            print(x)
        elif selection ==18:
            print("You have chosen the isprintable() method")
            ispi=("isprintable() Method\n The isprintable() method returns True if all the characters are printable, otherwise False. Example of none printable character can be carriage return and line feed.\nCode:\ntext = ""hello! \n there""\nx = text.isprintable()\nprint(x)")
            print(ispi)
            text = "hello! \n there"
            x = text.isprintable()
            print(out)
            print(x)
        elif selection ==19:
            print("You have chosen the isspace() method")
            space=("isspace() Method\nThe isspace() method returns True if all the characters in a string are whitespaces, otherwise False\nCode:\ntext = ""        ""\nx = text.isspace()\nprint(x)")
            print(space)
            text = "        "
            x = text.isspace()
            print(out)
            print(x)
        elif selection ==20:
            print("You have chosen the istitle() method")
            isti=("istitle() Method\n The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False. Symbols and numbers are ignored. \nCode:\ntext = ""covid 19""\nx = text.istitle()\nprint(x)")
            print(isti)
            text = "covid 19"
            x = text.istitle()
            print(out)
            print(x)
        elif selection ==21:
            print("You have chosen the isupper() method")
            isupe=("isupper() Method\n The isupper() method returns True if all the characters are in upper case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters. \nCode:\ntext = ""HELLO THERE""\nx = text.isupper()\nprint(x)")
            print(isupe)
            text = "HELLO THERE"
            x = text.isupper()
            print(out)
            print(x)
        elif selection ==22:
            print("You have chosen the join() method")
            joi=("join() Method\n The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.\nCode:\nelem = (in1, in2, in3, in4, in5)\nx = ""*"".join(elem)\nprint(x)")
            print(joi)
            elem = (in1, in2, in3, in4, in5)
            x = "*".join(elem)
            print(out)
            print(x)
        elif selection ==23:
            print("You have chosen the lower() method")
            low=("lower() Method\n The lower() method returns a string where all characters are lowercase. Symbols and Numbers are ignored.\nCode:\ntext = ""hello there""\nx = text.lower()\nprint(x)")
            print(low)
            text = "hello there"
            x = text.lower()
            print(out)
            print(x)
        elif selection ==24:
            print("You have chosen the lstrip() method")
            lstr=("lstrip() Method\n The lstrip() method removes any leading characters (space is the default leading character to remove)\nCode:\ntext ="" banana  ""\nx= text.lstrip()\nprint(""of all fruits"", x ,""is my favorite!"" )")
            print(lstr)
            text = "        banana  "
            x= text.lstrip()
            print(out)
            print("of all fruits", x ,"is my favorite!" )
        elif selection ==25:
            print("You have chosen the partition() method")
            part=("partition() Method\n The partition() method searches for a specified string, and splits the string into a tuple containing three elements.\nThe first element contains the part before the specified string.\nThe second element contains the specified string.\nThe third element contains the part after the string.\nCode:\ntext = ""The pandemic virus was gone""\nx = text.partition(""virus"")\nprint(x)")
            print(part)
            text = "The pandemic virus was gone"
            x = text.partition("virus")
            print(out)
            print(x)
        elif selection ==26:
            print("You have chosen the replace() method")
            repl=("replace() Method\n The replace() method replaces a specified phrase with another specified phrase.\nCode:\ntext = ""I want to eat apples and pineapples""\nx = text.replace(""apples"",""grapes"")\nprint(x)")
            print(repl)
            text = "I want to eat apples and pineapples"
            x = text.replace("apples","grapes")
            print(out)
            print(x)
        elif selection ==27:
            print("You have chosen the rfind() method")
            rfin=("rfind() Method\n The rfind() method finds the last occurrence of the specified value. The rfind() method returns -1 if the value is not found. The rfind() method is almost the same as the rindex() method.\nCode:\ntext = ""Hello there""\nx = text.rfind(""e"")\nprint(x)")
            print(rfin)
            text = "Hello there"
            x = text.rfind("e")
            print(out)
            print(x)
        elif selection ==28:
            print("You have chosen the rindex() method")
            rind=("rindex() Method\n The rindex() method finds the last occurrence of the specified value. It raises an exception if the value is not found. The rindex() method is almost the same as the rfind() method.\nCode:\ntext=""Hello world""\nx = text.rindex(""o"")\nprint(x)")
            print(rind)
            text="Hello world"
            x = text.rindex("o")
            print(out)
            print(x)
        elif selection ==29:
            print("You have chosen the rjust() method")
            rju=("rjust() Method\n The rjust() method will right align the string, using a specified character (space is default) as the fill character.\nCode:\ntext =""Hello there""\nx = text.rjust(20)\nprint(x, ""you are welcome"")")
            print(rju)
            text ="Hello there"
            x = text.rjust(20)
            print(out)
            print(x, "you are welcome")
        elif selection ==30:
            print("You have chosen the rpartition() method")
            rpar=("rpartition() Method\n The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.\nThe first element contains the part before the specified string.\nThe second element contains the specified string.\nThe third element contains the part after the string.\nCode:\ntext = ""The pandemic virus was gone, Thank God""\nx = text.rpartition(""was"")\nprint(x)")
            print(rpar)
            text = "The pandemic virus was gone, Thank God"
            x = text.rpartition("was")
            print(out)
            print(x)
        elif selection ==31:
            print("You have chosen the rsplit() method")
            rsp=("rsplit() Method\n The rsplit() method splits a string into a list, starting from the right. If no ""max"" is specified, this method will return the same as the split() method.\nCode:\nfruits = ""apple, banana, cherry""\nx = fruits.rsplit("", "")\nprint(x)")
            print(rsp)
            fruits = "apple, banana, cherry"
            x = fruits.rsplit(", ")
            print(out)
            print(x)
        elif selection ==32:
            print("You have chosen the rstrip() method")
            rstr=("rstrip() Method\n The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.\nCode:\ntext=""     banana     ""\nx= text.rstrip()\nprint(""of all fruit"",x , ""is my favorite")
            print(rstr)
            text="     banana     "
            x= text.rstrip()
            print(out)
            print("of all fruit",x , "is my favorite")
        elif selection ==33:
            print("You have chosen the split() method")
            spl=("split() Method\n The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.\nCode:\ntext=""hello there""\nx=text.split()\nprint(x)")
            print(spl)
            text="hello there"
            x=text.split()
            print(out)
            print(x)
        elif selection ==34:
            print("You have chosen the startswith() method")
            staw=("startswith() Method\n The startswith() method returns True if the string starts with the specified value, otherwise False.\nCode:\ntext=""hello there""\nx = text.startswith(""hello"")\nprint(x)")
            print(staw)
            text="hello there"
            x = text.startswith("hello")
            print(out)
            print(x)
        elif selection ==35:
            print("You have chosen the strip() method")
            stri=("strip() Method\n The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).\nCode:\ntext=""     banana     ""\nx = text.strip(""hello"")\nprint(""of all fruits"",x , ""is my favorite"")")
            print(stri)
            text="     banana     "
            x = text.strip("hello")
            print(out)
            print("of all fruits",x , "is my favorite")            
        elif selection ==36:
            print("You have chosen the swapcase() method")
            swac=("swapcase() Method\nThe swapcase() method returns a string where all the upper case letters are lower case and vice versa.\nCode:\ntext = ""hELLO tHERE""\nx = text.swapcase()\nprint(x)")
            print(swac)
            text = "hELLO tHERE"
            x = text.swapcase()
            print(out)
            print(x)
        elif selection ==37:
            print("You have chosen the title() method")
            tite=("title() Method\n The title() method returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after that will be converted to upper case.\nCode:\ntext=""hELLO tHere""\nx=text.title()\nprint(x)")
            print(tite)
            text="hELLO tHere"
            x=text.title()
            print(out)
            print(x)
        elif selection ==38:
            print("You have chosen the upper() method")
            uppr=("upper() Method\n The upper() method returns a string where all characters are in upper case. Symbols and Numbers are ignored.\nCode:\ntext=""hello there""\nx=text.upper()\nprint(x)")
            print(uppr)
            text="hello there"
            x=text.upper()
            print(out)
            print(x)
        elif selection ==39:
            print("You have chosen the zfill() method")
            zfil("zfill() Method\n The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length. If the value of the len parameter is less than the length of the string, no filling is done.\nCode:\ntext= ""50""\nx = text.zfill(10)\nprint(x)")
            print(zfil)
            text= "50"
            x = text.zfill(10)
            print(out)
            print(x)
    elif choice ==2:
         capst = ("capitalize() Method\nThe capitalize() method returns a string where the first character is upper case.\nCode:\ntext = ”hello there.”\nx = text.capitalize()\nprint(x)")
         print(capst)
         text = "hello there."
         x = text.capitalize()
         print(out)
         print(x)
         print("\n")
         
         casest = ("casefold() Method\nThe casefold() method returns a string where all the characters are lower case.\nCode:\ntext = ”Hello There.”\nx = text.casefold()\nprint(x)")
         print(casest)
         text = "Hello There."
         x = text.casefold()
         print(out)
         print(x)
         print("\n")
         
         centerst1=("center() Method\nThe center() method will center align the string, using a specified character (space is default) as the fill character.\nCode:\nDefault\ntext = ”CMMMS”\nx = text.center(15)\nprint(x)")
         print(centerst1)
         text = "CMMMS"
         x = text.center(15)
         print(out)
         print(x)         
         centerst2=("Character as Padding\nCode:\ntext = ”CMMMS”\ny = text.center(15, “*”)\nprint(y)")
         print(centerst2)
         text = "CMMMS"
         y = text.center(15, "*")
         print(out)
         print(y)
         print("\n")
         
         countst=("count() Method\nThe count() method returns the number of times a specified value appears in the string.\nCode:\ntext = ”Hello. Hello there, we are CMMMS.”\nx = text.count(“Hello”)\nprint(x)")
         print(countst)
         text = "Hello. Hello there, we are CMMMS."
         x = text.count("Hello")
         print(out)
         print(x)
         print("\n")
         
         encodest1=("encode() Method\nThe encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.\nCode:\ntext = “We are CMMMS.”\nx = text.encode()\nprint(x)")
         print(encodest1)
         text = "We are CMMMS."
         x = text.encode()
         print(out)
         print(x)
         
         encodest2=("Backslash Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""backslashreplace""))")
         print(encodest2)
         print(out)
         print(text.encode(encoding = "ascii", \
                           errors = "backslashreplace"))
         
         encodest3=("Ignore\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""ignore""))")
         print(encodest3)
         print(out)
         print(text.encode(encoding = "ascii", \
                           errors = "ignore"))
         encodest4=("Name Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""namereplace""))")
         print(encodest4)
         print(out)
         print(text.encode(encoding = "ascii", \
                           errors = "namereplace"))
         encodest5=("Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""replace""))")
         print(encodest5)
         print(out)
         print(text.encode(encoding = "ascii", \
                           errors = "replace"))
         
         encodest6=("XML Character Replace\nCode:\nprint(text.encode(encoding = ""ascii"", \ \n                  errors = ""xmlcharrefreplace""))")
         print(encodest6)
         print(out)
         print(text.encode(encoding = "ascii", \
                           errors = "xmlcharrefreplace"))
         
         encodest7=("Strict\nCode:\nprint(text.encode(encoding = ""utf-8"", \ \n                  errors = ""utf-8""))")
         print(encodest7)
         print(out)
         print(text.encode(encoding = "utf-8", \
                           errors = "strict"))
         print("\n")
         endst=("endswith() Method\nThe endswith() method returns True if the string ends with the specified value, otherwise False.\nCode:\ntext = “Hello There.”\nx = text.endswith(“.”)\nprint(x)")
         print(endst)
         text = "Hello There."
         x = text.endswith(".")
         print(out)
         print(x)
         print("\n")
         
         expst1=("expandtabs() Method The expandtabs() method sets the tab size to the specified number of whitespaces.\nDefault\nCode:\ntext = “H\te\tl\tl\to“\nprint(text)")
         print(expst1)
         text = "H\te\tl\tl\to"
         print(out)
         print(text)
         expst2=("Sample\nCode:\nprint(text.expandtabs(5))")
         print(expst2)
         print(out)
         print(text.expandtabs(5))
         print("You have chosen the kind() method")
         findst=("find() Method\nThe find() method finds the first occurrence of the specified value.\nCode:\ntext = ”Hello there.”\nx = text.find(”there”)\nprint(x)")
         print(findst)
         text = "Hello there."
         x = text.find("there")
         print(out)
         print(x)
         print("\n")
         
         formst=("format() Method\nThe format() method formats the specified value(s) and insert them inside the string's placeholder.\nCode:\ntext1 = ""We are {name}, we consist of {no} members"". format \ \n        (name = ""CMMMS"", no = 5)\ntext2 = ""We are {0}, we consist of {1} members"". format(""CMMMS"", 5)\ntext3 = ""We are {}, we consist of {} members"". format(""CMMMS"", 5)\nprint(text1)\nprint(text2)\nprint(text3)")
         print(formst)
         text1 = "We are {name}, we consist of {no} members". format \
                 (name = "CMMMS", no = 5)
         text2 = "We are {0}, we consist of {1} members". format("CMMMS", 5)
         text3 = "We are {}, we consist of {} members". format("CMMMS", 5)
         print(out)
         print(text1)
         print(text2)
         print(text3)
         print("\n")
         
         indst=("index() Method\nThe index() method finds the first occurrence of the specified value.\nCode:\ntext = ”Hello there, we are CMMMS.”\nx = text.index(""we"")\nprint(x)")
         print(indst)
         text = "Hello there, we are CMMMS."
         x = text.index("we")
         print(out)
         print(x)
         print("\n")
         
         isast=("isalnum() Method\nThe isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).\nCode:\ntext = ”CMMMS”\nx = text.isalnum()\nprint(x)")
         print(isast)
         text = "CMMMS"
         x = text.isalnum()
         print(out)
         print(x)
         print("\n")
         
         alphast = ("isalpha() Method\nThe isalpha() method returns True if all the characters are alphabet letters (a-z).\nCode:\ntext = ”CMMMS”\nx = text.isalpha()\nprint(x)")
         print(alphast)
         text = "CMMMS"
         x = text.isalpha()
         print(out)
         print(x)
         print("\n")
         
         decst=("isdecimal() Method\nThe isdecimal() method returns True if all the characters are decimals (0-9). This method is used on unicode objects.\nCode:\ntext1 = ""\u0030""\ntext2 = ""\u0047""\nx = text1.isdecimal()\ny = text1.isdecimal()\nprint(x)\nprint(y)")
         print(decst)
         text1 = "\u0030"
         text2 = "\u0047"
         x = text1.isdecimal()
         y = text1.isdecimal()
         print(out)
         print(x)
         print(y)
         print("\n")
         
         isdig=("isdigit() Method\nThe idsigit() method returns True if all the characters are digits, otherwise False. Exponents like ², are also considered to be digit. \nCode:\ntext = “19”\nx = text.isdigit()\nprint(x)")
         print(isdig)
         text = "19"
         x = text.isdigit()
         print(out)
         print(x)
         print("\n")
         
         isid=("isidentifier() Method\nThe ididentifier() method returns True if the string is a valid identifier, otherwise False. \n A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces. \nCode:\ntext =""Sample""\nx = text.isidentifier()\nprint(x)")
         print(isid)
         text ="Sample"
         x = text.isidentifier()
         print(out)
         print(x)
         print("\n")
         
         islo=("islower() Method\nThe islower() method returns True if all the characters are in lower case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters.\nCode:\ntext=""hello there""\nx = text.islower()\nprint(x)")
         print(islo)
         text="hello there"
         x = text.islower()
         print(out)
         print(x)
         print("\n")
         
         isnu=("isnumeric() Method\nThe isnumeric() method returns True if all the characters are numeric (0-9), otherwise False. Exponents, like ² and ¾ are also considered to be numeric values. \nCode:\ntext= ""54321""\nx = text.isnumeric()\nprint(x)")
         print(isnu)
         text= "54321"
         x = text.isnumeric()
         print(out)
         print(x)
         print("\n")
         
         ispi=("isprintable() Method\nThe isprintable() method returns True if all the characters are printable, otherwise False. Example of none printable character can be carriage return and line feed.\nCode:\ntext = ""hello! \n there""\nx = text.isprintable()\nprint(x)")
         print(ispi)
         text = "hello! \n there"
         x = text.isprintable()
         print(out)
         print(x)
         print("\n")
         
         space=("isspace() Method\nThe isspace() method returns True if all the characters in a string are whitespaces, otherwise False\nCode:\ntext = ""        ""\nx = text.isspace()\nprint(x)")
         print(space)
         text = "        "
         x = text.isspace()
         print(out)
         print(x)
         print("\n")
         
         isti=("istitle() Method\nThe istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False. Symbols and numbers are ignored. \nCode:\ntext = ""covid 19""\nx = text.istitle()\nprint(x)")
         print(isti)
         text = "covid 19"
         x = text.istitle()
         print(out)
         print(x)
         print("\n")
         
         isupe=("isupper() Method\nThe isupper() method returns True if all the characters are in upper case, otherwise False. Numbers, symbols and spaces are not checked, only alphabet characters. \nCode:\ntext = ""HELLO THERE""\nx = text.isupper()\nprint(x)")
         print(isupe)
         text = "HELLO THERE"
         x = text.isupper()
         print(out)
         print(x)
         print("\n")
         
         joi=("join() Method\nThe join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.\nCode:\nelem = (in1, in2, in3, in4, in5)\nx = ""*"".join(elem)\nprint(x)")
         print(joi)
         elem = (in1, in2, in3, in4, in5)
         x = "*".join(elem)
         print(out)
         print(x)
         print("\n")
         
         low=("lower() Method\nThe lower() method returns a string where all characters are lowercase. Symbols and Numbers are ignored.\nCode:\ntext = ""hello there""\nx = text.lower()\nprint(x)")
         print(low)
         text = "hello there"
         x = text.lower()
         print(out)
         print(x)
         print("\n")
         
         lstr=("lstrip() Method\nThe lstrip() method removes any leading characters (space is the default leading character to remove)\nCode:\ntext ="" banana  ""\nx= text.lstrip()\nprint(""of all fruits"", x ,""is my favorite!"" )")
         print(lstr)
         text = "        banana  "
         x= text.lstrip()
         print(out)
         print("of all fruits", x ,"is my favorite!" )
         print("\n")
         
         part=("partition() Method\nThe partition() method searches for a specified string, and splits the string into a tuple containing three elements.\nThe first element contains the part before the specified string.\nThe second element contains the specified string.\nThe third element contains the part after the string.\nCode:\ntext = ""The pandemic virus was gone""\nx = text.partition(""virus"")\nprint(x)")
         print(part)
         text = "The pandemic virus was gone"
         x = text.partition("virus")
         print(out)
         print(x)
         print("\n")
         
         repl=("replace() Method\nThe replace() method replaces a specified phrase with another specified phrase.\nCode:\ntext = ""I want to eat apples and pineapples""\nx = text.replace(""apples"",""grapes"")\nprint(x)")
         print(repl)
         text = "I want to eat apples and pineapples"
         x = text.replace("apples","grapes")
         print(out)
         print(x)
         print("\n")
         
         rfin=("rfind() Method\nThe rfind() method finds the last occurrence of the specified value. The rfind() method returns -1 if the value is not found. The rfind() method is almost the same as the rindex() method.\nCode:\ntext = ""Hello there""\nx = text.rfind(""e"")\nprint(x)")
         print(rfin)
         text = "Hello there"
         x = text.rfind("e")
         print(out)
         print(x)
         print("\n")
            
         rind=("rindex() Method\nThe rindex() method finds the last occurrence of the specified value. It raises an exception if the value is not found. The rindex() method is almost the same as the rfind() method.\nCode:\ntext=""Hello world""\nx = text.rindex(""o"")\nprint(x)")
         print(rind)
         text="Hello world"
         x = text.rindex("o")
         print(out)
         print(x)
         print("\n")
        
         rju=("rjust() Method\nThe rjust() method will right align the string, using a specified character (space is default) as the fill character.\nCode:\ntext =""Hello there""\nx = text.rjust(20)\nprint(x, ""you are welcome"")")
         print(rju)
         text ="Hello there"
         x = text.rjust(20)
         print(out)
         print(x, "you are welcome")
         print("\n")
        
         rpar=("rpartition() Method\nThe rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.\nThe first element contains the part before the specified string.\nThe second element contains the specified string.\nThe third element contains the part after the string.\nCode:\ntext = ""The pandemic virus was gone, Thank God""\nx = text.rpartition(""was"")\nprint(x)")
         print(rpar)
         text = "The pandemic virus was gone, Thank God"
         x = text.rpartition("was")
         print(out)
         print(x)
         print("\n")
        
         rsp=("rsplit() Method\nThe rsplit() method splits a string into a list, starting from the right. If no ""max"" is specified, this method will return the same as the split() method.\nCode:\nfruits = ""apple, banana, cherry""\nx = fruits.rsplit("", "")\nprint(x)")
         print(rsp)
         fruits = "apple, banana, cherry"
         x = fruits.rsplit(", ")
         print(out)
         print(x)
         print("\n")
        
         rstr=("rstrip() Method\nThe rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.\nCode:\ntext=""     banana     ""\nx= text.rstrip()\nprint(""of all fruit"",x , ""is my favorite")
         print(rstr)
         text="     banana     "
         x= text.rstrip()
         print(out)
         print("of all fruit",x , "is my favorite")
         print("\n")
        
         spl=("split() Method\nThe split() method splits a string into a list. You can specify the separator, default separator is any whitespace.\nCode:\ntext=""hello there""\nx=text.split()\nprint(x)")
         print(spl)
         text="hello there"
         x=text.split()
         print(out)
         print(x)
         print("\n")
        
         staw=("startswith() Method\nThe startswith() method returns True if the string starts with the specified value, otherwise False.\nCode:\ntext=""hello there""\nx = text.startswith(""hello"")\nprint(x)")
         print(staw)
         text="hello there"
         x = text.startswith("hello")
         print(out)
         print(x)
         print("\n")
        
         stri=("strip() Method\nThe strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).\nCode:\ntext=""     banana     ""\nx = text.strip(""hello"")\nprint(""of all fruits"",x , ""is my favorite"")")
         print(stri)
         text="     banana     "
         x = text.strip("hello")
         print(out)
         print("of all fruits",x , "is my favorite")
         print("\n")
        
         swac=("swapcase() Method\nThe swapcase() method returns a string where all the upper case letters are lower case and vice versa.\nCode:\ntext = ""hELLO tHERE""\nx = text.swapcase()\nprint(x)")
         print(swac)
         text = "hELLO tHERE"
         x = text.swapcase()
         print(out)
         print(x)
         print("\n")
        
         tite=("title() Method\nThe title() method returns a string where the first character in every word is upper case. Like a header, or a title. If the word contains a number or a symbol, the first letter after that will be converted to upper case.\nCode:\ntext=""hELLO tHere""\nx=text.title()\nprint(x)")
         print(tite)
         text="hELLO tHere"
         x=text.title()
         print(out)
         print(x)
         print("\n")
        
         uppr=("upper() Method\nThe upper() method returns a string where all characters are in upper case. Symbols and Numbers are ignored.\nCode:\ntext=""hello there""\nx=text.upper()\nprint(x)")
         print(uppr)
         text="hello there"
         x=text.upper()
         print(out)
         print(x)
         print("\n")
        
         zfil=("zfill() Method\nThe zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length. If the value of the len parameter is less than the length of the string, no filling is done.\nCode:\ntext= ""50""\nx = text.zfill(10)\nprint(x)")
         print(zfil)
         text= "50"
         x = text.zfill(10)
         print(out)
         print(x)
         print("\n")
#built-in method      
elif selection ==6:
    print("You have selected Python Object: Built-in Functions")
    print("Please choose on how you want to search method")
    print("1) Select Buiilt-in function ")
    print("2) Select all Built-in function")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) abs")
        print("2) all")
        print("3) any")
        print("4) ascii")
        print("5) bin")
        print("6) bool")
        print("7) bytearray")
        print("8) bytes")
        print("9) callable")
        print("10) chr")
        print("11) compile")
        print("12) complex")
        print("13) delattr")
        print("14) dict")
        print("15) dir")
        print("16) divmod")
        print("17) enumerate")
        print("18) eval")
        print("19) exec")
        print("20) filter")
        print("21) float")
        print("22) format")
        print("23) frozenset")
        print("24) getattr")
        print("25) globals")
        print("26) hasattr")
        print("27) hex")
        print("28) id")
        print("29) input")
        print("30) int")
        print("31) isintance")
        print("32) issubclass")
        print("33) iter")
        print("34) len")
        print("35) list")
        print("36) locals")
        print("37) map")
        print("38) max")
        print("39) memoryview")
        print("40) mean")
        print("41) next")
        print("42) object")
        print("43) oct")
        print("44) open")
        print("45) ord")
        print("46) pow")
        print("47) print")
        print("48) range")
        print("49) reversed")
        print("50) round")
        print("51) set")
        print("52) setattr")
        print("53) slice")
        print("54) sorted")
        print("55) str")
        print("56) sum")
        print("57) super")
        print("58) tupple")
        print("59) type")
        print("60) vars")
        print("61) zip")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen the abs() method")
            abs1=("abs() Function\nThe abs() function returns the absolute value of the specified number.")
            print(abs1)
        elif selection ==2:
            print("You have chosen the all() method")
            all1=("all() Function\nThe all() function returns True if all items in an iterable are true, otherwise it returns False.\nIf the iterable object is empty, the all() function also returns True.")
            print(all1)
        elif selection ==3:
            print("You have chosen the any() method")
            any1=("any() Function\nThe any() function returns True if any item in an iterable are true, otherwise it returns False.\nIf the iterable object is empty, the any() function will return False.")
            print(any1)
        elif selection ==4:
            print("You have chosen the ascii() method")
            ascii1=("ascii() Function\nThe ascii()function returns a readable version of any object (Strings, Tuples, Lists, etc).\nIt will replace any non-ascii characters with escape characters.")
            print(ascii1)
        elif selection ==5:
            print("You have chosen the bin() method")
            bin1=("bin() Function\nThe bin() function returns the binary version of a specified integer.\nThe result will always start with the prefix 0b.")
            print(bin1)
        elif selection ==6:
            print("You have chosen the bool() method")
            bool1=("bool() Function\nThe bool() function returns the boolean value of a specified object.")
            print(bool1)
        elif selection ==7:
            print("You have chosen the bytearray() method")
            byteaaray=("byteaaray() Function\nThe byteaaray() function returns a bytearray object. It can convert objects into bytearray objects,\nor create empty bytearray object of the specified size.")
            print(byteaaray)
        elif selection ==8:
            print("You have chosen the bytes() method")
            bytes1=("bytes() Function\nThe bytes() function returns a bytes object. It can convert objects into\nbytes objects, or create empty bytes object of the specified size.")
            print(bytes1)
        elif selection ==9:
            print("You have chosen the callable() method")
            callable1=("callable() Function\nThe callable() function returns True if the specified object is callable, otherwise it returns False.")
            print(callable1)
        elif selection ==10:
            print("You have chosen the chr() method")
            chr1=("chr() Function\nThe chr() function returns the character that represents the specified unicode.")
            print(chr1)
        elif selection ==11:
            print("You have chosen the compile() method")
            compile1=("compile() Function\nThe compile() function returns the specified source as a code object, ready to be executed.")
            print(compile1)
        elif selection ==12:
            print("You have chosen the complex() method")
            complex1=("complex() Function\nThe complex() function returns a complex number by specifying\na real number and an imaginary number.")
            print(complex1)
        elif selection ==13:
            print("You have chosen the delattr() method")
            delattr1=("delattr() Function\nThe delattr() function will delete the specified attribute from the specified object.")
            print(delattr1)
        elif selection ==14:
            print("You have chosen the dict() method")
            dict1=("dict() Function\nThe dict() function creates a dictionary. A dictionary is a collection which is unordered, changeable and indexed.")
            print(dict1)
        elif selection ==15:
            print("You have chosen the dir() method")
            dir1=("dir() Function\nThe dir() function returns all properties and methods of the specified object,\nwithout the values. This function will return all the properties and methods, even built-in\nproperties which are default for all object.")
            print(dir1)
        elif selection ==16:
            print("You have chosen the divmod() method")
            divmod1=("divmod() Function\nThe divmod() function returns a tuple containing the quotient and\nthe remainder when argument1 (divident) is divided by argument2 (divisor).")
            print(divmod1)
        elif selection ==17:
            print("You have chosen the enumerate() method")
            enumerate1=("enumerate() Function\nThe enumerate() function takes a collection (e.g. a tuple)\nand returns it as an enumerate object. It adds a counter as the key of the enumerate object.")
            print(enumerate1)
        elif selection ==18:
            print("You have chosen the eval() method")
            eval1=("eval() Function\nThe eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.")
            print(eval1)
        elif selection ==19:
            print("You have chosen the exec() method")
            exec1=("exec() Function\nThe exec() function executes the specified Python code. The exec() function\naccepts large blocks of code, unlike the eval() function which only accepts a single expression.")
            print(exec1)
        elif selection ==20:
            print("You have chosen the filter() method")
            filter1=("filter() Function\nThe filter() function returns an iterator were the items are filtered through\na function to test if the item is accepted or not.")
            print(filter1)
        elif selection ==21:
            print("You have chosen the float() method")
            float1=("float() Function\nThe float() function converts the specified value into a floating point number. ")
            print(float1)
        elif selection ==22:
            print("You have chosen the format() method")
            format1=("format() Function\nThe format() function formats a specified value into a specified format.")
            print(format1)
        elif selection ==23:
            print("You have chosen the frozenset() method")
            frozenset1=("frozenset() Function\nThe frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).")
            print(frozenset1)
        elif selection ==24:
            print("You have chosen the getattr() method")
            getattr1=("getattr() Function\nThe getattr() function returns the value of the specified attribute from the specified object.")
            print(getattr1)
        elif selection ==25:
            print("You have chosen the globals() method")
            globals1=("globals() Function\nThe globals() function returns the global symbol table as a dictionary. A symbol table contains necessary information about the current program.")
            print(globals1)
        elif selection ==26:
            print("You have chosen the hasattr() method")
            hasattr1=("hasattr() Function\nThe hasattr() function function returns True if the specified object has the specified attribute, otherwise False.")
            print(hasattr1)
        elif selection ==27:
            print("You have chosen the hex() method")
            hex1=("hex() Function\nThe hex() function converts the specified number into a hexadecimal value. The returned string always starts with the prefix 0x.")
            print(hex1)
        elif selection ==28:
            print("You have chosen the id() method")            
            id1=("id() Function\nThe id() function returns a unique id for the specified object. All objects in Python has its own unique id. The id is assigned to the object when it is created. \n The id is the object's memory address, and will be different for each time you run the program. \n (except for some object that has a constant unique id, like integers from -5 to 256). ")
            print(id1)
        elif selection ==29:
            print("You have chosen the input() method")
            input1=("input() Function\nThe input() function allows user input.")
            print(input)
        elif selection ==30:
            print("You have chosen the int() method")
            int1=("int() Function\nThe int() function converts the specified value into an integer number.")
            print(int1)
        elif selection ==31:
            print("You have chosen the isinstance() method")
            isinstance1=("isinstance() Function\nThe isinstance() function returns True if the specified object is of the specified type, otherwise False.\n If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.")
            print(isinstance1)
        elif selection ==32:
            print("You have chosen the issubclass() method")
            issubclass1=("issubclass() Function\nThe issubclass() function returns an iterator object.")
            print(issubclass1)
        elif selection ==33:
            print("You have chosen the iter() method")
            iter1=("iter() Function\nThe iter() function converts the specified number into a hexadecimal value. The returned string always starts with the prefix 0x.")
            print(iter1)
        elif selection ==34:
            print("You have chosen the len() method")
            len1=("len() Function\nThe len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.")
            print(len1)
        elif selection ==35:
            print("You have chosen the list() method")
            list1=("list() Function\nThe list() function creates a list object. A list object is a collection which is ordered and changeable.")
            print(list1)
        elif selection ==36:
            print("You have chosen the locals() method")
            locals1=("locals() Function\nThe locals() function returns the local symbol table as a dictionary. A symbol table contains necessary information about the current program.")
            print(locals1)
        elif selection ==37:
            print("You have chosen the map() method")
            map1=("map() Function\nThe map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.")
            print(map1)
        elif selection ==38:
            print("You have chosen the max() method")
            max1=("max() Function\nThe max() function returns the item with the highest value, or the item with the highest value in an iterable. \n If the values are strings, an alphabetically comparison is done.")
            print(max1)
        elif selection ==39:
            print("You have chosen the memoryview() method")
            memoryview1=("memoryview() Function\nThe memoryview() function returns a memory view object from a specified object.")
            print(memoryview1)
        elif selection ==40:
            print("You have chosen the min() method")
            min1=("min() Function\nThe min() function returns the item with the lowest value, or the item with the lowest value in an iterable. If the values are strings, an alphabetically comparison is done.")
            print(min1)
        elif selection ==41:
            print("You have chosen the next() method")
            nxtbu=("next() Function\nThe next() function returns the next item in an iterator. You can add a default return value, to return if the iterable has reached to its end.")
            print(nxtbu)
        elif selection ==42:
            print("You have chosen the object() method")
            objbu=("object() Function\nThe object() function returns an empty object. You cannot add new properties or methods to this object.\nThis object is the base for all classes, it holds the built-in properties and methods which are default for all classes.")
            print(objbu)
        elif selection ==43:
            print("You have chosen the oct() method")
            oct1=("oct() Function\nThe oct() function converts an integer into an octal string. Octal strings in Python are prefixed with 0o.")
            print(oct1)
        elif selection ==44:
            print("You have chosen the open() method")
            opbu=("open() Function\nThe open() function opens a file, and returns it as a file object.")
            print(opbu)
        elif selection ==45:
            print("You have chosen the ord() method")
            ord1=("ord() Function\nThe ord() function returns the number representing the unicode code of a specified character.")
            print(ord1)
        elif selection ==46:
            print("You have chosen the pow() method")
            pow1=("pow() Function\nThe pow() function returns the value of x to the power of y (xy).\nFor instance, if a third parameter is present, it returns x to the power of y, modulus z.")
            print(pow1)
        elif selection ==47:
            print("You have chosen the print() method")
            prtbu=("print() Function\nThe print() function prints the specified message to the screen, or other standard output device.\nThe message can be a string, or any other object, the object will be converted into a string before written to the screen.")
            print(prtbu)
        elif selection ==48:
            print("You have chosen the range() method")
            rng=("range() Function\nThe range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.")
            print(rng)
        elif selection ==49:
            print("You have chosen the reversed() method")
            revbu=("reversed() Function\nThe reversed() function returns a reversed iterator object.")
            print(revbu)
        elif selection ==50:
            print("You have chosen the round() method")
            rndbu=("round() Function\nThe round() function returns a floating point number that is a rounded version\nof the specified number, with the specified number of decimals.")
            print(rndbu)
        elif selection ==51:
            print("You have chosen the set() method")
            stbu=("set() Function\nThe set() function creates a set object.The items in a set list are\nunordered, so it will appear in random order.")
            print(stbu)
        elif selection ==52:
            print("You have chosen the setattr() method")
            stat=("setattr() Function\nThe setattr() function sets the value of the specified attribute of the specified object.")
            print(stat)
        elif selection ==53:
            print("You have chosen the slice() method")
            slc=("slice() Function\nThe slice() function returns a slice object. A slice object is used to specify\nhow to slice a sequence.")
            print(slc)
        elif selection ==54:
            print("You have chosen the sorted() method")
            srtbu=("sorted() Function\nThe sorted() function returns a sorted list of the specified iterable object.\nYou can specify ascending or descending order.")
            print(srtbu)
        elif selection ==55:
            print("You have chosen the str() method")
            str=("str() Function\nThe str() function converts the specified value into a string.")
            print(str)
        elif selection ==56:
            print("You have chosen the sum() method")
            smbu=("sum() Function\nThe sum() function returns a number, the sum of all items in an iterable.")
            print(smbu)
        elif selection ==57:
            print("You have chosen the super() method")
            spbu=("super() Function\nThe super() function is used to give access to methods and properties of a parent or sibling class.")
            print(spbu)
        elif selection ==58:
            print("You have chosen the tuple() method")
            tpbu=("tuple() Function\nThe tuple() function creates a tuple object. Always remember, you cannot\nchange or remove items in a tuple.")
            print(tpbu)
        elif selection ==59:
            print("You have chosen the type() method")
            tybu=("type() Function\nThe type() function returns the type of the specified object.")
            print(tybu)
        elif selection ==60:
            print("You have chosen the vars() method")
            vrs=("vars() Function\nThe vars() function returns the __dict__ attribute of an object. The __dict__ attribute is a dictionary\ncontaining the object's changeable attributes. Keep in mind that calling the vars() function without parameters\nwill return a dictionary containing the local symbol table.")
            print(vrs)
        elif selection ==61:
            print("You have chosen the zip() method")
            zip1=("zip() Function\nThe zip() function returns a zip object, which is an iterator of tuples where the first item in each passed\niterator is paired together, and then the second item in each passed iterator are paired together etc. If the passed\niterators have different lengths, the iterator with the least items decides the length of the new iterator.")
            print(zip1)
    elif choice ==2:
        abs1=("abs() Function\nThe abs() function returns the absolute value of the specified number.")
        print(abs1)
        print("\n")
        
        all1=("all() Function\nThe all() function returns True if all items in an iterable are true, otherwise it returns False.\nIf the iterable object is empty, the all() function also returns True.")
        print(all1)
        print("\n")
        
        any1=("any() Function\nThe any() function returns True if any item in an iterable are true, otherwise it returns False.\nIf the iterable object is empty, the any() function will return False.")
        print(any1)
        print("\n")

        ascii1=("ascii() Function\nThe ascii()function returns a readable version of any object (Strings, Tuples, Lists, etc).\nIt will replace any non-ascii characters with escape characters.")
        print(ascii1)
        print("\n")

        bin1=("bin() Function\nThe bin() function returns the binary version of a specified integer.\nThe result will always start with the prefix 0b.")
        print(bin1)
        print("\n")

        bool1=("bool() Function\nThe bool() function returns the boolean value of a specified object.")
        print(bool1)
        print("\n")

        byteaaray=("byteaaray() Function\nThe byteaaray() function returns a bytearray object. It can convert objects into bytearray objects,\nor create empty bytearray object of the specified size.")
        print(byteaaray)
        print("\n")

        bytes1=("bytes() Function\nThe bytes() function returns a bytes object. It can convert objects into\nbytes objects, or create empty bytes object of the specified size.")
        print(bytes1)
        print("\n")

        callable1=("callable() Function\nThe callable() function returns True if the specified object is callable, otherwise it returns False.")
        print(callable1)
        print("\n")

        chr1=("chr() Function\nThe chr() function returns the character that represents the specified unicode.")
        print(chr1)
        print("\n")

        compile1=("compile() Function\nThe compile() function returns the specified source as a code object, ready to be executed.")
        print(compile1)
        print("\n")

        complex1=("complex() Function\nThe complex() function returns a complex number by specifying\na real number and an imaginary number.")
        print(complex1)
        print("\n")

        delattr1=("delattr() Function\nThe delattr() function will delete the specified attribute from the specified object.")
        print(delattr1)
        print("\n")

        dict1=("dict() Function\nThe dict() function creates a dictionary. A dictionary is a collection which is unordered, changeable and indexed.")
        print(dict1)
        print("\n")

        dir1=("dir() Function\nThe dir() function returns all properties and methods of the specified object,\nwithout the values. This function will return all the properties and methods, even built-in\nproperties which are default for all object.")
        print(dir1)
        print("\n")

        divmod1=("divmod() Function\nThe divmod() function returns a tuple containing the quotient and\nthe remainder when argument1 (divident) is divided by argument2 (divisor).")
        print(divmod1)
        print("\n")

        enumerate1=("enumerate() Function\nThe enumerate() function takes a collection (e.g. a tuple)\nand returns it as an enumerate object. It adds a counter as the key of the enumerate object.")
        print(enumerate1)
        print("\n")

        eval1=("eval() Function\nThe eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.")
        print(eval1)
        print("\n")

        exec1=("exec() Function\nThe exec() function executes the specified Python code. The exec() function\naccepts large blocks of code, unlike the eval() function which only accepts a single expression.")
        print(exec1)
        print("\n")

        filter1=("filter() Function\nThe filter() function returns an iterator were the items are filtered through\na function to test if the item is accepted or not.")
        print(filter1)
        print("\n")
        
        float1=("float() Function\nThe float() function converts the specified value into a floating point number. ")
        print(float1)
        print("\n")

        format1=("format() Function\nThe format() function formats a specified value into a specified format.")
        print(format1)
        print("\n")

        frozenset1=("frozenset() Function\nThe frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).")
        print(frozenset1)
        print("\n")

        getattr1=("getattr() Function\nThe getattr() function returns the value of the specified attribute from the specified object.")
        print(getattr1)
        print("\n")

        globals1=("globals() Function\nThe globals() function returns the global symbol table as a dictionary. A symbol table contains necessary information about the current program.")
        print(globals1)
        print("\n")

        hasattr1=("hasattr() Function\nThe hasattr() function function returns True if the specified object has the specified attribute, otherwise False.")
        print(hasattr1)
        print("\n")

        hex1=("hex() Function\nThe hex() function converts the specified number into a hexadecimal value. The returned string always starts with the prefix 0x.")
        print(hex1)
        print("\n")

        id1=("id() Function\nThe id() function returns a unique id for the specified object. All objects in Python has its own unique id. The id is assigned to the object when it is created. \n The id is the object's memory address, and will be different for each time you run the program. \n (except for some object that has a constant unique id, like integers from -5 to 256). ")
        print(id1)
        print("\n")

        input1=("input() Function\nThe input() function allows user input.")
        print(input1)
        print("\n")

        int1=("int() Function\nThe int() function converts the specified value into an integer number.")
        print(int1)
        print("\n")

        isinstance1=("isinstance() Function\nThe isinstance() function returns True if the specified object is of the specified type, otherwise False.\n If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.")
        print(isinstance1)
        print("\n")

        issubclass1=("issubclass() Function\nThe issubclass() function returns an iterator object.")
        print(issubclass1)
        print("\n")
        
        iter1=("iter() Function\nThe iter() function converts the specified number into a hexadecimal value. The returned string always starts with the prefix 0x.")
        print(iter1)
        print("\n")

        len1=("len() Function\nThe len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.")
        print(len1)
        print("\n")

        list1=("list() Function\nThe list() function creates a list object. A list object is a collection which is ordered and changeable.")
        print(list1)
        print("\n")

        locals1=("locals() Function\nThe locals() function returns the local symbol table as a dictionary. A symbol table contains necessary information about the current program.")
        print(locals1)
        print("\n")

        map1=("map() Function\nThe map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.")
        print(map1)
        print("\n")

        max1=("max() Function\nThe max() function returns the item with the highest value, or the item with the highest value in an iterable. \n If the values are strings, an alphabetically comparison is done.")
        print(max1)
        print("\n")

        memoryview1=("memoryview() Function\nThe memoryview() function returns a memory view object from a specified object.")
        print(memoryview1)
        print("\n")

        min1=("min() Function\nThe min() function returns the item with the lowest value, or the item with the lowest value in an iterable. If the values are strings, an alphabetically comparison is done.") 
        print(min1)
        print("\n")
        
        nxtbu=("next() Function\nThe next() function returns the next item in an iterator. You can add a default return value, to return if the iterable has reached to its end.")
        print(nxtbu)
        print("\n")

        objbu=("object() Function\nThe object() function returns an empty object. You cannot add new properties or methods to this object.\nThis object is the base for all classes, it holds the built-in properties and methods which are default for all classes.")
        print(objbu)
        print("\n")

        oc1t=("oct() Function\nThe oct() function converts an integer into an octal string. Octal strings in Python are prefixed with 0o.")
        print(oct1)
        print("\n")

        opbu=("open() Function\nThe open() function opens a file, and returns it as a file object.")
        print(opbu)
        print("\n")

        ord1=("ord() Function\nThe ord() function returns the number representing the unicode code of a specified character.")
        print(ord1)
        print("\n")

        pow1=("pow() Function\nThe pow() function returns the value of x to the power of y (xy).\nFor instance, if a third parameter is present, it returns x to the power of y, modulus z.")
        print(pow1)
        print("\n")

        prtbu=("print() Function\nThe print() function prints the specified message to the screen, or other standard output device.\nThe message can be a string, or any other object, the object will be converted into a string before written to the screen.")
        print(prtbu)
        print("\n")

        rng=("range() Function\nThe range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.")
        print(rng)
        print("\n")

        revbu=("reversed() Function\nThe reversed() function returns a reversed iterator object.")
        print(revbu)
        print("\n")

        rndbu=("round() Function\nThe round() function returns a floating point number that is a rounded version\nof the specified number, with the specified number of decimals.")
        print(rndbu)
        print("\n")

        stbu=("set() Function\nThe set() function creates a set object.The items in a set list are\nunordered, so it will appear in random order.")
        print(stbu)
        print("\n")

        stat=("setattr() Function\nThe setattr() function sets the value of the specified attribute of the specified object.")
        print(stat)
        print("\n")

        slc=("slice() Function\nThe slice() function returns a slice object. A slice object is used to specify\nhow to slice a sequence.")
        print(slc)
        print("\n")

        srtbu=("sorted() Function\nThe sorted() function returns a sorted list of the specified iterable object.\nYou can specify ascending or descending order.")
        print(srtbu)
        print("\n")

        str=("str() Function\nThe str() function converts the specified value into a string.")
        print(str)
        print("\n")

        smbu=("sum() Function\nThe sum() function returns a number, the sum of all items in an iterable.")
        print(smbu)
        print("\n")

        spbu=("super() Function\nThe super() function is used to give access to methods and properties of a parent or sibling class.")
        print(spbu)
        print("\n")

        tpbu=("tuple() Function\nThe tuple() function creates a tuple object. Always remember, you cannot\nchange or remove items in a tuple.")
        print(tpbu)
        print("\n")

        tybu=("type() Function\nThe type() function returns the type of the specified object.")
        print(tybu)
        print("\n")

        vrs=("vars() Function\nThe vars() function returns the __dict__ attribute of an object. The __dict__ attribute is a dictionary\ncontaining the object's changeable attributes. Keep in mind that calling the vars() function without parameters\nwill return a dictionary containing the local symbol table.")
        print(vrs)
        print("\n")

        zip1=("zip() Function\nThe zip() function returns a zip object, which is an iterator of tuples where the first item in each passed\niterator is paired together, and then the second item in each passed iterator are paired together etc. If the passed\niterators have different lengths, the iterator with the least items decides the length of the new iterator.")
        print(zip1)

        
        



#file method         
elif selection ==7:
    print("You have selected Python Object: File Method")
    print("Please choose on how you want to search method")
    print("1) Select File method")
    print("2) Select File mode")
    print("3) Select File attribute")
    print("4) Select all File method")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) close")
        print("2) fileno")
        print("3) flush")
        print("4) read")
        print("5) isatty")
        print("6) readable")
        print("7) readline")
        print("8) readlines")
        print("9) seek")
        print("10) seekable")
        print("11) tell")
        print("12) truncate")
        print("13) writable")
        print("14) write")
        print("15) writelines")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen the close() method")
            clfl=("close() Method\nThe close() method closes an open file. You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.read())\nf.close()")
            print(clfl)
            f = open("cmmms.txt","r")
            print(out)
            print(f.read())
            f.close()
        elif selection ==2:
            print("You have chosen the fileno() method")
            flno=("fileno() Method\nThe fileno() method returns the file descriptor of the stream, as a number. An error will occur if the operator system does not use a file descriptor.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.fileno())")
            print(flno)
            f = open("cmmms.txt","r")
            print(out)
            print(f.fileno())            
        elif selection ==3:
            print("You have chosen the flush() method")
            flu=("flush() Method\nThe flush() method cleans out the internal buffer.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.write(""One more line"")\nf.flush()\nf.write(""And another line"")")
            f = open("cmmms.txt","a")
            f.write("One more line")
            print(out)
            f.flush()
            f.write("And another line")
        elif selection ==4:
            print("You have chosen the read() method")
            refl=("read() Method\nThe read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
            print(refl)
            f = open("cmmms.txt","r")
            print(out)
            print(f.read())            
        elif selection ==5:
            print("You have chosen the isatty() method")
            atfl=("isatty() Method\nThe isatty() method returns True if the file stream is interactive, example: connected to a terminal device.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.isatty())")
            print(atfl)
            f = open("cmmms.txt","r")
            print(out)
            print(f.isatty())
        elif selection ==6:
            print("You have chosen the readable() method")
            rdbfl=("readable() Method\nThe readable() method returns True if the file is readable, False if not.\nCode\nf = open(""cmmms.txt"",""r"")\nprint(f.readable())")
            print(rdbfl)
            f = open("cmmms.txt","r")
            print(out)
            print(f.readable())
        elif selection ==7:
            print("You have chosen the readline() method")
            rlnfl=("readline() Method\nThe readline() method returns one line from the file. You can also specified how many bytes from the line to return, by using the size parameter.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.readline())")
            print(rlnfl)
            f = open("cmmms.txt","r")
            print(out)
            print(f.readline())
        elif selection ==8:
            print("You have chosen the readlines() method")
            rlns=("readlines() Method\nThe readlines() method returns a list containing each line in the file as a list item.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.readlines())")
            print(rlns)
            f = open("cmmms.txt","r")
            print(out)
            print(f.readlines())
        elif selection ==9:
            print("You have chosen the seek() method")
            sefl=("seek() Method\nThe seek() method sets the current file position in a file stream. The seek() method also returns the new position.\nCode:\nf = open(""cmmms.txt"",""r"")\nf.seek(5)\nprint(f.readline())")
            print(sefl)
            f = open("cmmms.txt","r")
            print(out)
            f.seek(5)
            print(f.readline())
        elif selection ==10:
            print("You have chosen the seekable() method")
            skfl=("seekable() Method\nThe seekable() method returns True if the file is seekable, False if not.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.seekable())")
            print(skfl)
            f = open("cmmms.txt","r")
            print(out)
            print(f.seekable())
        elif selection ==11:
            print("You have chosen the tell() method")
            tlf=("tell() Method\nThe tell() method returns the current file position in a file stream. Tip: You can change the current file position with the seek() method.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.tell())")
            print(tlf)
            f = open("cmmms.txt","r")
            print(out)
            print(f.tell())
        elif selection ==12:
            print("You have chosen the truncate() method")
            trfl=("truncate() Method\nThe truncate() method resizes the file to the given number of bytes. If the size is not specified, the current position will be used.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.truncate(20)\nf.close()\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
            print(trfl)
            f = open("cmmms.txt","a")
            print(out)
            f.truncate(20)
            f.close()
            f = open("cmmms.txt","r")
            print(f.read())
        elif selection ==13:
            print("You have chosen the writable() method")
            wrb=("writable() Method\nThe writable() method returns True if the file is writable, False if not. A file is writable if it is opened using ""a"" for append or ""w"" for write.\nCode:\nf = open(""cmmms.txt"",""a"")\nprint(f.writable())")
            print(wrb)
            f = open("cmmms.txt","a")
            print(out)
            print(f.writable())
        elif selection ==14:
            print("You have chosen the write() method")
            wfl=("write() Method\nThe write() method writes a specified text to the file. Where the specified text will be inserted depends on the file mode and stream position.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.write(""Hello there"")\nf.close()\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
            print(wfl)
            f = open("cmmms.txt","a")
            print(out)
            f.write("Hello there")
            f.close()
            f = open("cmmms.txt","r")
            print(f.read())
        elif selection ==15:
            print("You have chosen the writelines() method")
            wlns=("writelines() Method\nThe writelines() method writes the items of a list to the file. Where the texts will be inserted depends on the file mode and stream position.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.writelines([""Hello there"", ""Roger that""])\nf.close()\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
            print(wlns)
            f = open("cmmms.txt","a")
            print(out)
            f.writelines(["Hello there", "Roger that"])
            f.close()
            f = open("cmmms.txt","r")
            print(f.read())
    elif choice ==2:
        print("1) reading only")
        print("2) reading only in binary format")
        print("3) reading and writing")
        print("4) reading and writing in binary format")
        print("5) writing")
        print("6) writing only in binary format")
        print("7) writing and reading")
        print("8) writing and reading in binary format")
        print("9) appending")
        print("10) appending in binary format")
        print("11) appending and reading")
        print("12) appending and reading in binary format")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen reading only")
            rmd=("r\nOpens a file for reading only. The file pointer is placed at the beginning of the file which is the default mode.")
            print(rmd)
        elif selection ==2:
            print("You have chosen reading only in binary format")
            rbmd=("rb\nOpens a file for reading only in binary format. The file pointer is placed at the\nbeginning of the file which is the default mode.")
            print(rbmd)
        elif selection ==3:
            print("You have chosen reading and writing")
            rpmd=("r+\nOpens a file for both reading and writing. The file pointer is placed at the beginning of the file.")
            print(rpmd)
        elif selection ==4:
            print("You have chosen reading and writing in binary format")
            rbpmd=("rb+\nOpens a file for both reading and writing in binary format. The file pointer is placed\nat the beginning of the file.")
            print(rbpmd)
        elif selection ==5:
            print("You have chosen writing")
            wmd=("w\nOpens a file for writing only. Overwrites the file if the file exists.\nIf the file does not exist, it creates a new file for writing.")
            print(wmd)
        elif selection ==6:
            print("You have chosen writing only in binary format")
            wbmd=("wb\nOpens a file for writing only in binary format. Overwrites the file if the file exists.\nIf the file does not exist, it creates a new file for writing.")
            print(wbmd)
        elif selection ==7:
            print("You have chosen writing and reading")
            wpmd=("w+\nOpens a file for both writing and reading. Overwrites the file if the file exists.\nIf the file does not exist, it creates a new file for reading and writing.")
            print(wpmd)
        elif selection ==8:
            print("You have chosen writing and reading in binary format")
            wbpmd=("wb+\nOpens a file for both writing and reading in binary format. Overwrites the file if\n the file exists. If the file does not exist, it creates a new file for reading and writing.")
            print(wbpmd)
        elif selection ==9:
            print("You have chosen appending")
            amd1=("a\nOpens a file for appending. The file pointer is at the end of the file, if the file exists. That is,\nthe file is in the append mode. If the file does not exist, it creates a new file for writing.")
            print(amd1)
        elif selection ==10:
            print("You have chosen appending in binary format")
            abmd=("ab\nOpens a file for appending in binary format. The file pointer is at the end of the file, if the file exists.\nThat is, the file is in the append mode. If the file does not exist, it creates a new file for writing.")
            print(abmd)
        elif selection ==11:
            print("You have chosen appending and reading")
            apmd=("a+\nOpens a file for both appending and reading. The file pointer is at the end of the file, if the file exists.\n The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.")
            print(apmd)

        elif selection ==12:
            print("You have chosen appending and reading in binary format")
            abpmd=("ab+\nOpens a file for both appending and reading in binary format. The file pointer is\nat the end of the file,if the file exists. The file opens in the append mode. If the file does not\nexist, it creates a new file for reading and writing.")
            print(abpmd)
            
    elif choice ==3:
        print("1) file.closed")
        print("2) file.mode")
        print("3) file.name")
        print("4) file.softspace")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen the file.closed attribute")
            flxat=("file.closed\nReturns True if the file is closed, otherwise it will returns False.")
            print(flxat)
        elif selection == 2:
            print("You have chosen the file.mode attribute")
            flmd=("file.mode\nReturns the access mode with which the file was opened.")
            print(flmd)
        elif selection == 3:
                print("You have chosen the file.name attribute")
                flnm=("file.name\nReturns the name of the file.")
                print(flnm)
        elif selection == 4:
                print("You have chosen the file.softspace attribute")
                flsf=("file.softspace\nReturns False is space explicitly required with print. Otherwise it will returns True.")
                print(flsf)                 
    elif choice ==4:
        clfl=("close() Method\nThe close() method closes an open file. You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.read())\nf.close()")
        print(clfl)
        f = open("cmmms.txt","r")
        print(out)
        print(f.read())
        f.close()
        print("\n")
        
        flno=("fileno() Method\nThe fileno() method returns the file descriptor of the stream, as a number. An error will occur if the operator system does not use a file descriptor.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.fileno())")
        print(flno)
        f = open("cmmms.txt","r")
        print(out)
        print(f.fileno())
        print("\n")
        
        flu=("flush() Method\nThe flush() method cleans out the internal buffer.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.write(""One more line"")\nf.flush()\nf.write(""And another line"")")
        f = open("cmmms.txt","a")
        f.write("One more line")
        print(out)
        f.flush()
        f.write("And another line")
        print("\n")
        
        refl=("read() Method\nThe read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
        print(refl)
        f = open("cmmms.txt","r")
        print(out)
        print(f.read())
        print("\n")
        
        atfl=("isatty() Method\nThe isatty() method returns True if the file stream is interactive, example: connected to a terminal device.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.isatty())")
        print(atfl)
        f = open("cmmms.txt","r")
        print(out)
        print(f.isatty())
        print("\n")
        
        rdbfl=("readable() Method\nThe readable() method returns True if the file is readable, False if not.\nCode\nf = open(""cmmms.txt"",""r"")\nprint(f.readable())")
        print(rdbfl)
        f = open("cmmms.txt","r")
        print(out)
        print(f.readable())
        print("\n")
        
        rlnfl=("readline() Method\nThe readline() method returns one line from the file. You can also specified how many bytes from the line to return, by using the size parameter.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.readline())")
        print(rlnfl)
        f = open("cmmms.txt","r")
        print(out)
        print(f.readline())
        print("\n")
        
        rlns=("readlines() Method\nThe readlines() method returns a list containing each line in the file as a list item.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.readlines())")
        print(rlns)
        f = open("cmmms.txt","r")
        print(out)
        print(f.readlines())
        print("\n")
        
        sefl=("seek() Method\nThe seek() method sets the current file position in a file stream. The seek() method also returns the new position.\nCode:\nf = open(""cmmms.txt"",""r"")\nf.seek(5)\nprint(f.readline())")
        print(sefl)
        f = open("cmmms.txt","r")
        print(out)
        f.seek(5)
        print(f.readline())
        print("\n")
        
        skfl=("seekable() Method\nThe seekable() method returns True if the file is seekable, False if not.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.seekable())")
        print(skfl)
        f = open("cmmms.txt","r")
        print(out)
        print(f.seekable())
        print("\n")
        
        tlf=("tell() Method\nThe tell() method returns the current file position in a file stream. Tip: You can change the current file position with the seek() method.\nCode:\nf = open(""cmmms.txt"",""r"")\nprint(f.tell())")
        print(tlf)
        f = open("cmmms.txt","r")
        print(out)
        print(f.tell())
        print("\n")
        
        trfl=("truncate() Method\nThe truncate() method resizes the file to the given number of bytes. If the size is not specified, the current position will be used.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.truncate(20)\nf.close()\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
        print(trfl)
        f = open("cmmms.txt","a")
        print(out)
        f.truncate(20)
        f.close()
        f = open("cmmms.txt","r")
        print(f.read())
        print("\n")
        
        wrb=("writable() Method\nThe writable() method returns True if the file is writable, False if not. A file is writable if it is opened using ""a"" for append or ""w"" for write.\nCode:\nf = open(""cmmms.txt"",""a"")\nprint(f.writable())")
        print(wrb)
        f = open("cmmms.txt","a")
        print(out)
        print(f.writable())
        print("\n")
        
        wfl=("write() Method\nThe write() method writes a specified text to the file. Where the specified text will be inserted depends on the file mode and stream position.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.write(""Hello there"")\nf.close()\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
        print(wfl)
        f = open("cmmms.txt","a")
        print(out)
        f.write("Hello there")
        f.close()
        f = open("cmmms.txt","r")
        print(f.read())
        print("\n")
        
        wlns=("writelines() Method\nThe writelines() method writes the items of a list to the file. Where the texts will be inserted depends on the file mode and stream position.\nCode:\nf = open(""cmmms.txt"",""a"")\nf.writelines([""Hello there"", ""Roger that""])\nf.close()\nf = open(""cmmms.txt"",""r"")\nprint(f.read())")
        print(wlns)
        f = open("cmmms.txt","a")
        print(out)
        f.writelines(["Hello there", "Roger that"])
        f.close()
        f = open("cmmms.txt","r")
        print(f.read())
        print("\n")
        
        rmd=("r\nOpens a file for reading only. The file pointer is placed at the beginning of the file which is the default mode.")
        print("\n")
        print(rmd)

        rbmd=("rb\nOpens a file for reading only in binary format. The file pointer is placed at the\nbeginning of the file which is the default mode.")
        print("\n")
        print(rbmd)

        rpmd=("r+\nOpens a file for both reading and writing. The file pointer is placed at the beginning of the file.")
        print("\n")
        print(rpmd)

        rbpmd=("rb+\nOpens a file for both reading and writing in binary format. The file pointer is placed\nat the beginning of the file.")
        print("\n")
        print(rbpmd)

        wmd=("w\nOpens a file for writing only. Overwrites the file if the file exists.\nIf the file does not exist, it creates a new file for writing.")
        print("\n")
        print(wmd)

        wbmd=("wb\nOpens a file for writing only in binary format. Overwrites the file if the file exists.\nIf the file does not exist, it creates a new file for writing.")
        print("\n")
        print(wbmd)

        wpmd=("w+\nOpens a file for both writing and reading. Overwrites the file if the file exists.\nIf the file does not exist, it creates a new file for reading and writing.")
        print("\n")
        print(wpmd)

        wbpmd=("wb+\nOpens a file for both writing and reading in binary format. Overwrites the file if\n the file exists. If the file does not exist, it creates a new file for reading and writing.")
        print("\n")
        print(wbpmd)

        amd=("a\nOpens a file for appending. The file pointer is at the end of the file, if the file exists. That is,\nthe file is in the append mode. If the file does not exist, it creates a new file for writing.")
        print("\n")
        print(amd)

        abmd=("ab\nOpens a file for appending in binary format. The file pointer is at the end of the file, if the file exists.\nThat is, the file is in the append mode. If the file does not exist, it creates a new file for writing.")
        print("\n")
        print(abmd)

        apmd=("a+\nOpens a file for both appending and reading. The file pointer is at the end of the file, if the file exists.\n The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.")
        print("\n")
        print(apmd)

        abpmd=("ab+\nOpens a file for both appending and reading in binary format. The file pointer is\nat the end of the file,if the file exists. The file opens in the append mode. If the file does not\nexist, it creates a new file for reading and writing.")
        print("\n")
        print(abpmd)
        
        flxat=("file.closed\nReturns True if the file is closed, otherwise it will returns False.")
        print("\n")
        print(flxat)

        flmd=("file.mode\nReturns the access mode with which the file was opened.")
        print("\n")
        print(flmd)

        flnm=("file.name\nReturns the name of the file.")
        print(flnm)

        flsf=("file.softspace\nReturns False is space explicitly required with print. Otherwise it will returns True.")
        print(flsf)
elif selection == 8:
    print("You have selected Python Object: Keywords")
    print("Input 5 elements to be used in keywords")
    in1 = int(input("Enter 1st number: "))
    in2 = int(input("Enter 2nd number: "))
    in3 = int(input("Enter 3rd number: "))
    in4 = input("Enter 1st Element: ")
    in5 = input("Enter 2nd Element: ")
    print("Please choose on how you want to search the method")
    print("1) Select Keywords")
    print("2) Select All Keywords")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        print("1) And")
        print("2) As")
        print("3) Assert")
        print("4) Break")
        print("5) Class")
        print("6) Continue")
        print("7) Def")
        print("8) Del")
        print("9) Elif")
        print("10) Else")
        print("11) Except")
        print("12) False")
        print("13) Finally")
        print("14) For")
        print("15) From")
        print("16) Global")
        print("17) If")
        print("18) Import")
        print("19) In")
        print("20) Is")
        print("21) Lambda")
        print("22) None")
        print("23) Nonlocal")
        print("24) Not")
        print("25) Or")
        print("26) Pass")
        print("27) Raise")
        print("28) Return")
        print("29) True")
        print("30) Try")
        print("31) While")
        print("32) With")
        print("33) Yield")
        selection= int(input("Enter your choice: "))
        print("\n")
        if selection == 1:
            print("You have chosen the And keyword")
            andk=("and keyword\nThe and keyword is a logical operator. Logical operators are used to combine conditional statements.\nCode:\nx = (in1 > in2 and in1 < in3)\nprint(x)")
            print(andk)
            x = (in1 > in2 and in1 < in3)
            print(out)
            print(x)
        elif selection ==2:
            print("You have chosen the As keyword")
            ask=("as keyword\nThe as keyword is used to create an alias.\nCode:\nimport calendar as c\n            print(c.month_name[12])")
            print(ask)
            import calendar as c
            print(out)
            print(c.month_name[12])
        elif selection ==3:
            print("You have chosen the Assert keyword")
            assk=("assert keyword\nThe assert keyword is used when debugging code. The assert keyword lets you test if a condition\nin your code returns True, if not, the program will raise an Assertion Error.\nYou can write a message to be written if the code returns False.\nCode:\nTRUE\nx = in4\nassert x == in4\nFALSE\nassert x == in5")
            print(assk)
            x = in4
            print(out)
            print("TRUE")
        elif selection ==4:
            print("You have chosen the Break keyword")
            brk=("break keyword\nThe break keyword is used to break out or end a loop.\nCode:\nfor i in range (in1):\n   if i > 5:\n     break\n print(i)")
            print(brk)
            for i in range (in1):
                if i > 5:
                    break
            print(out)
            print(i)

        elif selection ==5:
            print("You have chosed the Class Keyword")
            clsk=("class keyword\nThe class keyword is used to create a class. A class is like an object constructor.\nCode:\nclass Element:\n  el1 = in1\n el2 = in2\n el3 = in3\n el4 = in4\n el5 = in5\n el = Element()\nprint(el.el1, el.el2, el.el3, el.el4, el.el5)")
            print(clsk)
            class Element:
               el1 = in1
               el2 = in2
               el3 = in3
               el4 = in4
               el5 = in5
            el = Element()
            print(out)
            print(el.el1, el.el2, el.el3, el.el4, el.el5)
        elif selection ==6:
            print("You have chosen the Continue keyword")
            conk=("continue keyword\nThe continue keyword is used to end the current iteration in a loop\n(a for loop or a while loop), and continues to the next iteration.\nCode:\nfor i in range (in1):\n    if i == 5:\n        continue\n  print(i)")
            print(conk)
            for i in range (in1):
                if i == 5:
                    continue
                print(out)
                print(i)

        elif selection ==7:
            print("You have chosen the Def keyword")
            defk=("def keyword\nThe def keyword is used to create, (or define) a function.\nCode:\ndef cmmms_function():\n print(in1, in2, in3, in4, in5)\ncmmms_function()")
            print(defk)
            def cmmms_function():
                print(out)
                print(in1, in2, in3, in4, in5)
                cmmms_function()

        elif selection ==8:
            delk=("del keyword\nThe del keyword is used to delete objects. In Python everything is an object,\nso the del keyword can also be used to delete variables, lists, or parts of a list etc.\nCode:\Deleting a Whole Class\nclass Element:\n  el1 = in1\n el2 = in2\n el3 = in3\n el4 = in4\n el5 = in5\ndel Element\nprint(Element)\n\nDeleting a Specific Variable\nx = in1\ndel x\nprint(x)")
            print(delk)
            class Element:
                el1 = in1
                el2 = in2
                el3 = in3
                x = in4
                el5 = in5
            print(out)
            print ("Deleting a Whole Class")            
            del Element
            print("NameError: name 'Element' is not defined")
            
            print("\nDeleting a Specific Variable")
            x = in4
            del x
            print("NameError: name 'x' is not defined")

        elif selection ==9:
            print("You have chosen the Elif keyword")
            elifk=("elif keyword\nThe elif keyword is used in conditional statements (if statements), and is short for else if.\nCode:\nfor i in range (-5, 5):\n   if i > 0:\n     print(in1)\n    elif i == 0:\n      print(int2)")
            print(elifk)
            print(out)
            for i in range (-5, 5):
                if i > 0:
                    print(in1)
                elif i == 0:
                    print(in2)
                

        elif selection ==10:
            print("You have chosen the Else keyword")
            elsek=("else keyword\nThe else keyword is used in conditional statements (if statements), and decides\nwhat to do if the condition is False. The else keyword can also be used in try...except blocks.\nCode:\nx = in1\ntry:\n  x > in2\nexcept:\n  print(""Something went wrong."")\nelse:\n print(""Code executed with no errors."")")
            print(elsek)
            print(out)
            x = in1
            try:
                x > in2
            except:
                print("Something went wrong.")
            else:
                print("Code executed with no errors.")

        elif selection ==11:
            print("You have chosen the Except keyword")
            eptk=("except keyword\nThe except keyword is used in try...except blocks. It defines a block of code to run if the try block raises an error.\nYou can define different blocks for different error types, and blocks to execute if nothing went wrong.\nCode:\ntry:\n   x > in1\nexcept:\n  print(""Something went wrong."")")
            print(eptk)
            print(out)
            try:
                x > in1
            except:
                print("Something went wrong.")

        elif selection ==12:
            print("You have chosen the False keyword")
            falsek=("False keyword\nThe False keyword is a Boolean value, and result of a comparison operation. The False keyword is the same as 0.\nCode:\ nprint(10 > 12)")
            print(out)
            print(falsek)
            print(10 > 12)
        elif selection ==13:
            print("You have chosen the Finally keyword")
            finallyk=("finally keyword\nThe finally keyword is used in try...except blocks. It defines a block of\n code to run when the try...except...else block is final. The finally block will be executed no\n matter if the try block raises an error or not. This can be useful to close objects and clean up resources.\nCode:\ntry:\n x > 3 except:\n print(“something went wrong)\nelse:\n   print (“Nothing went wrong”)\nfinally:\n    print(“The try...except block is finished”)")
            print(finallyk)
            print(out)
            try:
                x > 3
            except:
                print("something went wrong")
            else:
                print ("Nothing went wrong")
            finally:
                print("The try...except block is finished")

        elif selection ==14:
            print("You have chosen the For keyword")
            fork=("for keyword\nThe For keyword is used to create a for loop. It can be used to iterate through a sequence, like a list, tuple, etc.\nCode:\nfor x in range = (1,9):\n   print(x)")
            print(fork)
            for x in range (1,9):
                print(out)
                print(x)

        elif selection ==15:
            print("You have chosen the From keyword")
            fromk=("from keyword\nThe from keyword is used to import only a specified section from a module. \nCode:\nfrom datetime import time\nx = time (hour = 5)\nprint(x)")
            print(fromk)
            from datetime import time
            x = time (hour = 5)
            print(out)
            print(x)

        elif selection ==16:
            print("You have chosen the Global keyword")
            globalk=("and global\nThe global keyword is used to create global variables from a no-global scope, e.g. inside a function.\nCode:\ndef cmmmsfunction()\n   global x\n  x = int4\ncmmmsfunction():\nprint(x)")
            print(globalk)
            print(out)
            def cmmmsfunction():
                global x
                x = int4
                cmmmsfunction()
                print(x)

        elif selection ==17:
            print("You have chosen the If keyword")
            fk=("if keyword\nThe if keyword is used to create conditional statements (if statements), and\nallows you to execute a block of code only if a condition is True. Use the else keyword to\nexecute code if the condition is False.\nCode:\nx = in1\nif x > in2:\n   print(“TRUE”)\n else:\n     print(""FALSE"")")
            print(fk)
            print(out)
            x = in1
            if x > in2:
                print("TRUE")
            else:
                print("FALSE")

        elif selection ==18:
            print("You have chosen the Import keyword")
            importk=("import keyword\nThe import keyword is used to import modules.\nCode:\nimport datetime\nx = datetime.datetime.now()\nprint(x)")
            print(importk)
            import datetime
            x = datetime.datetime.now()
            print(out)
            print(x)

        elif selection ==19:
            print("You have chosen the In keyword")
            ink=("in keyword\nIn python, the in keyword has two purposes: (1) It is used to check if a value is present in a sequence (list,range, string etc.)\nand (2) It can also be used to iterate through a sequence in a for loop.\nCode:\nx = [in1, in2, in3] \nif in2 in x:, \nprint(“TRUE”)")
            print(ink)
            print(out)
            x = [in1, in2, in3, in4, in5]
            if in2 in x:
                print("TRUE")
                
        elif selection ==20:
            print("You have chosen the Is keyword")
            isk=("is keyword\nThe is keyword is used to test if two variables refer to the same object.\nCode:\nx = [in, in2, in3, in4, in5]\ny = x\nprint(x is y)")
            print(isk)
            x = [in1, in2, in3, in4, in5]
            y = x
            print(out)
            print(x is y)
            
        elif selection ==21:
            print("You have chosen the Lambda keyword")
            lambdak=("lambda keyword\nThe lambda keyword is used to create small anonymous functions.\nA lambda function can take any number of arguments, but can only have one expression.\nThe expression is evaluated and the result is returned.\nCode:\nx = lambda a : a + in1\nprint(x(in2))")
            print(lambdak)
            x = lambda a : a + in1
            print(out)
            print(x(in2))

        elif selection ==22:
            print("You have chosen the None keyword")
            nonek=("None keyword\nThe None keyword is used to define a null value, or no value at all.\nNone is not the same as 0, False, or an empty string.\nNone is a data type of its own (NoneType) and only None can be None.\nCode:\nx = None\nprint(x)")
            print(nonek)
            x = None
            print(out)
            print(x)

        elif selection ==23:
            print("You have chosen the Nonlocal keyword")
            nonlocalk=("Nonlocal Keyword\nThe nonlocal is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.")
            print(nonlocalk +"\n")
            print("Code:")
            print("def myfunc1():")
            print("    x = in4")
            print("    def myfunc2():")
            print("        nonlocal x")
            print("        x = in5")
            print("    def myfunc2():")
            print("    return x")
            print("print(myfunc1())")
            print("\n Output:\n")
            def  myfunc1():
                x = in4
                def myfunc2():
                    nonlocal x
                    x = in5
                    myfunc2()
                    return x
                print(myfunc1())
                
        elif selection ==24:
            print("You have chosen the Not keyword")
            notk=("Not Keyword\nThe not keyword is a logical operator. The return value will be True if the statement(s) are not True, otherwise it will return False.")
            print(notk +"\n")
            print("Code:")
            print("x = false")
            print("print(not x)")

        elif selection ==25:
            print("You have chosen the Or keyword")
            ork=("Or Keyword\nThe or keyword is a logical operator. Logical operators are used to combine conditional statements. The return value will be True if one of the statements return True, otherwise it will return False.")
            print(ork +"\n")
            print("Code:")
            print("x = (in1 > in2 or in3)")
            print("print(x)")
            print("\nOutput:")
            x = (in1 > in2 or in3)
            print(x)

        elif selection ==26:
            print("You have chosen the Pass keyword")
            passk=("Pass Keyword\nThe pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.\n Note that in python, empty code is not allowed in loops, function definitions, class definitions, or in if statements.")
            print(passk +"\n")
            print("Example Code:")
            print("for x in [in1, in2, in3];")
            print("    pass")
            print("def myfunction:")
            print("    pass")
            print("Class Person")
            print("    pass")

        elif selection ==27:
            print("You have chosen the Raise keyword")
            raisek=("Raise Keyword\nThe raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.")
            print(raisek +"\n")
            print("Code:")
            print("x = in1")
            print("if x < 0:")
            print(" raise Exception(\"Sorry, no numbers below zero\")")
            print("\nOutput:")
            x = in1
            if x < 0:
                raise Exception("Sorry, no numbers below zero.")

        elif selection ==28:
            print("You have chosen the Return keyword")
            returnk=("Return Keyword\nThe return keyword keyword is use to exit a function and return a value.")
            print(returnk +"\n")
            print("Code:")
            print("def myfunction():")
            print(" return in1+in2")
            print("print(myfunction())")
            print("\nOutput:")
            def myfunction():
                return in1+in2
            print(myfunction())

        elif selection ==29:
            print("You have chosen the True keyword")
            truek=("True Keyword\nThe true keyword is a Boolean value, and result of a comparison operation. The True keyword is the same as 1 (False is the same as 0).")
            print(truek +"\n")
            print("Code:")
            print("print(in1 > in2)")
            print("Note: if in1 is greater than in2, Output should be true")
            print("\nOutput:")
            print(in1 > in2)

        elif selection ==30:
            print("You have chosen the Try keyword")
            tryk=("Try Keyword\nThe try keyword is used in try...except blocks. It defines a block of code test if it contains any errors. You can define different blocks for different error types, and blocks to execute if nothing went wrong.")
            print(tryk +"\n")
            print("Code:")
            print("try:")
            print(" in1 > 3")
            print("except:")
            print("print(\"Something went wrong\")")
            print("\nOutput:")
            try:
                in1 > 3
            except:
                print("Something went wrong")

        elif selection ==31:
            print("You have chosen the and While keyword")
            whilek=("While Keyword\nThe while keyword is used to create a while loop. A while loop will continue until the statement is false.")
            print(whilek +"\n")
            print("Code:")
            print("in1 = 0")
            print("\n")
            print("while in1 < 9:")
            print(" print(in1)")
            print(" in1 = in1 + 1")
            print("\nOutput:")
            while in1 < 9:
                print(in1)
                in1 = in1 + 1

        elif selection ==32:
            print("You have chosen the With keyword")
            withk=("With Keyword\nThe with keyword is used to simplify exception handling.")
            print(withk +"\n")
            print("Code:")
            print("with open('cmmms.txt','w') as my file")
            print(" myfile.write(\"Hello World!\")")
            print("\nOutput:")
            print("cmmms.txt file should have a \"Hello World!\" text.")

        elif selection ==33:
            print("You have chosen the Yield keyword")
            yieldk=("Yield Keyword\nThe yield keyword is use to exit a function and return a generator.")
            print(yieldk +"\n")
            print("Code:")
            print("def function1():")
            print(" for a in range(in1):")
            print("     yield a*a")
            print("f = function1()")
            print("for a in f:")
            print("print(a)")
            print("\nOutput:")
            def function1():
                for a in range(6):
                    yield a*a
                f = function1()
                for a in f:
                    print(a)
        
    elif choice ==2:
        andk=("and keyword\nThe and keyword is a logical operator. Logical operators are used to combine conditional statements.\nCode:\nx = (in1 > in2 and in1 < in3)\nprint(x)")
        print(andk)
        x = (in1 > in2 and in1 < in3)
        print(out)
        print(x)
        print("\n")
        
        ask=("as keyword\nThe as keyword is used to create an alias.\nCode:\nimport calendar as c\n            print(c.month_name[12])")
        print(ask)
        import calendar as c
        print(out)
        print(c.month_name[12])
        
       
        assk=("assert keyword\nThe assert keyword is used when debugging code. The assert keyword lets you test if a condition\nin your code returns True, if not, the program will raise an Assertion Error.\nYou can write a message to be written if the code returns False.\nCode:\nTRUE\nx = in4\nassert x == in4\nFALSE\nassert x == in5")
        print(assk)
        x = in4
        print(out)
        print("TRUE")
        
        brk=("break keyword\nThe break keyword is used to break out or end a loop.\nCode:\nfor i in range (in1):\n   if i > 5:\n     break\n print(i)")
        print(brk)
        for i in range (in1):
            if i > 5:
                break
            print(out)
            print(i)
        
        clsk=("class keyword\nThe class keyword is used to create a class. A class is like an object constructor.\nCode:\nclass Element:\n  el1 = in1\n el2 = in2\n el3 = in3\n el4 = in4\n el5 = in5\n el = Element()\nprint(el.el1, el.el2, el.el3, el.el4, el.el5)")
        print(clsk)
        class Element:
            el1 = in1
            el2 = in2
            el3 = in3
            el4 = in4
            el5 = in5
        el = Element()
        print(out)
        print(el.el1, el.el2, el.el3, el.el4, el.el5)
        
        conk=("continue keyword\nThe continue keyword is used to end the current iteration in a loop\n(a for loop or a while loop), and continues to the next iteration.\nCode:\nfor i in range (in1):\n    if i == 5:\n        continue\n  print(i)")
        print(conk)
        for i in range (in1):
            if i == 5:
                continue
            print(out)
            print(i)
            
        defk=("def keyword\nThe def keyword is used to create, (or define) a function.\nCode:\ndef cmmms_function():\n print(in1, in2, in3, in4, in5)\ncmmms_function()")
        print(defk)
        def cmmms_function():
            print(out)
            print(in1, in2, in3, in4, in5)
            cmmms_function()
            
        delk=("del keyword\nThe del keyword is used to delete objects. In Python everything is an object,\nso the del keyword can also be used to delete variables, lists, or parts of a list etc.\nCode:\Deleting a Whole Class\nclass Element:\n  el1 = in1\n el2 = in2\n el3 = in3\n el4 = in4\n el5 = in5\ndel Element\nprint(Element)\n\nDeleting a Specific Variable\nx = in1\ndel x\nprint(x)")
        print(delk)
        class Element:
            el1 = in1
            el2 = in2
            el3 = in3
            x = in4
            el5 = in5
        print(out)
        print ("Deleting a Whole Class")
        del Element
        print("NameError: name 'Element' is not defined")
        print("\nDeleting a Specific Variable")
        x = in4
        del x
        print("NameError: name 'x' is not defined")
        
        elifk=("elif keyword\nThe elif keyword is used in conditional statements (if statements), and is short for else if.\nCode:\nfor i in range (-5, 5):\n   if i > 0:\n     print(in1)\n    elif i == 0:\n      print(in2)")
        print(elifk)
        print(out)
        for i in range (-5, 5):
            if i > 0:
                print(in1)
            elif i == 0:
                print(in2)
             
            
        elsek=("else keyword\nThe else keyword is used in conditional statements (if statements), and decides\nwhat to do if the condition is False. The else keyword can also be used in try...except blocks.\nCode:\nx = in1\ntry:\n  x > in2\nexcept:\n  print(""Something went wrong."")\nelse:\n print(""Code executed with no errors."")")
        print(elsek)
        print(out)
        x = in1
        try:
            x > in2
        except:
            print("Something went wrong.")
        else:
            print("Code executed with no errors.")
        
        eptk=("except keyword\nThe except keyword is used in try...except blocks. It defines a block of code to run if the try block raises an error.\nYou can define different blocks for different error types, and blocks to execute if nothing went wrong.\nCode:\ntry:\n   x > in1\nexcept:\n  print(""Something went wrong."")")
        print(eptk)
        print(out)
        try:
            x > in1
        except:
            print("Something went wrong.")          
        
        falsek=("False keyword\nThe False keyword is a Boolean value, and result of a comparison operation. The False keyword is the same as 0.\nCode:\ nprint(10 > 12)")
        print(out)
        print(falsek)
        print(10 > 12)

        finallyk=("finally keyword\nThe finally keyword is used in try...except blocks. It defines a block of\n code to run when the try...except...else block is final. The finally block will be executed no\n matter if the try block raises an error or not. This can be useful to close objects and clean up resources.\nCode:\ntry:\n x > 3 except:\n print(“something went wrong)\nelse:\n   print (“Nothing went wrong”)\nfinally:\n    print(“The try...except block is finished”)")
        print(finallyk)
        print(out)
        try:
            x > 3
        except:
            print("something went wrong")
        else:
            print ("Nothing went wrong")
        finally:
            print("The try...except block is finished")
        
        fork=("for keyword\nThe For keyword is used to create a for loop. It can be used to iterate through a sequence, like a list, tuple, etc.\nCode:\nfor x in range = (1,9):\n   print(x)")
        print(fork)
        for x in range (1,9):
            print(out)
            print(x)
        
        fromk=("from keyword\nThe from keyword is used to import only a specified section from a module. \nCode:\nfrom datetime import time\nx = time (hour = 5)\nprint(x)")
        print(fromk)
        from datetime import time
        x = time (hour = 5)
        print(out)
        print(x)
        
        globalk=("and global\nThe global keyword is used to create global variables from a no-global scope, e.g. inside a function.\nCode:\ndef cmmmsfunction():\n   global x\n  x = int4\ncmmmsfunction()\nprint(x)")
        print(globalk)
        print(out)
        def cmmmsfunction():
            global x
            x = int4
            cmmmsfunction()
            print(x)
        
        ifk=("if keyword\nThe if keyword is used to create conditional statements (if statements), and\nallows you to execute a block of code only if a condition is True. Use the else keyword to\nexecute code if the condition is False.\nCode:\nx = in1\nif x > in2:\n  print(“TRUE”)\n else:\n     print(""FALSE"")")
        print(ifk)
        print(out)
        x = in1
        if x > in2:
            print("TRUE")
        else:
            print("FALSE")
        
        importk=("import keyword\nThe import keyword is used to import modules.\nCode:\nimport datetime\nx = datetime.datetime.now()\nprint(x)")
        print(importk)
        import datetime
        x = datetime.datetime.now()
        print(out)
        print(x)
        
        ink=("in keyword\nIn python, the in keyword has two purposes: (1) It is used to check if a value is present in a sequence (list,range, string etc.)\nand (2) It can also be used to iterate through a sequence in a for loop.\nCode:\nx = [in1, in2, in3] \nif in2 in x:, \nprint(“TRUE”)")
        print(ink)
        print(out)
        x = [in1, in2, in3, in4, in5]
        if in2 in x:
            print("TRUE")
        
        isk=("is keyword\nThe is keyword is used to test if two variables refer to the same object.\nCode:\nx = [in, in2, in3, in4, in5]\ny = x\nprint(x is y)")
        print(isk)
        x = [in1, in2, in3, in4, in5]
        y = x
        print(out)
        print(x is y)
        
        lambdak=("lambda keyword\nThe lambda keyword is used to create small anonymous functions.\nA lambda function can take any number of arguments, but can only have one expression.\nThe expression is evaluated and the result is returned.\nCode:\nx = lambda a : a + in1\nprint(x(in2))")
        print(lambdak)
        x = lambda a : a + in1
        print(out)
        print(x(in2))
    
        nonek=("None keyword\nThe None keyword is used to define a null value, or no value at all.\nNone is not the same as 0, False, or an empty string.\nNone is a data type of its own (NoneType) and only None can be None.\nCode:\nx = None\nprint(x)")
        print(nonek)
        x = None
        print(out)
        print(x)
        
        nonlocalk=("Nonlocal Keyword\nThe nonlocal is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.")
        print(nonlocalk +"\n")
        print("Code:")
        print("def myfunc1():")
        print("    x = in4")
        print("    def myfunc2():")
        print("        nonlocal x")
        print("        x = in5")
        print("    def myfunc2():")
        print("    return x")
        print("print(myfunc1())")
        print("\n Output:\n")
        def  myfunc1():
            x = in4
            def myfunc2():
                nonlocal x
                x = in5
                myfunc2()
                return x
            print(myfunc1())
        
        ork=("Or Keyword\nThe or keyword is a logical operator. Logical operators are used to combine conditional statements. The return value will be True if one of the statements return True, otherwise it will return False.")
        print(ork +"\n")
        print("Code:")
        print("x = (in1 > in2 or in3)")
        print("print(x)")
        print("\nOutput:")
        x = (in1 > in2 or in3)
        print(x)
        
        passk=("Pass Keyword\nThe pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.\n Note that in python, empty code is not allowed in loops, function definitions, class definitions, or in if statements.")
        print(passk +"\n")
        print("Example Code:")
        print("for x in [in1, in2, in3];")
        print("    pass")
        print("def myfunction:")
        print("    pass")
        print("Class Person")
        print("    pass")
        
        raisek=("Raise Keyword\nThe raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.")
        print(raisek +"\n")
        print("Code:")
        print("x = in1")
        print("if x < 0:")
        print(" raise Exception(\"Sorry, no numbers below zero\")")
        print("\nOutput:")
        x = in1
        if x < 0:
            raise Exception("Sorry, no numbers below zero.")
        
        returnk=("Return Keyword\nThe return keyword keyword is use to exit a function and return a value.")
        print(returnk +"\n")
        print("Code:")
        print("def myfunction():")
        print(" return in1+in2")
        print("print(myfunction())")
        print("\nOutput:")
        def myfunction():
            return in1+in2
        print(myfunction())
        
        truek=("True Keyword\nThe true keyword is a Boolean value, and result of a comparison operation. The True keyword is the same as 1 (False is the same as 0).")
        print(truek +"\n")
        print("Code:")
        print("print(in1 > in2)")
        print("Note: if in1 is greater than in2, Output should be true")
        print("\nOutput:")
        print(in1 > in2)
        
        tryk=("Try Keyword\nThe try keyword is used in try...except blocks. It defines a block of code test if it contains any errors. You can define different blocks for different error types, and blocks to execute if nothing went wrong.")
        print(tryk +"\n")
        print("Code:")
        print("try:")
        print(" in1 > 3")
        print("except:")
        print("print(\"Something went wrong\")")
        print("\nOutput:")
        try:
            in1 > 3
        except:
            print("Something went wrong")
        
        whilek=("While Keyword\nThe while keyword is used to create a while loop. A while loop will continue until the statement is false.")
        print(whilek +"\n")
        print("Code:")
        print("in1 = 0")
        print("\n")
        print("while in1 < 9:")
        print(" print(in1)")
        print(" in1 = in1 + 1")
        print("\nOutput:")
        while in1 < 9:
            print(in1)
            in1 = in1 + 1
            
        withk=("With Keyword\nThe with keyword is used to simplify exception handling.")
        print(withk +"\n")
        print("Code:")
        print("with open('cmmms.txt','w') as my file")
        print(" myfile.write(\"Hello World!\")")
        print("\nOutput:")
        print("cmmms.txt file should have a \"Hello World!\" text.")
        
        yieldk=("Yield Keyword\nThe yield keyword is use to exit a function and return a generator.")
        print(yieldk +"\n")
        print("Code:")
        print("def function1():")
        print(" for a in range(in1):")
        print("     yield a*a")
        print("f = function1()")
        print("for a in f:")
        print("print(a)")
        print("\nOutput:")
        def function1():
            for a in range(6):
                yield a*a
            f = function1()
            for a in f:
                print(a)
elif selection != (1,8):
    print("Choose from 1 to 8 only")
    print(mainMenu())







