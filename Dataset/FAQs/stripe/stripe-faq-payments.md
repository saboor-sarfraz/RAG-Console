# Stripe FAQ — Payments

**Source:** Stripe Support  
**Category:** Payments  
**FAQ ID:** STRIPE-PAY  
**Last Updated:** 2024-12-01  

---

## General Payment Questions

---

**Q: What payment methods does Stripe support?**

A: Stripe supports a wide range of payment methods, including:

- **Cards:** Visa, Mastercard, American Express, Discover, JCB, UnionPay, Diners Club
- **Digital wallets:** Apple Pay, Google Pay, Link, Alipay, WeChat Pay
- **Bank debits:** ACH Direct Debit (US), SEPA Direct Debit (Europe), BACS (UK), BECS (Australia)
- **Bank redirects:** iDEAL (Netherlands), Bancontact (Belgium), Sofort (Europe), Przelewy24 (Poland)
- **Buy Now, Pay Later:** Klarna, Afterpay/Clearpay, Affirm
- **Vouchers:** Boleto (Brazil), OXXO (Mexico), Konbini (Japan)
- **Cryptocurrency:** via third-party integrations

Availability depends on your business location and the currency you charge in. You can see which payment methods are available for your account in the Stripe Dashboard under **Settings > Payment methods**.

---

**Q: How long does it take for a payment to process?**

A: Most card payments are processed almost instantly — within a few seconds. However, certain payment method types have longer processing times:

| Payment Method | Processing Time |
|---|---|
| Credit / Debit Card | Immediate (seconds) |
| ACH Direct Debit | 3–5 business days |
| SEPA Direct Debit | 3–6 business days |
| BACS Direct Debit | 3–5 business days |
| iDEAL / Bancontact | 1–2 business days |
| Klarna / Afterpay | Immediate (Stripe receives funds later) |
| Boleto | 1–3 business days after customer pays |

A "succeeded" status in the Dashboard means the payment was captured and funds will be included in your next payout.

---

**Q: Why was a customer's payment declined?**

A: Payments can be declined for many reasons. Stripe provides a decline code in the API response that explains why:

**Common decline codes and their meanings:**

| Decline Code | Meaning | Recommended Action |
|---|---|---|
| `card_declined` | Generic decline from the card issuer | Ask customer to contact their bank or use another card |
| `insufficient_funds` | Card doesn't have enough balance | Customer should use a different card or add funds |
| `expired_card` | Card has passed its expiry date | Customer needs to update their card |
| `incorrect_cvc` | CVC/CVV entered incorrectly | Ask customer to re-enter the security code |
| `do_not_honor` | Issuer has blocked the transaction | Customer must contact their bank |
| `lost_card` | Card reported lost | Do not retry; contact the customer |
| `stolen_card` | Card reported stolen | Do not retry |
| `fraud` | Stripe's fraud detection flagged the charge | Review the charge carefully; do not retry blindly |
| `card_velocity_exceeded` | Too many charges attempted in a short time | Wait before retrying |
| `processing_error` | Technical error at the network level | Retry the payment |

Stripe also assigns a `network_status` field that shows whether the decline came from the card network or Stripe's own systems (Radar).

---

**Q: What is the difference between authorization and capture?**

A: Stripe separates card payments into two steps:

- **Authorization**: Verifies that the card is valid and reserves the specified amount on the cardholder's account. No money moves yet, but the amount is "held."
- **Capture**: Actually moves the reserved funds from the customer's account to your Stripe balance.

By default, Stripe authorizes and captures in a single API call (when you set `capture_method: automatic`). Setting `capture_method: manual` lets you authorize now and capture later — useful when:
- You need to confirm stock availability before charging
- The final amount isn't known at checkout (e.g., tips, hotel incidentals)
- You want to review orders before completing the charge

**Authorization hold timeline:** Most card networks hold authorizations for **7 days**. If not captured within this window, the authorization expires and the hold is released. You can extend authorizations on some card networks with an incremental authorization request.

---

**Q: Can I charge a customer in a currency different from my settlement currency?**

A: Yes. Stripe supports charging customers in one currency and settling (receiving payouts) in another. This is called **presentment currency** (what the customer sees) vs. **settlement currency** (what you receive).

Key things to know:
- Stripe performs the currency conversion using the live exchange rate plus a **1.5% conversion fee** (2% for conversions involving EUR or GBP for non-EU/UK accounts).
- The exchange rate is locked at the time the charge is created.
- You can see both the presentment amount and the converted settlement amount in the Dashboard and API.
- If your account supports multiple settlement currencies (via multi-currency settlement), you can receive funds in the same currency the customer was charged, avoiding conversion fees.

---

**Q: What is a Payment Intent?**

A: A **PaymentIntent** is the core API object in Stripe's modern payments integration. It tracks the complete lifecycle of a payment attempt, including:

- The amount and currency
- Which payment method was used
- The current status of the payment
- Any required authentication steps (like 3D Secure)

**PaymentIntent statuses:**

