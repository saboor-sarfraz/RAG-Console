# Organizing Pages and Content in Notion

**Category:** Pages & Content  
**Article ID:** NOTION-018  
**Last Updated:** 2024-10-30  

---

## Overview

Notion gives you a lot of freedom in how you structure your content. This flexibility is powerful, but it can also feel overwhelming without a system. This article covers how to organize your pages, sidebar, and workspace for clarity and efficiency.

---

## The Notion Content Hierarchy

Understanding Notion's hierarchy is the first step to staying organized:

```
Workspace
  ├── Teamspace (Business/Enterprise plans)
  │     └── Pages
  │           └── Sub-pages
  ├── Private Section
  │     └── Pages (only visible to you)
  └── Shared Section
        └── Pages (shared with specific people)
```

Every page can have unlimited sub-pages nested within it. There is no technical limit on nesting depth.

---

## Sidebar Organization

The sidebar is your navigation hub. Here's how to keep it clean:

### Starring Pages (Favorites)

Pin your most-used pages to the top of the sidebar:
1. Hover over a page in the sidebar.
2. Click **•••** > **Add to Favorites**.
3. The page appears in the **Favorites** section at the top.

Only you see your own favorites — they're personal to your account.

### Hiding Pages from the Sidebar

You can move pages deeper in the hierarchy to keep the top level of your sidebar uncluttered:
- Drag a page onto another page to nest it as a sub-page.
- The parent page now acts as both a container and a document.

### Creating Sidebar Sections (Dividers)

On personal workspaces, you can't create custom named sections in the sidebar (aside from the default Private/Shared sections). However, you can simulate sections by:
- Creating a top-level page as a "folder" (e.g., **📁 Projects**)
- Nesting relevant pages inside it

### Reordering Sidebar Pages

Drag and drop pages up or down in the sidebar to reorder them. The order is personal to each user and doesn't affect how others see the workspace.

---

## Page Organization Strategies

### Strategy 1: Hierarchical Structure

Organize content with a clear parent-child structure. Good for wikis and documentation.

```
📚 Engineering Wiki
  ├── 📄 Architecture Overview
  ├── 📁 Onboarding
  │     ├── 📄 Dev Environment Setup
  │     └── 📄 Code Review Process
  └── 📁 Runbooks
        ├── 📄 Deployment Checklist
        └── 📄 Incident Response
```

**Pros:** Easy to navigate, clear ownership  
**Cons:** Content can get buried deeply

### Strategy 2: Hub and Spoke (MOC - Map of Contents)

Keep all pages flat, but create a central "hub" page with links to everything. This is called a Map of Contents (MOC) or Home page.

```
🏠 Team Home (hub page)
  - Links to: Projects, People, Processes, Tools, Templates
  
  (Linked pages are all at the same hierarchy level)
```

**Pros:** Everything is one click away from the hub  
**Cons:** Requires discipline to maintain the hub page

### Strategy 3: Database-Driven Organization

Instead of pages and sub-pages, use a master database where each entry is a page. Use filters and views to navigate.

```
📊 All Projects Database
  - View 1: "Active Projects" (filtered by Status = Active)
  - View 2: "By Team" (grouped by Team property)
  - View 3: "Timeline" (Gantt view of start/end dates)
```

**Pros:** Powerful filtering and sorting, great for tracking  
**Cons:** Less suited for rich, narrative documentation

---

## Linking Between Pages

Notion makes it easy to cross-reference pages without duplicating content.

### Inline Page Links

Type `@` followed by a page name to create a mention/link to that page:
- The link appears inline in the text
- The linked page's title is shown
- Hovering shows a preview

Example: "For setup instructions, see @Dev Environment Setup"

### Page Mentions vs. Sub-pages

- **@mention link**: Creates a clickable reference to another page, without nesting it
- **Sub-page**: Actually nests the page inside the current page in the hierarchy

Use @mentions when pages are related but shouldn't be nested (e.g., linking from a meeting note to a project page).

### Backlinks

