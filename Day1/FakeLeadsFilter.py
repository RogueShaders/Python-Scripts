leads = [
    {"name": "Alice", "budget": 500, "source": "Facebook"},
    {"name": "Bob", "budget": 1500, "source": "Google Ads"},
]

for x in leads:
   if x["budget"] >= 1000:
      print(x)