from UHF_Reader import *

### determine places with corresponding Tag ID
### place = {"ID1":"placeName1" , "ID2":"placeName2" , ... }
place = {"3000E2000019601002092630BB145FEB":"F201" , "3000E2000019601002102630BBB9978A":"F202" ,
         "3000E2000017840D014626700B60097B":"F016" , "3000E2000017840D015026700B6E216A":"F014" ,
         }

while True:
    ID = getID()                         ### read Tag
    if (ID!=""):                         ### if there is tag exist
        if ID in place:
            placeName = place[ID]                     ### get place name
            print(ID , "    " , placeName)            ### show ID , its place
        else:
            print(ID , "    " , "**Unknown place**")  ### show ID , place is not registered (*Unknown*)
           
