# Stripe FAQ — Billing & Subscriptions

**Source:** Stripe Support  
**Category:** Billing & Subscriptions  
**FAQ ID:** STRIPE-BILL  
**Last Updated:** 2024-11-20  

---

## Subscriptions & Recurring Billing

---

**Q: How do I set up recurring billing with Stripe?**

A: Stripe's **Subscriptions API** handles recurring billing. The typical setup is:

1. Create a **Product** (what you're selling, e.g., "Pro Plan")
2. Create a **Price** on that product (e.g., $29/month, billed monthly)
3. Create a **Customer** with an attached payment method
4. Create a **Subscription** linking the Customer to the Price

Stripe automatically creates invoices and charges the customer on each billing cycle. If a payment fails, Stripe retries according to your configured **Smart Retries** schedule.

**Using Stripe Billing without code:** You can also set up subscriptions using **Stripe Checkout** (hosted payment page) or the no-code **Payment Links** feature — no backend integration required.

---

**Q: What happens when a subscription payment fails?**

A: Stripe handles failed subscription payments through an automated retry system called **Smart Retries**.

**Default retry schedule:**
- 1st retry: 3 days after initial failure
- 2nd retry: 5 days after 1st retry
- 3rd retry: 7 days after 2nd retry

After all retries are exhausted, Stripe sends a **final failure notification** and the subscription moves to the status you configured under **Settings > Billing > Manage failed payments**:

| Setting | Behavior |
|---|---|
| **Cancel the subscription** | Subscription is canceled; customer must resubscribe |
| **Mark subscription as unpaid** | Subscription pauses; you decide when to cancel |
| **Leave subscription as past due** | Subscription stays active; you handle the dunning |

You can also configure **dunning emails** — automated emails sent to customers asking them to update their payment method. These are enabled in **Settings > Billing > Email customers about failed payments**.

---

**Q: What is a Subscription status and what does each one mean?**

A: Stripe subscriptions have the following statuses:

| Status | Meaning |
|---|---|
| `active` | Subscription is current and the customer is being charged successfully |
| `trialing` | Subscription is in a free trial period; not yet charged |
| `past_due` | The most recent invoice payment failed; retries are pending |
| `unpaid` | All retries failed; the subscription is paused pending payment |
| `canceled` | Subscription has been ended (by you, the customer, or due to non-payment) |
| `incomplete` | Initial payment requires action (e.g., 3D Secure authentication) |
| `incomplete_expired` | Initial payment was not completed within 23 hours |
| `paused` | Subscription has been manually paused (no invoices generated) |

---

**Q: How do free trials work in Stripe?**

A: You can add a trial period to any subscription. During the trial:
- No charge is made to the customer
- The subscription status is `trialing`
- You can optionally collect and verify a payment method upfront (recommended)

**Setting a trial:**
```json
{
  "customer": "cus_xxx",
  "items": [{ "price": "price_xxx" }],
  "trial_period_days": 14
}
```

**Trial end behavior:** When the trial ends, Stripe generates the first invoice and attempts to charge the saved payment method. If no payment method was collected during the trial, the invoice will fail.

**Best practice:** Use a **SetupIntent** during the trial signup flow to collect and verify the payment method without charging, so the first invoice after trial succeeds automatically.

You can also set a specific `trial_end` timestamp instead of a number of days for more precise trial expiry control.

---

**Q: Can I offer coupons and discounts?**

A: Yes. Stripe supports **Coupons** and **Promotion Codes**.

**Coupon types:**
- **Percentage off** (e.g., 20% off)
- **Fixed amount off** (e.g., $10 off)

**Duration options:**
- **Once** – Applied to the first invoice only
- **Repeating** – Applied for a set number of billing cycles
- **Forever** – Applied to every invoice for the lifetime of the subscription

**Promotion Codes** are customer-facing codes (like `SAVE20`) that map to an underlying Coupon. You can limit promotion codes by:
- Maximum number of redemptions
- Expiry date
- Minimum order amount
- First-time customers only

To apply a discount, attach a coupon directly to a Customer or Subscription via the API or Dashboard.

---

**Q: How do I handle mid-cycle subscription changes (upgrades and downgrades)?**

A: When a customer changes their subscription plan mid-cycle, Stripe **prorates** the charges by default.

**Example:**
- Customer is on a $30/month plan
- On day 15 (halfway through the billing cycle), they upgrade to a $60/month plan
- Stripe calculates:
  - Credit for unused time on the old plan: ~$15
  - Charge for remaining time on the new plan: ~$30
  - Net charge on next invoice: ~$15

**Proration behavior options** (set via `proration_behavior`):

| Value | Behavior |
|---|---|
| `create_prorations` (default) | Generates proration line items on the next invoice |
| `always_invoice` | Immediately invoices the customer for the proration difference |
| `none` | No proration; customer is billed full price at next renewal |

You can preview exactly what the next invoice will look like before applying changes using the **Upcoming Invoice** endpoint.

---

**Q: What is the difference between an Invoice and a PaymentIntent in the context of subscriptions?**

A: These two objects work together in Stripe's billing system:

- **Invoice**: Represents a bill — a list of line items, applied discounts, taxes, and the total amount due. Invoices are created automatically for each subscription billing cycle.
- **PaymentIntent**: The attempt to collect payment for an invoice. Each Invoice has a PaymentIntent attached to it that tracks whether the payment succeeded, failed, or requires customer action.

**Invoice statuses:**

| Status | Meaning |
|---|---|
| `draft` | Invoice is being built; not yet finalized |
| `open` | Invoice is finalized and payment is being collected |
| `paid` | Payment was collected successfully |
| `void` | Invoice was canceled before payment |
| `uncollectible` | All collection attempts failed; marked as a bad debt |

---

**Q: How does Stripe handle taxes on subscriptions?**

A: Stripe offers two approaches to tax handling:

**Option 1: Stripe Tax (automatic)**
Stripe Tax automatically calculates and collects the correct sales tax, VAT, or GST for each transaction based on:
- Your business location (tax nexus)
- The customer's location
- The type of product/service

Enable it in **Settings > Tax** and add a `automatic_tax: { enabled: true }` flag to your subscriptions or invoices.

**Option 2: Manual tax rates**
Create **Tax Rate** objects with specific percentages and apply them to subscriptions or invoice line items manually. You control when and to whom taxes apply.

**Tax ID collection:** For B2B sales, you can collect customers' VAT/GST registration numbers and optionally apply reverse-charge mechanisms (where the business customer accounts for VAT themselves).

---

**Q: Can customers manage their own subscriptions?**

A: Yes, using the **Stripe Customer Portal**. The hosted portal lets customers:
- View current subscription and next billing date
- Upgrade or downgrade their plan
- Update their payment method
- Download past invoices
- Cancel their subscription

**Setup:**
1. Enable the portal in **Settings > Billing > Customer portal**.
2. Configure which actions customers can perform.
3. Generate a portal session link via the API and redirect the customer to it — no additional UI work required.

The portal is fully hosted and maintained by Stripe, so you don't need to build subscription management UI yourself.

---

**Q: What is metered billing and how does it work?**

A: **Metered billing** (also called usage-based billing) lets you charge customers based on how much of your service they consume each billing period, rather than a flat rate.

**How to set it up:**
1. Create a Price with `billing_scheme: per_unit` and `usage_type: metered`.
2. During the billing cycle, report usage by creating **UsageRecords**:
   ```json
   POST /v1/subscription_items/{id}/usage_records
   {
     "quantity": 1500,
     "timestamp": 1700000000,
     "action": "increment"  // or "set" to set an absolute value
   }
   ```
3. At the end of the billing period, Stripe totals the reported usage and charges accordingly.

**Tiered pricing:** You can also configure tiered pricing where the unit cost decreases as usage increases (volume tiers) or use graduated pricing where different tiers have different rates.

---

**Q: How do I cancel a subscription?**

A: Subscriptions can be canceled immediately or at the end of the current billing period.

**Cancel immediately:**
```
DELETE /v1/subscriptions/{id}
```

**Cancel at period end (customer retains access until renewal date):**
```json
POST /v1/subscriptions/{id}
{
  "cancel_at_period_end": true
}
```

When `cancel_at_period_end` is true:
- The subscription status remains `active`
- A `cancel_at` timestamp is set showing when cancellation will occur
- Stripe sends a cancellation confirmation email (if configured)
- You can reverse the cancellation by updating `cancel_at_period_end` to `false`

---

## Related FAQ Sections

- [Stripe FAQ — Payments](./stripe-faq-payments.md)
- [Stripe FAQ — Disputes & Chargebacks](./stripe-faq-disputes.md)
- [Stripe FAQ — Account & Verification](./stripe-faq-accounts.md)

---

*Couldn't find your answer? [Contact Stripe Support](https://support.stripe.com)*
