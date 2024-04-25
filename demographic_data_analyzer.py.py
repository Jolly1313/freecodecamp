import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/fbello19/freecodecamp_projects/main/adult.data.csv"
df = pd.read_csv(url, header=None)

# Assign column names
column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
                'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
                'hours-per-week', 'native-country', 'salary']
df.columns = column_names

# 1. How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# 4. What percentage of people with advanced education make more than 50K?
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_higher_education = (higher_education['salary'] == '>50K').mean() * 100

# 5. What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_lower_education = (lower_education['salary'] == '>50K').mean() * 100

# 6. What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100

# 9. Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

# Print out the results
print("1. Race counts:\n", race_counts)
print("\n2. Average age of men:", round(average_age_men, 1))
print("\n3. Percentage with Bachelor's degree:", round(percentage_bachelors, 1))
print("\n4. Percentage with advanced education earning >50K:", round(percentage_higher_education, 1))
print("\n5. Percentage without advanced education earning >50K:", round(percentage_lower_education, 1))
print("\n6. Minimum work hours per week:", min_work_hours)
print("\n7. Percentage of rich among those who work fewest hours:", round(rich_percentage, 1))
print("\n8. Country with highest percentage of rich:", highest_earning_country)
print("   Percentage:", round(highest_earning_country_percentage, 1))
print("\n9. Most popular occupation for those earning >50K in India:", top_IN_occupation)
