
"""
    Time Complexity:- O(m+n)
    Space Complexity:- O(m+n)
"""
def merge_two_sorted_list_with_auxiliary_space(list1, list2):
    merged_list = []
    m = 0
    n = 0
    while (m < len(list1) and n < len(list2)):
        if(list1[m] > list2[n]):
            merged_list.append(list2[n])
            n += 1
        else:
            merged_list.append(list1[m])
            m += 1
        
    while(m < len(list1)):
        merged_list.append(list1[m])
        m += 1

    while(n < len(list2)):
        merged_list.append(list2[n])
        n += 1

    return merged_list


print(merge_two_sorted_list_with_auxiliary_space([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


"""
    Time complexity:- O(m*n) , worst case:- O(n^2), since insert takes -> O(n)
    Space:- O(m) where m < n
"""

def merge_two_sorted_list_without_auxiliary_space(list1, list2):
    m = 0
    n = 0
    while (m < len(list1) and n < len(list2)):
        if(list1[m] > list2[n]):
            list1.insert(m, list2[n])
            n += 1
            m += 1
        else:
            m += 1
        
    if n < len(list2):
        list1.extend(list2[n:])

    return list1


print(merge_two_sorted_list_without_auxiliary_space([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))