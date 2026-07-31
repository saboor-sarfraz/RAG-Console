# Stripe FAQ — Account & Verification

**Source:** Stripe Support  
**Category:** Account & Verification  
**FAQ ID:** STRIPE-ACCT  
**Last Updated:** 2024-12-03  

---

## Account Setup & Verification

---

**Q: What information does Stripe need to verify my account?**

A: Stripe is required to collect identity and business information under financial regulations (KYC — Know Your Customer). What's required depends on your business type:

**For individuals / sole proprietors:**
- Full legal name
- Date of birth
- Home address
- Last 4 digits of SSN (US) or equivalent government ID number
- Phone number and email

**For businesses (LLCs, corporations, partnerships):**
- Business legal name and DBA (doing business as) name
- Business address
- Business tax ID (EIN in the US)
- Details on the business type and industry
- Information about beneficial owners (anyone owning 25%+ of the company)
- A representative with signing authority (name, DOB, address, SSN/ID)

**Document uploads:** In some cases, Stripe may request:
- Government-issued photo ID (passport, driver's license, national ID)
- Proof of address (utility bill, bank statement)
- Business registration documents

Stripe may ask for additional information as you process more volume or if automated verification can't confirm details.

---

**Q: How long does account verification take?**

A: Verification timeline varies:

- **Standard verification:** Most accounts are verified automatically within **minutes to a few hours** using Stripe's automated checks.
- **Manual review:** If Stripe needs to manually verify documents, this can take **1–3 business days**.
- **Additional information requests:** If Stripe sends a request for more information, the review clock pauses until you respond.

You can check your verification status in the Dashboard under **Settings > Account > Your details**. Any pending requirements are shown with deadlines.

**Impact of incomplete verification:** Stripe may allow you to process a limited amount before requiring verification. Once limits are reached, payouts may be paused or additional charges blocked until verification is complete.

---

**Q: Why is my account restricted or under review?**

A: Stripe may restrict accounts for several reasons:

| Reason | Common Triggers |
|---|---|
| **Identity verification needed** | Missing or unverified personal/business info |
| **High dispute rate** | Chargeback rate exceeds network thresholds |
| **Suspicious activity** | Unusual transaction patterns flagged by risk systems |
| **Prohibited business** | Business type not permitted by Stripe's Terms of Service |
| **Compliance issue** | Regulatory requirements for your industry or region |
| **Fraud signals** | Potential compromised account or fraudulent activity |

**What to do:** Stripe typically sends an email explaining the restriction and what action is needed. Log into your Dashboard — there will usually be a banner explaining the issue and a link to resolve it.

If you believe a restriction is in error, contact Stripe Support with details about your business and transactions.

---

**Q: What businesses does Stripe not support?**

A: Stripe has a list of **prohibited and restricted businesses**. Prohibited businesses are not allowed on Stripe at all; restricted businesses may be allowed with additional review and approval.

**Prohibited businesses (examples):**
- Illegal products or services in the merchant's jurisdiction
- Child sexual abuse material
- Weapons (certain types), ammunition, and firearm accessories (where restricted by law)
- Drugs and drug paraphernalia (for illegal substances)
- Pyramid schemes and multi-level marketing fraud
- "Get rich quick" schemes
- Counterfeit goods
- Unauthorized aggregation of others' payment flows

**Restricted businesses (require prior approval):**
- Financial services (money transmission, lending, investment advice)
- Gambling and gaming
- Nutraceuticals and supplements with unapproved health claims
- Travel services
- Adult content (requires approval and additional terms)
- Firearms and ammunition (where legally permitted)
- Marketplaces and platforms

If your business falls into a restricted category, contact Stripe before launching to discuss eligibility.

---

**Q: How do payouts work and when will I receive my money?**

A: After a successful charge, funds flow from the customer's bank → Stripe → your bank account. This involves two timelines:

**1. Funds availability (when Stripe holds the money):**
- Card payments: Stripe holds funds for a **2-day rolling period** by default (for new accounts)
- After your account establishes a track record, this often moves to **instant or next-day** payouts
- Some payment methods (e.g., ACH) have longer settlement timelines on Stripe's end

**2. Payout speed (when Stripe sends to your bank):**

| Payout Schedule | Description |
|---|---|
| **Standard (2 days)** | Default for most accounts; funds arrive 2 business days after becoming available |
| **Daily automatic** | Funds paid out every business day |
| **Weekly / Monthly** | Scheduled payouts on a specific day |
| **Manual** | You trigger payouts manually |
| **Instant Payouts** | Available for eligible accounts; funds arrive within 30 minutes (1.5% fee, minimum $0.50) |

You can configure your payout schedule under **Settings > Payouts**.

**New account holds:** Brand new Stripe accounts typically have a 7-day rolling payout delay while establishing a payment history. This reduces gradually with a good payment track record.

---

**Q: Can I have multiple Stripe accounts?**

A: Yes, with some conditions:

- You can create multiple accounts under the same login for different businesses.
- Each business entity (legal entity) should have its own Stripe account.
- You cannot use multiple accounts to circumvent Stripe's policies or payout delays.
- If you're building a platform where others accept payments, use **Stripe Connect** instead of creating separate Stripe accounts for each user.

To create an additional account: Click your account name in the Dashboard (top left) > **New account**.

---

**Q: What is Stripe Connect and when do I need it?**

A: **Stripe Connect** is Stripe's platform and marketplace solution. You need it if:
- You're building a platform where **other businesses or individuals** accept payments through your product
- You need to **split payments** between multiple parties
- You operate a marketplace (e.g., freelancers getting paid through your app)

**Connect account types:**

| Type | Description | Control Level |
|---|---|---|
| **Standard** | Connected accounts have their own Stripe account and dashboard | User manages own settings |
| **Express** | Stripe-hosted onboarding; simplified dashboard for connected accounts | Mixed |
| **Custom** | Fully white-labeled; you control the entire UX | Full |

Standard is simplest to implement. Custom requires the most work but gives the most control. Express is a middle ground suited to most marketplaces.

---

**Q: How do I close my Stripe account?**

A: To close your Stripe account:

1. **Resolve all pending items:** Ensure there are no outstanding disputes, refunds, or payouts pending.
2. **Cancel all active subscriptions** if you're using Stripe Billing.
3. Go to **Settings > Account > Close account**.
4. Follow the prompts to confirm closure.

**Important:**
- You cannot close an account with a positive balance. Withdraw remaining funds first.
- Closed accounts cannot be reopened. Make sure you export any necessary data (invoices, transaction history) before closing.
- Your data is retained by Stripe for regulatory and legal compliance purposes even after account closure.

---

**Q: What should I do if I suspect my Stripe account has been compromised?**

A: Act immediately:

1. **Change your password** at stripe.com.
2. **Enable or reset two-factor authentication (2FA)** under **Settings > Security**.
3. **Revoke all API keys** in **Developers > API keys** and create new ones. Update your integration with the new keys.
4. **Review recent activity:** Check **Payments**, **Payouts**, and **Connected accounts** for any unauthorized activity.
5. **Contact Stripe Support** immediately to report the suspected compromise.

**Signs of account compromise:**
- Unexpected payouts to unfamiliar bank accounts
- API keys used from unknown IP addresses
- Sudden spikes in payment volume from unknown sources
- Unauthorized changes to payout bank account or business details

Stripe's security team can review access logs and help you secure the account.

---

## Related FAQ Sections

- [Stripe FAQ — Payments](./stripe-faq-payments.md)
- [Stripe FAQ — Billing & Subscriptions](./stripe-faq-billing.md)
- [Stripe FAQ — Disputes & Chargebacks](./stripe-faq-disputes.md)

---

*Couldn't find your answer? [Contact Stripe Support](https://support.stripe.com)*
