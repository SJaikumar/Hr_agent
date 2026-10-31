import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()


model_client=OpenAIChatCompletionClient(model="gpt-4o-mini")

agent= AssistantAgent(
    name="hr_assistant",
    model_client=model_client,
    system_message="You are an HR Assistant",
)

#async def main():
    #await Console(agent.run_stream(task="Generate a job description of a python developer in five distinctive lines. " \
    #"I do not need any company details. Just the skills required for a python developer. The output should be formatted in a" \
    #"sequence order as in 1,2,3, 4,5"))
    #await model_client.close()


async def main():
    try:
        while True:
            # Get role from user
            job_role = input(
                "\nEnter job role (or 'exit' to quit): "
            ).strip()

            if job_role.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not job_role:
                print("Please enter a job role.")
                continue

            # Your original prompt, now dynamic
            prompt = (
                f"Generate a job description of a {job_role} "
                "in five distinctive lines. "
                "I do not need any company details. "
                f"Just the skills required for a {job_role}. "
                "The output should be formatted in sequence "
                "order as 1, 2, 3, 4, 5."
            )

            await Console(
                agent.run_stream(task=prompt)
            )

    finally:
        await model_client.close()

asyncio.run(main())

