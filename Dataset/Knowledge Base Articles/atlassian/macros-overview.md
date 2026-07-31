# Using Macros in Confluence

**Product:** Confluence Cloud  
**Category:** Page Editing  
**Article ID:** CONF-089  
**Last Updated:** 2024-09-18  

---

## Overview

Macros are dynamic content blocks you can embed in Confluence pages. They go beyond static text to display live data, auto-generate navigation, format content visually, and pull in information from Jira and other tools. This article covers how to insert and configure the most commonly used macros.

---

## What is a Macro?

A **macro** is a special block that Confluence renders dynamically when a page is viewed. Instead of manually maintaining content, macros fetch or generate it automatically.

Examples of what macros can do:
- Automatically generate a table of contents from your headings
- Display a list of all pages in a space
- Embed a Jira issue list filtered by project and status
- Show a warning or info banner
- Display a roadmap or task list
- Embed code with syntax highlighting

---

## Inserting a Macro

There are two ways to insert a macro in the Confluence editor:

### Method 1: Type `/` (Slash Command)

1. Click inside the editor where you want the macro.
2. Type `/` followed by the macro name (e.g., `/table of contents`).
3. Select the macro from the dropdown list.

### Method 2: Insert Menu

1. In the editor toolbar, click **+** (Insert content).
2. Browse or search for a macro.
3. Click the macro to insert it.

After inserting, most macros open a **configuration panel** where you can set parameters.

---

## Commonly Used Macros

### 1. Table of Contents

**What it does:** Automatically generates a linked table of contents from the headings (H1, H2, H3) on your page. Updates automatically when headings change.

**Insert:** `/table of contents`

**Key settings:**
- **Minimum heading level** – Lowest heading level to include (default: H1)
- **Maximum heading level** – Highest heading level to include (default: H6)
- **Type** – Flat list or indented hierarchy
- **Style** – Choose bullet style (disc, circle, square, decimal, etc.)

**Best use:** Long documentation pages, technical specifications, runbooks.

---

### 2. Info / Note / Warning / Tip Panels

**What it does:** Displays colored callout boxes to highlight important information.

| Macro | Color | Use For |
|---|---|---|
| **Info** | Blue | General information |
| **Note** | Yellow | Cautions or things to be aware of |
| **Warning** | Red | Critical warnings or dangerous actions |
| **Tip** | Green | Helpful suggestions or best practices |
| **Success** | Green | Positive outcomes or completed states |

**Insert:** `/info`, `/note`, `/warning`, `/tip`

**Example output:**
```
⚠️  Warning: Deleting this configuration cannot be undone.
```

---

### 3. Code Block

**What it does:** Displays code with syntax highlighting and a copy button.

**Insert:** `/code`

**Key settings:**
- **Language** – Select programming language for syntax highlighting (Python, JavaScript, SQL, Bash, Java, YAML, JSON, etc.)
- **Title** – Optional label shown above the code block
- **Line numbers** – Toggle on/off

**Example use:** Documenting API examples, configuration snippets, command-line instructions.

---

### 4. Jira Issues

**What it does:** Embeds a live list of Jira issues on a Confluence page, pulled from a JQL query.

**Insert:** `/jira issues`

**Key settings:**
- **Server** – Select your connected Jira site
- **Display options** – Show as a table or single issue
- **JQL query** – Filter issues (e.g., `project = ENG AND status = "In Progress"`)
- **Columns** – Choose which fields to display (Summary, Assignee, Status, Priority, etc.)
- **Maximum results** – Limit the number of issues shown

**Example JQL:**
```
project = "BACKEND" AND sprint in openSprints() AND assignee = currentUser()
```

**Best use:** Sprint pages, project overviews, release notes.

---

### 5. Page Tree

**What it does:** Displays a hierarchical list of pages in a space, rooted at a specified parent page.

**Insert:** `/page tree`

**Key settings:**
- **Root page** – The page whose children/descendants are displayed
- **Depth** – How many levels deep to show
- **Include excerpts** – Show page excerpts below each title

