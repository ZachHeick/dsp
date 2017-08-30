import csv

with open('faculty.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    header = next(csv_reader, None)

    degree_freq = dict()
    titles_freq = dict()
    emails = list()
    email_domains = set()

    for row in csv_reader:
        degrees = [deg.replace('.', '') for deg in row[1].split()]
        title = row[2].split()[0]
        emails.append(row[3])

        for deg in degrees:
            if deg not in degree_freq:
                degree_freq[deg] = 1
            else:
                degree_freq[deg] += 1

        if title not in titles_freq:
            titles_freq[title] = 1
        else:
            titles_freq[title] += 1

    print(degree_freq)
    print(titles_freq)
    print(emails)

    for email in emails:
        email_domain = email.split('@')[-1]
        email_domains.add(email_domain)

    print(list(email_domains))

    f.close()

