from collections import defaultdict
# Create a defaultdict with a default value of 0
dd = defaultdict(int)
# Add some key-value pairs
dd['apple'] += 1        
dd['banana'] += 2
dd['orange'] += 3
# Print the defaultdict
print(dd.items())

# Create a defaultdict with a default value of an empty list
dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
dd_list['vegetables'].append('beetroot')
print(dd_list.items())
print(dd_list['guava'])

#creating a defaultdict with a default value of an empty string
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)
print(sd['farewell'])  # Output: '' (empty string, not present, returns default value instead of KeyError)

#text processing example
words=['apple','banana','avocado','orange','beetroot','anjeer', 'wonton']
grouped=defaultdict(list)
for word in words:
    first_letter=word[0]
    grouped[first_letter].append(word)
    
for key,values in grouped.items():
    print(f"{key}:{values}")


defdict=defaultdict(lambda: 'N/A')
defdict['name'] = 'Alice'
print(defdict['name'])  # Output: 'Alice'
print(defdict['age'])   # Output: 'N/A' (not present, returns default value from lambda function)
print(defdict.__missing__('classs'))