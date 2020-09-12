name = input("enter the name :")
dob = input("enter the dob [dd--mm-yyyy] :")
contact = input("enter the contact number:")
d = dob.split("-")
password = contact[:3] + name[-3:] + d[2]
print("YOUR PASSEWORD IS :", password)
