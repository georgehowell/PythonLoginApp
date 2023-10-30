# room_num = {'john': 425, 'tom': 212, 'isaac': 345}
# for k, v in room_num.items():
#     print (k + ' is in room ' + str(v))
def get_values(lst, key):
    # base case: if the list is empty, return an empty list
    if not lst:
        return []
 
    # get the first dictionary in the list
    first_dict = lst[0]
 
    # check if the key is in the first dictionary
    if key in first_dict:
        # if the key is in the dictionary, add the value to the result list
        result = [first_dict[key]]
    else:
        # if the key is not in the dictionary, the result list is empty
        result = []
 
    # recursively call the function on the rest of the list
    result += get_values(lst[1:], key)
 
    return result
 
 
# initializing list
test_list = [{'gfg': 1, 'is': 2, 'good': 3},
             {'gfg': 2}, {'best': 3, 'gfg': 4}]
 
# printing original list
print("The original list is : " + str(test_list))
 
# get values of 'gfg' key using recursive method
res = get_values(test_list, 'gfg')
 
# printing result
print("The values corresponding to key : " + str(res))
# this code contributed by tvsk
