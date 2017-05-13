# Read file lines as list
lists = list(open('Artist_lists_small.txt', encoding='utf-8').readlines())


# Join all lines
total_list = ','.join(lists)


for i in range(len(lists)):
    j = lists[i]
    # Convert string into list of artists
    lists[i] = j.replace('\n', '').split(',')

# Find all unique artists
artists = list(set(total_list.replace('\n', '').split(',')))

vector_list = dict()
list_length = len(lists)

for artist in artists:
    vector_list[artist] = list()

# Enumerate the lists
for i, j in enumerate(lists):
    for k in j:
        # Append the index of the list to the vector_list[<artist>]
        vector_list[k].append(i)

final = list()

##### CORE ALGORITHM START #####
for i in range(len(artists)):
    # Compare the artist only with subsequent artists as current artist would've
    # already been compared with previous artists
    for j in range(i + 1, len(artists)):
        # Take the set of indices of artists[i]
        a = set(vector_list[artists[i]])
        # Take the set of indices of artists[j]
        b = set(vector_list[artists[j]])
        # If the number of common indices is >50 add the pair to the final list
        if len(list(a.intersection(b))) > 50:
            final.append((artists[i], artists[j]))
        #print(i, j)
##### CORE ALGORITHM END #####

print(final)
print(len(final))

#Time Complexity - O(n^2/2)
