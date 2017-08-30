import csv

with open('faculty.csv') as r:
    emails = list()
    csv_reader = csv.reader(r, delimiter=',')
    header = next(csv_reader, None)
    for row in csv_reader:
        emails.append(row[3])
    r.close()

with open('emails.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter='\n')
    csv_writer.writerow(emails)
    f.close()

