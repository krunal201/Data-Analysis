import pandas as pd
import numpy as np#

df=pd.read_csv('student_performance_large_dataset.csv')
#/print(df.isnull().sum())
df.dropna(inplace=True)

df = df[(df['Age'] > 0) & (df['Study_Hours_per_Week'] >= 0)]
df['Preferred_Learning_Style'] = df['Preferred_Learning_Style'].str.title().str.strip()


######################Discriptive############################
#1
lowest_age= df['Age'].min()
lowest_study_hour= df['Study_Hours_per_Week'].min()
df_subset_1 = pd.DataFrame({
    'Lowest Age': [lowest_age],
    'Lowest Study Hours per Week': [lowest_study_hour]
})

print(df_subset_1)

#2
ps5=df[['Age','Preferred_Learning_Style','Online_Courses_Completed']].head(10)
print(ps5)

#3
df13= df[(df['Attendance_Rate (%)']>50) & (df['Assignment_Completion_Rate (%)']>50)].head(10)
print(df13)

#4
ps14= df[(df['Attendance_Rate (%)'].between(60,70)) & (df['Online_Courses_Completed']>6)]
print(ps14)

#5
p5=df[(df['Study_Hours_per_Week'] > 20) & (df['Online_Courses_Completed'] > 0)]
print(p5[['Study_Hours_per_Week','Online_Courses_Completed']])

#7
# Filter students aged 18 to 21
students_18_21 = df[(df['Age'] >= 18) & (df['Age'] <= 21)]

# Count the most common learning styles
learning_styles_count = students_18_21['Preferred_Learning_Style'].value_counts()
print(learning_styles_count)


#8
avg_study_hour=df['Study_Hours_per_Week'].mean()
study_df=pd.DataFrame(
    {
        'k':['Average Study Hours Per Week'],
        'v':[avg_study_hour]
    }
)
print(study_df)

#9
social=df['Use_of_Educational_Tech'].value_counts(normalize=True)['Yes'] * 100
usage=pd.DataFrame(
    {
        'Use':socail.index,
        'Per':socail.values
    }
)
print(social)