# Using Formulas in Notion Databases

**Category:** Databases  
**Article ID:** NOTION-058  
**Last Updated:** 2024-11-10  

---

## Overview

Formula properties in Notion let you compute values dynamically from other properties in your database. They work similarly to spreadsheet formulas and support a range of functions for math, text manipulation, dates, and logic. This article covers how to write and use Notion formulas effectively.

---

## What is a Formula Property?

A **Formula** property calculates a value automatically based on:
- Other properties in the same database entry
- Built-in functions
- Constants and operators

Formulas are **read-only** — their values are computed, not entered manually. They update automatically when the underlying data changes.

Common use cases:
- Calculate days until a deadline
- Concatenate first name and last name into a full name
- Show whether a task is overdue
- Compute a priority score from multiple properties
- Format a date or number for display

---

## Creating a Formula Property

1. Open a database in Table view.
2. Click **+** in the column headers to add a new property.
3. Name the property (e.g., "Days Remaining").
4. Click the property type and select **Formula**.
5. Click **Edit formula** to open the formula editor.
6. Write your formula using the syntax described below.
7. Click **Done** to save.

---

## Formula Syntax Basics

### Referencing Properties

Use the **`prop()`** function to reference any other property in the current database entry:

```
prop("Property Name")
```

Example: If you have a property called "Price":
```
prop("Price") * 1.2
```

> **Note:** Property names are case-sensitive and must match exactly.

### Data Types

Formulas work with five data types:

| Type | Example |
|---|---|
| **Number** | `42`, `3.14`, `prop("Quantity")` |
| **Text (String)** | `"hello"`, `prop("Name")` |
| **Boolean** | `true`, `false`, `prop("Checkbox")` |
| **Date** | `now()`, `prop("Due Date")` |
| **List** | Output of certain functions |

---

## Operators

### Arithmetic Operators

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | `prop("A") + prop("B")` |
| `-` | Subtraction | `prop("Budget") - prop("Spent")` |
| `*` | Multiplication | `prop("Price") * prop("Quantity")` |
| `/` | Division | `prop("Revenue") / prop("Costs")` |
| `^` | Exponentiation | `prop("Base") ^ 2` |
| `%` | Modulo | `prop("N") % 7` |

### Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Logical Operators

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both must be true | `prop("A") > 0 and prop("B") > 0` |
| `or` | Either must be true | `prop("A") == "Yes" or prop("B") == "Yes"` |
| `not` | Negation | `not prop("Checkbox")` |

### String Concatenation

Use `+` to join strings:
```
prop("First Name") + " " + prop("Last Name")
```

---

## Common Formula Functions

### Math Functions

| Function | Description | Example |
|---|---|---|
| `abs(n)` | Absolute value | `abs(-5)` → `5` |
| `ceil(n)` | Round up to nearest integer | `ceil(4.2)` → `5` |
| `floor(n)` | Round down to nearest integer | `floor(4.9)` → `4` |
| `round(n)` | Round to nearest integer | `round(4.5)` → `5` |
| `max(a, b)` | Maximum of two values | `max(prop("A"), prop("B"))` |
| `min(a, b)` | Minimum of two values | `min(prop("A"), prop("B"))` |
| `sqrt(n)` | Square root | `sqrt(16)` → `4` |
| `cbrt(n)` | Cube root | `cbrt(27)` → `3` |
| `log(n, b)` | Logarithm (base b) | `log(100, 10)` → `2` |

### Text (String) Functions

| Function | Description | Example |
|---|---|---|
| `length(text)` | Character count | `length("hello")` → `5` |
| `lower(text)` | Lowercase | `lower("HELLO")` → `"hello"` |
| `upper(text)` | Uppercase | `upper("hello")` → `"HELLO"` |
| `trim(text)` | Remove leading/trailing spaces | `trim(" hi ")` → `"hi"` |
| `contains(text, sub)` | Check if substring exists | `contains(prop("Tags"), "urgent")` |
| `replace(text, pattern, replacement)` | Replace text | `replace("foo bar", "bar", "baz")` |
| `slice(text, start, end)` | Extract substring | `slice("hello", 0, 3)` → `"hel"` |
| `test(text, pattern)` | Regex test (returns boolean) | `test(prop("Email"), "@")` |
| `format(value)` | Convert any value to string | `format(prop("Number"))` |

### Date Functions

