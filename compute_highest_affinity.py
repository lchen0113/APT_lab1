# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").

  sitedic={}
  for n in range(len(site_list)):
    if site_list[n] in sitedic.keys():
      sitedic[site_list[n]].add(user_list[n])
    else:
      sitedic[site_list[n]]=set([user_list[n]])
  #print sitedic[sitedic.keys()[1]]

  affinity=0

  for i in range(len(sitedic.keys())):
    for j in range(i+1,len(sitedic.keys())):
      if len(sitedic[sitedic.keys()[i]].intersection(sitedic[sitedic.keys()[j]]))>affinity:
        affinity=len(sitedic[sitedic.keys()[i]].intersection(sitedic[sitedic.keys()[j]]))
        sites=[sitedic.keys()[i],sitedic.keys()[j]]
        sites.sort(key=str.lower)
  result=(sites[0],sites[1])
  #print result

  return result
