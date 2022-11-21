# if i'm hungry
#     then i"ll have breakfast
# else
#     I won't have breakfast

hungry_for_breakfast = False
hungry_for_lunch = True


if hungry_for_breakfast:
    print("I'll have breakfast")
elif hungry_for_lunch:
    print("I'll have lunch")
else:
    print("I won't have breakfast or lunch")

# or
if hungry_for_breakfast or hungry_for_lunch:
    print("I'll have breakfast or lunch")
else:
    print("I won't have breakfast and lunch")

# and
if hungry_for_breakfast and hungry_for_lunch:
    print("I'll have breakfast and lunch")
else:
    print("I won't have breakfast or lunch")

# not
if not hungry_for_breakfast:
    print("I'll not have breakfast")
else:
    print("I will have breakfast")
