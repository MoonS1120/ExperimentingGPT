import openai

openai.api_key = "API-KEY"

prompt = "Write a paragraph using these information. \'Year 11 Student\',\'Joined Garden international school in Year 4\', \'Passionate about STEM\', \'hope to contribute to the school community in a positive way\'"

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.2,
)

message = completions.choices[0].text

print(message)
