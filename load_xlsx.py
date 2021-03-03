import pandas
from matplotlib import pyplot

def show_chart(x, y, stock_name):
  pyplot.plot(x, y)
  pyplot.xlabel('Date')
  pyplot.ylabel('Algorithm Key')
  #pyplot.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
  pyplot.gcf().set_size_inches(100, 10.5)
  #pyplot.savefig('storage/dcim/' + stock_name + '.png')

stock_code = "600848"

df = pandas.read_excel("colab/stock_data.xlsx")

date = []
algorithm_key = []

i = 0
for index, row in df.iterrows():
  date.append(i)
  algorithm_key.append(row['price_change'])
  i = i + 1
 # if i > 100:
 #   break

date.reverse()
algorithm_key.reverse()

for x, y in zip(date, algorithm_key):
  print(str(x) + " " + str(y))
  
#show_chart(date, algorithm_key, stock_code)
