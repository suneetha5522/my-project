string1="hello how are you"
string2="PYTHON is a interpreter language"
#print(dir(string))

#capilaze() Method:-
print("python Is Dynamic Language".capitalize())

#Case Fold() Method:-
print("QizzBHHHH".casefold())

#Center method:-
print(string1.center(50,"#"))
print("VIJETHA SUPER MARKET".center(30))

#Count Method:-
print("let it be let it be".count("e",1,40))
print("aeiouaeiou".count("u"))
print(string2.count("r",10,40))

#Encode method:-
print("'pythön!".encode('UTF-8','strict'))
print("'pythön!".encode('ascii','replace'))
print("'pythön!".encode('ascii','xmlcharrefreplace'))
print("'pythön!".encode('ascii','backslashreplace'))
print("'pythön!".encode('ascii','backslashreplace'))
print("pythön!".encode())

#endswith():-
print(string2.endswith("language"))
print((string2.endswith("is",0,20)))

#startswith():-
print("hi good morning".startswith("hi"))
print("hi good morning".startswith("morning",8,20))

#Expand tab:-
print("pyth\t0n".expandtabs(8))

#Find ():-
print("let it be let it be".find("be"))
print("let it be".find("small"))
print("let it be".rfind("small"))

#index():-
print("hi good morning".index("good"))
print("hi good morning".index("good",3,-1))
print("hi good morning".rindex("good"))

#isalnum:-
print("hi23".isalnum())
print("hi 123".isalnum())

#isalpha:-
print("hi".isalpha())
print("hi 123".isalpha())

#isdecimal:-
print("1213".isdecimal())
print("abc123".isdecimal())

#isdigit:-
print("123".isdigit())

#islower:-
print("suneetha".islower())
print("SUNEETHA".islower())

#isprintable:=
print("hi how are".isprintable())
print("hi how are\n".isprintable())
print("  ".isprintable())


#isspace:-
print("hi how are you".isspace())
print("\n\t ".isspace())

#join:-
s1 = "charan"
s2="sankeerth"
sep=","
print(sep.join(s1))
print(s1.join(s2))


#ljust:
print("suneetha".ljust(30,"*"))

#rjust:-
print("charan".rjust(30,"*"))

#strip methods:-
print("   charan     \n".rstrip())

#partition:-
print("hi how are you".partition("how"))
print("hi how are you".rpartition("you"))


#replace:-
print("suneetha charan".replace("charan","nagesh"))
print("let it be let it be".replace("let","don't"))
print("let it be let it be".count("let"))

#split:-
print("suneetha".split())




 # , '', '', '', '',
  #'', '', '', 'rsplit', '', 'split', 'splitlines', '', '', 'swapcase',
  #'', '', '', 'zfill']
""" ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook """
