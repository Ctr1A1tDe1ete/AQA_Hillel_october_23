minutes = int(input("how many minutes have passed since the beginning of the day"))

# print((minutes // 1440), minutes % 60)

print(((minutes // 60) % 24), minutes % 60)