| Function | Description |
|---|---|
| `now()` | Current date and time |
| `today()` | Current date (no time) |
| `dateStart(date)` | Start of a date range |
| `dateEnd(date)` | End of a date range |
| `dateAdd(date, n, unit)` | Add time to a date |
| `dateSubtract(date, n, unit)` | Subtract time from a date |
| `dateBetween(d1, d2, unit)` | Time between two dates |
| `formatDate(date, format)` | Format a date as a string |
| `year(date)` | Extract year |
| `month(date)` | Extract month (0-indexed) |
| `date(date)` | Extract day of month |
| `hour(date)` | Extract hour |
| `minute(date)` | Extract minute |
| `timestamp(date)` | Unix timestamp in ms |
| `fromTimestamp(n)` | Date from Unix timestamp |

**Date unit options:** `"years"`, `"months"`, `"weeks"`, `"days"`, `"hours"`, `"minutes"`, `"seconds"`, `"milliseconds"`

### Logical / Conditional Functions

| Function | Description |
|---|---|
| `if(condition, trueValue, falseValue)` | If-then-else |
| `ifs(cond1, val1, cond2, val2, ..., default)` | Multi-condition if |
| `switch(value, case1, result1, case2, result2, ..., default)` | Switch statement |
| `empty(value)` | Returns true if value is empty/null |
| `not(boolean)` | Logical NOT |

---

## Practical Formula Examples

### Days Until Due Date

```
dateBetween(prop("Due Date"), now(), "days")
```

### Is Overdue?

```
if(
  prop("Due Date") < now() and not prop("Done"),
  "Overdue",
  "On Track"
)
```

### Completion Percentage

```
round(prop("Tasks Done") / prop("Total Tasks") * 100) + "%"
```

### Priority Score (weighted formula)

```
prop("Impact") * 2 + prop("Urgency") * 3 - prop("Effort")
```

### Full Name from First + Last

```
prop("First Name") + " " + prop("Last Name")
```

### Days Since Created

```
dateBetween(now(), prop("Created time"), "days")
```

### Weeks Until Event

```
floor(dateBetween(prop("Event Date"), now(), "days") / 7)
```

### Budget Remaining

```
prop("Budget") - prop("Spent")
```

### Status Label with Emoji

```
if(prop("Status") == "Done", "✅ Done",
  if(prop("Status") == "In Progress", "🔄 In Progress",
    "⬜ Not Started"))
```

---

## Tips and Gotchas

- **Empty properties return null.** If a referenced property has no value, the formula may return an error. Use `if(empty(prop("X")), 0, prop("X"))` to handle nulls safely.
- **Date properties must exist.** If `prop("Due Date")` is empty, date functions will fail. Guard with `if(empty(prop("Due Date")), "No date", ...)`.
- **Checkbox properties return booleans.** Use them directly in logic: `if(prop("Done"), "Complete", "Pending")`.
- **Multi-select and relation properties** are not directly supported in formulas (they return lists, which have limited function support). Use Rollups for aggregations on relations.
- **Formula results are display-only.** You can't sort or filter by formula outputs in all view types (though Table view does allow it).
- **Formulas can't reference other formulas.** If you need chained calculations, use intermediate number properties.

---

## Frequently Asked Questions

**Q: Can I use a formula result in another formula?**  
A: No. Notion formulas cannot reference other formula properties. Restructure your logic to compute everything in a single formula, or use a regular Number property as an intermediate value that you update manually.

**Q: Why does my date formula show an error?**  
A: The most common cause is that the date property is empty. Wrap your formula with `if(empty(prop("Date")), "", <your formula>)`.

**Q: How do I display a formula result as currency?**  
A: Formulas output text or numbers. For a Number property you can set a format (currency, percentage), but formula results displayed as text need manual formatting, e.g.:  
`"$" + format(round(prop("Total") * 100) / 100)`

**Q: Can formulas reference properties from related databases?**  
A: No, not directly. Use a **Rollup** property to pull data from a related database and then reference that Rollup in a formula.

---

## Related Articles

- [Working with databases in Notion](./notion-databases-overview.md)
- [Rollup properties in Notion](./rollup-properties.md)
- [Filtering and sorting databases](./filters-and-sorting.md)
- [Notion database templates](./database-templates.md)

---

*Was this article helpful?* 👍 👎  
*Need more help? Visit [Notion Help Center](https://www.notion.so/help)*
