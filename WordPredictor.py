import requests
import numpy as np

res = requests.get(
    "https://gist.githubusercontent.com/pradeepradyumna/7a180e81eec66457263c5581f13dc8b9/raw/a4bf95089dc7683fb0ee11161fcbfdaac5e99ecf/sampledata.txt")  # "https://github.com/pradeepradyumna/SampleData/blob/master/sampledata.txt")

data = res.text


# Markov Chains Algorithm

def generatetable(data, k):
    T = {}
    for i in range(len(data)-k):
        x = data[i:i+k]
        y = data[i+k]

        if T.get(x) is None:
            T[x] = {}
            T[x][y] = 1
        else:
            if T[x].get(y) is None:
                T[x][y] = 1
            else:
                T[x][y] += 1
    return T


k = 5
inital_content = "right"

T = generatetable(data.lower(), k)

for i in range(len(data)):
    inp = inital_content[-k:]

    possible_chars = list(T[inp].keys())
    possible_values = list(T[inp].values())

    sum_ = sum(T[inp].values())

    probabs = np.array(possible_values)/sum_

    next_char = np.random.choice(possible_chars, p=probabs)

    inital_content += next_char

    print(inital_content)
