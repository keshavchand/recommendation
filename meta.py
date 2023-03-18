# Take the sample and generate python code

Disease = {}
DiseaseReverseIndex = {}
f = open("sample.txt", "r")


def preprocess(data):
    data = data.split(",")[0].strip()
    for i, d in enumerate(data):
        if d == '_':
            break
    return data[i + 1:]

while True:
    line = f.readline()
    if (len(line) == 0): break
    disease = preprocess(line)
    _ = f.readline()
    symptoms = []

    while True:
        line = f.readline()
        if len(line) == 0 or line == "\n":
            break
        symptom = preprocess(line)
        symptoms.append(symptom)
        if symptom not in DiseaseReverseIndex:
            DiseaseReverseIndex[symptom] = []
        DiseaseReverseIndex[symptom].append(disease) 

    Disease[disease] = symptoms

import pickle
pickle.dump(Disease, open("disease.pickle", "wb"))
pickle.dump(DiseaseReverseIndex, open("diseaseRevIdx.pickle", "wb"))
