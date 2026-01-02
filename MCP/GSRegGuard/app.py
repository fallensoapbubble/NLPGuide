import json
import gradio as gr
from transformers import pipeline

# LOAD THE AI MODEL
# We use a Zero-Shot Classification pipeline. 
# It runs locally on your machine (CPU friendly).
# It can categorize text into ANY labels we give it.
print("Loading AI Model... this may take a minute...")
# framework="pt" forces PyTorch
# device=-1 tells it to use CPU (since you don't have NVIDIA CUDA set up yet)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", framework="pt")


def compliance_audit(text: str) -> str:
    """
    Analyzes communication text for regulatory compliance risks.

    Args:
        text (str): The email or chat log to audit.

    Returns:
        str: A JSON string containing risk_score, flag, and status.
    """
    # Define our custom financial risk labels
    candidate_labels = ["insider trading risk", "financial advice", "normal business conversation"]
    
    # Run the AI model
    output = classifier(text, candidate_labels)
    
    # Extract the highest scoring label
    top_label = output['labels'][0]
    top_score = output['scores'][0]
    
    # Determine Status based on a Risk Threshold (e.g., 70% confidence)
    risk_found = top_label in ["insider trading risk", "financial advice"] and top_score > 0.7
    
    result = {
        "flag": top_label.upper().replace(" ", "_"),
        "risk_score": round(top_score, 2),
        "status": "NON_COMPLIANT" if risk_found else "COMPLIANT",
        "action_required": "Escalate to Compliance" if risk_found else "None"
    }

    return json.dumps(result)

# Create the Gradio Interface
demo = gr.Interface(
    fn=compliance_audit,
    inputs=gr.Textbox(placeholder="Paste email/chat log here...", lines=3),
    outputs=gr.Textbox(label="Audit Result (JSON)"),
    title="RegGuard: MNPI Risk Detection System",
    description="Agentic Compliance tool that detects Insider Trading risks using Zero-Shot LLM techniques."
)

# Launch the interface and MCP server
if __name__ == "__main__":
    demo.launch(mcp_server=True)