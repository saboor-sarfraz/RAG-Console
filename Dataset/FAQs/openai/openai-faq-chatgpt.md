# OpenAI FAQ — ChatGPT

**Source:** OpenAI Help Center  
**Category:** ChatGPT  
**FAQ ID:** OAI-CHAT  
**Last Updated:** 2024-12-08  

---

## ChatGPT General Questions

---

**Q: What is the difference between ChatGPT Free, Plus, and Team plans?**

A: OpenAI offers several ChatGPT subscription tiers:

| Feature | Free | Plus ($20/mo) | Team ($25/user/mo) | Enterprise (custom) |
|---|---|---|---|---|
| GPT-4o access | Limited | Full | Full | Full |
| GPT-4o-mini | Unlimited | Unlimited | Unlimited | Unlimited |
| o1 / o3-mini | No | Yes (limited) | Yes | Yes |
| Message limits | Lower cap | Higher cap | Highest | Custom |
| Advanced data analysis | No | Yes | Yes | Yes |
| Image generation (DALL·E) | No | Yes | Yes | Yes |
| Custom GPTs | Use only | Create & use | Create & use | Create & use |
| File uploads | Limited | Yes | Yes | Yes |
| Browsing (web search) | Limited | Yes | Yes | Yes |
| Team workspace | No | No | Yes | Yes |
| Admin controls | No | No | Yes | Yes |
| Conversation history off option | Yes | Yes | Yes | Yes |
| API access | No | No | No | Separate |

**Note:** Message limits for GPT-4o on Plus reset every 3 hours. When you hit the cap, ChatGPT automatically falls back to GPT-4o-mini so you can keep chatting.

---

**Q: What is GPT-4o and how is it different from GPT-4?**

A: **GPT-4o** ("o" for "omni") is OpenAI's flagship multimodal model. Key differences from GPT-4:

- **Speed:** GPT-4o is significantly faster than GPT-4 Turbo
- **Cost:** Cheaper to run (important for API users)
- **Multimodal:** GPT-4o natively handles text, images, and audio in both input and output (native audio capabilities are progressively rolling out)
- **Vision:** GPT-4o has strong image understanding — analyze charts, photos, screenshots, documents
- **Same intelligence:** GPT-4o matches or exceeds GPT-4 Turbo on most benchmarks

**GPT-4o-mini** is a smaller, faster, cheaper version — great for most everyday tasks and high-volume applications.

---

**Q: What are Custom GPTs and how do I create one?**

A: **Custom GPTs** (formerly "GPTs") are personalized versions of ChatGPT configured for specific purposes. They can have:
- A custom name and profile picture
- Custom instructions (a persistent system prompt)
- Specific capabilities enabled or disabled (web browsing, code execution, image generation)
- Uploaded knowledge files (PDFs, docs) the GPT references when answering
- Custom actions (API integrations with external services)

