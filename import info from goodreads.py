import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Fn8oiwOhbpxC38NeqoEw", "isbns": "9781632168146"})
print(res.json())
