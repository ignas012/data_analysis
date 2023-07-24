from data_cleanup import df_func
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = df_func()

# Finding the total number of deposits and no deposits
total_users = df.shape[0]
user_w_deposit = (df['has_deposit'] == True).sum()
user_wo_deposit = (df['has_deposit'] == False).sum()
pav = ['People without a deposit', 'People with a deposit']
vert = [user_wo_deposit, user_w_deposit]

# Plotting the bar graph
plt.figure() 
plt.bar(pav, vert, color = ((0/255, 153/255, 255/255), (255/255, 77/255, 77/255)))
plt.ylabel('Count') 
plt.title('Total people with and without deposit') 

# Putting the numbers in the bars
for i in range(len(pav)):
    plt.text(i, vert[i]/2, str(vert[i]), ha='center', va='center', color = 'white')
    percentage = "{:.3f}".format(vert[i] * 100 / total_users)
    plt.text(i, vert[i], str(percentage + "%"), ha='center', va='bottom', color = 'black')


# Defining the age ranges for analysis
age_groups = [(17, 29), (30, 39), (40, 59), (60, 74), (75, float('inf'))]
groups = ['Young adults', 'Adults', 'Middle aged', 'Senior citizens', 'Elderly']

values1 = []
values2 = []

# Filtering data to find deposits numbers per age groups
for age_range in age_groups:
    group_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
    has_deposit_count = (group_df['has_deposit'] == True).sum()
    total_count = group_df.shape[0]
    values1.append(has_deposit_count)
    values2.append(total_count - has_deposit_count)
    
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Plotting the bar graph
ax1 = axs[0]
ax1.bar(groups, values1, label="Has deposited", color=(255/255, 77/255, 77/255))
ax1.bar(groups, values2, bottom=values1, label="Hasn't deposited", color=(0/255, 153/255, 255/255))
ax1.set_ylabel('Count')
ax1.set_xticklabels(groups, rotation=45, ha='center')
ax1.set_yscale('log')
ax1.set_ylim(1, 40000)
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.87))
ax1.set_xlabel('Age range', weight='bold')
ax1.set_title('Demographic impact on deposits')

def log_tick_formatter(val, pos=None):
    return f"{int(val):,}"

ax1.yaxis.set_major_formatter(FuncFormatter(log_tick_formatter))

for bar in ax1.patches:
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 4 + bar.get_y(), round(bar.get_height()), ha='center', color='white', weight='bold', size=8)

categories = df['education'].unique()
counts = []
deposits = []

# Filtering data to find deposits numbers per education level
for category in categories:
    count = (df['education'] == category).sum()
    deposit_count = ((df['education'] == category) & (df['has_deposit'] == True)).sum()
    counts.append(count)
    deposits.append(deposit_count)

groups2 = ['Basic four years', 'Basic six years', 'Basic nine years', 'High school', 'Professional course', 'University degree', 'illiterate', 'None']
v1 = deposits
v2 = [c - d for c, d in zip(counts, deposits)]

# Plotting the bar graph
ax2 = axs[1]
ax2.bar(groups2, v1, label="Has deposited", color=(255/255, 77/255, 77/255))
ax2.bar(groups2, v2, bottom=v1, label="Hasn't deposited", color=(0/255, 153/255, 255/255))
ax2.set_ylabel('Count')
ax2.set_xticklabels(groups2, rotation=45, ha='center')
ax2.set_yscale('log')
ax2.set_ylim(1, 50000)
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.87))
ax2.yaxis.set_major_formatter(FuncFormatter(log_tick_formatter))
ax2.set_xlabel('Education', weight='bold')

for bar in ax2.patches:
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 3 + bar.get_y(), round(bar.get_height()), ha='center', color='white', weight='bold', size=8)

marital_status_categories = ['married', 'single', 'divorced', 'nan']
groups3 = ['Married', 'Single', 'Divorced', 'None']
vv1 = []
vv2 = []

# Filtering data to find deposits numbers per marital status
for category in marital_status_categories:
    total_count = (df['marital'] == category).sum()
    deposit_count = ((df['marital'] == category) & (df['has_deposit'] == True)).sum()
    vv1.append(deposit_count)
    vv2.append(total_count - deposit_count)

# Plotting the bar graph
ax3 = axs[2]
ax3.bar(groups3, vv1, label="Has deposited", color=(255/255, 77/255, 77/255))
ax3.bar(groups3, vv2, bottom=vv1, label="Hasn't deposited", color=(0/255, 153/255, 255/255))
ax3.set_ylabel('Count')
ax3.set_xticklabels(groups3, rotation=45, ha='center')
ax3.set_yscale('log')
ax3.set_ylim(1, 40000)
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.87))
ax3.yaxis.set_major_formatter(FuncFormatter(log_tick_formatter))
ax3.set_xlabel('Marital status', weight='bold')

for bar in ax3.patches:
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 4 + bar.get_y(), round(bar.get_height()), ha='center', color='white', weight='bold', size=8)

plt.tight_layout(pad=4) 
def demographic_plot():
    plt.show()