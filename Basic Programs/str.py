# str=Kumar   This is Invalid in python.
# In python, strings are any characters represented within single or double quotes

str1='Kumar'      
str2="Kumar"  
  
str3="'Kumar'"     
str4='"Kumar"'     
# print(str)
print(str1)
print(str2)
print(str3)
print(str4)



# Multiline String Literals

# type 1
mul = """
    Kumar
        Deepak
            Mohanty """
print(mul)

# type 2
mul1= '''
    Hi
      I am Kumar
                From Balasore'''
print(mul1)

name = '''Hi Guys I am "Kumar" from 'balasore' '''
print(name)

name1='My name is \'Kumar Deepak \'  '
print(name1)

naam="DEEPAK"
print(naam[0])
print(naam[-6])
print(naam[1])
print(naam[-5])
print(naam[3])
print(naam[-3])

op= naam[0]+ naam[1:5].lower()+ naam[len(naam)-1]
print(op)

