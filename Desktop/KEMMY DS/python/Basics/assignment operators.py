# Assignment operators
sum=5
sum+=6
print(sum)
# multipy given that we have two products a laptop and a mouse such that the price of the laptop is 300,000and the price of a mouse is 50,000
# use a for loop to find the total sum of the products
laptop=300000
mouse=50000
sum = 0 #laptop + mouse
prices=[300000,50000]
product_prices=[laptop,mouse]
for price in product_prices:
    sum+=price
print(f"The total sum of the price{sum:,}")
# the variables should be defined out of the loop scoop(anything within the indentation affects it)

