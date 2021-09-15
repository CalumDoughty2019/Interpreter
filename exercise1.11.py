#1.
all = "All"
work = "work"
andd = "and"
no = "no"
play = "play"
makes = "makes"
jack = "jack"
a = "a"
dull = "dull"
boy = "boy"
print(all, work, andd, no, play, makes, jack, a, dull, boy + ".")

#2.
print(6*(1-2))

#3.
#Big comment here for testing
print(6*(1-2))

#4.
bruce = 6
print(bruce + 4)

#5.
# print("")
# P = 10000
# n = 12
# r = (P / 100) * 8
# print("Please input a no. of years")
# print(">>>")
# t = int(input())
# A = (1+(r/n))**t
# AA = P*A
# print(A)
# print(AA)

#6.
print("")
#>>> 5 % 2
# 9 % 5
# 15 % 12
# 12 % 15
# 6 % 6
# 0 % 7
# 7 % 0

#7.
print("")
#clock = 12
#AM = False

print("What is the current time?")
print(">")
current = int(input())

print("What is the no. of hours to wait?")
print(">")
hours = int(input())

answer = (current + hours) % 24
print(str(answer) + ":00")