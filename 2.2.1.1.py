
email = str(input("Enter Your Email : "))
password = str(input("Enter Your Password : "))
  
if userExists(email, password):
      print("Welcome!")
else:
      print("Sorry, Invalid Credentials!")