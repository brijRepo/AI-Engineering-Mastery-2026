Problem 1: VALID PARENTHESIS - Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Brute-Force:
 while "()" in s or "{}" in s or "[]" in s, keep replacing it with blank and if s is blank, its valid
 O(N^2)

Optimized:
for every open bracket, append the closing bracket in a blank list, else check if not equal to current character, return false. Return true at last
O(N)


Problem 2: MERGE SORTED ARRAY - You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Optimized:
compare each list from end and keep adding the larger element from the end in list1. merge all list2 if elements are left
O(N)


Problem 3: BEST TIME TO BUY AND SELL STOCK - You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Optimized:
for each price, if price < min_price update min_price and if max_profit < current_profit then update max_profit and return it at last
O(N)