Notion automatically tracks which pages mention or embed a given page. To see backlinks:
1. Open a page.
2. Click the **•••** menu > **View backlinks**, or look for the **N backlinks** indicator near the top of the page.

Backlinks help you discover what pages reference the current page — useful for understanding how content is connected.

---

## Moving Pages

### Method 1: Drag and Drop in Sidebar

Drag a page in the sidebar to a new location:
- Drop onto a page to nest it as a child
- Drop between pages to place it at that level

### Method 2: Move Command

1. Open the page.
2. Click **•••** > **Move to**.
3. Search for and select the destination page or workspace section.

### Method 3: Breadcrumb Navigation

At the top of a page, the breadcrumb trail shows the current page's location. Click any part of the breadcrumb to navigate up the hierarchy.

---

## Duplicating Pages

1. Right-click a page in the sidebar (or click **•••**).
2. Select **Duplicate**.
3. A copy is created as a sibling page with "Copy of [name]" prefix.
4. Sub-pages and content are duplicated as well.

---

## Deleting and Restoring Pages

### Deleting a Page

1. Right-click the page in the sidebar.
2. Select **Delete**.

Or from inside the page:
1. Click **•••**.
2. Select **Delete**.

> **Note:** Deleting a page also deletes all its sub-pages.

### Restoring from Trash

1. In the sidebar, click **Trash** (at the bottom).
2. Find the deleted page.
3. Click **Restore** to bring it back, or click **Delete permanently** to remove it forever.

Pages in Trash are kept for **30 days** before being auto-deleted.

---

## Locking Pages

Locking prevents accidental edits to important pages.

1. Open the page.
2. Click **•••** > **Lock page**.
3. The page becomes read-only for all viewers.

To edit a locked page, click **•••** > **Unlock page**.

---

## Page History and Version Control

Notion keeps a version history of every page.

### Viewing Page History

1. Open a page.
2. Click **•••** > **Page history**.
3. Browse snapshots by date and time.
4. Click any snapshot to preview it.
5. Click **Restore version** to roll back to that state.

> **Note:** Page history retention depends on your plan:
> - **Free plan**: 7 days
> - **Plus plan**: 30 days
> - **Business plan**: 90 days
> - **Enterprise plan**: Unlimited

---

## Searching for Content

### Quick Search

- Press `Ctrl+P` / `Cmd+P` or click the **Search** option in the sidebar.
- Type any keyword, page title, or content.
- Results are ranked by recency and relevance.

### Filtering Search Results

In the search panel:
- Filter by **Last edited** (date range)
- Filter by **Created by** (specific person)
- Filter by **In** (a specific page or database)

### Full-Text Search

Notion searches within page content, not just titles. This means you can find a page based on a word or phrase buried inside it.

---

## Frequently Asked Questions

**Q: Can I sort sub-pages in the sidebar alphabetically?**  
A: Not automatically. You can manually drag pages into alphabetical order, or use a database view instead for alphabetical sorting.

**Q: How do I prevent team members from deleting important pages?**  
A: You can lock a page to prevent edits, but Notion doesn't have granular delete permissions on individual pages (outside of workspace-level access). For sensitive content, restrict access to fewer people.

**Q: Can I have the same page appear in two places?**  
A: You can use **linked database views** (for database pages) or create an **@mention link** to the page from anywhere. The page itself only lives in one place.

**Q: Is there a way to see all pages in my workspace at once?**  
A: Go to **Settings > Settings > Members** to see a member list, but there's no native "all pages" view. You can use the Notion API or a third-party tool like Notionlytics for workspace audits.

---

## Related Articles

- [Getting started with Notion](./getting-started-with-notion.md)
- [Working with databases in Notion](../databases/notion-databases-overview.md)
- [Sharing pages and setting permissions](./sharing-and-permissions.md)
- [Using the Notion Web Clipper](../integrations/web-clipper.md)

---

*Was this article helpful?* 👍 👎  
*Need more help? Visit [Notion Help Center](https://www.notion.so/help)*
