import random
R_ADVICE = "check on google then try again!!!"
R_EATING = "I eat nothing because i am a bot!"

def unknown():
    dont_know=["Enter valid statement😌😌","try another way🤔🤔",
    "Please enter again😞😞","sorry! enter again🤫🤫",
    "no! check again😑😑"]
    return (dont_know[random.randrange(0,5)])
