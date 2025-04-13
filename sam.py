import pandas as pd

file_path = "M:\My\DAV\student_performance_large_dataset.csv"
df = pd.read_csv(file_path)

# Convert Final_Grade to numerical values for correlation analysis
#grade_mapping = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'F': 1}
df['Final_Grade_Numeric'] = df['Final_Grade'].map(grade_mapping)

# Display the first few rows of the dataframe
print(df.head())

#app:layout_constraintTop_toBottomOf="@+id/typeLayout"