leads = [
    {"name": "Alice", "budget": 500, "source": "Facebook"},
    {"name": "Bob", "budget": 1500, "source": "Google Ads"},
]

def filter_leads_by_budget(leads, min_budget):
    result = [ ]
    for lead in leads:
        if lead["budget"] >= min_budget:
            result.append(lead)
    return result

for lead in filter_leads_by_budget(leads, 1000):
    print(f"Name: {lead['name']} | Budget: {lead['budget']} | Source: {lead['source']}")
