# Selection sorting
# find the index of minimum value in a list
# can use build-in function min
def find_min_index(i_list):
    mining = 0
    for i in range(1, len(i_list)):
        if i_list[i] < i_list[mining]:
            mining = i
    return mining


def selection_sorting(a_list):
    for i in range(0, len(a_list) - 1):
        if len(a_list) <= 1:
            return a_list
        elif a_list[i] > find_min_index(a_list[i + 1:]):
            index_min = a_list.index(min(a_list[i + 1:]))
            a_list[i], a_list[index_min] = a_list[index_min], a_list[i]
    return a_list


list_input = [7, 3, 5, 1, 9, 4]
print(selection_sorting(list_input))
