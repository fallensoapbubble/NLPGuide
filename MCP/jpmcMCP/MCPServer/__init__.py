# 2. Mock Data Layer
# In a real job, these would be API calls to Jira REST API or AWS CloudWatch.
# For this demo, we simulate the database to keep it runnable locally.
MOCK_TICKETS = {
    "JIRA-101": {
        "title": "Fix memory leak in Vector DB", 
        "status": "Open", 
        "priority": "High"
    },
    "JIRA-102": {
        "title": "Update Terraform scripts for EKS", 
        "status": "In Progress", 
        "priority": "Medium"
    }
}

MOCK_LOGS = {
    "build-88": "ERROR: Connection refused to Redis at 127.0.0.1:6379\n[CRITICAL] Deployment failed.",
    "build-89": "SUCCESS: All unit tests passed. Artifact uploaded to S3."
}

