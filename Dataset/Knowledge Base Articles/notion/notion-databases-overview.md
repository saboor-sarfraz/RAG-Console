# Working with Databases in Notion

**Category:** Databases  
**Article ID:** NOTION-042  
**Last Updated:** 2024-11-28  

---

## Overview

Databases are one of Notion's most powerful features. A Notion database is a collection of pages that share a structured set of properties. Each row (entry) in a database is itself a full Notion page, allowing you to combine the structure of a spreadsheet with the richness of documents.

---

## What is a Notion Database?

Think of a Notion database as a flexible table where:
- Each **row** is a page with its own content
- Each **column** is a **property** (field) that describes or categorizes that entry
- The whole table can be visualized in multiple ways (Table, Board, Calendar, List, Gallery, Timeline)

Common uses for databases:
- Task and project trackers
- CRM and contact lists
- Content calendars
- Meeting logs
- Bug trackers
- Reading lists
- Inventory management

---

## Creating a Database

### Inline vs. Full-Page Database

Databases can be created in two modes:

| Mode | Description |
|---|---|
| **Inline** | Embedded within a page alongside other content |
| **Full-page** | Occupies an entire page; opened directly from the sidebar |

To create a database:
1. On any page, type `/` to open the command menu.
2. Search for and select a database type:
   - `/table` – Table view
   - `/board` – Board (Kanban) view
   - `/calendar` – Calendar view
   - `/list` – List view
   - `/gallery` – Gallery view
   - `/timeline` – Timeline / Gantt view
3. Choose **Inline** or **Full page** when prompted.

---

## Database Views

A single database can be displayed in multiple **views**. Views are different visualizations of the same underlying data — they don't duplicate or split the data.

### Table View

A spreadsheet-style grid. Best for:
- Viewing all entries and properties at a glance
- Sorting and filtering data
- Bulk editing

### Board View (Kanban)

Cards organized into columns based on a **Select** or **Status** property. Best for:
- Project workflows (To Do / In Progress / Done)
- Content pipelines
- Issue tracking

### Calendar View

Entries placed on a calendar based on a **Date** property. Best for:
- Content calendars
- Event tracking
- Scheduling

### List View

A simple vertical list of entries with selected properties shown inline. Best for:
- Meeting logs
- Minimal task lists
- Quick reference

### Gallery View

Entries displayed as image cards. Best for:
- Visual asset libraries
- Portfolio pages
- Mood boards

### Timeline View

A Gantt-chart style view with start and end dates. Best for:
- Project planning
- Milestone tracking
- Resource scheduling

### Adding a New View

1. Open a database.
2. Click **+ Add view** in the view bar at the top.
3. Name the view and select a view type.
4. Configure view-specific settings (group by, filter, etc.).

---

## Database Properties

Properties are the columns in your database. Each property has a **type** that determines what kind of data it holds.

### Property Types

| Property | Description | Example Use |
|---|---|---|
| **Title** | The main name of the entry (required, always first) | Task name |
| **Text** | Free-form plain text | Notes, description |
| **Number** | Numeric value with optional format | Price, quantity, score |
| **Select** | Single choice from a predefined list | Status, category |
| **Multi-select** | Multiple choices from a predefined list | Tags, labels |
| **Status** | A structured Select with To-do/In Progress/Done groups | Task status |
| **Date** | A date or date range with optional time | Due date, event date |
| **Checkbox** | A boolean true/false toggle | Completed, published |
| **URL** | A clickable web link | Reference link |
| **Email** | An email address | Contact email |
| **Phone** | A phone number | Contact number |
| **Formula** | A calculated value based on other properties | Days until due, total cost |
| **Relation** | A link to entries in another database | Linked project, assigned person |
| **Rollup** | Aggregated data from a related database | Sum of tasks, count of entries |
| **Created time** | Auto-filled when the entry was created | Audit log |
| **Created by** | Auto-filled with the creator's name | Audit log |
| **Last edited time** | Auto-filled with the last modification time | Audit log |
| **Last edited by** | Auto-filled with the last editor's name | Audit log |
| **Files & media** | Uploaded files or images | Attachments |
| **Person** | A Notion workspace member | Assignee, owner |
| **Button** | A clickable button that triggers an automation | Run workflow |

### Adding a Property

1. In Table view, click **+** in the header row to add a new column.
2. Name the property.
3. Click the property type icon to select a type.
4. Configure type-specific options (e.g., list options for Select, linked database for Relation).

