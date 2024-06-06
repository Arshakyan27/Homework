# 8. Dictionaries Exercise:
# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.

def find_book(title):
    books = {'rafi':'samvel','artur':'sherlock','dastaevski':'apushy'}
    for k,v in books.items():
        if title == v:
            return k
        
print(find_book('samvel'))