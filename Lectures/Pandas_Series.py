import pandas as pd

mountain_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])

print(mountain_height)

####################################################################
print('####################################################################')

mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height)

####################################################################
print('####################################################################')
print(mountains_height[0])  # 2061.0
print(mountains_height["Goverla"])  # 2061.0

####################################################################
print('####################################################################')
print(mountains_height[["Pip_Ivan", "Goverla", "Gutin_Tomnatik"]])



####################################################################
print('####################################################################')


mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height[1:3])
print(mountains_height["Brebenskyl":"Petros"])


####################################################################
print('####################################################################')
print(mountains_height.Petros)  # 2022.5
print(mountains_height.Brebenskyl)  # 2035.8

####################################################################
print('####################################################################')
print(mountains_height > 2030)
print(mountains_height[mountains_height > 2030])



####################################################################
print('####################################################################')
print("Goverla" in mountains_height)  # True


####################################################################
print('####################################################################')
sort_index = mountains_height.sort_index()
print(sort_index)

####################################################################
print('####################################################################')

mountains_height.sort_values(inplace=True, ascending=False)
print(mountains_height)

####################################################################
print('####################################################################')



mountains_height = pd.Series(
    {"Goverla": 2061, "Brebenskyl": 2035.8, "Pip_Ivan": 2028.5},
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height)

mountains_height.fillna(0, inplace=True)

print(mountains_height)