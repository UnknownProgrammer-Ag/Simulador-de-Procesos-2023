import csv


def csv_opener(direc):
    file = open(direc, newline='')
    reader = csv.reader(file)
    next(reader)
    data = []
    for row in reader:
        id = int(row[0])
        tam = int(row[1])
        tA = int(row[2])
        tI = int(row[3])
        data.append([id, tam, tA, tI])
    return data
