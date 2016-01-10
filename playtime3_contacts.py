# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
	"Shannon": {
		"Phone": "202-555-1234",
		"Twitter": "@svt827",
		"Github": "@shannonturner"
	},
	"Beyonce": {
		"Phone": "303-404-9876",
		"Twitter": "@beyonce",
		"Github": "@bey"
	},
	"Tegan and Sara": {
		"Phone": "301-777-3313",
		"Twitter": "@teganandsara",
		"Github": "@heartthrob"
	}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

for key,value in contacts.items():
    print "{0}'s contact information is:".format(key)
    print "\tPhone: {0}".format(contacts.get(key).get('Phone'))
    print "\tTwitter: {0}".format(contacts.get(key).get('Twitter'))
    print "\tGithub: {0}".format(contacts.get(key).get('Github'))


print "\n"

# Goal 2:  Display that information as an HTML table.

print '<table border="1">'

for key,value in contacts.items():
	print '\t<tr>'
	print '\t\t<td colspan="2"> {0} </td>'.format(key)
	print '\t</tr>'
	print '\t<tr>'
	print '\t\t<td> Phone: {0} </td>'.format(contacts.get(key).get('Phone'))
	print '\t\t<td> Twitter: {0} </td>'.format(contacts.get(key).get('Twitter'))
	print '\t\t<td> Github: {0} </td>'.format(contacts.get(key).get('Github'))
	print '\t</tr>'

print '</table>'

print '\n'

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

contacts_html = '<table border="1">'

for key,value in contacts.items():
	contacts_html += '''\n\t<tr>\n\t\t<td colspan="3"> {0} </td>\n\t</tr>\n\t
	<tr>\n\t\t<td> Phone: {1} </td>\n\t\t<td> Twitter: {2} </td>\n\t\t<td> Github: {3} </td>\n\t
	</tr>'''.format(key,contacts.get(key).get('Phone'),contacts.get(key).get('Twitter'),contacts.get(key).get('Github'))

contacts_html += '\n</table>'

# print contacts_html, '\n'

with open('../resources/contacts_goal3.html','w') as contacts_file:
	contacts_file.write(contacts_html)
	

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).

#read in the file bring the entire contents in as a string, which I'm converting to a list of the rows...
with open("../resources/contacts.csv","r") as contacts_file:
	contacts = contacts_file.read().split("\n")

# print contacts,'\n'

# ['Name,Phone,Github,Twitter', 'Shannon,202-555-1234,@shannonturner,@svt827', 
# 'Beyonce,303-404-9876,@bey,@beyonce', 'Tegan and Sara,301-777-3313,@heartthrob,@teganandsara'] 

#I think I'd like to create lists for each piece of information so that I can convert those lists into a dictionary...
names = []
phone_numbers = []
twitter_handles = []
github_handles = []

#first creat lists within the list (list of column headers, list of Shannon info, list of Beyonce info, etc.)
for index, contact in enumerate(contacts): 
	contacts[index] = contact.split(",") 

#remove the first mini list (the column headers/labels) and creates a new list containing them
labels = contacts.pop(0) 

# print labels,'\n'
# print contacts,'\n'

#loop through the list of lists again, and create separate lists for each type of data (all the names, all the phone numbers, etc.)
#Is this an extra step? Can I create a dictionary right from the "Shannon" list??
for index, contact in enumerate(contacts): 
	names.append(contacts[index][0])
	phone_numbers.append(contacts[index][1])
	github_handles.append(contacts[index][2])
	twitter_handles.append(contacts[index][3])

# print labels,'\n'
# print names,'\n'
# print phone_numbers,'\n'
# print github_handles,'\n'
# print twitter_handles,'\n'

#create the dictionary for the data. 
contacts_dict = {}

#for each name, create a dictionary entry with their contact info into contacts_dict
for name, phone, github, twitter in zip(names, phone_numbers, github_handles, twitter_handles):
	#assign the name of the key as 'name' to be an entry in contacts_dict;
	key = name  
	# assign the value of this key as an empty dictionary
	contacts_dict[key] = {} 
	# add the contact info for 'key'
	#could I do something else here... a loop?? perhaps if I had kept all the contact info together?
	contacts_dict[key][labels[1]] = phone
	contacts_dict[key][labels[2]] = github
	contacts_dict[key][labels[3]] = twitter

#print contacts_dict,'\n'

#create the HTML string

contacts_g4_html = '<table border="1">'

for key,value in contacts_dict.items():
	contacts_g4_html += '''\n\t<tr>\n\t\t<td colspan="3"> {0} </td>\n\t</tr>\n\t
	<tr>\n\t\t<td> Phone: {1} </td>\n\t\t<td> Twitter: {2} </td>\n\t\t<td> Github: {3} </td>\n\t
	</tr>'''.format(key,contacts_dict.get(key).get('Phone'),contacts_dict.get(key).get('Twitter'),contacts_dict.get(key).get('Github'))

contacts_g4_html += '\n</table>'

# print contacts_g4_html, '\n'

# write the HTML to a new file
with open('../resources/contacts_goal4.html','w') as contacts_g4_file:
	contacts_g4_file.write(contacts_g4_html)
