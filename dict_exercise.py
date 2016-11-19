contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Kristen Link Logan"] = {
    "github":"https://github.com/kristenlinklogan"
}

contacts["Sarah Roche"] = {
    "twitter":"sarahrroche",
    "github":"https://github.com/sarahrroche"
}

contacts["Dee Cater"] = {
    "twitter":"@deecater",
    "github":"https://github.com/deecater/"
}

contacts["Alison McCauley"] = {
    "twitter":"@alisonjo2786",
    "github":"https://github.com/alisonjo2786"
}

print contacts
# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner

# two ways to loop through a dictionary
    # 1) use the keys() method to create a list of all the keys to loop through

print "\n"

for contact in contacts.keys():
    print contact
    print contacts[contact]

print "\n"

    # 2) use items() and loop through the nested dictionary
for key,value in contacts.items():
    print key, '\t',value

print "\n"

for key,value in contacts.items():
    print "{0}'s info:".format(key)
    print "\ttwitter: ", contacts.get(key).get('twitter')
    print "\tgithub: ", contacts.get(key).get('github')
