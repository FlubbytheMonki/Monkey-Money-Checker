account = input("Do you have an account? [Y/N]")


if account.lower() == "y":
  username = input("What is your username?")
  password = input("What is your password?")

  
  if username == "flub" and password == "monkeys":
    print("Welcome,",username,"!")
  else:
    print("No such account exists. Please try again.")


elif account.lower() == "n":
  account_ask = input("Would you like to create an account? [Y/N]")
  if account_ask.lower() == "y":
    new_username = input("What would you like your username to be?")
    new_password = input("What would you like your password to be?")
    

