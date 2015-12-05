#program to print the song 99 bottles of beer
#use range and a loop



for bottles in range(99,2,-1):
	print "{0} bottles of beer on the wall, {0} bottles of beer ...".format(bottles)
	print "If one of those bottles should hapen to fall, {0} bottles of beer on the wall".format(bottles-1)

#to handle the singular bottle when I finally get to 1
print "2 bottles of beer on the wall, 2 bottles of beer ..."
print "If one of those bottles should hapen to fall, 1 bottle of beer on the wall"
