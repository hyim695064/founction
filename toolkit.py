# def greet(name):
#     print("hello", name)
# greet("agent x")
#2
# def add(a, b):
#     print(a +b)
# add(3, 4)
#3
# def square(n):
#     print(n ** 2)
# square(5)
# square(12)
#4
# def greet_with_title(name, title="agent"):
#     print("hello", title, name)
# greet_with_title("x")
# greet_with_title("x", title = "person")
#5
# def describe(name, level, active):
#      print("name", name)
#      print("level", level)
#      print("active", active)
# describe(name = "agent x", level = 5, active =True)
# describe(level = 5, active = True, name = "agent x")
# #6
# def multiply(a, b=2):
#     print(a *b)
# multiply(4)
# multiply(4,9)
# def print_largest(a, b, c):
#     if a >= b and  c:
#         print(a)
#     elif b >= a and  c:
#         print(b)
#     elif c >= a and  b:
#         print(c)
# print_largest(3, 8, 5)
# print_largest(10, 2, 7)
# print_largest(4, 4, 1)
# def show_fahrenheit(c):
#     print((c *9/5)+32)
# show_fahrenheit(0)
# show_fahrenheit(100)
# show_fahrenheit(37.5)
# def check_even(n):
#     if n  % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# check_even(4)
# check_even(7)
#10
# def summarize(items):
#     largest = items[0]
#     smallest = items[0]
#     for num in items:
#         if largest < num:
#             largest = num
#         if smallest > num:
#             smallest = num
#     print("sum", sum(items))
#     print("smallest", smallest)
#     print("largest", largest)
# summarize([4, 9, 2, 10, 3])
#p2s1
def show_all(*args):
    for item in args:
        print(item)
show_all("radio", "map", "flashlight")    



