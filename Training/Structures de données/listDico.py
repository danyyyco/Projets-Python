listDico = [

    {
        'name': 'Denver',
        'age': 22,
        'notes':[12,18,19,10]
    },

    {
        'name': 'Foster',
        'age': 27,
        'notes':[15,16,9,7]
    },

    {
        'name': 'Heider',
        'age': 17,
        'notes':[15,10,0,5]
    }
]

print(listDico)
print(listDico[0]['notes'][0])
print(listDico[0]['notes'][1])
print(listDico[0]['notes'][2])
print(listDico[0]['notes'][3])
print(listDico[1]['notes'][0])

average1 = listDico[0]['notes'][0] + listDico[0]['notes'][1] + listDico[0]['notes'][2] + listDico[0]['notes'][3] / 4
print(average1)

average2 = listDico[1]['notes'][0] + listDico[1]['notes'][1] + listDico[1]['notes'][2] + listDico[1]['notes'][3] / 4
print(average2)

average3 = listDico[2]['notes'][0] + listDico[2]['notes'][1] + listDico[2]['notes'][2] + listDico[2]['notes'][3] / 4
print(average3)

listDico[0]["Average"] = average1
listDico[1]["Average"] = average2
listDico[2]["Average"] = average3

print(listDico)