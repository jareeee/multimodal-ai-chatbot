# Import library
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
from tools import visualize_concept, talker
from image_save import upload_image_to_imgur

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL") # Customizable model name
client = OpenAI()

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

with open("developer_message.txt") as f:
    DEVELOPER_PROMPT = f.read()

tools = [
    {
        "type": "function",
        "name": "visualize_concept",
        "description": "Membuat diagram visual, flowchart, atau ilustrasi berdasarkan konsep teknis. Gunakan tool ini HANYA jika pengguna secara eksplisit meminta 'diagram', 'gambar', 'visualisasi', 'ilustrasi', atau 'gambarkan'.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "Deskripsi singkat dan jelas dalam bahasa Inggris mengenai konsep yang akan divisualisasikan. Contoh: 'A flowchart explaining the Git branching model' atau 'The architecture of a Transformer network'."
                }
            },
            "required": ["topic"],
            "additionalProperties": False,
        }
    }
]

# Fungsi yang akan dihubungkan ke Gradio
def chat_interface(history):
    try:
        messages = [{"role": "system", "content": DEVELOPER_PROMPT}]
        for msg in history:
            if isinstance(msg, dict) and "role" in msg and "content" in msg:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

        response = client.responses.create(
            model=MODEL,
            input=messages,
            tools=tools,
            tool_choice="auto",
        )
        image = None

        if response.output[0].type == "function_call":
            function_call = response.output[0]
            if function_call.name == "visualize_concept":
                topic = json.loads(function_call.arguments).get("topic")
                if topic:
                    image = visualize_concept(topic)
                    image_path = "temp_image.png"
                    image.save(image_path)
                    imgur_url = upload_image_to_imgur(image_path)

                    messages.append(function_call)
                    messages.append({
                        "type": "function_call_output",
                        "call_id": function_call.call_id,
                        "output": f"![Diagram]({imgur_url}"
                    })

                    response = client.responses.create(
                        model=MODEL,
                        input=messages,
                        tools=tools,
                    )

        reply = response.output_text
        history += [{"role": "assistant", "content": reply}]
        # talker(reply) # remove comment if you want to enable TTS
        return history, image
    except Exception as e:
        print(f"Error in chat_interface: {e}")
        # Tambahkan error message ke history dan return default values
        error_message = f"Maaf, terjadi error: {str(e)}"
        history += [{"role": "assistant", "content": error_message}]
        return history, None

# Bangun Antarmuka (UI) dengan Gradio
with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(height=500, type="messages")
        image_output = gr.Image(height=500)
    with gr.Row():
        entry = gr.Textbox(label="Chat with our AI Assistant:")
    with gr.Row():
        clear = gr.Button("Clear")

    def do_entry(message, history):
        history += [{"role":"user", "content":message}]
        return "", history

    entry.submit(do_entry, inputs=[entry, chatbot], outputs=[entry, chatbot]).then(
        chat_interface, inputs=chatbot, outputs=[chatbot, image_output]
    )
    clear.click(lambda: None, inputs=None, outputs=chatbot, queue=False)



ui.launch(inbrowser=True)