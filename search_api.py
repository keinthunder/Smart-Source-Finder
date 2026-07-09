from duckduckgo_search import DDGS

def search_web(question):

    websites = []

    search = DDGS()

    results = search.text(question, max_results=5)

    for result in results:

        title = result["title"]
        url = result["href"]

        websites.append({
            "title": title,
            "url": url
        })

    return websites
