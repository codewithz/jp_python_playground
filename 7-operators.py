# and
# or
# not

# Loan Processing System.

high_income=False
good_credit=True
student=False
#------------------------------------------------------------
if high_income and good_credit:
    print("Eligible")
else:
    print('Not Eligible')

# -----------------------------------------------------------
if not student:
    print('Eliigible')
else:
    print('Not Eligible')

#--------------------------------------------------------------

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not Eligible')

#-------------------------------------------------------------

#Ternary Operators

age=17;
# message='';
#
# if age>=18:
#     message='Eligible'
# else:
#     message='Not Eligible'

message='Eligible' if age>=18 else 'Not Eligible'
print('Age:',message)


# age = incomingAge!=null? incomingAge:0;

#----------------------------------------------------------------
# Chaining Comparison Operators
# age should be between 18 and 65

# 18 <= age <= 65

age=20;

if 18 <= age <= 65:
    print('Eligible')