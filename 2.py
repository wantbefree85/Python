seconds = input("Please input time in seconds: ")
hours = int(seconds) // 3600
minutes = (int(seconds) - (int(hours) * 3600)) // 60
sec = int(seconds) - (minutes * 60 + hours * 3600)
print(str(hours) + ":" + str(minutes) + ":" + str(sec))