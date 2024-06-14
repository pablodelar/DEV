from collections import OrderedDict

# Store each person's languages, keeping track of who responded first.
fav_languages = OrderedDict()

fav_languages['jen'] = ['python', 'ruby']
fav_languages['sarah'] = ['c']
fav_languages['edward'] = ['ruby', 'go']
fav_languages['phil'] = ['python', 'haskell']

print(type(fav_languages)) # collections.OrderedDict

# Display the results, in the same order they were entered.
for name, langs in fav_languages.items():
    print(name + ":")
    for lang in langs:
        print("  - " + lang)