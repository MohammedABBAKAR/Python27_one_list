# Two Lists inside a List to One
# Programmer Pete is trying to combine two lists inside one list into one without 
# changing the order of the list nor the type and because he's pretty advanced
#  he made it without blinking, but I want you to make it, too.

# Examples
# one_list([[1, 2], [3, 4]]) ➞ [1, 2, 3, 4]

# one_list([["a", "b"], ["c", "d"]]) ➞ ["a", "b", "c", "d"]

# one_list([[True, False], [False, False]]) ➞ [True, False, False, False]
# Notes
# Remember to return the list.
# Check Resources for more info.











def one_list(nested_lists):
    # Concatenate the two lists inside the nested list
    return nested_lists[0] + nested_lists[1]

# Examples
print(one_list([[1, 2], [3, 4]]))          # Output: [1, 2, 3, 4]
print(one_list([["a", "b"], ["c", "d"]]))  # Output: ["a", "b", "c", "d"]
print(one_list([[True, False], [False, False]]))  # Output: [True, False, False, False]
