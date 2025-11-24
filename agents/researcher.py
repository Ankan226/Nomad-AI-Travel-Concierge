from agents.base import Agent
from tools.search_tool import SearchTool

class ResearcherAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Scout",
            role="Travel Researcher",
            instructions="""You are a travel researcher. 
            1. Use the search tool to find real-time info.
            2. CRITICAL: If the search tool returns "No results found" or errors, DO NOT FAIL. 
               Instead, generate the best possible answer using your own internal knowledge about the location.
            3. Always return a summary of: Top 3 Attractions, Local Cuisine, and General Weather trends."""
        )
        self.search_tool = SearchTool()

    def perform_research(self, location):
        # 1. Search for general info
        print(f"   [Scout] Searching for attractions in {location}...")
        info = self.search_tool.run(f"top tourist attractions in {location} 2024")
        
        # 2. Search for weather
        print(f"   [Scout] Searching for weather in {location}...")
        weather = self.search_tool.run(f"current weather forecast {location} this week")
        
        # 3. Synthesize (With Fallback Logic)
        synthesis_prompt = f"""
        Research Task: Gather travel info for {location}.
        
        Raw Search Results (Attractions): {info}
        Raw Search Results (Weather): {weather}
        
        INSTRUCTIONS:
        - If the raw results contain useful info, summarize them.
        - If the raw results say "No results" or "Error", IGNORE the tool and write a detailed report based on your own knowledge of {location}.
        - Format the output clearly for the Planner agent.
        """
        return self.generate_response(synthesis_prompt)