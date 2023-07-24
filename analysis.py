import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from data_cleanup import df_func
from matplotlib.ticker import FuncFormatter

df = df_func()

def log_tick_formatter(val, pos=None):
    return f"{int(val):,}"

# Calculating Chi-square and p-value for each column
def calculate_values(df, column_group):
    chi2_values = []
    p_values = []
    result = ""

    for column in column_group:
        cross_table = pd.crosstab(df[column], df['has_deposit'])
        chi2, p, _, _ = chi2_contingency(cross_table)
        chi2_values.append(chi2)
        p_values.append(p)
        result += f"Column: {column} ┃Chi-square: {chi2} ┃p-value: {p}\n"

    return chi2_values, p_values, result

columns = ['default', 'housing', 'loan', 'emp_var_rate', 'contact', 'month', 'campaign', 'duration', 'education', 'marital', 'job', 'age']

# Calculating Chi-square and p-value for all columns
chi2_all, p_all, result = calculate_values(df, columns)

# Plotting p-values and Chi-square values per column
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

ax1 = axs[0]
ax1.bar(columns, chi2_all, label='Chi-square')
ax1.set_ylabel('Chi-square')
ax1.set_xticklabels(columns, rotation=90)
ax1.legend(loc='center right', bbox_to_anchor=(1, 0.87))
ax1.set_yscale('log')
ax1.set_title('Chi-square and p-values values for Each Column')

# Plotting p-values and Chi-square values per column
ax2 = axs[1]
ax2.bar(columns, p_all, color='r', label='p-value')
ax2.set_ylabel('p-value')
ax2.set_xticklabels(columns, rotation=90)
ax2.legend(loc='center right', bbox_to_anchor=(1, 0.87))
ax2.set_yscale('log')

def analysis_plot():
    plt.show()

# Export the chi2_all, p_all, and result for use in other files
def get_analysis_data():
    return chi2_all, p_all, result