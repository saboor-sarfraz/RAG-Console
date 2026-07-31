# OpenAI FAQ — API Usage

**Source:** OpenAI Help Center  
**Category:** API  
**FAQ ID:** OAI-API  
**Last Updated:** 2024-12-10  

---

## API Basics

---

**Q: How do I get access to the OpenAI API?**

A: To access the OpenAI API:

1. Create an account at [platform.openai.com](https://platform.openai.com).
2. Add a payment method under **Settings > Billing**.
3. Generate an API key under **API keys**.
4. Use the key in your requests via the `Authorization: Bearer YOUR_API_KEY` header.

New accounts receive a small free credit (amount varies by promotion). After the credit is exhausted or expires, usage is billed to your payment method.

**Organization accounts:** If you're part of an organization, your admin may provide you with an Organization ID, which you pass as `OpenAI-Organization: org-xxx` in your API headers. This ensures usage is billed to and tracked under the correct organization.

---

**Q: What models are available through the API?**

A: OpenAI offers several model families through the API:

**GPT-4 family (most capable):**
- `gpt-4o` – Omni model; fast, multimodal (text + image input), strong reasoning
- `gpt-4o-mini` – Smaller, cheaper version of GPT-4o; great for most tasks
- `gpt-4-turbo` – Previous generation; large context window (128K tokens)
- `gpt-4` – Original GPT-4; slower and more expensive than newer variants

**o-series (reasoning models):**
- `o1` – Deep reasoning model; thinks before answering; excels at math, coding, logic
- `o1-mini` – Faster, cheaper reasoning model
- `o3-mini` – Latest reasoning model with extended thinking capabilities

**GPT-3.5 family (legacy, low-cost):**
- `gpt-3.5-turbo` – Older but cheap and fast; suitable for simpler tasks

**Specialized models:**
- `text-embedding-3-small` / `text-embedding-3-large` – Text embeddings for semantic search and RAG
- `whisper-1` – Speech-to-text transcription
- `tts-1` / `tts-1-hd` – Text-to-speech
- `dall-e-3` / `dall-e-2` – Image generation
- `gpt-4o-realtime-preview` – Low-latency audio + text for real-time applications

Use the `/v1/models` endpoint to see the full current list of available models.

---

**Q: How does the token-based pricing work?**

A: OpenAI charges based on the number of **tokens** processed. Tokens are chunks of text — roughly 1 token ≈ 4 characters or ¾ of a word in English.

**Pricing is split into:**
- **Input tokens** (your prompt + conversation history sent to the model) — cheaper
- **Output tokens** (the model's response) — more expensive

**Example pricing (approximate, check platform.openai.com for current rates):**

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| gpt-4o | $2.50 | $10.00 |
| gpt-4o-mini | $0.15 | $0.60 |
| o1 | $15.00 | $60.00 |
| o1-mini | $3.00 | $12.00 |
| gpt-3.5-turbo | $0.50 | $1.50 |
| text-embedding-3-small | $0.02 | — |

**Batch API discount:** Using the Batch API (for non-real-time, async requests) gives you a **50% discount** on both input and output tokens. Results are returned within 24 hours.

**Prompt caching discount:** For long, repetitive prompts, OpenAI automatically applies **prompt caching** when the same prefix is reused. Cached input tokens are charged at a 50% discount.

---

**Q: What is a context window and why does it matter?**

A: The **context window** is the maximum amount of text (measured in tokens) that a model can process in a single request — including both your input (system prompt + conversation history + user message) and the model's output.

**Current context windows:**

| Model | Context Window |
|---|---|
| gpt-4o | 128,000 tokens |
| gpt-4o-mini | 128,000 tokens |
| o1 | 200,000 tokens |
| gpt-3.5-turbo | 16,385 tokens |

**Why it matters for RAG:**
- Larger context windows let you send more retrieved documents in a single prompt
- But larger contexts cost more (more input tokens)
- Models can also lose focus on information in the middle of very long contexts ("lost in the middle" problem) — keep the most relevant context near the beginning or end

**Practical rule:** Keep your total prompt + expected output under 90% of the context window to avoid truncation errors.

---

**Q: What is the difference between the Chat Completions API and the Assistants API?**

A: These are two distinct APIs for different use cases:

**Chat Completions API (`/v1/chat/completions`)**
- Stateless — you send the full conversation history every request
- Simple, flexible, and fast
- You manage conversation state in your own application
- Best for: Simple chatbots, one-off completions, custom integrations

```json
{
  "model": "gpt-4o",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is RAG?"}
  ]
}
```

**Assistants API (`/v1/assistants`)**
- Stateful — OpenAI manages conversation threads for you
- Supports built-in tools: Code Interpreter, File Search (RAG), Function Calling
- Persistent Threads store conversation history server-side
- Best for: Complex workflows requiring tool use, long multi-turn conversations, file-based Q&A

**When to use which:**
- For RAG pipelines you build yourself: **Chat Completions** (more control, lower cost)
- For rapid prototyping with file Q&A: **Assistants API** with File Search
- For agentic workflows with multiple tools: **Assistants API**

---

**Q: How do I use function calling / tool use in the API?**

A: Function calling lets the model decide when to call a function you define and returns a structured JSON payload that your code can execute.

**Basic workflow:**
1. Define your functions (tools) in the `tools` array.
2. Send a message. The model may respond with a `tool_calls` object instead of text.
3. Execute the function in your own code.
4. Send the function result back to the model as a `tool` role message.
5. The model generates a final response using the function output.

**Example tool definition:**
```json
{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Get the current weather for a location",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "City and state, e.g. 'San Francisco, CA'"
        },
        "unit": {
          "type": "string",
          "enum": ["celsius", "fahrenheit"]
        }
      },
      "required": ["location"]
    }
  }
}
```

**`tool_choice` parameter:**
- `"auto"` (default) – Model decides whether to call a tool
- `"none"` – Model never calls a tool (always returns text)
- `{"type": "function", "function": {"name": "get_weather"}}` – Force a specific function call

---

**Q: What are rate limits and how do I handle them?**

A: Rate limits restrict how many requests or tokens you can use per minute, day, or month. They prevent overuse and ensure fair access.

**Rate limit dimensions:**

| Limit Type | Description |
|---|---|
| **RPM** | Requests per minute |
| **TPM** | Tokens per minute |
| **RPD** | Requests per day |
| **TPD** | Tokens per day |
| **IPM** | Images per minute (for image models) |

Limits vary by model and your **usage tier** (which increases automatically as you spend more with OpenAI).

**Usage tiers:**

| Tier | Requirement |
|---|---|
| Free | $0 spent |
| Tier 1 | $5 paid |
| Tier 2 | $50 paid + 7 days since first payment |
| Tier 3 | $100 paid + 7 days |
| Tier 4 | $250 paid + 14 days |
| Tier 5 | $1,000 paid + 30 days |

**Handling rate limit errors (HTTP 429):**
- Implement **exponential backoff** — wait progressively longer before retrying (e.g., 1s, 2s, 4s, 8s)
- Add **jitter** (random delay) to avoid thundering herd problems
- Process large batches via the **Batch API** to avoid real-time rate limits
- Monitor usage in the Dashboard and request limit increases if needed

---

**Q: How do I use the Embeddings API for RAG?**

A: The Embeddings API converts text into high-dimensional numerical vectors that capture semantic meaning. These vectors are used in RAG pipelines to find relevant documents.

**Endpoint:** `POST /v1/embeddings`

**Request:**
```json
{
  "model": "text-embedding-3-small",
  "input": "How do I set up a Stripe subscription?",
  "encoding_format": "float"
}
```

**Response:** Returns a vector of 1,536 floats (for `text-embedding-3-small`) or 3,072 floats (for `text-embedding-3-large`).

**Model comparison:**

| Model | Dimensions | Performance | Cost |
|---|---|---|---|
| `text-embedding-3-small` | 1,536 | Good | Cheapest |
| `text-embedding-3-large` | 3,072 | Best | Moderate |
| `text-embedding-ada-002` | 1,536 | Legacy | Low |

**Dimension reduction:** `text-embedding-3` models support the `dimensions` parameter to reduce output size (e.g., `"dimensions": 512`) with minimal quality loss — useful for reducing storage costs in large-scale RAG systems.

**RAG pipeline overview:**
1. **Index time:** Chunk documents → embed each chunk → store vectors in a vector DB (Pinecone, Qdrant, Weaviate, etc.)
2. **Query time:** Embed user query → find top-K similar vectors → retrieve chunks → pass to GPT-4o as context

---

**Q: What is streaming and how do I implement it?**

A: Streaming lets you receive model output **token by token** as it's generated, rather than waiting for the full response. This dramatically improves perceived latency in user-facing applications.

**Enable streaming:**
```json
{
  "model": "gpt-4o",
  "messages": [...],
  "stream": true
}
```

**Response format:** The API returns a series of **Server-Sent Events (SSE)**. Each event contains a partial `delta` object:
```
data: {"choices":[{"delta":{"content":"Hello"},"finish_reason":null}]}
data: {"choices":[{"delta":{"content":" world"},"finish_reason":null}]}
data: {"choices":[{"delta":{},"finish_reason":"stop"}]}
data: [DONE]
```

**OpenAI Python SDK (streaming example):**
```python
from openai import OpenAI
client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Tell me a joke"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## Related FAQ Sections

- [OpenAI FAQ — ChatGPT](../chatgpt/openai-faq-chatgpt.md)
- [OpenAI FAQ — Billing & Usage](../billing/openai-faq-billing.md)
- [OpenAI FAQ — Safety & Content Policy](../safety/openai-faq-safety.md)

---

*Couldn't find your answer? Visit [OpenAI Help Center](https://help.openai.com)*
