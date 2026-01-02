# 3. Define Tools (The Actions)


'''
Type Hinting (ticket_id: str): 
This is crucial. 
It tells the LLM that it must provide a string. 
If it tries to provide a number, the validation layer will catch it
'''


from __init__ import MOCK_TICKETS,MOCK_LOGS
from agent import mcp

@mcp.tool()
def fetch_jira_ticket(ticket_id: str) -> str:
    """
    Retrieves ticket details from the Issue Tracking System (Jira).
    Use this tool when the user asks about a specific task, bug, or feature request.
    
    Args:
        ticket_id: The unique identifier (e.g., 'JIRA-101')
    """
    # Simulate DB lookup
    ticket = MOCK_TICKETS.get(ticket_id)
    
    # Handle the "Not Found" edge case (Critical for production code)
    if not ticket:
        return f"Error: Ticket {ticket_id} not found in the system."
        
    return f"Ticket {ticket_id}: {ticket['title']} | Status: {ticket['status']} | Priority: {ticket['priority']}"









@mcp.tool()
def analyze_build_failure(build_id: str) -> str:
    """
    Fetches CI/CD logs for a specific build ID.
    Use this tool when a user reports a deployment failure or pipeline error.
    """
    log = MOCK_LOGS.get(build_id)
    
    if not log:
        return "Error: Build logs not found."
        
    return f"Build {build_id} Logs:\n{log}"