import pandas as pd

# Sample DataFrame with missing values
data = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, 2, 3, None]
})

# Dropping rows with any missing values
cleaned_data_drop = data.dropna()
print('cleaned \n',cleaned_data_drop)

# Filling missing values with 0
cleaned_data_fill = data.fillna(0)
print(cleaned_data_fill)

# Sample DataFrame with duplicates
data = pd.DataFrame({
    'A': [1, 2, 2, 4],
    'B': [5, 6, 6, 8]
})

# Removing duplicate rows
cleaned_data = data.drop_duplicates()
print(cleaned_data)

# Sample DataFrame
data = pd.DataFrame({
    'A': ['1', '2', '3', '4']
})
print('before \n',data)
print(data.dtypes)
# Converting data type of column 'A' to integer
data['A'] = data['A'].astype(int)
print('after \n',data)
print(data.dtypes)

# Sample DataFrame
data = pd.DataFrame({
    'A': ['Hello', 'World', 'Pandas', 'Python']
})

# Converting column 'A' to lowercase
data['A'] = data['A'].str.lower()
print(data)