import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

df=pd.read_csv('student_performance_large_dataset.csv')
#print(df0.head())



#age between 18 to 21 and study hours per week greater than 30.
'''
ps2= df[(df['Age'].between(18, 21)) & (df['Study_Hours_per_Week'] > 30)]
print(ps2)
plt.figure(figsize=(6, 5))
sb.boxplot(y=ps2['Study_Hours_per_Week'], color="lightblue")
plt.title('Study Hours per Week for Students Aged 18-21')
plt.ylabel('Study Hours per Week')
plt.grid(True)
plt.show()'''


'''
lowest age and lowest study hours per week.
ps3 = df[df['Study_Hours_per_Week'] == df['Age'].min()]
print(ps3[['Age','Study_Hours_per_Week']])
'''

'''
4
max_age=df['Age'].max()
min_study_hourse=df['Study_Hours_per_Week'].min()
ps4= df[(df['Age']==max_age) & (df['Study_Hours_per_Week']==min_study_hourse)]
print(ps4[['Age','Study_Hours_per_Week']])
'''

'''
#age pref. learning style and course completed.
ps5=df[['Age','Preferred_Learning_Style','Online_Courses_Completed']]
print(ps5)
'''


'''
#gender f/m and pref. learning style and study hours per week.

ps6=df[['Gender','Preferred_Learning_Style','Study_Hours_per_Week']]
print(ps6)
'''

'''
#pref. learning style is auditory and study hours per week greater than 30 and participate in discussion= y/n.
ps7 = df[(df['Preferred_Learning_Style'] == 'Auditory') & 
         (df['Study_Hours_per_Week'] > 30) & 
         (df['Participation_in_Discussions'] == 'Yes') |
         (df['Participation_in_Discussions'] == 'NO')]
print(ps7)
'''

'''
#8] pref. learning style is kinesthetic and use of educational tech is yes or no.
ps8=df[(df['Preferred_Learning_Style'] == 'Kinesthetic') &(df['Preferred_Learning_Style']) & (df ['Use_of_Educational_Tech'])]
print(ps8)
'''


'''
#9social media usage per week and study hour per week.
ps9 = df[['Use_of_Educational_Tech', 'Study_Hours_per_Week']]
print(ps9)
'''

'''
#10 online course completion and academic performance.
ps10 = df[['Online_Courses_Completed', 'Attendance_Rate (%)']]
print(ps10)
'''


'''
#11 Self Reported stress(high, low, medium) and exam score.
ps11 = df[['Self_Reported_Stress_Level', 'Exam_Score (%)']]
print(ps11)
'''


'''
#12 Self Reported stress is high and exam score is greater than 60.
ps12 = df[(df['Self_Reported_Stress_Level'] == 'High') & (df['Exam_Score (%)'] > 60)]
print(ps12)
'''

'''
#13 Attendance rate and assignment completion rate more than 50.
df13= df[(df['Attendance_Rate (%)']>50) & (df['Assignment_Completion_Rate (%)']>50)]
print(df13)
'''

'''
#14 Online course completed more than 6 and attendance rate is between 60 to 70. 
ps14= df[(df['Attendance_Rate (%)'].between(60,70)) & (df['Online_Courses_Completed']>6)]
print(ps14)
'''


'''
#15 Study hours per week and sleep hours per night.
ps15=df[['Study_Hours_per_Week','Sleep_Hours_per_Night']]
print(ps15)
'''


'''
#16 Relationship between sleep hours per night and exam scores.
ps16=df[['Sleep_Hours_per_Night','Exam_Score (%)']]
print(ps16)
'''

'''
#17Number of online courses completed by students who study more than 20 hours per week.
ps17 = df[df['Study_Hours_per_Week'] > 20][['Online_Courses_Completed']]
print(ps17)
'''

'''
#18 Impact of high stress on students’ sleep hours per night.
ps18= df[df['Self_Reported_Stress_Level'] == 'High'][['Sleep_Hours_per_Night']]
print(ps18)
'''

'''
#19Number of online courses completed by students with high vs. low stress.
ps19=ps32 = df[['Online_Courses_Completed', 'Exam_Score']]
print(ps19)
'''

#20 Do students with higher attendance rates perform better on exams?
'''ps20=df[['Attendance_Rate (%)', 'Exam_Score (%)']]
print(ps20)'''

#fig, axes = plt.subplots(3, 3, figsize=(15, 12)) 
'''
sb.scatterplot(x=df['Sleep_Hours_per_Night'], y=df['Exam_Score (%)'], ax=axes[1, 1], color="red")
axes[1, 1].set_title("Sleep Hours per Night vs. Exam Scores")
axes[1, 1].set_xlabel("Sleep Hours per Night")
axes[1, 1].set_ylabel("Exam Score (%)")
plt.show()
'''
plt.figure(figsize=(8, 6))
#1
'''
plt.figure(figsize=(8, 6))  # Create a single figure
sb.boxplot(x=df['Self_Reported_Stress_Level'], y=df['Exam_Score (%)'])
plt.title("Self-Reported Stress Level vs. Exam Scores")
plt.xlabel("Stress Level")
plt.ylabel("Exam Score (%)")
plt.grid(True)
plt.show()'''

#2
'''
plt.figure(figsize=(8, 6))
sb.countplot(x=df['Self_Reported_Stress_Level'])
plt.title("Count of Students by Stress Level")
plt.xlabel("Self-Reported Stress Level")
plt.ylabel("Number of Students")
#plt.grid(True)
plt.show()'''

