from utils.router_llm import classify_query


class RouterAgent:

    def __init__(
        self,
        knowledge_agent,
        maintenance_agent,
        compliance_agent,
        lessons_agent
    ):

        self.agents = {

            "knowledge": knowledge_agent,

            "maintenance": maintenance_agent,

            "compliance": compliance_agent,

            "lessons_learned": lessons_agent

        }

    def route(self, query):


        

        category = classify_query(query)

        print(f"[Router] Category: {category}")

        # ------------------------------------
        # Agent Routing
        # ------------------------------------

        if category not in self.agents:

            category = "knowledge"

        answer, results = self.agents[category].analyze(query)

        return category, answer, results