Problem 1: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Brute-Force:
for every element of the array, check if other element is summing up to target and add the indices
O(N^2)

Optimized:
for each element of the array, return the index if complement else add the index
O(N)


Problem 2: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Brute-Force:
for every element of the array, check if other element is duplicate and return true else return false
O(N^2)

Optimized:
return false if length of array is not equal to the length of its set else return true
O(1)


Problem 3: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Brute-Force:
sort both strings, then check if equal
O(NlogN)

Optimized:
for each element of an array, increase the frequency of character and decrease the frequency of character in that hashmap for each of the other array, then check if any character has non-zero value
O(N)
