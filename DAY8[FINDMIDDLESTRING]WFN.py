string = input("Please provide a word")

def mid(string):
    truemiddle = len(string)
    length = len(string)
    if length % 2 == 0:
        return ("No true middle")
    else:
        return (string[(length // 2)])

print(mid(string))