| Status | Meaning |
|---|---|
| `requires_payment_method` | Waiting for the customer to provide a payment method |
| `requires_confirmation` | Ready to be confirmed and processed |
| `requires_action` | Customer must complete an action (e.g., 3D Secure) |
| `processing` | Payment is being processed |
| `succeeded` | Payment completed successfully |
| `canceled` | Payment was canceled |

PaymentIntents replace the older Charges API and are required for SCA-compliant integrations in Europe.

---

**Q: What is 3D Secure and when is it required?**

A: **3D Secure (3DS)** is an additional authentication layer for card payments where the cardholder verifies their identity with their bank (typically via a one-time code or biometric confirmation). It reduces fraud liability for merchants.

**When 3DS is triggered:**
- **Mandatory:** Required by law for card payments in the European Economic Area (EEA) under Strong Customer Authentication (SCA) regulations. Also mandated for certain cards in India and other markets.
- **Requested by the issuer:** Some banks automatically trigger 3DS even outside regulated regions.
- **Requested by Stripe Radar:** Your fraud rules can request 3DS for suspicious transactions.

**When 3DS is NOT required:**
- Low-value transactions (under €30 in the EEA)
- Merchant-initiated transactions (MIT) such as subscription renewals
- Transactions flagged as low risk by the bank

If a customer abandons the 3DS challenge, the PaymentIntent moves to `requires_action` and the payment is not completed. You should prompt the customer to complete the authentication.

---

**Q: How do I issue a full or partial refund?**

A: You can issue refunds from the Dashboard or via the API.

**From the Dashboard:**
1. Go to **Payments**.
2. Click the payment you want to refund.
3. Click **Refund**.
4. Choose **Full refund** or enter a partial amount.
5. Select a **reason** (optional): Duplicate, Fraudulent, or Customer request.
6. Click **Refund**.

**Via the API:**
```
POST /v1/refunds
{
  "charge": "ch_xxxxxxx",
  "amount": 500  // optional; omit for full refund (amount in cents)
}
```

**Refund timeline:** Refunds typically appear on the customer's statement within **5–10 business days**, though this varies by bank. Stripe initiates the refund immediately upon your request; the bank processes it on their end.

**Note:** Stripe's processing fees are **not returned** when you issue a refund. If you need to transfer refund costs to the customer, you can deduct the fee amount from the refunded sum.

---

**Q: What is Stripe Radar and how does it prevent fraud?**

A: **Stripe Radar** is Stripe's machine learning–based fraud detection system. It evaluates every payment in real time using signals including:

- Card and device fingerprinting
- IP address and geolocation
- Velocity checks (e.g., many charges in a short time)
- Behavioral patterns across Stripe's global network of millions of businesses

**Radar actions:**
- **Allow** – Process the payment normally
- **Review** – Flag for manual review (charge succeeds but appears in a "Review" queue)
- **Block** – Decline the payment before it reaches the card network

**Radar Rules:** You can write custom rules in the Dashboard (**Radar > Rules**) using a simple condition syntax:

```
# Block payments from high-risk countries
block if :ip_country: in ('KP', 'IR', 'SY')

# Request 3D Secure for large transactions
request_three_d_secure if :amount_in_usd: > 500

# Review payments where billing and shipping countries differ
review if :card_country: != :shipping_country:
```

Radar is included by default. Radar for Fraud Teams (with advanced rules and risk scores) is available on paid plans.

---

**Q: Can I save a customer's payment method for future charges?**

A: Yes. Stripe allows you to save payment methods using **Customer** and **PaymentMethod** objects.

**How it works:**
1. Create a **Customer** object to represent the person.
2. Attach a **PaymentMethod** to the Customer.
3. Use the Customer ID in future PaymentIntents for one-click payments or off-session charges.

**Setup Intent:** For saving a payment method *without* immediately charging the customer, use a **SetupIntent**. This collects and verifies the payment method, handles any required authentication (like 3DS), and creates a reusable PaymentMethod — all without charging anything upfront.

**Important:** You must disclose to customers that you're saving their payment information for future use, and obtain appropriate consent. This is both a Stripe requirement and often a legal requirement under GDPR and similar regulations.

---

**Q: What currencies does Stripe support?**

A: Stripe supports **135+ currencies** for presentment (charging customers). Settlement currency options (currencies you can receive payouts in) depend on your account country.

Common currencies include: USD, EUR, GBP, CAD, AUD, JPY, CHF, SGD, HKD, NZD, SEK, NOK, DKK, PLN, CZK, MXN, BRL, INR, and many more.

Minimum charge amounts vary by currency. For USD, the minimum charge is **$0.50**. For zero-decimal currencies (like JPY), Stripe amounts are in the base unit (e.g., ¥50 = `50`, not `5000`).

---

## Related FAQ Sections

- [Stripe FAQ — Billing & Subscriptions](./stripe-faq-billing.md)
- [Stripe FAQ — Disputes & Chargebacks](./stripe-faq-disputes.md)
- [Stripe FAQ — Account & Verification](./stripe-faq-accounts.md)

---

*Couldn't find your answer? [Contact Stripe Support](https://support.stripe.com)*
