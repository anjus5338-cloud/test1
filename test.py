#Q1. CSV file ko Pandas DataFrame me load karo aur first 5 rows dekho.
import pandas as pd
df = pd.read_csv("Heart_Disease_Prediction.csv")
print(df.head())

'''Q2. Dataset ka shape check karo:
    - Total rows kitni hain?
    - Total columns kitne hain?'''
x= df.shape
print(x)

#Q3. Dataset ke saare column names list karo
x1 = df.columns
print(x1)

'''Q4. Dataset me missing values detect karo.
    - Kaun-kaun se columns me missing values hain?'''
x2 = df.isnull()
print(x2)

#Q5. Har column me kitne missing values hain, ye find karo.
x3 = x2.sum()
print(x3)

#Q6. Har column ke missing values ka percentage calculate karo.

#Q7. Dataset me total duplicate rows kitni hain?
x5 = df.duplicated().sum()
print(x5)

'''Q8. Duplicate rows ko dataset se remove karo
    aur naya shape check karo.'''
x6 = df.drop_duplicates()
print(x6.shape)

#Q9. Numeric columns aur categorical columns ko identify karo.
x7 = df.describe()
print(x7)

x8 = df.value_counts()
print(x8)

'''Q10. Numeric columns ke missing values ko
     mean ya median se fill karo'''
print(df[x7].fillna(df[x7].mean()))

'''Q11. Categorical columns ke missing values ko
     mode se fill karo'''
print(df[x7].fillna(df[x7].mean()))

'''Q12. Verify karo ki ab dataset me
     koi missing value nahi bachi hai.'''
     
#Q13. Heart disease prediction ka target column kaunsa hai?
#Q14. Target column ka distribution find karo
     #(Heart Disease = 0 aur 1 ka count).
'''Q15. Patients ki:
     - Average age
     - Minimum age
     - Maximum age
     find karo'''
x14  = df["Age"].mean()
print(x14)
x15 = df["Age"].min()
print(x15)
x16 = df["Age"].max()
print(x16)

'''Q16. Gender vs Heart Disease ka analysis karo:
     - Male aur Female count
     - Kis gender me heart disease zyada hai?'''
male = 0
female = 0
for i in df["Sex"]:
    if i == 1:
        female+=1
    else:
        male+=1
print(female)
print(male)

#Q17. Age ke basis par Heart Disease ka trend analyze karo.
age = df["Age"]
Heart_Disease = df["Heart Disease"]
unique_age = age.unique
count= 0
for x in age:
    for y in Heart_Disease:
        if x > 50 or y == "Present":
            count+=1
        else:
            count+=1
print(count)
            
        
    


        
        
        
        
        
    
    
    
'''Q18. Cholesterol ke basis par check karo
     ki high cholesterol walon me
     heart disease zyada hai ya nahi.'''
     
    

        
        
      

