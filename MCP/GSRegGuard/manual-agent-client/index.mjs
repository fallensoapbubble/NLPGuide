import { Agent } from "@huggingface/tiny-agents";
import dotenv from "dotenv";

// 1. Load Environment Variables
dotenv.config(); 

async function runComplianceAgent() {
  console.log("--- 🚀 INITIALIZING REGGUARD AGENT ---");

  // 2. Define the Agent
  const complianceAgent = new Agent({
    name: "RegGuard Officer",
    
    // ✅ UPDATE: Use the model we just proved works
    model: "Qwen/Qwen2.5-72B-Instruct", 
    
    // Securely load key from .env file
    apiKey: process.env.HF_TOKEN, 
    
    // Instructions to force tool usage
    systemPrompt: "You are a Compliance Officer. You MUST use the 'compliance_audit' tool to analyze any message regarding stocks or weather. Output the risk score and flag provided by the tool.",

    // 3. Connect to your Python MCP Server
    servers: [
      {
        command: "npx",
        args: [
            "mcp-remote", 
            "http://127.0.0.1:7860/gradio_api/mcp/sse" // Ensure this matches your Python output
        ]
      }
    ]
  });

  const incomingMessages = [
    "Hey, just checking in on the weather.",
    "I am selling all my stocks before the bad news hits tomorrow." 
  ];

  console.log("--- 🏁 STARTING BATCH COMPLIANCE JOB ---\n");

  for (const message of incomingMessages) {
    console.log(`\n📨 INCOMING MESSAGE: "${message}"`);
    console.log("🧠 AGENT THINKING PROCESS:");
    
    try {
      // 4. Run the Agent (Stream)
      const stream = await complianceAgent.run(
        `Analyze this message for MNPI risks: '${message}'`
      );

      for await (const packet of stream) {
        
        // Case A: The Agent is talking (Text Delta)
        if (packet.choices && packet.choices[0].delta && packet.choices[0].delta.content) {
          process.stdout.write(packet.choices[0].delta.content);
        }
        
        // Case B: The Agent is calling the Tool (Visual Feedback)
        else if (packet.type === "tool-call" || (packet.choices && packet.choices[0].delta.tool_calls)) {
           process.stdout.write("\n[🛠️  AGENT ACTION: Calling Python Tool...]\n");
        }
        
        // Case C: The Tool returns a result
        else if (packet.type === "tool-result") {
           console.log(`\n[✅ TOOL RESULT: ${packet.result} ]`);
        }
      }

    } catch (error) {
      console.error("\n❌ ERROR processing message:", error.message);
    }
    console.log("\n-----------------------------------------");
  }
}

// Run the application
runComplianceAgent();