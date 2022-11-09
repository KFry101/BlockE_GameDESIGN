password= str(hash(input("what is your password? " )))

print(password)

pass2= str(hash(input("what is your password again? " )))

print(pass2)

if (password == pass2):
    print ("they match")
else:
    print("no match")