import csv

def load_dataset(filename):
  with open(filename, 'rU') as csv_data:
    reader = csv.reader(csv_data)
    header = reader.next()
    return [row for row in reader]
