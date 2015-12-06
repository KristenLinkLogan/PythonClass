#new version of the PB&J program that uses a while loop

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

#get the ingredient amounts
bread_slices = raw_input("How many slices of bread do you have? ")
pb = raw_input("How many servings of peanut butter do you have? ")
jelly = raw_input("How many servings of jelly do you have? ")

#convert the string input variables into integers
bread_slices = int(bread_slices)
pb = int(pb)
jelly = int(jelly)

#set the number of sandwiches made (initialize sandwiches variable)
sandwiches = 0

while bread_slices >= 2 and pb >=1 and jelly >=1:
	sandwiches = sandwiches + 1
	print "Making sandwich #{0}".format(sandwiches)
	bread_slices = bread_slices - 2
	pb = pb - 1
	jelly = jelly - 1
	
	# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

	if min(bread_slices/2,pb,jelly) > 0:
		print "I have enough bread for {0} more sandwich(es), enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread_slices/2,pb,jelly)
	elif bread_slices <= 1:
		print "All done; I ran out of bread."
	elif pb == 0:
		print "All done; I ran out of peanut butter."
	elif jelly == 0:
		print "All done; I ran out of jelly"


if sandwiches == 0:
	print "There aren't enough ingredients to make a sandwich."
# elif sandwiches == 1:
# 	print "All done; only had enough ingredients for {0} sandwich.".format(sandwiches)
# else:
# 	print "All done; had enough ingredients for {0} sandwich(es)".format(sandwiches)
