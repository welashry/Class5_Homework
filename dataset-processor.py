import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





diabetes_df = pd.read_csv('diabetes.csv',

                           sep=',',

                           header=0)
print(diabetes_df.to_string())


print(diabetes_df.describe())


print(diabetes_df.corr())


# Plotting histogram

plt.hist(diabetes_df['BMI'], bins=10, color='g')

plt.title('BMI')

plt.xlabel('BMI')

plt.ylabel('Count')

plt.savefig(f'plots/bmi_hist.png', format='png')

plt.clf()

#Ploting PiePlot



labels='Male','Female'
x=(diabetes_df['SEX'].value_counts(1))

sizes=x
colors = ['gold', 'yellowgreen',]
plt.pie(sizes, colors=colors,labels=labels,
startangle=90, autopct='%.1f%%')

plt.axis('equal')
plt.legend()

plt.savefig(f'plots/pie_chart.png', format='png')


#Plotting scatterplot

plt.scatter(diabetes_df['BMI'], diabetes_df['SEX'], color='b')

plt.title('BMI to SEX')

plt.xlabel('BMI')

plt.ylabel('SEX')

plt.savefig(f'plots/SEX_to_BMI.png', format='png')






