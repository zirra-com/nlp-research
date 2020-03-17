import csv
import random

def get_sentences(path):
    with open(path) as fl:
        processed = list(csv.reader(fl, skipinitialspace=True))
        return [item for sublist in processed for item in sublist if len(item) > 5]

def join_sentences(layoff_sentences, other_sentences):
    final = []
    i, j = 0, 0
    while i < len(layoff_sentences) and j < len(other_sentences):
        if random.randint(0, 100) < 50:
            final.append([1, layoff_sentences[i]])  # append mini list
            i += 1
        else:
            final.append([0, other_sentences[j]])
            j += 1

    if i < len(layoff_sentences):
        final += layoff_sentences[i:]
    if j < len(other_sentences):
        final += other_sentences[j:]
    return final

def makecsv(name, data: []):
    with open(name, 'w', newline='') as fl:
        writer = csv.writer(fl)
        writer.writerows(data)


path1 = ''
path2 = ''
final = join_sentences(get_sentences(path1), get_sentences(path2))

makecsv('data/layoff/all.csv', final)
