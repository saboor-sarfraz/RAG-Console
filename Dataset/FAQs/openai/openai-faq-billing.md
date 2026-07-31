# OpenAI FAQ — Billing & Usage

**Source:** OpenAI Help Center  
**Category:** Billing & Usage  
**FAQ ID:** OAI-BILL  
**Last Updated:** 2024-11-30  

---

## Billing Questions

---

**Q: How does OpenAI billing work?**

A: OpenAI uses two separate billing systems:

**1. ChatGPT subscriptions (chatgpt.com)**
- Monthly subscription fee ($20/month for Plus, $25/user/month for Team)
- Charged on the same date each month via credit card
- Managed at chatgpt.com under **Settings > Subscription**

**2. API usage (platform.openai.com)**
- Pay-as-you-go: You're charged based on tokens used
- Pre-purchase credits or add a payment method for automatic recharge
- Billing cycle: Monthly; invoices generated on the 1st of each month
- Managed at platform.openai.com under **Settings > Billing**

**These are completely separate.** A ChatGPT Plus subscription does **not** give you API access, and API credits do not provide ChatGPT Plus features. You pay for each independently.

---

**Q: How do I set up billing for the API?**

A: 

1. Go to [platform.openai.com](https://platform.openai.com).
2. Click **Settings** > **Billing**.
3. Click **Add payment method**.
4. Enter your credit/debit card details or set up automatic recharge.
5. Optionally, set a **monthly spending limit** to cap your costs.

**Auto-recharge:** When your credit balance falls below a threshold, OpenAI automatically charges your card and adds credit to your account. You set the recharge amount and trigger threshold.

**Manual top-up:** You can also manually buy credits in set amounts ($5, $10, $25, $50, $100, or custom amounts up to $500 at a time for new accounts).

---

**Q: How do I track my API usage and costs?**

A: Several tools are available:

**Dashboard usage page:**
- Go to **platform.openai.com > Usage**
- See daily and cumulative token usage broken down by model
- View costs in real time (with a small delay)

**Activity log:**
- See individual API call logs under **Settings > API keys > (key) > Usage**

**Billing history:**
- Go to **Settings > Billing > Billing history** for monthly invoices and transaction history

**Usage limits:**
- Set a **soft limit** (you receive an email warning when approached)
- Set a **hard limit** (API calls stop when this is reached)
- Configure under **Settings > Limits**

**Monitoring by API key:** You can assign usage limits per API key, making it easy to track spend per project or team member.

---

**Q: Why was I charged more than I expected?**

A: Common reasons for unexpected charges:

**1. You forgot about both input and output tokens**
Pricing covers both your prompt (input) and the model's response (output). Long conversation histories are re-sent with every message, so a long chat accumulates input tokens quickly.

**2. A high-traffic day or spike**
Check your usage graph in the dashboard. Spikes may come from an application bug causing excess requests or a legitimate traffic increase.

**3. Streaming connections left open**
If your code establishes streaming connections and fails to close them properly, you may accumulate charges.

**4. Embeddings at scale**
Embedding large document sets can consume significant tokens. For 1,000 documents of ~1,000 tokens each, you'd use ~1 million tokens for embedding alone.

**5. Auto-recharge triggered multiple times**
If your balance depleted and recharged several times in a month, you may see multiple charges on your credit card statement even though your monthly invoice shows the correct total.

**Resolution:** Check **Usage > Activity** for a breakdown of calls. If you see unexpected usage you didn't initiate, check for compromised API keys and rotate them immediately.

---

**Q: How do I set spending limits to control my API costs?**

A: Go to **platform.openai.com > Settings > Limits**:

**Monthly budget (hard limit):** Once your usage reaches this amount in a calendar month, all API calls return an error (`429 - quota exceeded`) until the next month resets. This prevents runaway spending.

**Email notification (soft limit):** Get an email when you've spent a specified percentage of your monthly budget. Use this as an early warning before hitting the hard limit.

**Per-key limits:** You can set separate usage limits on individual API keys under **Settings > API keys**, which is useful for limiting spend by project or team.

**Recommended setup for new integrations:**
1. Set a hard limit at 2–3x your expected monthly spend
2. Set a soft limit at ~70% of the hard limit
3. Monitor usage daily during the first week of a new integration

---

**Q: Does OpenAI offer any free tier or credits?**

A: 

**For new API accounts:**
OpenAI has offered free credits ($5 or $18 in past promotions) that expire after a certain period (typically 3 months). Check your current credit balance under **Settings > Billing > Credits** — this reflects any active free credits.

**For ChatGPT:**
The free tier of ChatGPT provides access to GPT-4o-mini with limited GPT-4o messages per day, with no credit card required.

**Research and non-profit programs:**
OpenAI offers the **Researcher Access Program** and grants to academic institutions and non-profits. Applications are reviewed case by case.

**Startup programs:**
OpenAI has partnerships with accelerators and cloud providers (Azure, AWS) that may offer credits. Check with your accelerator or cloud provider.

---

**Q: Can I get a refund on API credits?**

A: 

**Pre-purchased credits:** Unused API credits may be refundable within a short window after purchase if they haven't been used. Contact OpenAI Support with your account details and reason for the refund request.

**Credits from expired promotions:** Free or promotional credits that have expired are generally not refundable or extendable.

**Charges for usage:** Usage-based charges for API calls that were actually made are generally non-refundable. If you believe there was an error (e.g., charges for calls you didn't initiate due to a compromised API key), contact Support with evidence.

**ChatGPT Plus subscriptions:** Monthly subscriptions are generally not prorated or refunded for mid-cycle cancellations. Canceling stops future billing but does not refund the current month.

---

**Q: How does the Batch API save money?**

A: The **Batch API** is designed for processing large volumes of requests where results don't need to be returned in real time. Benefits:

- **50% discount** on both input and output tokens vs. standard API pricing
- No rate limit concerns (processed asynchronously)
- Results returned within 24 hours (SLA)

**How it works:**
1. Create a `.jsonl` file where each line is a self-contained API request
2. Upload the file via the Files API
3. Submit a batch job referencing the file
4. Poll for completion or receive a webhook notification
5. Download results as a `.jsonl` file

**Ideal for:**
- Embedding large document sets for RAG pipelines
- Running evaluations on test datasets
- Generating content at scale (product descriptions, summaries)
- Processing customer feedback or support tickets

**Not ideal for:** Real-time user-facing applications where latency matters.

---

**Q: What payment methods does OpenAI accept?**

A: 

**Credit/debit cards:** Visa, Mastercard, American Express, Discover (US). International cards are generally accepted.

**Not accepted:**
- PayPal
- Bank transfers / ACH
- Cryptocurrency
- Prepaid or gift cards (these often fail due to address verification requirements)

**For Enterprise plans:** OpenAI may offer invoiced billing with net payment terms. Contact the sales team to discuss enterprise payment options.

**Tax:** OpenAI may collect applicable taxes (VAT, GST, sales tax) depending on your location and account type. Provide your tax ID if you're a business to ensure correct tax treatment.

---

## Related FAQ Sections

- [OpenAI FAQ — API Usage](../api/openai-faq-api.md)
- [OpenAI FAQ — ChatGPT](../chatgpt/openai-faq-chatgpt.md)
- [OpenAI FAQ — Safety & Content Policy](../safety/openai-faq-safety.md)

---

*Couldn't find your answer? Visit [OpenAI Help Center](https://help.openai.com)*
