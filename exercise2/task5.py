def smallest_average(person1: dict, person2: dict, person3: dict):
    # Calculating smallest average
    average_person1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    average_person2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    average_person3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    # Determining the contestant with the smallest average
    if average_person1 < average_person2 and average_person1 < average_person3:
        return person1["name"], person1
    elif average_person2 < average_person1 and average_person2 < average_person3:
        return person2["name"], person2
    else:
        return person3["name"], person3


person1 = {"name": "Pentti", "result1": 5, "result2": 70, "result3": 1}
person2 = {"name": "Seppo", "result1": 2, "result2": 10, "result3": 5}
person3 = {"name": "Jorma", "result1": 3, "result2": 5, "result3": 9}

smallestavg_name, smallestavg_results = smallest_average(person1, person2, person3)
print(
    "Contestant with the smallest average:",
    smallestavg_name,
    "\nFull results:",
    smallestavg_results,
)
