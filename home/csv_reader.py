
import csv
import pandas as pd
# opening the CSV file
with open('files/Book.csv','r', encoding='UTF-8', newline='', errors='ignore')as myfile:
   
  # reading the CSV file
  csvFile = csv.reader(myfile)
  #df = pd.read_csv('files/Book_1.csv')
  #print(df.head())
 
  # displaying the contents of the CSV file

  for lines in csvFile:
        print(lines)
 