# control flow structures
# it determines the order in which code is executed basing on loops and conditions
#conditional statements # these are statements that base on a particular condition eg if,elif,else
# if condition is executed only  when the condition is true


# create a program that asks a user  for the food type bought in the market ,the programe should print you bought chicken if the user 
#enters chicken and liver when the user enters liver and else if the user enters fish
food_type=(input("Enter the food type")).lower()
if food_type!='chicken'or food_type!='liver'or food_type!='fish':
    print('Please choose from chicken,liver or fish')
if food_type=='chicken':
    print("You bought chicken in the market")
elif food_type=='liver':
    print("you bought liver in the market")
else:
    print('You bought fish from the market ')
    # Approach 2
   # food_type=(input("Enter the food type")).lower()
#if food_type=='chicken':
 #   print("You bought chicken in the market")
#elif food_type=='liver':
 #   print("you bought liver in the market")
#elif food_type=='fish':
 #   print('you bought fish from the market')
#else:
 #   print('Please choose from the above chicken,liver or fish ')
    
    
