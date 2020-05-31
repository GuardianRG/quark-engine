import copy


def remove_dup_list(element):
    """
    Remove the duplicate elements in  given list.
    """
    return list(set(element))


def contains(small_list, big_list):
    """
    check the sequence pattern within two list.
    -----------------------------------------------------------------
    small = ["getCellLocation", "sendTextMessage"]
    big_list = ["put", "getCellLocation", "query", "sendTextMessage"]
    then it will return true.
    -----------------------------------------------------------------
    small = ["getCellLocation", "sendTextMessage"]
    big_list = ["sendTextMessage", "put", "getCellLocation", "query"]
    then it will return False.

    """
    big_copy = copy.deepcopy(big_list)

    # Delete elements that do not exist in the small list
    for item in big_copy:
        if item not in small_list:
            big_copy.remove(item)

    for i in range(len(big_copy) - len(small_list) + 1):
        for j in range(len(small_list)):
            if big_copy[i + j] != small_list[j]:
                break
        else:
            return True
    return False
