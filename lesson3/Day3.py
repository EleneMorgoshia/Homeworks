# print("this is a lesson 2 ") 
 
 #  #string and its abilities

# #for short strings
# name="elene" 

# #length of the variable
# print(len(name)) #len-(length) of the variable 

#------------------------------

# #for  longer  strings- use """.........."""
# my_sentence="""Hello,first lesson will be held
# in 19 september,
# pls do not be late""" 
# print(my_sentence)

#--------------------------------
# knows_programing=True

# if True:
#     print("hello") #indentation by using tab

#-------------------------------

# full_name="Elene Morgoshia" #5+1(space)+9=15
# print(len(full_name))

# #every string should be realised as a list
# print(full_name[0]) #the first index
# print(full_name[6]) #do not forget the space!


#------------------------------
# #how to print the letter from  string
# full_name="Elene Morgoshia"
# print("l"in full_name) 
# print("M"not in full_name) 

#--------------------------------

#how to slice strings
# full_name="Elene Morgoshia"
# print(full_name[2:9]) #starting  with 2 and ending  with 8
# # print(full_name[2:9:2]) #guideline of skiiping letters: #start:finish:step
# print(full_name[0:15]) 
# print(full_name[:6]) 

# ----------------------------------
#printing the negative index

# full_name="Elene Morgoshia"
# print(full_name[-1]) #[-1]-printing the last letter
# print(full_name[-4]) # s
# print(full_name[-4]+"abc")
# print(full_name[-1:-6:-2])

# ---------------------------------------
#methods of string 
# 1)string.upper()
# 2)len(string)

# full_name="Elene Morgoshia"
# print(full_name.upper()) #incrreasing the letters
# full_name2="ELENE MORGOSHIA"
# print(full_name2.lower())

# # STRIP
# full_name3="  ELENE    "
# print(full_name3.strip()) #cutting the space
 
# #REPLACE (1)Something that will be changed 2)New variable )
# print(full_name2.replace(" ","#")) 
# print(full_name2.replace("E","#"))

#-----------------------------------------
# REVIEW
# 1)Short strings and long strings- using""" fot longer one

# 2)Function len- length of a variable .   len(variable)

# 3)IF statement - if True:, or if False: 
#                       print("something") - do not forget to make space 

# 4)printing a length of a long string- do not miss a "space" while counting  letters 

# 5)Positions(Indexes) of  letters in string-  full_name[0]-the first letter

# 6)printing letters from string- print("letter"in string) or print("letter"not in string)
#                        The result is True-if there is the letter you want, False-if there is not the letter you are looking for.

# 7)Slicing strings-  print(full_name[2:9])- starting  with 2 and ending  with 8 -RULE
#   Print(full_name[:5])=[from 0 to 4] print(full_name[2:])=[from 2 to the last letter]

# 8)guideline of skiiping letters- print(full_name[2:9:2]) START-FINISH-STEP

# 9)printing the negative index- print(full_name[-1])-printing the last letter

#10)string.upper - encreasing the letters
#11)string.lower-decreasing the letters
#12)STRIP-cutting the space
#13)replace-replacing the variable to another variable.

#-------------------------------
#HOMEWORK

is_longstring="""Choosing profession is one of the most important dicisions in your life. 
It is the time , when you are leading not just with  your passion,but also the job perspective . That's why, you should try to find 
a job,which will be a mix of 2 valuable things. First- love and interest  in the spacific field , second- High INCOME """

print(is_longstring[-1])





print(is_longstring)

name="Elene Morgoshia"
print(len(name))
print(name[0])
print(name[14])
print(name[0:15])
print(name[0:15:2])
print(name.lower()) #do not forget ()
name2="IOANE"
print(name2.upper())
if  True:
       print("YES")

print(name2.replace("I",":)"))
print(name2.replace("E",""))
print(is_longstring.replace("o",":)"))
print(is_longstring.upper())
print(is_longstring.lower())
print(is_longstring[0:20:2])
print(is_longstring[:30])
print(is_longstring[30:40])
print("I"in is_longstring)
print("k"not in is_longstring)
print(is_longstring[-1:-3:-10]+"abcd")

name3="  M O R G O   "
print(name3.strip()) #what if i have space in between string letters-  It will not remove spaces between the letters!
print(name3.replace(" ",""))