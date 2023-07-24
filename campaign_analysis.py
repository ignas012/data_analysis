from data_cleanup import df_func
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.ticker import FuncFormatter

df = df_func()

# Filtering data to find deposits numbers per contacting methods
telephone = (df['contact'] == 'telephone').sum()
cellular = (df['contact'] == 'cellular').sum()
tel_t = ((df['contact'] == 'telephone') & (df['has_deposit'] == True)).sum()
cel_t= ((df['contact'] == 'cellular') & (df['has_deposit'] == True)).sum()

group = ['Telephone', 'Cellular']
value1 = [tel_t, cel_t]
value2 = [telephone - tel_t, cellular - cel_t]
x_axis = np.arange(len(group))

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Plotting the bar graph
ax1 = axs[0]
bars1 = ax1.bar(x_axis - 0.2, value1, width=0.4, label='Has deposited')
bars2 = ax1.bar(x_axis + 0.2, value2, width=0.4, label="Hasn't deposited")
ax1.set_xticks(x_axis)
ax1.set_xticklabels(group)
ax1.set_ylim(1, 23000)
ax1.set_xlabel('Contact type', weight='bold')
ax1.set_ylabel('Count')
ax1.set_title('Campaign impact on deposits')
ax1.legend(loc='center left', bbox_to_anchor=(1, 0.87))

for bar1, bar2 in zip(bars1, bars2):
    height1 = bar1.get_height()
    height2 = bar2.get_height()
    ax1.text(bar1.get_x() + bar1.get_width() / 2, height1 / 2, str(height1), ha='center', va='center', color='white', weight='bold')
    ax1.text(bar2.get_x() + bar2.get_width() / 2, height2 / 2, str(height2), ha='center', va='center', color='white', weight='bold')

campaign = df['campaign'].unique()
v1 = []
v2 = []
g = []

# Filtering data to find deposits numbers per campaign
for camp in campaign:
    count_with_deposit = ((df['campaign'] == camp) & (df['has_deposit'] == True)).sum()
    count_total = (df['campaign'] == camp).sum()
    count_without_deposit = count_total - count_with_deposit

    if count_with_deposit > 0 or count_without_deposit > 0:
        v1.append(count_with_deposit)
        v2.append(count_without_deposit)
        g.append(str(camp))

# Plotting the linear graph
ax2 = axs[1]
ax2.plot(g, v1, marker='o', linestyle='', label='Has Deposit')
ax2.plot(g, v2, marker='o', linestyle='', label='No Deposit')
label_spacing = 500

def log_tick_formatter(val, pos=None):
    return f"{int(val):,}"

ax2.set_ylim(0.5, 25000)
ax2.yaxis.set_major_locator(plt.MultipleLocator(base=100))
ax2.set_xlabel('Campaign number', weight='bold')
ax2.set_ylabel('Count')
ax2.grid(True)
ax2.legend()
ax2.set_yscale('log')
ax2.set_xticklabels(g, rotation=90, ha='center')
ax2.yaxis.set_major_formatter(FuncFormatter(log_tick_formatter))
ax2.legend(loc='center left', bbox_to_anchor=(1, 0.87))

months = df['month'].unique()
v1 = []
v2 = []
g = months

# Filtering data to find deposits numbers per month
for i, month in enumerate(months):
    count_with_deposit = ((df['month'] == month) & (df['has_deposit'] == True)).sum()
    count_total = (df['month'] == month).sum()
    count_without_deposit = count_total - count_with_deposit
    v1.append(count_with_deposit)
    v2.append(count_without_deposit)

# Plotting the linear graph        
ax3 = axs[2]
ax3.plot(g, v1, marker='o', label='Has Deposit')
ax3.plot(g, v2, marker='o', label='No Deposit')
label_spacing = 500

ax3.set_ylim(0.5, 25000)
ax3.yaxis.set_major_locator(plt.MultipleLocator(base=100))
ax3.set_xlabel('Month', weight='bold')
ax3.set_ylabel('Count')
ax3.grid(True)
ax3.legend()
ax3.set_yscale('log')
ax3.set_xticklabels(g, rotation=45, ha='center')
ax3.yaxis.set_major_formatter(FuncFormatter(log_tick_formatter))
ax3.legend(loc='center left', bbox_to_anchor=(1, 0.87))

plt.tight_layout()
def campaign_plot():
    plt.show()