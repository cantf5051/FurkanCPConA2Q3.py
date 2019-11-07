'''

Essential unit: P.Con.
Assignment: A3
Question: Q#1
Name: Furkan Canturk
Pseudoname: FC
Date: 2019/10/29
Teacher&Class: ICS3UI-01 for Ms. Harris
Modification:
Question:
    Find a data set you are interested in. The data set must have at least 100
    rows and 10 columns. Create a flowchart, then write a program
    that reads in your txt or csv file and writes out a summary file
    containing averages &/or max and min values for the data set
    and whatever other total information is relevant.
Acknowledgements:


'''

import csv

# initialize data set
data = []
# Opend raw data file in csv
with open('E:/FurkanCPConA3/rawdataset.csv') as csv_file:
    # Read the data in text form
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Convert to float numbers
    for row in csv_reader:
        numbers = [float(x) for x in row]
        data.append(numbers)
csv_file.close()
# Data processing
mx = []
mn = []
av = []
for dindex, column in enumerate(zip(*data)):
    mx.append(max(column))
    mn.append(min(column))
    av.append(sum(column)/len(column))
#print ('maximum values for each row:',mx, 'minimum values for each row:',mn,'average values for each row:',av,)

# Write summary into file
csv_columns = ['Gaspe',
             'Keewatin-Baffin',
             'Maritime',
             'Missouri',
             'N-Saskatchewan',
             'Okanagan-Similkameen',
             'Pacific-Coastal-Cote-Pacifique',
             'S-Saskatchewan',
             'St-Lawrence-St-Laurent',
             'Winnipeg']
# Data dictionary for water sources
summary = {'Gaspe':[],
             'Keewatin-Baffin':[],
             'Maritime':[],
             'Missouri':[],
             'N-Saskatchewan':[],
             'Okanagan-Similkameen':[],
             'Pacific-Coastal-Cote-Pacifique':[],
             'S-Saskatchewan':[],
             'St-Lawrence-St-Laurent':[],
             'Winnipeg':[]
             }

# create an index for mx, mn, av
i=0
for key in summary:
    summary[key] = [mx[i], av[i], mn[i]]
    #print (summary[key])
    i = i + 1

with open('E:/FurkanCPConA3/summary.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerow(summary)
