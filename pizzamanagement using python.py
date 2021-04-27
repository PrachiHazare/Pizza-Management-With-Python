customerid="CUSTOMER1"
customerpass="PASSWORD"
adminid="ADMIN"
adminpass="ADMIN"
Vegpizza=10
Nonvegpizza=10

while True:
  print("Press 1. for customer, 2. for admin 3. to exit")
  main=input()
  if main=="3":
    break
  elif main=="1":
    while True:
      print("Enter user Id or type BACK to go back: ")
      uid=input().upper()
      if uid=="BACK":
        break
      elif uid==customerid:
        print("Enter Password: ")
        pwd=input().upper()
        if pwd==customerpass:
          print("Welcome",uid)
          print("Press 1 to view menu, 2 to order")
          v=input()
          if v=="1":
            print(f"Veg Pizza's: {Vegpizza} \nNon veg pizza's: {Nonvegpizza}")
          elif v=="2":
            print("Press 1 to order veg, Press 2 to order non-veg")
            ch=input()
            if ch=="1":
              print("Enter Number of veg pizzas you would order: ")
              n=int(input())
              Vegpizza-=n 
              print(f"{n} veg pizza's ordered")
            elif ch=="2":
              print("Enter Number of non-veg pizzas you would order: ")
              n=int(input())
              Nonvegpizza-=n 
              print(f"{n} non-veg pizza's ordered")
            else:
              print("Invalid Choice")
          else:
            print("Invalid Choice")
        else:
          print("Wrong Password")
      else:
        print("Wrong Id")
  elif main=="2":
    while True:
      print("Enter user Id or type BACK to go back: ")
      aid=input().upper()
      if aid=="BACK":
        break
      elif aid==adminid:
        print("Enter Password: ")
        pwd=input().upper()
        if pwd==adminpass:
          print("Welcome",aid)
          print("Press 1 to view menu, 2 to manage stocks")
          v=input()
          if v=="1":
            print(f"Veg Pizza's: {Vegpizza} \nNon veg pizza's: {Nonvegpizza}")
          elif v=="2":
            print("Press 1 to manage veg, Press 2 to manage non-veg")
            ch=input()
            if ch=="1":
              print("Enter Number of veg pizzas you would add: ")
              n=int(input())
              Vegpizza+=n 
              print(f"{n} veg pizza's added, No of veg pizza: {Vegpizza}")
            elif ch=="2":
              print("Enter Number of non-veg pizzas you would add: ")
              n=int(input())
              Nonvegpizza+=n 
              print(f"{n} non-veg pizza's added, No of non veg pizza's: {Nonvegpizza}")
            else:
              print("Invalid Choice")
          else:
            print("Invalid Choice")
        else:
          print("Wrong Password")
      else:
        print("Wrong Id")
  else:
    print("Invalid choice")

