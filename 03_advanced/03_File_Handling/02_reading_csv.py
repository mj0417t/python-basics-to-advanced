import csv,io
csv_data="""Year, Industry, Value
2014, Manufacturing,75644
2014, Manufacturing,2434235
2014, Manufacturing,132
"""

#Instead of a physical file, we used StringIO to 
# create a file-like object. 
# The CSV reader parses each line into a list of values.
csvfile=io.StringIO(csv_data)
csvreader=csv.reader(csvfile)
for row in csvreader:
    print(row)