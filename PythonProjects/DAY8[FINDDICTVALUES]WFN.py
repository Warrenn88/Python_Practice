statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",}

def online_count(statuses):
    list2 = []
    for key in statuses.keys():
        list2.append(statuses[key])
    result = list2.count("online")
    return result

print(online_count(statuses))