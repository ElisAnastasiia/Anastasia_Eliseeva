from collections import Counter
from itertools import groupby

"""
 Task №1
 
 In this task you will create a function that takes
 a list of non-negative integers and strings and
 returns a new list with the strings filtered out.
"""

def arr_filter(arr):
    filtered = [num for num in arr if isinstance(num, (int))]
    return filtered

def Task1():
    print("Task-1 ")
    list_1 = [1, 2, "a", "b"]
    list_2 = [1, "a", "b", 0, 15]
    list_3 = [1, 2, "aasf", '1', "123", 123]
    print(arr_filter(list_1))
    print(arr_filter(list_2))
    print(arr_filter(list_3))

"""
 Task №2

 In this task, function takes a string input,
 and returns the first character that is not repeated anywhere in the string.
"""

def first_non_repeating_letter():
    print("\n Task-2")
    string = input("Input text 'sTreSS': ")
    dict = {}
    lowercase_string = string.lower()

    for ch in lowercase_string:
        if ch in dict:
            dict[ch] = dict[ch] + 1
        else:
            dict[ch] = 1

    for ch in lowercase_string:
        if ch in dict and dict[ch] == 1:
            index = lowercase_string.find(ch)
            return print("First non-repeated letter: ",string[index])

"""
 Task №3
 
 Digital root is the recursive sum of all the digits in a number.
 Given n, take the sum of the digits of n. If that value has more than one digit,
 continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
"""

def digital_root(n):
    print("\n Task-3")
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return print("Result: ",n)

"""
 Task №4

 Count the number of pairs in the array, the sum of which will give target
"""

def Task4():
    print("\n Task-4 ")
    arr = [1, 3, 6, 2, 2, 0, 4, 5]
    n = len(arr)
    sum = 5
    count = 0
    list = []
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                list += (arr[i],arr[j])
                count += 1
    return print(" number of pairs: ", count,"\n",
          [(list[i],list[i+1]) for i in range(0,len(list),2)] )

"""

Task №5

program that
· makes this string uppercase
· gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name.
 Last name and first name of a guest come in the result between parentheses separated by a comma.
"""

def Task5(s):
    print("\n  Task-5 ")
    sorted_list = ["({}, {})".format(*reversed(name.split(":"))).upper()
                            for name in s.split(";")]

    return print("".join(sorted(sorted_list)))





if __name__ == '__main__':
    Task1()
    first_non_repeating_letter()
    digital_root(942)
    Task4()
    s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    Task5(s)
