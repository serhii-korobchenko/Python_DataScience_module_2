import pandas as pd

numbers = pd.Series([1, 2, 3, 4, 5])
numbers.drop([1,3], inplace=True)
print(numbers)

####################################################################
print('####################################################################')

import pandas as pd

data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"},
    "age": {"1": 25, "2": 32, "3": 19}
}

employees = pd.DataFrame(data)

employees = employees.drop(["2"])
print(employees)

####################################################################
print('####################################################################')



data = {
    "name": {"1": "Michael", "2": "John", "3": "Liza"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia"},
    "age": {"1": 25, "2": 32, "3": 19}
}

employees = pd.DataFrame(data)

employees = employees.drop(["age"], axis=1)
print(employees)