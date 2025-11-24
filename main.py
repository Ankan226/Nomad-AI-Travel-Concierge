import sys
from colorama import Fore, Style, init
from agents.researcher import ResearcherAgent
from agents.planner import PlannerAgent

# Initialize colors
init(autoreset=True)

def main():
    print(Fore.CYAN + "==========================================")
    print(Fore.CYAN + "   NOMAD: AI CAPSTONE TRAVEL CONCIERGE    ")
    print(Fore.CYAN + "==========================================\n")

    # 1. User Input
    destination = input("Where do you want to go? (e.g., Tokyo, Paris): ")
    days = input("How many days? (e.g., 3): ")

    print(Fore.YELLOW + f"\n[Manager] Activating Agents for a {days}-day trip to {destination}...\n")

    # 2. Initialize Agents
    researcher = ResearcherAgent()
    planner = PlannerAgent()

    # 3. Execution Step 1: Research
    print(Fore.GREEN + "[Manager] Tasking 'Scout' (Researcher) to gather intel...")
    research_summary = researcher.perform_research(destination)
    print(Fore.WHITE + "Research Complete. Summary received.")
    
    # DEBUG: See what the researcher found (Proof of Context Passing)
    print(Fore.LIGHTBLACK_EX + f"DEBUG_DATA: {research_summary}") 

    # 4. Execution Step 2: Planning
    print(Fore.GREEN + f"\n[Manager] Tasking 'Atlas' (Planner) to build the {days}-day itinerary...")
    final_plan = planner.create_itinerary(research_summary, days)

    # 5. Output
    print(Fore.MAGENTA + "\n" + "="*20 + " FINAL ITINERARY " + "="*20)
    print(Fore.WHITE + final_plan)
    print(Fore.MAGENTA + "="*57)

if __name__ == "__main__":
    main()