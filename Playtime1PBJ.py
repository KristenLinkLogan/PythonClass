#program that says whether or not I can make a sandwich based on amout of ingredients

#define the variables
bread = 9
pb = 5
jelly = 1

 # if you have enough ingredients to make at least 1 sandwich
if bread >= 2 and pb >= 1 and jelly >= 1:
	# if you have least as much jelly as pb, and at least 2 slices of bread for each serving of jelly
	if jelly <= pb and jelly * 2 <= bread: 
		# you can make as many sandwiches as you have servings of jelly
		sandwiches = jelly 
		print "You can make this many peanut butter & jelly sandwiches: {0}".format(sandwiches)
		#if there is still some pb and bread left
		if (pb-jelly > 0) and (bread-(jelly*2) >= 1):
			#you can make some pb-only sandwiches
			# extra serving of pb available is what is left after using the same number of servings as jelly servings
			extra_pb = pb-jelly
			# extra slices of bread is what is left after using the number of slices needed to use up the jelly servings
			extra_bread = bread-(jelly*2)
			#if the amount of peanut butter left can be used up with the extra bread
			if extra_pb * 2 <= extra_bread:
				#the number of peanut butter sandwiches you can make is equal to the number of servings of peanut butter left
				pb_sandwiches = extra_pb
				print "And you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
			#else if there is not enough bread to use up all the extra peanut butter
			elif extra_pb * 2 > extra_bread:
				#you can make as many sandwiches as can be made with the bread left over (same as below!! -- need to make a function??
				# if you have an even number of slices of bread
				if extra_bread % 2 == 0:
					# you can make as many sandwiches as the # of slices / 2
					pb_sandwiches = extra_bread / 2 
					print "And you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
				# else you have an odd number of slices of bread left over
				elif extra_bread == 1:
					print "You can also make 1 open-faced peanut butter sandwich."
				else:
					# you can make as many sandwiches as the # of slices - 1 divided by 2
					pb_sandwiches = (extra_bread-1)/2
					#you have 1 slice of bread left. if there is still some pb left, you can make 1 open-faced pb sandwich
					if pb_sandwiches < extra_pb:
						print "And you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
						print "You can also make 1 open-faced peanut butter sandwich."
					#you have 1 slice of bread left, but no more pb left
					else:
						print "And you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
			else:
				print "I missed something! (1)"
	# else if you have less pb than, and at least 2 slices of bread for each serving of pb
	elif pb < jelly and pb * 2 <= bread:  
		# you can make as many sandwiches as you have servings of pb
		sandwiches = pb 
		print "You can make this many peanut butter & jelly sandwiches: {0}".format(sandwiches)
	# else you have less bread than you need to use all of your pb or jelly
	elif (jelly <= pb and jelly * 2 > bread) or (pb < jelly and pb * 2 > bread): 
		# if you have an even number of slices of bread
		if bread % 2 == 0: 
			# you can make as many sandwiches as the # of slices / 2
			sandwiches = bread / 2 
			print "You can make this many peanut butter & jelly sandwiches: {0}".format(sandwiches)
		# else you have an odd number of slices of bread
		else:
			# you can make as many sandwiches as the # of slices - 1 divided by 2
			sandwiches = (bread-1)/2
			# you have 1 slice of bread left. if there is still some pb & jelly left, you can make 1 open-faced sandwich
			if sandwiches < pb and sandwiches < jelly:  
				print "You can make this many peanut butter & jelly sandwiches: {0}".format(sandwiches)
 				print "You can also make 1 open-faced peanut butter & jelly sandwich."
			# you have 1 slice of bread left, but not enough pb & jelly to use it
			else:
				print "You can make this many peanut butter & jelly sandwiches: {0}".format(sandwiches)
	else:
		print "I missed something! (2)" 
#else you have enough ingredients to make at least one pb sandwich
elif bread >=2 and pb >=1 and jelly == 0:
	if pb * 2 <= bread:
		#you can make as many pb sandwiches as servings of pb
		pb_sandwiches = pb
		print "There's no jelly, but you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
	elif pb * 2 > bread:
		#bread is the limiting factor
		if bread % 2 == 0:
			#you can make as many sandwiches as the number of slices divided by 2
			pb_sandwiches = bread / 2
			print "There's no jelly, but you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
		else:
			#there is an odd number of slices of bread
			#you can make as many sandwiches as the # of slices minus 1 divided by 2
			pb_sandwiches = (bread-1)/2
			#you have 1 slice of bread left, can you use it to make an open-faced pb sandwich?
			if pb_sandwiches < pb:
				print "There's no jelly, but you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
				print "You can also make 1 open-faced peanut butter sandwich."
			else:
				#you have 1 slice of bread left, but not enough pb to use it
				print "There's no jelly, but you can make this many peanut butter sandwiches: {0}".format(pb_sandwiches)
elif bread == 1 and pb >=1 and jelly >=1:
	print "You only have 1 slice of bread, but you can make an open-faced peanut butter & jelly sandwich."
elif bread == 1 and pb >= 1 and jelly == 0:
	print "You only have 1 slice of bread and no jelly, but you can make an open-faced peanut butter sandwich."
elif bread < 0 or pb < 0 or jelly < 0:
	print "You cannot have a negative amount of bread, peanut butter, or jelly."
#else you don't have enough ingredients to make a sandwich
else:
	print "Looks like you don't have lunch today :("
	if bread == 0 and pb >=1 and jelly >= 1:
		print "You don't have any bread."
	elif bread == 0 and pb == 0 and jelly >=1:
		print "You don't have any bread or peanut butter."
	elif bread == 0 and pb == 0 and jelly == 0:
		print "You don't have any bread, peanut butter, or jelly."
	elif bread ==0 and pb >=1 and jelly ==0:
		print "You don't have any bread or jelly."
	elif bread > 0 and pb == 0 and jelly >=1:
		print "You don't have any peanut butter."
	elif bread > 0 and pb == 0 and jelly == 0:
		print "You don't have any peanut butter or jelly."
	else:
		print "I missed something! (3)"
