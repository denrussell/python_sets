'''
1. Python Sets Adventure
Objective: The aim of this assignment is to deepen your understanding and 
application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare 
the flight routes of your airline with a competitor. You have two sets of flight 
destinations, one for each airline. Write a Python program to find out:
1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

Example Code:
'''
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def find_common_route(airline1, airline2):
    common_routes = airline1.intersection(airline2)
    print(common_routes)    

def find_unique_route(airline1, airline2):
    unique_routes = airline1.difference(airline2)
    print(unique_routes)

def unique_in_both(airline1, airline2):
    unique_routes = airline1.symmetric_difference(airline2)
    if unique_routes:
        print("Yes. There are destinations that neither airline shares:", unique_routes)
    else:
        print("No. All destinations are shared between the airlines.")


routes = find_common_route(our_routes, competitor_routes)
routes = find_unique_route(our_routes, competitor_routes)
routes = unique_in_both(our_routes, competitor_routes)

