import pandas as pd

# file_path
attendance_file = r'C:\Users\tiosb\Downloads\INTRO TO CONTROL THEORY (EEME6601) Attendance 11_21_2024 (Responses) - Form Responses 1.csv'
grades_file = r'C:\Users\tiosb\Downloads\2024-12-05T1717_Grades-EEMEE6601_001_2024_3_-_INTRO_TO_CONTROL_THEORY.csv'


# pdread
attendance_df = pd.read_csv(attendance_file)
grades_df = pd.read_csv(grades_file)

# extract uni from email address
attendance_df['Email Prefix'] = attendance_df['Email Address'].str.split('@').str[0].str.lower()

# extract uni from gradebook
grades_df['SIS User ID'] = grades_df['SIS User ID'].str.lower()

# find in SIS User ID but not in Email Prefix
missing_students = grades_df[~grades_df['SIS User ID'].isin(attendance_df['Email Prefix'])]

# out put to path
output_file = 'C:/Users/tiosb/Downloads/Missing_Students_Full.csv'
missing_students.to_csv(output_file, index=False)

print(f"missing student has been saved to {output_file}")
