# - [ ] 135. **[Practice]** Parse a URL string to get domain, path, query.


"""
We’ll extract:

Domain

Path

Query parameters

example :

https://example.com/products/shoes?id=10&color=black
"""

# method 1
from urllib.parse import urlparse, parse_qs

def parse_url(url):
    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path
    query = parse_qs(parsed.query)

    return domain, path, query


# Example
url = "https://example.com/products/shoes?id=10&color=black"
print(parse_url(url)) # ('example.com', '/products/shoes', {'id': ['10'], 'color': ['black']})

"""
urlparse(url) → breaks URL into parts

parsed.netloc → domain

parsed.path → path

parsed.query → raw query string

parse_qs() → converts query string into dictionary
"""

# manual parsing
def parse_url(url):
    # Remove protocol (http:// or https://)
    if "://" in url:
        url = url.split("://")[1]

    # Separate domain and rest
    parts = url.split("/", 1)
    domain = parts[0]

    rest = parts[1] if len(parts) > 1 else ""

    # Separate path and query
    if "?" in rest:
        path, query = rest.split("?", 1)
    else:
        path = rest
        query = ""

    return domain, "/" + path if path else "", query


# Example
url = "https://example.com/products/shoes?id=10&color=black"
print(parse_url(url))


# convert query to dictionary manually
def parse_query(query_string):
    params = {}
    if query_string:
        pairs = query_string.split("&")
        for pair in pairs:
            key, value = pair.split("=")
            params[key] = value
    return params