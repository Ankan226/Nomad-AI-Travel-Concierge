from agents.base import Agent

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Atlas",
            role="Itinerary Designer",
            instructions="You are an expert travel logistician. You take raw research notes and convert them into a generic Day-by-Day itinerary. Be concise and formatted."
        )

    def create_itinerary(self, research_data, days):
        prompt = f"""
        Based on the following research:
        {research_data}
        
        Create a {days}-day itinerary. Use emojis. Make it exciting.
        """
        return self.generate_response(prompt)