# 🤖 DomainBot – Your Smart Domain-Specific Assistant

DomainBot is a sleek and intelligent Streamlit-based chatbot that allows you to explore expert-level responses within **specific domains** like Space, IT, and Medical. With support for **multiple LLMs (via Ollama)**, dynamic **temperature control**, and a beautiful UI, DomainBot is ideal for focused, contextual, and creative conversations.

---

## 🚀 Features

- 🌐 **Domain Restriction** – Only answer questions in selected domain (Space, IT, or Medical)
- 🤖 **Switchable LLMs** – Choose from `gemma3:4b`, `tinyllama:latest`, or `phi3:3.8b`
- 🔁 **Temperature Control** – Adjust creativity with a user-friendly slider (Low to High)
- 💬 **Streamlit UI** – Clean, elegant, and responsive frontend
- 💡 **System Prompts** – Ensures responses stay on-topic and domain-specific
- 🛠️ **Locally Hosted** – Powered by Ollama, no external APIs or cloud costs

---

## 🧠 Domains & Behavior

| Domain | Description | Sample Questions |
|--------|-------------|------------------|
| **Space** | Covers astronomy, astrophysics, cosmology | “What are quasars?”, “What causes solar flares?” |
| **IT** | Software, networking, coding, systems | “Explain REST APIs”, “What is TCP/IP?” |
| **Medical** | Health, treatments, anatomy, diseases | “What is diabetes?”, “How does insulin work?” |

If a question is **off-topic**, the bot will respond with a polite refusal (enforced via system prompt).

---

## ⚙️ LLMs Available

| Model | Description |
|-------|-------------|
| `gemma3:4b` | Lightweight, high-quality open model by Google |
| `tinyllama:latest` | Distilled version of LLaMA2, optimized for speed |
| `phi3:3.8b` | Small but strong Microsoft model with code/data reasoning |

All models are loaded locally via [Ollama](https://ollama.com).

---

## 🎨 Temperature Control (Creativity)

| Range | Effect |
|-------|--------|
| **0.0 – 0.3** | Low: Factual, accurate, deterministic |
| **0.4 – 0.8** | Medium: Balanced and coherent |
| **0.9 – 2.0** | High: Creative, speculative, or imaginative |

---

## 💻 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/domainbot.git
cd domainbot
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Or install manually:
```bash
pip install streamlit requests
```

### 4. Pull LLMs via Ollama
Install Ollama if not already, then:
```bash
ollama pull gemma:4b
ollama pull tinyllama
ollama pull phi3:3.8b
```

### 5. Run the Chatbot
```bash
streamlit run domain_chatbot.py
```
---

## 📁 File Structure
```bash
📦 domainbot/
 ┣ chatbot_icon.png         # Optional UI icon
 ┣ domain_chatbot.py        # Main Streamlit app
 ┣ requirements.txt         # Python dependencies
 ┗ README.md                # You're reading it
```
---
## 🧪 Example Prompts
### Space (Low Temp)
What causes lunar eclipses?
### IT (Medium Temp)
Compare Node.js and Python for backend systems.
### Medical (High Temp)
Describe a futuristic surgery using nanobots.

---

## ✍️ Author
Built by [Saqib Mehdi](https://github.com/SaqibMehdi123)
For learning, productivity, and domain-specific tasks with local LLMs.

## 📄 License
MIT License – Use it, modify it, improve it!
