# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# import data and take a look
import pandas as pd

df = pd.read_csv('stroopData.csv')
print(df)


# %%
# get summary statistics
df[['Congruent', 'Incongruent']].describe()


# %%
# clean data frame prior to analysis

# convert index into participant id
df.reset_index(level=0, inplace=True)
df['ParticipantID'] = df['index'] + 1
del df['index']

# reshape data frame into long format
stroop_df = pd.melt(df,     id_vars = 'ParticipantID',     value_vars = ['Congruent', 'Incongruent'],     var_name = 'ConditionType',     value_name = 'ResponseTime')

print(stroop_df)


# %%
# import visualization library
import seaborn as sns


# %%
# box plot with swarm to check for outliers

sns.boxplot(data = stroop_df,     x = 'ConditionType',     y = 'ResponseTime')

sns.swarmplot(data = stroop_df,     x = 'ConditionType',     y = 'ResponseTime',     color = '.25')


# %%
# histogram

sns.displot(stroop_df,     x = 'ResponseTime',     col = 'ConditionType',     multiple = 'dodge')


# %%
# empirical cumulative distributions

sns.displot(stroop_df,     x = 'ResponseTime',     hue = 'ConditionType',     kind = 'ecdf',     palette = 'Accent')


# %%
# kernel density estimation

sns.displot(stroop_df,     x = 'ResponseTime',     hue = 'ConditionType',     kind = 'kde',     fill = True,     palette = 'Accent')


# %%
# paired sample t-test
from scipy import stats

t_val, p_val = stats.ttest_rel(df.Incongruent, df.Congruent)
print("t-distribution = %g" % t_val)
print("p-value = %g" % p_val)


# %%
# adjusted p-value

adj_p_val = p_val / 2
print("adjusted p-value = %g" % adj_p_val)