#3
'''
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=["blue","gray", "pink"], startangle=90)
plt.title("Gender Distribution")
plt.ylabel("")  # Remove y-axis label
plt.show()'''

#4
'''
sb.barplot(x=df['Assignment_Completion_Rate (%)'], y=df['Attendance_Rate (%)'])
plt.title("Assignment Completion Rate vs. Attendance Rate")
plt.xlabel("Assignment Completion Rate (%)")
plt.ylabel("Attendance Rate (%)")
plt.show()'''

#5
df = df[df['Study_Hours_per_Week'] < 100]
sb.barplot(x=df['Preferred_Learning_Style'], y=df['Study_Hours_per_Week'], estimator=np.mean)

# Formatting
plt.title("Preferred Learning Style vs. Study Hours per Week")
plt.xlabel("Preferred Learning Style")
plt.ylabel("Study Hours per Week")
plt.xticks(rotation=45)  # Rotate labels to avoid overlap
plt.show()
'''
# Set the style
sns.set(style="whitegrid")

fig.suptitle("Student Performance Data Analysis", fontsize=16)

# 1. Boxplot – Study Hours per Week for Students Aged 18-21
ps2 = df[(df['Age'].between(18, 21)) & (df['Study_Hours_per_Week'] > 30)]
sns.boxplot(y=ps2['Study_Hours_per_Week'], ax=axes[0, 0], color="lightblue")
axes[0, 0].set_title("Study Hours per Week for Students Aged 18-21")
axes[0, 0].set_ylabel("Study Hours per Week")

# 2. Histogram – Distribution of Study Hours per Week
sns.histplot(df['Study_Hours_per_Week'], bins=20, kde=True, ax=axes[0, 1], color="purple")
axes[0, 1].set_title("Distribution of Study Hours per Week")
axes[0, 1].set_xlabel("Study Hours per Week")
axes[0, 1].set_ylabel("Count")

# 3. Bar Chart – Preferred Learning Style vs. Study Hours per Week
sns.barplot(x=df['Preferred_Learning_Style'], y=df['Study_Hours_per_Week'], ax=axes[1, 0])
axes[1, 0].set_title("Preferred Learning Style vs. Study Hours per Week")
axes[1, 0].set_xlabel("Preferred Learning Style")
axes[1, 0].set_ylabel("Study Hours per Week")
axes[1, 0].tick_params(axis='x', rotation=45)

# 4. Scatter Plot – Sleep Hours per Night vs. Exam Scores
sns.scatterplot(x=df['Sleep_Hours_per_Night'], y=df['Exam_Score (%)'], ax=axes[1, 1], color="red")
axes[1, 1].set_title("Sleep Hours per Night vs. Exam Scores")
axes[1, 1].set_xlabel("Sleep Hours per Night")
axes[1, 1].set_ylabel("Exam Score (%)")

# 5. Boxplot – Self-Reported Stress Level vs. Exam Scores
sns.boxplot(x=df['Self_Reported_Stress_Level'], y=df['Exam_Score (%)'], ax=axes[2, 0])
axes[2, 0].set_title("Self-Reported Stress Level vs. Exam Scores")
axes[2, 0].set_xlabel("Stress Level")
axes[2, 0].set_ylabel("Exam Score (%)")

# 6. Bar Chart – Online Courses Completed by High vs. Low-Stress Students
sns.barplot(x=df['Self_Reported_Stress_Level'], y=df['Online_Courses_Completed'], ax=axes[2, 1])
axes[2, 1].set_title("Online Courses Completed by Stress Levels")
axes[2, 1].set_xlabel("Self-Reported Stress Level")
axes[2, 1].set_ylabel("Online Courses Completed")

# 7. Scatter Plot – Attendance Rate vs. Exam Scores
sns.scatterplot(x=df['Attendance_Rate (%)'], y=df['Exam_Score (%)'], ax=axes[3, 0], color="green")
axes[3, 0].set_title("Attendance Rate vs. Exam Scores")
axes[3, 0].set_xlabel("Attendance Rate (%)")
axes[3, 0].set_ylabel("Exam Score (%)")

# 8. Pie Chart – Gender Distribution
df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', ax=axes[3, 1], colors=["blue", "pink"], startangle=90)
axes[3, 1].set_title("Gender Distribution")
axes[3, 1].set_ylabel("")

# 9. Line Plot – Study Hours per Week vs. Online Courses Completed
sns.lineplot(x=df['Study_Hours_per_Week'], y=df['Online_Courses_Completed'], ax=axes[4, 0], color="orange")
axes[4, 0].set_title("Study Hours per Week vs. Online Courses Completed")
axes[4, 0].set_xlabel("Study Hours per Week")
axes[4, 0].set_ylabel("Online Courses Completed")

# 10. Bar Chart – Assignment Completion Rate vs. Attendance Rate
sns.barplot(x=df['Assignment_Completion_Rate (%)'], y=df['Attendance_Rate (%)'], ax=axes[4, 1])
axes[4, 1].set_title("Assignment Completion Rate vs. Attendance Rate")
axes[4, 1].set_xlabel("Assignment Completion Rate (%)")
axes[4, 1].set_ylabel("Attendance Rate (%)")

# Adjust layout and show the plot
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

'''