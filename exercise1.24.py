#1.
location = ""
print("Health Board         No. of new cases        Average age of patient (yrs)")
for i in range(1, 14):
    if i == 1:
        location = "Ayreshire & Arran"
        total = 0
        num = int(input("How many new cases for " + location + "?: "))
        for j in range(1, num):
            id1 = int(input("Please enter your patient ID number: "))
            age1 = int(input("Please enter your age: "))
            total += age1
        average = total / num
    elif i == 2:
        location = "Borders"
    elif i == 3:
        location = "Dumfries & Galloway"
    elif i == 4:
        location = "Fife"
    elif i == 5:
        location = "Forth Valley"
    elif i == 6:
        location = "Grampian"
    elif i == 7:
        location = "Greater Glasgow & Clyde"
    elif i == 8:
        location = "Highland"
    elif i == 9:
        location = "Lanarkshire"
    elif i == 10:
        location = "Lothian"
    elif i == 11:
        location = "Orkney"
    elif i == 12:
        location = "Shetland"
    elif i == 13:
        location = "Tayside"
    else:
        location = "Eileanan Siar Western Isles"

    #print()
#print("Finished")
print()
