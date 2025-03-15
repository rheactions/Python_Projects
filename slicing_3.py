def is_rotation(s1,s2):
    if len(s1) != len(s2):
        return False

    temp = s1

    for _ in range (len(s1)):
        temp = temp[1:] + temp [0]
        if temp == s2:
            return True

    # for _ in range(len(s1)):
    #     temp = temp [:3] + temp[3]
    #     if temp == s2 :
    #         return True
    # this is wrong logic as temp [:3] choose everything from starting till second last i.e abc
    # and then [3 ] guves us last charater which is d ,
    #then concatenating would give us abcd which is unchanged we want to shift d to the front
    #so take last character which [-1] + [:3]

    # for _ in range(len(s1)):
    #     temp = temp [-1] + temp[:3]
    #         if temp == s2 :
    #             return True

    return False

print(is_rotation('abcd','dabc'))