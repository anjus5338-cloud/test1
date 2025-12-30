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
x4 =( df.isnull().sum()/len(df))*100
print(x4)


#Q7. Dataset me total duplicate rows kitni hain?
x5 = df.duplicated().sum()
print(x5)

'''Q8. Duplicate rows ko dataset se remove karo
    aur naya shape check karo.'''
x6 = df.drop_duplicates()
print(x6.shape)

#Q9. Numeric columns aur categorical columns ko identify karo.
x7 = df.select_dtypes(include="number").columns
print(x7)
x8 = df.select_dtypes(include="object").columns
print(x8)


'''Q10. Numeric columns ke missing values ko
     mean ya median se fill karo'''
for col in x7:
    if df[col].isnull().sum()>0:
        x = df[col].mean()
        df[col].fillna(x,inplace = True)
        
print(df.isnull().sum())


'''Q11. Categorical columns ke missing values ko
     mode se fill karo'''
for col in x8:
    if df[col].isnull().sum()>0:
        x = df[col].mean()
        df[col].fillna(x,inplace = True)
        
print(df.isnull().sum())

'''Q12. Verify karo ki ab dataset me
     koi missing value nahi bachi hai.'''
print(df.isnull().sum())

     
#Q13. Heart disease prediction ka target column kaunsa hai?
#Ans."Heart disease"
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
gender_heart = pd.crosstab(df['Sex'],df['Heart Disease'])
print(gender_heart)

#Q17. Age ke basis par Heart Disease ka trend analyze karo.
Age_heart = df.groupby("Heart Disease")["Age"].mean()
print(Age_heart)

    
'''Q18. Cholesterol ke basis par check karo
     ki high cholesterol walon me
     heart disease zyada hai ya nahi.'''
     
Heart_disease = df.groupby("Heart Disease")['Cholesterol'].mean()
print(Heart_disease)

#Q19.Blood pressure inka heart disease se relation analyze kro
blood_pressure = df.groupby("Heart Disease")["BP"].mean()
print(blood_pressure)

x18 = x6.to_csv("clean_data.csv", index=False)


     
    

        
        
      

