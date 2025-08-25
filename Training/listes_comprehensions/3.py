list_persons = [
    {
        "nom":"Marie",
        "age":30
    },
    {
        "nom": "Terry",
        "age": 40
    },
    {
        "nom": "Murielle",
        "age": 50
    },
    {
        "nom": "Peter",
        "age": 10
    },
    {
        "nom": "Pat",
        "age": 18
    },
]

persons_plus_30 = [person["nom"] for person in list_persons if person["age"] > 30]
print(persons_plus_30)