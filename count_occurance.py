#count occurance of each element in the list


list = ['a',2,2,'b','c']
# in order to avoid counting the same element twice we will use set
#add the i in set to keep track of counter items
counted = set()
# if you wrote counted = ()
# the expression counted = () is incorrect because ()
# represents an empty tuple, which is immutable
# (cannot be changed after creation).
# This would not be suitable for storing elements that
# you want to keep track of, because tuples do not
# support the add() method.

for i in list:
    if i not in counted:

        print(f"{i} - {list.count(i)}")
        counted.add(i)

