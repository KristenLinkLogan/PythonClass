# Challenge Level: Intermediate and Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially because you're putting them up on GitHub!

# For the purposes of this exercise, we're going to use unrealistically perfect and uniform addresses, and one-word first names :)

studybuddy_1 = 'Alison McCauley, 1234 County Line Road, Skaneateles, NY 13152'
studybuddy_2 = 'Dee Cater, 555 Bradford Pkwy, Syracuse, NY 13224'
studybuddy_3 = 'Andrea Bianchi, 987 South St, Jamesville, NY 13078'
studybuddy_4 = 'Kristen Link Logan, 264 Craig Street, Syracuse, NY 13211'
studybuddy_5 = 'Nina Verity, 111 Bridge St, Solvey, NY 13209'

# Goal 1: Create a program that simply shows all the ZIP codes.
# Sample output:
# 13152
# 13224
# 13078
# (etc)

# bud1_len = len(studybuddy_1)
# bud2_len = len(studybuddy_2)
# bud3_len = len

print studybuddy_1[-5:]
print studybuddy_2[-5:]
print studybuddy_3[-5:]
print studybuddy_4[-5:]
print studybuddy_5[-5:]

# Goal 2: Modify your program to output all the ZIP codes on the same line, with an an explanatory sentence.
# Sample output: (but use any language you want!)
# Our study group included people from these ZIP codes: 13152, 13224, 13078, (etc).

print "Our study group included people from these ZIP codes: {0}, {1}, {2}, {3}, {4}.".format(studybuddy_1[-5:],studybuddy_2[-5:],studybuddy_3[-5:],studybuddy_4[-5:],studybuddy_5[-5:])

# Goal 3: Modify your program to show each study buddy's first name and ZIP code.
# Sample output: (again, use any language you want!)
# Alison lives in 13152.
# Dee lives in 13224.
# Andrea lives in 13078.
# (etc)

bud1_end = studybuddy_1.find(" ")
bud2_end = studybuddy_2.find(" ")
bud3_end = studybuddy_3.find(" ")
bud4_end = studybuddy_4.find(" ")
bud5_end = studybuddy_5.find(" ")

print "{0} lives in {1}".format(studybuddy_1[0:bud1_end],studybuddy_1[-5:])
print "{0} lives in {1}".format(studybuddy_2[0:bud2_end],studybuddy_2[-5:])
print "{0} lives in {1}".format(studybuddy_3[0:bud3_end],studybuddy_3[-5:])
print "{0} lives in {1}".format(studybuddy_4[0:bud4_end],studybuddy_4[-5:])
print "{0} lives in {1}".format(studybuddy_5[0:bud5_end],studybuddy_5[-5:])
