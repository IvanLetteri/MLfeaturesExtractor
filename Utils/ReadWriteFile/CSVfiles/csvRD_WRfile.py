import csv

row = ['1', 'test', 'test2']
with open('dataset.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()

