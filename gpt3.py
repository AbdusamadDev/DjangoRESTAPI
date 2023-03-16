import openai
import gradio as gr

openai.api_key = "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"


def openai_chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.8,
    )
    message = completions.choices[0].text
    return message.strip()


def chatbot(inp, history=[]):
    output = openai_chat(inp)
    print(inp)
    print(output)
    history.append((inp, output))
    return history, history


gr.Interface( 
    fn=chatbot,
    inputs=["text", "state"],
    outputs=["chatbot", "state"]).launch(debug=True, share=True)

