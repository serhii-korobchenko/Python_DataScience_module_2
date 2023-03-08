import pandas as pd

data = pd.Series([1, 2, 3])
data[3] = 4
print(data)

####################################################################
print('####################################################################')

data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"}
}

employees = pd.DataFrame(data)
employees["age"] = [25, 32, 19]
print(employees)

####################################################################
print('####################################################################')



data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"},
    "age": {"1": 25, "2": 32, "3": 19}
}

employees = pd.DataFrame(data)

new_employee = pd.Series(["Jhon", "Denmark", 23], ["name", "country", "age"])

employees = employees.append(new_employee, ignore_index=True)
print(employees)