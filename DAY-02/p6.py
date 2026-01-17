user={
    "First name": "ABC",
    "middle name": "AAA",
    "last name": "XYZ",
    "Parents":{
        "Father":{
            "Name":"AAAAA"
        },
        "Mother":{
            "Name":"ABBAA"
        }
    },
    "qualification":["SSC","HSC","BCA"],
    "hobbies":{"Drawing","driving"},
    "isAlive":True
}

print(user)
print(user["isAlive"])
user["isAlive"] = False
print(user["isAlive"])
print(type(user))