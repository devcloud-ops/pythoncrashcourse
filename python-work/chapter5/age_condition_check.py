age_faisal=40
age_abdullah=12

corret_statement=' '.join(("\nthat is correct, Faisal's age is more than 30",
                           "and Abdullah's age is less than 40"))

if (age_faisal >= 30) and (age_abdullah<=40):
    print(corret_statement)
    
if (age_faisal >= 30) and (age_abdullah<=11):
    print('that is not the correct answer!')
