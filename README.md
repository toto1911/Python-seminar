# Python-seminar


 Problem Statement for FromToDivisible

    	
Bearland consists of N cities, numbered 1 through N. 
Some pairs of cities are connected by one-way roads of unit length. 
The distance from city X to city Y is the smallest number of roads you need to
traverse in order to get from X to Y.

The road network has a special structure. 
You are given a description of this structure: two int[]s a and b, each with M elements. 
For each pair of distinct cities (X,Y), there is a one-way road from X to Y if and only 
if there is at least one index i such that X is divisible by a[i] and Y is divisible by b[i].

For example, suppose that N = 7, M = 1, a[0] = 2, and b[0] = 3. 
In this case the country has 7 cities and it contains the following one-way 
roads: 2 -> 3, 2 -> 6, 4 -> 3, 4 -> 6, 6 -> 3, and 6 -> 6.

You are given the int N. 
You are also given two ints S and T: the source city where you start your 
journey and the target city you want to reach.
 
Finally, you are given the int[]s a and b described above.

If there is no path from S to T, return -1. Otherwise, compute and return the distance from S to T.
