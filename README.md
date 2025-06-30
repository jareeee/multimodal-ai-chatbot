# Multimodal AI Coding Assistant

This is a prototype of an advanced AI assistant designed to help developers and students understand complex technical concepts. This assistant not only responds with text but is also capable of generating visual diagrams and providing voice responses, creating an interactive and multimodal learning experience.

---

## 🚀 Key Features

- **💬 Context-Aware Conversations:** Remembers conversation history to provide relevant and coherent answers.
- **🎨 Concept Visualization (Tool Use):** Can generate diagrams, architectural plans, or flowcharts on the fly when requested by the user, thanks to DALL-E 3 integration.
- **🔊 Voice Responses (Text-to-Speech):** Every response from the assistant is automatically spoken aloud for a more natural user experience.
- **🖥️ Interactive Web UI:** Built with Gradio for an easy-to-use interface accessible through a web browser.
- **🧠 Customizable Persona:** The assistant's behavior and expertise are defined through an external system prompt.
- **🤖 Multi-Model Support:** Designed to easily switch between different underlying AI models (e.g., GPT-4o, GPT-3.5-Turbo).

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x
- **AI Models:** OpenAI (GPT-4o / GPT-3.5-Turbo, DALL-E 3, TTS-1)
- **UI Framework:** Gradio
- **Audio Processing:** Pydub
- **Core Libraries:** openai, gradio, python-dotenv, pydub

---

## ⚙️ Installation and Setup

Follow these steps to get this project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate an Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.

Using Conda:
```bash
conda create --name ai_assistant python=3.10
conda activate ai_assistant
```

### 3. Install Dependencies
Install all the required libraries from the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
You will need an OpenAI API key for the application to work.

a. Create a new file named .env in the root project folder.
b. Copy and paste the following format into the .env file:
```python
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MODEL="gpt-4o-mini"
```
c. Replace sk-xxxxxxxx... with your valid OpenAI API key.
d. You can change the MODEL to any other supported model, such as gpt-3.5-turbo.

IMPORTANT: Never share your .env file or your API key. This file is included in .gitignore by default to prevent it from being uploaded to GitHub.

### ▶️ How to Run
Once all installation and configuration steps are complete, run the application with the following command from your terminal:

```bash
python main.py
```
The application will start and provide a local URL (usually http://127.0.0.1:7860) that you can open in your browser.

💡 Usage Examples

***Asking a Basic Concept***:

**You**: "What is the difference between var, let, and const in JavaScript?"\
**AI**: (Provides a textual explanation and speaks it aloud)

***Requesting a Visualization***:

**You**: "Please draw me a basic diagram of a Transformer architecture."\
**AI**: (Calls the visualize_concept tool, generates a diagram, displays it in the UI, and then provides a textual explanation of the diagram, which it also speaks aloud)