---

## Filtering

Filters narrow down which entries are shown in a view.

### Adding a Filter

1. Click **Filter** in the view bar.
2. Click **+ Add filter**.
3. Choose a property to filter on.
4. Set the condition (e.g., `Status` **is** `In Progress`).
5. The view updates immediately.

### Filter Conditions

Conditions vary by property type:

- **Text**: contains, does not contain, is, is not, is empty, is not empty
- **Number**: =, ≠, >, <, ≥, ≤, is empty, is not empty
- **Select / Status**: is, is not, is empty, is not empty
- **Date**: is, is before, is after, is on or before, is on or after, is within (last week, this month, etc.)
- **Checkbox**: is checked, is not checked
- **Person**: contains, does not contain, is empty, is not empty

### Advanced Filters (Filter Groups)

You can combine filters with **AND** / **OR** logic:
- **AND** – All conditions must be true
- **OR** – Any condition being true is enough

Click **Add filter group** to create a nested group of conditions.

---

## Sorting

Sorting orders entries by a chosen property.

1. Click **Sort** in the view bar.
2. Click **+ Add sort**.
3. Choose a property to sort by.
4. Select **Ascending** or **Descending**.
5. Drag to reorder multiple sorts.

---

## Grouping

Grouping organizes entries by a shared property value.

1. Click **Group** in the view bar.
2. Select a property to group by (typically a Select, Status, or Person property).
3. Entries are organized into named sections.

You can collapse and expand groups, and hide empty groups.

---

## Linked Databases (Views Across Pages)

You can display the same database in multiple places using **linked views**.

1. On any page, type `/linked`.
2. Select **Create linked database**.
3. Search for and select the database you want to link.
4. A synced view of that database appears on the page.

Changes made in the linked view update the original database in real time.

---

## Relations and Rollups

### Relations

A **Relation** property links two databases together. For example, linking a Tasks database to a Projects database lets you associate each task with a project.

To add a relation:
1. Add a property of type **Relation**.
2. Choose the database to relate to.
3. Each entry will show a picker to link to entries in the other database.

When you create a relation, you can optionally show a **back-relation** — a corresponding Relation property in the other database that shows which entries link back.

### Rollups

A **Rollup** lets you pull aggregate information from a related database.

Example: If Tasks are related to Projects, a Rollup on the Projects database can show:
- Count of related tasks
- Number of completed tasks
- Sum of estimated hours

To add a rollup:
1. Add a Relation first.
2. Add a property of type **Rollup**.
3. Select the Relation to use, the property to roll up, and the aggregation function (count, sum, average, min, max, etc.).

---

## Database Templates

Database templates let you predefine the content and structure of new entries.

1. Open a database.
2. Click the dropdown arrow next to the **New** button.
3. Click **+ New template**.
4. Design the template: add default content, set default property values.
5. Click **Back** to save.

When creating a new entry, select the template from the dropdown to apply it.

---

## Frequently Asked Questions

**Q: Can I export a Notion database?**  
A: Yes. Click **•••** > **Export** on a database page. You can export as Markdown, CSV, or PDF. For large databases, use **Settings > Export** to export the entire workspace.

**Q: How do I delete a property?**  
A: Click the property header, scroll to the bottom of the property settings, and click **Delete property**. This cannot be undone and will remove that data from all entries.

**Q: What's the difference between Select and Status properties?**  
A: Both are single-choice menus, but **Status** has a built-in grouping system (To-do, In Progress, Complete) that Notion uses for progress tracking and the status board view. Use Status for task/workflow tracking; use Select for categorization.

**Q: Is there a row limit for databases?**  
A: There is no documented hard limit, but very large databases (tens of thousands of rows) may load more slowly. For very large data sets, consider using the Notion API with pagination.

**Q: Can I link to a specific entry in a database?**  
A: Yes. Open the entry (page), click **Copy link** from the **•••** menu or the Share button, and paste it anywhere.

---

## Related Articles

- [Getting started with Notion](../getting-started/getting-started-with-notion.md)
- [Using Notion formulas](./notion-formulas.md)
- [Setting up a Notion project tracker](../templates/project-tracker.md)
- [Notion API: querying databases](../api/querying-databases.md)

---

*Was this article helpful?* 👍 👎  
*Need more help? Visit [Notion Help Center](https://www.notion.so/help)*