**Creating a Custom GPT:**
1. Go to [chatgpt.com](https://chatgpt.com) and click **Explore GPTs** > **Create**.
2. Use the **GPT Builder** (conversational setup) or click **Configure** for manual setup.
3. Fill in: Name, description, instructions, capabilities, and knowledge files.
4. Set sharing: **Only me**, **Anyone with link**, or **Everyone** (public in GPT store).
5. Click **Save**.

**Use cases for Custom GPTs:**
- Customer support bots trained on your documentation
- Coding assistants with your company's style guide
- Data analysis helpers pre-loaded with your schema
- Writing assistants matching a specific tone or format

Custom GPT creation requires a **Plus, Team, or Enterprise** plan.

---

**Q: Does ChatGPT remember previous conversations?**

A: ChatGPT has two memory systems:

**1. Memory (persistent across conversations)**
ChatGPT can remember facts you tell it across separate sessions (e.g., your name, job, preferences). Memory items are stored and referenced in future conversations automatically.

- View and manage memories: Click your profile > **Settings > Personalization > Manage memory**
- You can delete individual memories or clear all memories
- Available on Plus and higher plans; available to some Free users

**2. Conversation history (within a single session)**
Within one conversation, ChatGPT remembers everything said in that session — this is the standard context window behavior, not persistent memory.

**Turning off history:**
Go to **Settings > Data controls > Improve the model for everyone** (toggle off). When off:
- Conversations are not saved to your history
- OpenAI does not use them to train models
- Memory does not update during these sessions

---

**Q: Can ChatGPT browse the internet?**

A: Yes, ChatGPT has a built-in web browsing tool available on **Plus, Team, and Enterprise** plans (and sometimes Free with limitations). When browsing is used:
- ChatGPT searches the web in real time
- It reads and synthesizes content from web pages
- Responses include citations with links to sources

**When ChatGPT uses browsing:**
- You explicitly ask for current information ("What's in the news today?")
- The question involves recent events beyond its training data
- You paste a URL and ask ChatGPT to read it

**Limitations of browsing:**
- Some websites block web crawlers and ChatGPT can't access them
- ChatGPT may not always choose to browse even when it should
- Real-time data (live stock prices, sports scores) may still not be perfectly current

You can explicitly trigger browsing by saying "Search the web for..." or enabling it in the model tools.

---

**Q: What is Advanced Data Analysis and what can it do?**

A: **Advanced Data Analysis** (formerly "Code Interpreter") allows ChatGPT to write and execute Python code in a sandboxed environment. This enables:

**Data tasks:**
- Upload a CSV, Excel, or JSON file and ask ChatGPT to analyze it
- Clean and transform messy data
- Create charts and visualizations (matplotlib, seaborn, plotly)
- Run statistical analyses

**File tasks:**
- Convert files between formats (e.g., CSV to Excel, PDF to text)
- Merge or split files
- Compress or resize images

**Math and computation:**
- Solve complex math problems step by step
- Run iterative simulations
- Evaluate expressions

**How to use it:**
1. Ensure you're using GPT-4o (Advanced Data Analysis is only available with this model).
2. Upload a file by clicking the **attachment** icon in the chat input.
3. Ask your question about the data.

Files uploaded to ChatGPT in this context are processed in an isolated environment and not shared. Files expire after the conversation ends.

---

**Q: What file types can I upload to ChatGPT?**

A: Supported file types depend on what you want to do:

**Documents (for reading/Q&A):**
- PDF, DOCX, TXT, MD, HTML, CSV, JSON, XML

**Images (for vision tasks):**
- PNG, JPEG, WEBP, GIF (static)

**Data files (for Advanced Data Analysis):**
- CSV, XLSX, JSON, XML, TXT, TSV

**Code files:**
- Most programming language extensions (.py, .js, .ts, .java, .cpp, etc.)

**Not supported:**
- Video files
- Audio files (except via Whisper API separately)
- Executable files (.exe, .app)
- Encrypted or password-protected files
- Very large files (limits vary; typically a few hundred MB per file)

**File size limits:** Approximately 512 MB per file, and up to around 20 files per conversation (limits may vary and are subject to change).

---

**Q: Is my data used to train OpenAI's models?**

A: By default:
- **Free and Plus users:** Conversations **may** be used to train models unless you opt out.
- **Team and Enterprise users:** Conversations are **not** used to train models by default.

**To opt out (Free/Plus):**
- Go to **Settings > Data controls**
- Toggle off **"Improve the model for everyone"**

When opted out, your conversations are not used for training and are not retained beyond 30 days. The toggle is per-account and persists across sessions.

**API users:** Prompts sent via the API are **not used for training** by default.

**Important:** Even when you opt in to training, OpenAI states it applies safety reviews and filtering before using data. Personal or sensitive information may still be reviewed by humans for safety purposes.

---

**Q: Why did ChatGPT give me incorrect information?**

A: ChatGPT can make mistakes, including:

- **Hallucinations:** Generating confident-sounding but factually incorrect information
- **Outdated knowledge:** Information beyond the training cutoff (currently early 2024 for GPT-4o) may be incorrect
- **Math errors:** Despite improvements, GPT models can make arithmetic mistakes, especially in multi-step calculations
- **Misunderstanding context:** Ambiguous questions may be interpreted incorrectly

**Best practices to reduce errors:**
- For factual claims, ask ChatGPT to cite its sources or enable web browsing
- For important math, use the **Advanced Data Analysis** tool which runs actual Python code
- Double-check critical information against authoritative sources
- Ask ChatGPT to "think step by step" or explain its reasoning — this often reduces errors
- Break complex questions into smaller parts

ChatGPT is a language model, not a search engine or database. It's best used as a starting point for research, a drafting tool, or a code writing assistant — not as the sole source of truth for critical decisions.

---

**Q: What is ChatGPT's knowledge cutoff date?**

A: ChatGPT's training data has a **knowledge cutoff**, meaning it doesn't know about events after that date (unless it uses web browsing).

- **GPT-4o and GPT-4o-mini:** Early 2024
- **o1:** Early 2024
- **GPT-3.5-turbo:** January 2022

When you ask about recent events:
- If web browsing is available and enabled, ChatGPT will search the web
- If browsing is not available, ChatGPT will note that it doesn't have current information and may offer what it knew as of the cutoff

For time-sensitive queries, always verify with current sources.

---

## Related FAQ Sections

- [OpenAI FAQ — API Usage](../api/openai-faq-api.md)
- [OpenAI FAQ — Billing & Usage](../billing/openai-faq-billing.md)
- [OpenAI FAQ — Safety & Content Policy](../safety/openai-faq-safety.md)

---

*Couldn't find your answer? Visit [OpenAI Help Center](https://help.openai.com)*
