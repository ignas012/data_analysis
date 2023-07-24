from data_cleanup import df_func
from demographic_analysis import demographic_plot
from economical_analysis import  economical_plot
from campaign_analysis import  campaign_plot
from analysis import get_analysis_data, analysis_plot

df = df_func()
df.to_csv('filename.csv', index=False)

demographic_plot()
economical_plot()
campaign_plot()

chi2_all, p_all, result = get_analysis_data()

print("\n\n\n" + result)

analysis_plot()

"""
The lower the p-value, the more likely it is to have an effect or relationship on deposits.

The higher the Chi-square value, the more likely it is to have an effect or relationship on deposits.

"""