from mcp.server.fastmcp import FastMCP
from typing import Dict

# 1. Initialize the Server
# We name it specifically for the domain.
mcp = FastMCP("JPMC_SDLC_Fabric_Agent")




from __init__ import MOCK_TICKETS,MOCK_LOGS

# 5. Define Prompts (The Templates)

@mcp.prompt()
def generate_pr_description(ticket_id: str, changes: str) -> str:
    #Internal import to avoid circular import ERROR!!!!
    from tool import fetch_jira_ticket,analyze_build_failure

    from reso import architecture_guidelines,security_policies,coding_standards,docker_deployment_practices
    """
    Generates a standardized Pull Request description based on a Jira ticket.
    Ensures all PRs follow the JPMC Audit compliance format.
    """
    # Attempt to get ticket context (Simulating a DB fetch)
    ticket_info = MOCK_TICKETS.get(ticket_id, {"title": "Unknown", "priority": "Unknown"})
    
    # We return the *Instruction* to the LLM, not the final text itself.
    # The LLM will use this instruction to generate the actual PR text.
    return f"""
    You are a Senior Software Engineer at JPMC.
    Please draft a Pull Request description for the following task.
    
    CONTEXT:
    - Ticket ID: {ticket_id}
    - Ticket Title: {ticket_info['title']}
    - Actual Code Changes: {changes}
    
    COMPLIANCE REQUIREMENTS:
    1. Summary: Concise explanation of the "Why" and "What".
    2. Testing: List unit tests added or manual verification steps.
    3. Risk: High/Medium/Low assessment based on the priority ({ticket_info['priority']}).
    """

# 6. Entry Point (The Switch)







#    mcp dev src/agent.py
if __name__ == "__main__":
    # This starts the server and listens for connections
    mcp.run()

