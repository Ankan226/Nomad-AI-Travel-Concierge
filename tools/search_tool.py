import warnings
# Filter specific RuntimeWarnings from the library
warnings.filterwarnings("ignore", category=RuntimeWarning)

from ddgs import DDGS

class SearchTool:
    def run(self, query):
        print(f"   [Tool] Searching internet for: {query}")
        try:
            # Added region='wt-wt' to standardise results
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                results = DDGS().text(query, region='wt-wt', max_results=3)
            
            if not results:
                return "No results found."
            
            return "\n".join([f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}" for r in results])
        except Exception as e:
            return f"Error searching: {str(e)}"