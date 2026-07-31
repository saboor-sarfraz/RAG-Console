# Stripe FAQ — Disputes & Chargebacks

**Source:** Stripe Support  
**Category:** Disputes & Chargebacks  
**FAQ ID:** STRIPE-DISP  
**Last Updated:** 2024-10-15  

---

## Understanding Chargebacks and Disputes

---

**Q: What is a chargeback?**

A: A **chargeback** (also called a dispute) occurs when a customer contacts their bank to reverse a charge on their card, rather than requesting a refund directly from you. The bank investigates the claim and may forcibly return the funds to the customer.

When a chargeback is filed:
- The disputed amount is immediately **debited from your Stripe balance**
- A **$15 dispute fee** is charged (this fee is non-refundable regardless of outcome, except on some Visa disputes won by the merchant in the US)
- You have a window (typically **7–21 days** depending on the card network) to submit evidence

---

**Q: What are the common reasons for chargebacks?**

A: Card networks classify disputes into reason codes. Common categories include:

| Reason Category | Examples |
|---|---|
| **Fraudulent** | Customer claims they didn't authorize the transaction |
| **Product not received** | Customer claims the item was never delivered |
| **Product not as described** | Item differed significantly from the description |
| **Duplicate charge** | Customer was charged more than once for the same order |
| **Credit not processed** | Customer returned the item but didn't receive a refund |
| **Subscription canceled** | Customer claims they canceled before being charged |
| **Unrecognized** | Customer doesn't recognize the merchant name on their statement |

