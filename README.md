# Class5_Homework
1- Save your dataset "diabetes.csv" to your Desktop


2-Create a script on your Desktop called "dataset-processor.py" and follow the instructions below:-



- Import the libraries that you will need in your script(pandas-matplotlib):


               import pandas as pd

               import matplotlib.pyplot as plt

- Load the data:

                 diabetes_df = pd.read_csv('diabetes.csv',

                           sep=',',

                           header=0)

- To display the data in a table:


                                      print(diabetes_df.to_string())
- To get  summary statistics:

                              print(diabetes_df.describe())
- To Visualize the data,and get (histogram-scotther-pie) chart:


# Plotting histogram

                  plt.hist(diabetes_df['BMI'], bins=10, color='g')

                  plt.title('BMI')

                  plt.xlabel('BMI')

                  plt.ylabel('Count')

                  plt.savefig(f'plots/bmi__hist.png', format='png')

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

                 plt.savefig(f'plots/pie__chart.png', format='png')

 #Plotting scatterplot
 
                 plt.scatter(diabetes_df['BMI'], diabetes_df['SEX'], color='b')

                 plt.title('BMI to SEX')

                 plt.xlabel('BMI')

                 plt.ylabel('SEX')

                 plt.savefig(f'plots/SEX_2_BMI.png', format='png')

3-Now save your script with the python extension ".py" and run it on the terminal:
                                    python3 dataset-processor.py




