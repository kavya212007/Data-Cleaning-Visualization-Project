import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_data.csv")

# Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("Data Cleaning Completed!")

# Average Salary by Department
avg_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(6,4))
avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("salary_by_department.png")
plt.show()

print("Visualization Created Successfully!")