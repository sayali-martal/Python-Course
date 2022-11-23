months = {"jan": "January", "feb": "February", "mar": "March"}
numberKeys = {3: "January", 1: "February", 2: "March"}

print(months["jan"], numberKeys[3])

print(months.get("feb", "Not a valid key"))
print(months.get("apr", "Not a valid key"))