The most common chargeback reason is **fraud** (unauthorized use), which typically means the card was stolen or the customer is committing "friendly fraud" (falsely claiming they didn't make the purchase).

---

**Q: How do I respond to a dispute in Stripe?**

A: When a dispute is opened, Stripe notifies you via email and webhook (`charge.dispute.created`). You should:

1. Go to **Payments > Disputes** in the Dashboard.
2. Click the dispute to open it.
3. Review the **dispute reason** and the customer's claim.
4. Decide whether to **accept** the dispute (concede and refund) or **submit evidence** to fight it.

**Submitting evidence:**
Stripe provides a structured evidence form. The evidence types that matter most depend on the dispute reason:

| Dispute Reason | Most Important Evidence |
|---|---|
| Fraudulent | AVS/CVV match, 3DS authentication proof, device fingerprint, IP address, signed contract |
| Product not received | Shipping carrier tracking, proof of delivery, customer communication |
| Product not as described | Product description, photos, customer communications, refund policy |
| Duplicate charge | Receipt showing only one charge was made |
| Subscription canceled | Cancellation policy shown at signup, lack of cancellation request from customer |

Submit all relevant evidence before the deadline — you only get **one chance** to submit.

---

**Q: What happens after I submit evidence?**

A: After you submit evidence, the card network (Visa, Mastercard, etc.) reviews both sides and makes a final decision. This process typically takes **60–90 days**.

**Possible outcomes:**
- **You win:** The disputed funds are returned to your Stripe balance. The $15 dispute fee may or may not be refunded (depends on card network and region).
- **You lose:** The funds remain with the customer. The $15 dispute fee is not refunded.

Stripe notifies you of the outcome via email and a `charge.dispute.closed` webhook event.

**Win rates:** Industry-wide, merchants win approximately **40–45%** of fraud disputes when they submit evidence. Evidence quality and completeness significantly affects outcomes.

---

**Q: Should I accept a dispute or fight it?**

A: It depends on the situation:

**Accept the dispute if:**
- The dispute is legitimate (genuine error on your part)
- You don't have strong evidence to counter it
- The disputed amount is small and the cost of fighting isn't worth it
- You've already issued a refund (disputing is pointless in this case)

**Fight the dispute if:**
- You have clear evidence the transaction was legitimate
- You have proof of delivery, authentication, or customer acknowledgment
- The claim is clearly fraudulent (friendly fraud)

To accept a dispute: Click **Accept dispute** in the Dashboard. The funds stay with the customer and the dispute is closed.

---

**Q: How do I prevent chargebacks?**

A: The best strategy is prevention. Key measures:

**At checkout:**
- Use a recognizable **statement descriptor** — customers who don't recognize a charge are more likely to dispute it. Set this in **Settings > Public business information**.
- Enable **3D Secure** authentication for high-risk transactions — this shifts fraud liability to the issuing bank.
- Use **Stripe Radar** to block suspicious transactions before they complete.

**After purchase:**
- Send confirmation emails immediately after purchase.
- Keep customers informed of shipping status and delays.
- Make your **refund and cancellation policy** clear at checkout and in confirmation emails.
- Respond quickly to customer complaints — a resolved complaint is much better than a chargeback.

**For subscriptions:**
- Send a **reminder email** 3–7 days before a subscription renewal.
- Make cancellation easy and clearly communicated.
- Set a recognizable `statement_descriptor_suffix` so customers remember what they subscribed to.

---

**Q: What is the difference between a dispute and a refund?**

A: These are two different ways a payment can be reversed:

| | Refund | Dispute / Chargeback |
|---|---|---|
| **Initiated by** | You (the merchant) | Customer's bank |
| **Stripe fee** | Processing fee not returned | $15 dispute fee charged |
| **Speed** | 5–10 business days | 60–90 days for resolution |
| **Funds** | Deducted from your balance when issued | Immediately deducted when dispute is filed |
| **Impact on account** | Low | High — too many chargebacks can get your account flagged |

If a customer contacts you about an issue, issuing a refund proactively is almost always preferable to waiting for a chargeback. You avoid the $15 fee and the negative account signal.

---

**Q: What is Stripe's dispute fee?**

A: Stripe charges a **$15 fee per dispute** (€15 in Europe, equivalent in other currencies). This fee is:

- Charged immediately when the dispute is opened
- **Non-refundable** if you lose the dispute
- **Refunded** if you win certain Visa disputes (in the US) — Stripe passes through Visa's merchant dispute resolution fee credit

This fee is in addition to the loss of the disputed transaction amount.

---

**Q: What happens if I have too many chargebacks?**

A: Card networks (Visa, Mastercard) monitor merchants' **dispute rates**. If your dispute rate exceeds their thresholds, you may be enrolled in a monitoring program:

**Visa Dispute Monitoring Program (VDMP):**
- Threshold: More than 100 disputes in a month AND a dispute rate over 0.9%
- Consequences: Monthly fines, remediation requirements, potential account termination

**Mastercard Excessive Chargeback Program (ECP):**
- Threshold: More than 100 chargebacks in a month AND a dispute rate over 1.5%

Stripe may also review or restrict your account if dispute rates are high, as excessive chargebacks violate Stripe's **Terms of Service**.

**Monitoring your dispute rate:** Check your dispute rate in the Dashboard under **Payments > Disputes**. Aim to keep it below **0.5%** as a safety buffer.

---

**Q: Can I block customers who have filed chargebacks?**

A: Yes. You can use **Stripe Radar** to block future payments from customers associated with past disputes.

One approach is to create a Radar block rule using the card fingerprint:
```
block if :card_fingerprint: = 'abc123fingerprint'
```

You can also maintain a blocklist of customer email addresses, IP addresses, or card fingerprints via **Radar > Lists** in the Dashboard.

Note: Be cautious about blocking based on disputed transactions alone — some disputes are legitimate errors. Consider blocking only in cases of confirmed friendly fraud.

---

## Related FAQ Sections

- [Stripe FAQ — Payments](./stripe-faq-payments.md)
- [Stripe FAQ — Billing & Subscriptions](./stripe-faq-billing.md)
- [Stripe FAQ — Account & Verification](./stripe-faq-accounts.md)

---

*Couldn't find your answer? [Contact Stripe Support](https://support.stripe.com)*
