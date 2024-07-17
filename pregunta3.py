import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

# Define prompts
few_shot_prompt = "Translate the following sentence into French: Hello, how are you?"
cot_prompt = "Write a story about a robot who learns to feel emotions."
prompt_chain = "Write a poem about the beauty of nature. Then, continue the poem with a stanza about the changing seasons."
additional_prompt = "Generate a list of top 10 recommended books for summer reading."

# List of prompts
prompts = [few_shot_prompt, cot_prompt, prompt_chain, additional_prompt]

# Loop through prompts and generate responses
for index, prompt in enumerate(prompts, start=1):
    response = model.generate_content(prompt)
    
    # Save response to a file
    filename = f"response_{index}_{prompt[:20].replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Prompt:\n{prompt}\n\nResponse:\n{response.text}\n")
    
    # Print confirmation
    print(f"Saved response for prompt {index}: {prompt}")
    print(f"Saved to file: {filename}\n")
