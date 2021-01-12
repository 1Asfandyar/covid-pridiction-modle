#the dataset was downloaded from 
#kaggle.com  for covid symptoms checker

import pandas as pd #to manage things with dataframe
import numpy as np   #to deal with arrays
import matplotlib.pyplot as plot


#reading data
#
#
#
dataset = pd.read_csv("E:\Probability Quiz\Cleaned-Data.csv")
print("Shape of the original dataset is : ",dataset.shape)

#making a single column of ghender and symptoms
#will swap three columns with 1
Gender = []
for i in range(316800):
    if (dataset["Gender_Female"],1):
        Gender.append(0)
    elif (dataset["Gender_Male"],1):
        Gender.append(1)
    else:
        Gender.append(2)

#Dont know contact will be assumed as no contact 
#will swap three columns wd 1
Contact =[]
for i in range(316800):
    if (dataset["Contact_Yes"],1):
        Contact.append(1)
    else:
        Contact.append(0)

Symp =[]
for i in range(316800):
    if (dataset["None_Sympton"],1):
        Symp.append(0)
    else:
        Symp.append(1)


#When there is no-major or minor symptom
#
#
#
#
NO_symp = [0]*316800
NO_SYMP_COUNTER = 0


for i in range(316800):
    if dataset['Fever'][i]==1:
        continue
    if dataset[ 'Tiredness'][i]==1:
        continue
    if dataset[ 'Dry-Cough'][i]==1:
        continue
    if dataset[ 'Difficulty-in-Breathing'][i]==1:
        continue
    if dataset['Sore-Throat'][i]==1:
        continue
    if dataset[ 'Pains'][i]==1:
        continue
    if dataset[ 'Nasal-Congestion'][i]==1:
        continue
    if dataset[ 'Runny-Nose'][i]==1:
        continue
    if dataset[ 'Diarrhea'][i]==1:
        continue
    NO_symp[i] = 1
    NO_SYMP_COUNTER = NO_SYMP_COUNTER + 1



print(dataset.describe())


Gender = np.array(Gender)
Symp = np.array(Symp)
Contact = np.array(Contact)
NO_symp = np.array(NO_symp)
#excluding non-required columns
#from dataframe
dataset.drop(["Country","None_Sympton",'Contact_Dont-Know', 'Contact_No',
       'Contact_Yes', 'Gender_Female', 'Gender_Male',
       'Gender_Transgender','Severity_Mild', 'Severity_Moderate', 'Severity_None',
       'Severity_Severe',
       'None_Experiencing'],axis='columns',inplace =  True)

#by default shwoing 5 rows
#getting all the columns names
col_names = dataset.keys()
print(col_names)


Contact.reshape([316800,1])
Symp.reshape([316800,1])
Gender.reshape([316800,1])


#checking the arrays/list of the 
#made of the columns needed to be excluded 
    
arr1 = [0]*15

print(dataset.head())

for i in range(316800):
    if dataset['Fever'][i]==1:
        arr1[0] = arr1[0]+1
    if dataset[ 'Tiredness'][i]==1:
        arr1[1] = arr1[1]+1
    if dataset[ 'Dry-Cough'][i]==1:
        arr1[2] = arr1[2]+1
    if dataset[ 'Difficulty-in-Breathing'][i]==1:
        arr1[3] = arr1[3]+1
    if dataset['Sore-Throat'][i]==1:
        arr1[4] = arr1[4]+1
    if dataset[ 'Pains'][i]==1:
        arr1[5] = arr1[5]+1
    if dataset[ 'Nasal-Congestion'][i]==1:
        arr1[6] = arr1[6]+1
    if dataset[ 'Runny-Nose'][i]==1:
        arr1[7] = arr1[7]+1
    if dataset[ 'Diarrhea'][i]==1:
        arr1[8] = arr1[8]+1
    if dataset['Age_0-9'][i]==1:
        arr1[9] = arr1[9]+1
    if dataset[ 'Age_10-19'][i]==1:
        arr1[10] = arr1[10]+1
    if dataset[ 'Age_20-24'][i]==1:
        arr1[11] = arr1[11]+1
    if dataset[ 'Age_25-59'][i]==1:
        arr1[12] = arr1[12]+1
    if dataset[ 'Age_60+'][i]==1:
        arr1[13] = arr1[13]+1

arr1[-1] = NO_SYMP_COUNTER

#age factor is didived in 5 parts so    
#
#Ages columns here are mjutually exclusive among themsselves
#
#first nine columns are oring wd each other but then
# these set of{these coulumns} is mutually exclusive to 
#  the last index
#
#Applying probability concepts
Probabilities = [0]*(len(arr1))
for i in range(len(arr1)):
    if i<9:
        Probabilities[i] = arr1[i]/316800

age_sum = arr1[9]+arr1[10]+arr1[11]+arr1[12]+arr1[13]
symptom = arr1[0]+arr1[5]+arr1[1]+arr1[2]+arr1[3]+arr1[4]+arr1[6]+arr1[7]+arr1[8]+arr1[14]

for i in range(len(arr1)):
    if i<=8 or i == 14:
        Probabilities[i] = arr1[i]/symptom
    else:
        Probabilities[i] = arr1[i]/age_sum
Sum =0
for i in range(len(arr1)):
    Sum =Sum +  Probabilities[i]
    
print(Sum)#######showing 2 but desired is 1

print(Probabilities)

AND_Prob = 1

for i in range(9):
    AND_Prob = Probabilities[i] * AND_Prob 

print("And prob : ",AND_Prob)
OR_prob = 0
for i in range(9):
    OR_prob = Probabilities[i] + OR_prob

#################working fine#################
Total_probg = OR_prob - AND_Prob 

Totali = (Probabilities[-1] + Total_probg)

sum_of_last_or = Probabilities[14] /(Probabilities[14] + Total_probg )
print(Total_probg,'\n',Totali,'\n',sum_of_last_or)

######TEST ALSO WORKED TILL HERE########

for i in range(9):
    try:
        Probabilities[i] = arr1[i]/Totali
    except:
        print('this block cannot execute')

print((Probabilities)

#var = 0

#for i in range(len(arr1)):
#    var = var+  Probabilities[i]

#print(var)


#plotting probability on a bar graph 
#fig = plot.figure()
#plot.bar(col_names,Probabilities)
#plot.title('Probabbilties Values')
#plot.show()