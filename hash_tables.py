# example of hash table
voted = {}  # empty dict

def check_voter(name):
    if voted.get(name):
        print("You've already voted")
    else:
        voted[name] = True
        print("Thank you for voting")

check_voter("Tom")
check_voter("Tom")

print(voted)

# example 2, caching use case:
cache = {}

def get_page(url):
    if cache.get(url):
        print("Cache hit!")
        return cache[url]
    else:
        print("Fetching from server...")
        data = get_data_from_server(url)
        cache[url] = data
        return data
 
def get_data_from_server(url):
    # process the url from the server as response
    if url == "google.com":
        data = "https://www.google.com.my/index.html"
    elif url == "github.com":
        data = "https://github.com/"
    return data

print(get_page("google.com"))
print(get_page("google.com"))
# print(get_data_from_server())
print(get_page("github.com"))
print(cache)

# other clean example
print("####################################\n\n\n")
import time

DATABASE = {
    "linkedin": {
        "name": "LinkedIn",
        "followers": 5000,
    },
    "reddit": {
        "name": "Reddit",
        "subscribers": 250000,
    },
    "github": {
        "name": "GitHub",
        "stars": 1500,
    },
}

cache = {}

def get_page(url):
    if url in cache:
        print(f"Cache hit: {url}")
        return cache[url]

    print(f"Fetching {url} from server...")
    data = get_data_from_server(url)
    cache[url] = data
    return data

def get_data_from_server(url):
    time.sleep(1)  # simulate network delay
    return DATABASE.get(url, "404 Not Found")


print(get_page("linkedin"))
print(get_page("reddit"))
print(get_page("linkedin"))  # Cached

url_input = input("Enter your url: ")
#print({url_input}) # => "linkedin"
print(get_page(url_input))