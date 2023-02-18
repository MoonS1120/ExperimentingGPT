import openai

openai.api_key = "API-KEY"

completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Write a paragraph using these information. \'Year 11 Student\',\'Joined Garden international school in Year 4\', \'Passionate about STEM\', \'hope to contribute to the school community in a positive way\'",
    temperature=0.2,
    max_tokens=1024,
)

writing = completions.choices[0].text

print(writing)
