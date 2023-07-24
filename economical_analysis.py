from data_cleanup import df_func
import matplotlib.pyplot as plt
import numpy as np 
df = df_func()

# Filtering data to find deposits numbers per housing status
housing_T = (df['housing'] == True).sum()
housing_F = (df['housing'] == False).sum()
h_t_t = ((df['housing'] == True) & (df['has_deposit'] == True)).sum()
h_f_t = ((df['housing'] == False) & (df['has_deposit'] == True)).sum()

groups = ['Has housing', "Doesn't have housing"]
values1 = [h_t_t, h_f_t]
values2 = [housing_T - h_t_t, housing_F - h_f_t]

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Plotting the bar graph
ax1 = axs[0]
x_axis = np.arange(len(groups))
bars1 = ax1.bar(x_axis - 0.2, values1, width=0.4, label='Has deposited', color = '#00CC00')
bars2 = ax1.bar(x_axis + 0.2, values2, width=0.4, label="Hasn't deposited", color = '#800080')
ax1.set_xticks(x_axis)
ax1.set_xticklabels(groups)
ax1.set_ylim(1, 23000)
ax1.set_xlabel('Housing', weight='bold')
ax1.set_ylabel('Count')
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.87))
ax1.set_title('Economical impact on deposits')

for bar1, bar2 in zip(bars1, bars2):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    ax1.text(bar1.get_x() + bar1.get_width() / 2, height1 / 2, str(height1), ha='center', va='center', color='white', weight='bold')
    ax1.text(bar2.get_x() + bar2.get_width() / 2, height2 / 2, str(height2), ha='center', va='center', color='white', weight='bold')

# Filtering data to find deposits numbers per loan status
loan_T = (df['loan'] == True).sum()
loan_F = (df['loan'] == False).sum()
l_t_t = ((df['loan'] == True) & (df['has_deposit'] == True)).sum()
l_f_t = ((df['loan'] == False) & (df['has_deposit'] == True)).sum()

g = ['Has loan', "Doesn't have loan"]
v1 = [l_t_t , l_f_t]
v2 = [loan_T - l_t_t, loan_F - l_f_t]

# Plotting the bar graph
ax2 = axs[1]
x_axis = np.arange(len(g))
bars1 = ax2.bar(x_axis - 0.2, v1, width=0.4, label='Has deposited', color = '#00CC00')
bars2 = ax2.bar(x_axis + 0.2, v2, width=0.4, label="Hasn't deposited", color = '#800080')
ax2.set_xticks(x_axis)
ax2.set_xticklabels(g)
ax2.set_ylim(1, 35000)
ax2.set_xlabel('Loan', weight='bold')
ax2.set_ylabel('Count')
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.87))

for bar1, bar2 in zip(bars1, bars2):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    ax2.text(bar1.get_x() + bar1.get_width() / 2, height1 / 2, str(height1), ha='center', va='center', color='white', weight='bold')
    ax2.text(bar2.get_x() + bar2.get_width() / 2, height2 / 2, str(height2), ha='center', va='center', color='white', weight='bold')

emp_var_rates = [-3.4, -3.0, -2.9, -1.8, -1.7, -1.1, -0.2, -0.1, 1.1, 1.4]
g = ['-3.4', '-3.0', '-2.9', '-1.8', '-1.7', '-1.1', '-0.2', '-0.1', '1.1','1.4']
v1 = []
v2 = []


# Filtering data to find deposits numbers per employment rate
for loan_status in emp_var_rates:
    count_with_deposit = ((df['emp_var_rate'] == loan_status) & (df['has_deposit'] == True)).sum()
    count_total = (df['emp_var_rate'] == loan_status).sum()
    v1.append(count_with_deposit)
    v2.append(count_total - count_with_deposit)

# Plotting the linear graph
ax3 = axs[2]
ax3.plot(g, v1, marker='o', label='Has Deposit', color = '#00CC00')
ax3.plot(g, v2, marker='o', label='No Deposit', color = '#800080')
label_spacing = 250

for i in range(len(g)):
    ax3.text(g[i], v1[i] + label_spacing, str(v1[i]), ha='center', va='bottom')
    ax3.text(g[i], v2[i] - label_spacing, str(v2[i]), ha='center', va='top')
    
ax3.set_ylim(1, 20000)
ax3.set_xlabel('Employment variation rate', weight='bold')
ax3.set_ylabel('Count')
ax3.grid(True)
ax3.legend()
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.87))

plt.tight_layout(pad=4) 
def economical_plot():
    plt.show()