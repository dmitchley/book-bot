# def sort_on(items):
#     return items["num"]

# vehicles = [
#     {"name": "car", "num": 7},
#     {"name": "plane", "num": 10},
#     {"name": "boat", "num": 2}
# ]
# vehicles.sort(reverse=True, key=sort_on)
# print(vehicles)

merge_dictionary = {}
my_dictionary = {"key1": "value1", "key2": "value2"}
my_dictionary2 = {"key3": "value4", "key4": "value4"}
#my_dictionary["key10"] = "new_value"

merge_dictionary[my_dictionary.keys()] = my_dictionary.values()

pritn(merge_dictionary)

