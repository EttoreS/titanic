# %% [markdown]
# # Imports

# %%
import pandas as pd

# %% [markdown]
# ## codigo

# %%
df_titanic = pd.read_csv('data/tested.csv')
df_titanic

# %%
df_titanic.head()

# %%
df_titanic.tail()

# %%
df_titanic.info()

# %%
type(df_titanic)

# %%
series = df_titanic['Name']
series

# %%
type(series)

# %%
df_titanic[['Name']]

# %%
df_titanic.head()

# %%
df_titanic.columns

# %%



