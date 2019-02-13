#Input Details
qty=[2.0,5.2,7.3,2.2,3.1,4.0]
price=[10.0,45.0,34.0,51.0,23.0,56.0]
sl=[1,2,3,4,5,6]
print("VIJETHA".center(50))
print("SUPER MARKET".center(50,'*'))
print("Date:- 10 Feb 2019".rjust(50))
print("-"*50)
print("SL\tDescription\tQty\t Unit Rate\tTotal Cost\n")
#Calculating the Total price
a=qty[0]*price[0]
b=qty[1]*price[1]
c=qty[2]*price[2]
d=qty[3]*price[3]
e=qty[4]*price[4]
f=qty[5]*price[5]
#Printing the grocery along with price details
print(f"{sl[0]}    \t Sugar \t {qty[0]} \t {price[0]} \t {a}")
print(f"{sl[1]}    \t dal   \t {qty[1]} \t {price[1]} \t {b}")
print(f"{sl[2]}    \t salt  \t {qty[2]} \t {price[2]} \t {c}")
print(f"{sl[3]}    \t soups \t {qty[3]} \t {price[3]} \t {d}")
print(f"{sl[4]}    \t kaju  \t {qty[4]} \t {price[4]} \t {e}")
print(f"{sl[5]}    \t pista \t {qty[5]} \t {price[5]} \t {f}")
print("-"*50)
n=a+b+c+d+e+f #Sum of all items
GST=n*0.03    #Calculating the GST@3%
total=n+GST
print("Sub Total is    \t            {}".format(round(n,2)))
print("GST@ 3%\t\t\t\t\t\t\t",round(GST,2))
print("-"*50)
print("Total \t"'%.2f' % total)
