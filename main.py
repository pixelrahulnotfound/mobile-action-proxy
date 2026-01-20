import os
import time
from mobilerun import Mobilerun
from actions import set_action, clear_action

client = Mobilerun(
    api_key=os.environ.get("MOBILERUN_CLOUD_API_KEY")
)

DEVICE_ID = input("enter device id: ")

set_action("OPEN_PROFILE")
target_app=input("enter the target app: ")
print("\n")
# task=input("enter a task: )
tasks=input("enter some tasks: ")
print("\n")
task = client.tasks.run(
    llm_model="google/gemini-2.5-flash",
    device_id=DEVICE_ID,
    task=f"""
    Open the {target_app}.
    Navigate the app ui like a bug bounty hunter and perform {tasks}.
    
    """
)
# wait

# print("Task started, waiting for completion...")


