# creating a random dataset with pandas and numpy
import pandas as pd
import numpy as np 
from stuff import names, work_fields, countries

np_names = np.array(names)
np_work_fields = np.array(work_fields)
np_countries = np.array(countries)

rng = np.random.default_rng()

random_names = rng.choice(np_names, size=100)
random_ages = rng.integers(low=18, high=66, size=100)
random_work_field = rng.choice(np_work_fields, size=100)
random_salary =rng.integers(low=15080, high=10000000, size=100)
random_countries = rng.choice(np_countries, size=100)

df = pd.DataFrame({
    'Name': random_names,
    'Age': random_ages,
    'Work field': random_work_field,
    'Salary per year ($)': random_salary,
    'Country': random_countries
})

csv_file = df.to_csv('synthetic_dataset.csv', index=False, encoding='utf-8')

