import csv

#Q6
with open('faculty.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    header = next(csv_reader, None)

    faculty_dict = dict()

    for row in csv_reader:
        last_name = row[0].split()[-1]
        degrees = ' '.join([deg.replace('.', '') for deg in row[1].split()])
        split_title = row[2].split()
        title = ' '.join(split_title[:split_title.index('Professor') + 1])
        email = row[3]

        if last_name not in faculty_dict:
            faculty_dict[last_name] = [[degrees, title, email]]
        else:
            faculty_dict[last_name].append([degrees, title, email])

    print(list(faculty_dict.items())[:3])
    f.close()

#Q7
with open('faculty.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    header = next(csv_reader, None)
    professor_dict = dict()

    for row in csv_reader:
        name = row[0].split()
        first_name = name[0]
        last_name = name[-1]
        degrees = ' '.join([deg.replace('.', '') for deg in row[1].split()])
        split_title = row[2].split()
        title = ' '.join(split_title[:split_title.index('Professor') + 1])
        email = row[3]
        professor_dict[(first_name, last_name)] = [degrees, title, email]

    print(list(professor_dict.items())[:3])

    #Q8
    print(list(professor_dict.items()))

