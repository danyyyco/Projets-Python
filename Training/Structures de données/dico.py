capitals = {
    "France": "Paris",
    "United Kingdom": "London",
    "Deutschland": "Berlin",
    "Japan": "Tokyo",
    "China":"Pekin"
}
print(capitals)

capitals["Cameroon"] = "Yaounde"
print(capitals)

capitals.pop("Cameroon")
print(capitals)

capitals.pop("France")
print(capitals)

capitals["United Kingdom"] = "Londres"
print(capitals)

capitals["Royaume-uni"] = "Londres"
print(capitals)