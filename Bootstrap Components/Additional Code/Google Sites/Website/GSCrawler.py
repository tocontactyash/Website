import scholarly
import math
import json

# ------------------------------------ Google Scholar Crawler ------------------------------------ 

def get_from_GS(Name): 

    # Retrieve the author's data, fill-in
    search_query = scholarly.search_author(Name)
    author = next(search_query).fill()

    '''
    # Printing Author's Interests
    author.interests

    # Printing Author's Email Address
    print (author.email)

    # Printing Author's Picture
    print (author.url_picture)

    Print the titles of the author's publications
    print([pub.bib['title'] for pub in author.publications])
    '''

    return author


author  = get_from_GS('Yash Yadati')
print([pub.bib['title'] for pub in author.publications])

author.publications = author.publications[0].fill()
print([pub.bib['url'] for pub in author.publications])

#print (publi.fill)
# print(publi['bib']['url'])

# print(pub.publications[x].fill() for pub in author.publications)
# print(author.publications)  