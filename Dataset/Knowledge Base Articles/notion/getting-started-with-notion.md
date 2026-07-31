# Getting Started with Notion

**Category:** Getting Started  
**Article ID:** NOTION-001  
**Last Updated:** 2024-12-05  

---

## Welcome to Notion

Notion is an all-in-one workspace for your notes, tasks, wikis, and databases. Whether you're managing a personal project or collaborating with a team, Notion gives you the flexibility to build the exact system that works for you.

This guide walks you through the core concepts and helps you get up and running quickly.

---

## The Basics: Pages and Blocks

Everything in Notion is built from two fundamental building blocks.

### Pages

A **page** is the top-level unit of content in Notion. Think of a page like a document, but one that can contain almost anything — text, tables, images, embedded databases, and even other pages.

Pages can be:
- Standalone notes
- Project dashboards
- Wiki articles
- Database entries (a page can itself be a row in a database)

### Blocks

Every piece of content inside a page is a **block**. A block is the smallest unit of content.

Examples of blocks:
- Paragraph text
- Heading (H1, H2, H3)
- Bulleted list item
- Numbered list item
- To-do checkbox
- Toggle
- Quote
- Divider
- Image
- Video embed
- Code block
- Table
- Callout (colored box with icon)
- Database (inline or full-page)
- Embedded page

You can add a block by clicking the `+` icon that appears to the left of any line, or by typing `/` to open the **command menu** and searching for a block type.

---

## Notion's Hierarchy

Notion uses a simple nesting system:

```
Workspace
  └── Sidebar sections
        └── Pages
              └── Sub-pages
                    └── Sub-sub-pages (unlimited depth)
```

- **Workspace** – Your top-level environment, tied to your account or team.
- **Sidebar** – The left panel showing your pages and section dividers.
- **Pages** – Any page can contain sub-pages, making it both a document and a folder.

To create a sub-page: Open a page and type `/page` or click `+` and select **Page**.

---

## The Sidebar

The sidebar is your primary navigation in Notion. It shows:

- **Favorites** – Pages you've starred for quick access
- **Private** – Pages only you can see (on team plans)
- **Teamspaces** – Shared spaces for your organization (Notion Business/Enterprise)
- **Shared** – Pages shared with specific people
- **Trash** – Recently deleted pages (kept for 30 days)

### Organizing the Sidebar

- Drag pages to reorder them
- Drag a page onto another to make it a sub-page
- Right-click a page for options: rename, duplicate, move, delete, copy link

---

## Creating Your First Page

1. Click **+ New page** at the bottom of the sidebar, or press `Ctrl+N` / `Cmd+N`.
2. A blank page opens with a prompt to add a title.
3. Type your page title and press `Enter`.
4. Start adding content — type normally for a paragraph, or type `/` to choose a block type.

### Adding an Icon and Cover

- Click **Add icon** at the top of a page to add an emoji or custom image as the page icon.
- Click **Add cover** to add a background image to the page header.
- These make pages easier to identify in the sidebar.

---

## Basic Formatting

Notion supports Markdown-style shortcuts:

| Shortcut | Result |
|---|---|
| `# ` + space | Heading 1 |
| `## ` + space | Heading 2 |
| `### ` + space | Heading 3 |
| `- ` + space | Bulleted list |
| `1. ` + space | Numbered list |
| `[] ` + space | To-do checkbox |
| `> ` + space | Toggle block |
| `" ` + space | Quote block |
| ` ``` ` | Code block |
| `---` | Divider |

You can also select text and use the **formatting toolbar** that appears to apply bold, italic, underline, highlight colors, links, and more.

---

## Sharing and Collaboration

### Sharing a Page

1. Open the page you want to share.
2. Click **Share** in the top-right corner.
3. Choose one of:
   - **Invite** – Share with specific Notion members or email addresses
   - **Web** – Toggle **Share to web** to make the page publicly accessible via a link

### Sharing Options

| Option | Description |
|---|---|
| **Can edit** | Can modify content, add blocks, create sub-pages |
| **Can comment** | Can leave comments, but not edit content |
| **Can view** | Read-only access |
| **Full access** | Can edit, share, and manage permissions |

### Comments

- **Inline comments**: Highlight any text, then click the comment bubble icon that appears.
- **Page comments**: Click the comment icon in the top-right corner to open the comment thread for the whole page.
- Use `@mention` to notify a specific person in a comment.

### Real-Time Collaboration

Multiple people can edit the same page simultaneously. You'll see their cursor and name highlighted in real time.

---

## Templates

Notion has hundreds of templates for common use cases:

- Meeting notes
- Project tracker
- Weekly planner
- OKR tracker
- CRM
- Knowledge base
- Personal journal

### Using a Template

1. Click **Templates** in the left sidebar.
2. Browse by category or search by keyword.
3. Click a template to preview it.
4. Click **Use this template** to duplicate it into your workspace.

### Creating Your Own Template

1. Build a page with the structure you want to reuse.
2. Click **•••** > **Turn into template**.
3. The page becomes available in the **Templates** picker for your workspace.

---

## Keyboard Shortcuts

| Action | Shortcut |
|---|---|
| New page | `Ctrl+N` / `Cmd+N` |
| Open command menu | `/` |
| Bold | `Ctrl+B` / `Cmd+B` |
| Italic | `Ctrl+I` / `Cmd+I` |
| Underline | `Ctrl+U` / `Cmd+U` |
| Create a link | `Ctrl+K` / `Cmd+K` |
| Duplicate block | `Ctrl+D` / `Cmd+D` |
| Move block up | `Ctrl+Shift+↑` / `Cmd+Shift+↑` |
| Move block down | `Ctrl+Shift+↓` / `Cmd+Shift+↓` |
| Search | `Ctrl+P` / `Cmd+P` |
| Toggle sidebar | `Ctrl+\` / `Cmd+\` |

---

## Frequently Asked Questions

**Q: Is Notion free?**  
A: Yes. Notion has a free plan with unlimited pages and blocks for individuals. Paid plans (Plus, Business, Enterprise) add collaboration features, permission controls, and advanced admin tools.

**Q: Can I use Notion offline?**  
A: The Notion desktop app (Mac and Windows) caches recently visited pages for offline reading. However, changes made offline will sync once you reconnect to the internet.

**Q: How do I delete a page?**  
A: Right-click the page in the sidebar and select **Delete**, or open the page and click **•••** > **Delete**. Deleted pages go to the **Trash** and can be restored within 30 days.

**Q: Can I import from other tools?**  
A: Yes. Notion supports importing from Evernote, Confluence, Google Docs, Trello, Asana, and plain Markdown or CSV files. Go to **Settings > Import** to access the import tool.

---

## Related Articles

- [Working with databases in Notion](../databases/notion-databases-overview.md)
- [Organizing your Notion workspace](../getting-started/workspace-organization.md)
- [Notion for teams: sharing and permissions](../getting-started/team-sharing.md)
- [Using the Notion API](../api/notion-api-overview.md)

---

*Was this article helpful?* 👍 👎  
*Need more help? Visit [Notion Help Center](https://www.notion.so/help)*
