"""
Remove all characters from a given string that appear more than once in it.

Example

For str = "zaabcbd", the output should be removeDuplicateCharacters(str) = "zcd".
"""
def removeDuplicateCharacters(str):
    item = dict.fromkeys(str,0)
    for i in str:
        item[i]+=1
    return ''.join([i for i in item.keys() if item[i]==1])