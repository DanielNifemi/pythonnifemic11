customers = [
    {
        "name": "Omotola Fashola",
        "acct_num": "001",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": True
    },
    {
        "name": "Idiot Olamide",
        "acct_num": "010",
        "age": 32,
        "balance": 1_005,
        "type": "savings",
        "gender": "male",
        "is_married": False
    },
    {
        "name": "Abdur-Rahman Fashola",
        "acct_num": "020",
        "age": 26,
        "balance": 100_000,
        "type": "current",
        "gender": "male",
        "is_married": True
    },

    {
        "name": "Ololade Boyo",
        "acct_num": "031",
        "age": 18,
        "balance": 34_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Dorcas Charles",
        "acct_num": "011",
        "age": 19,
        "balance": 30_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Emmanuel Obsession",
        "acct_num": "092",
        "age": 76,
        "balance": 1_000_000,
        "type": "current",
        "gender": "male",
        "is_married": True
    },
    {
        "name": "Eden Ace",
        "acct_num": "041",
        "age": 16,
        "balance": 150_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Blessing Elon",
        "acct_num": "063",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
    {
        "name": "Odogwu Buga",
        "acct_num": "081",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "male",
        "is_married": False
    },
    {
        "name": "Abigail UCJ",
        "acct_num": "044",
        "age": 24,
        "balance": 10_000,
        "type": "savings",
        "gender": "female",
        "is_married": False
    },
]

names = [customer["name"] for customer in customers]
avg_age = sum(customer["age"] for customer in customers) / len(customers)
savings_account_holders = [customer for customer in customers if customer["type"] == "savings"]
print(names)
print(avg_age)
print(savings_account_holders)