**Best use:** Documentation hubs, knowledge base home pages.

---

### 6. Children Display

**What it does:** Lists only the direct child pages of the current page (simpler than Page Tree).

**Insert:** `/children display`

**Key settings:**
- **Depth** – How many levels of children to show (default: 1)
- **Excerpt** – Show or hide page excerpts
- **Style** – List or flat format

---

### 7. Expand

**What it does:** Creates a collapsible section. Content inside is hidden until the user clicks to expand it.

**Insert:** `/expand`

**Best use:**
- FAQs (question visible, answer hidden until clicked)
- Long optional details that would clutter the page
- Step-by-step instructions with expandable steps

---

### 8. Status

**What it does:** Adds a colored inline badge to label something with a status.

**Insert:** `/status`

**Configuration:**
- Choose a **color** (grey, green, yellow, red, blue, purple)
- Enter a **label** (e.g., `In Progress`, `Blocked`, `Approved`, `Draft`)

**Best use:** Decision logs, meeting notes, project pages.

---

### 9. Page Properties

**What it does:** Creates a structured metadata table at the top of a page. Can be aggregated by the **Page Properties Report** macro.

**Insert:** `/page properties`

**How it works:**
- Adds a two-column table (key | value)
- Fill in fields like `Owner`, `Status`, `Last Reviewed`, `Version`

**Used together with Page Properties Report** to build a live registry of pages with their metadata.

---

### 10. Page Properties Report

**What it does:** Aggregates Page Properties data from multiple pages into one table — like a live spreadsheet.

**Insert:** `/page properties report`

**Key settings:**
- **CQL query** – Specifies which pages to include (e.g., pages with a certain label)
- **Columns** – Which properties to display in the report

**Best use:** Project registries, content inventories, team meeting archives.

---

### 11. Roadmap

**What it does:** Displays a visual horizontal timeline with tasks or milestones. Built-in light Gantt chart.

**Insert:** `/roadmap`

**Features:**
- Add rows (tasks/milestones)
- Set start and end dates
- Color-code by type or status

**Best use:** Project pages, release planning, quarterly planning.

---

### 12. Recently Updated

**What it does:** Shows a list of recently modified pages in a space or across the site.

**Insert:** `/recently updated`

**Key settings:**
- **Space** – Filter by one or more spaces
- **Labels** – Filter by page labels
- **Maximum results** – Number of pages to show
- **Show user** – Display who last edited

**Best use:** Team dashboards, change logs.

---

## Editing and Removing Macros

### Edit a Macro

1. Click on the macro in the editor.
2. A toolbar appears — click the **Edit** (pencil) icon.
3. The configuration panel opens.
4. Make changes and click **Save** or press `Escape`.

### Remove a Macro

1. Click the macro in the editor.
2. Press `Backspace` or `Delete`.

Or:
1. Click the macro.
2. Click the **•••** icon in the macro toolbar.
3. Select **Delete**.

---

## Macro Permissions

Macros that pull data from Jira or other Atlassian tools require that:
- Your Confluence and Jira sites are linked (configured by a site admin)
- You have permission to view the data being displayed (e.g., Jira project access)

If a macro shows a permission error, contact your site admin.

---

## Tips for Using Macros Effectively

- **Don't overuse macros** – Pages with too many dynamic macros can load slowly.
- **Combine macros** – Use Page Properties + Page Properties Report for powerful wiki-style registries.
- **Use status macros in meeting notes** – Add colored status badges to action items and decisions.
- **Use the Table of Contents macro** on pages with 5+ headings for easier navigation.
- **Prefer native formatting** for simple callouts — only use macros when static text isn't enough.

---

## Related Articles

- [Getting started with Confluence](./getting-started-with-confluence.md)
- [Editing pages in Confluence](./editing-pages.md)
- [Linking Confluence pages to Jira issues](../jira/link-confluence-to-jira.md)
- [Confluence templates overview](./using-templates.md)

---

*Was this article helpful?* 👍 👎  
*Still need help? [Contact Atlassian Support](https://support.atlassian.com)*
