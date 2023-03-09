
#metacharacters
# .--period
# ^--starting point 
# $--ending point
#[]--range
# s='hello'#if 7hello then match it 
# pattern='[0-9]'
# a=re.match(pattern,s)
# if a:
#     print('matched')
# else:
#     print('not matched')


#email
import re
def validate_email(email):
    if(re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")
validate_email("dani123@gmail.com")
validate_email("dani123gmail.com.in")









#phone number
import re
def validate_number(number):
    if(re.search(r'^\+91-?\d{4}-?\d{3}-?\d{3}$|^0?\d{4}-?\d{3}-?\d{3}$',number)):  
        print("Valid Number")  
          
    else:  
        print("Invalid Number")
validate_number("1234567890")
validate_number("12344567890")











