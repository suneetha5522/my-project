# printing the bill including GST for super market

qty, price, sl = [2.458624586, 5.245816, 7.458632, 2.78636423, 3.45862, 4.4586621456], [10.4786526, 45.489626, 34.48622,
                  51.48622, 23.4826568, 56.789566], [1, 2, 3, 4, 5, 6]

print('%25s'%"VIJETHA")
print('%25s'%"SUPER MARKET")
print('%30s'%"Date:- 10 Feb 2019")
print("-"*50)
print("SL\tDescription \tQty\t Unit Rate\tTotal Cost\n")
# Calculating the Total price

a,b,c,d,e,f=qty[0]*price[0],qty[1]*price[1],qty[2]*price[2],qty[3]*price[3],qty[4]*price[4],qty[5]*price[5]

# Printing the grocery along with price details

print('%.2d'%sl[0]+"%11s" % 'Sugar'+ '\t' '%.2f'%qty[0]+'\t' '%.2f'%price[0]+'\t' '%.2f'%a)
print(f"{'%.2d'%sl[1]}    \t Sugar \t {'%.2f'%qty[1]} \t {'%.2f'%price[1]} \t {'%.2f'%b}")
print(f"{'%.2d'%sl[2]}    \t salt  \t {'%.2f'%qty[2]} \t {'%.2f'%price[2]} \t {'%.2f'%c}")
print(f"{'%.2d'%sl[3]}    \t soups \t {'%.2f'%qty[3]} \t {'%.2f'%price[3]} \t {'%.2f'%d}")
print(f"{'%.2d'%sl[4]}    \t kaju  \t {'%.2f'%qty[4]} \t {'%.2f'%price[4]} \t {'%.2f'%e}")
print(f"{'%.2d'%sl[5]}    \t pista \t {'%.2f'%qty[5]} \t {'%.2f'%price[5]} \t {'%.2f'%f}")
print("-"*50)

n = a + b + c + d + e + f       # Sum of all items
GST3, GST5, GST8 = (a+b)*(3/100), (c+d)*(5/100), (e+f)*(8/100)
total_GST = GST3 + GST5 + GST8
Grand_total = n+total_GST

# GST = n*(3/100)    #Calculating the GST@3%
print('%0-30s' % "Sub Total is", "{0:.2f}".format(n))
print('%0-30s' % "GST", "{0:.2f}".format(total_GST))
print("-"*50)
print('%0-30s' % "Total", "{0:.2f}".format(Grand_total))


