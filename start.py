from lib.googlelib import search



search_results = search("This is my query")
print(search_results)
for result in search_results:
    print(result.description)