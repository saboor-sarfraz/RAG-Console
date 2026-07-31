# Getting Started with Confluence

**Product:** Confluence Cloud  
**Category:** Getting Started  
**Article ID:** CONF-001  
**Last Updated:** 2024-11-10  

---

## Overview

Confluence is a team workspace where knowledge and collaboration meet. It is designed to help teams create, organize, and share work in a central, connected place. This article walks you through the basics of setting up and using Confluence for the first time.

---

## What is Confluence?

Confluence is a wiki-style collaboration tool built by Atlassian. Teams use it to:

- Write and maintain documentation
- Share meeting notes and project plans
- Build internal knowledge bases
- Collaborate on content in real time

Confluence integrates directly with Jira, allowing you to link issues, epics, and sprints to relevant documentation pages.

---

## Key Concepts

### Spaces

A **space** is the top-level container in Confluence. Think of it as a folder that holds all related pages for a team, project, or topic. There are two types of spaces:

- **Team spaces** – Used by departments or groups (e.g., Engineering, Marketing)
- **Personal spaces** – A private or public area for individual notes and drafts

Each space has its own homepage, permissions, and sidebar navigation.

### Pages

A **page** is the basic unit of content in Confluence. Pages live inside spaces and can be organized into parent-child hierarchies. You can use pages to write documentation, specs, meeting notes, how-to guides, and more.

Pages support rich content including:
- Text formatting (headings, bold, italic, lists)
- Tables
- Code blocks
- Images and file attachments
- Macros (dynamic content like table of contents, page trees, status labels)

### Page Tree

The **page tree** appears in the left sidebar and shows the hierarchy of pages within a space. A page can have unlimited child pages nested beneath it.

---

## Step 1: Create Your First Space

1. From the Confluence home screen, click **Create space** in the left sidebar.
2. Choose a space type:
   - **Team space** (recommended for most teams)
   - **Knowledge base space**
   - **Blank space**
3. Enter a **Space name** and a **Space key** (auto-generated but editable).
4. Set permissions — choose who can view and edit the space.
5. Click **Create space**.

> **Tip:** Space keys are short unique identifiers (e.g., `ENG` for Engineering). They appear in page URLs and cannot be changed after creation.

---

## Step 2: Create a Page

1. Navigate to your space.
2. Click the **Create** button (top navigation bar) or click **+** next to any page in the sidebar.
3. Choose a template or start with a **Blank page**.
4. Give your page a title.
5. Add content using the editor.
6. Click **Publish** to make the page visible to others.

> **Note:** Unpublished pages are saved as drafts and are only visible to you.

---

## Step 3: Organize Pages with a Hierarchy

To create a child page:

1. Hover over an existing page in the sidebar.
2. Click the **+** icon that appears next to it.
3. This creates a new page nested under the selected parent.

To move a page:
1. Open the page.
2. Click the **•••** (More options) menu at the top right.
3. Select **Move**.
4. Choose the new parent page or space.

---

## Step 4: Invite Team Members

1. Go to **Space Settings** (bottom of the left sidebar).
2. Click **Permissions**.
3. Under **Add users and groups**, search for team members by name or email.
4. Assign a permission level:
   - **Admin** – Full control over the space
   - **Editor** – Can create and edit pages
   - **Viewer** – Read-only access
5. Click **Save**.

---

## Step 5: Use Templates

Confluence comes with built-in templates to speed up common tasks:

| Template | Use Case |
|---|---|
| Meeting Notes | Record decisions, action items, and attendees |
| Project Plan | Track milestones and deliverables |
| How-To Article | Write step-by-step guides |
| Decision Log | Document choices and rationale |
| Product Requirements | Define features and specs |
| Retrospective | Capture sprint or project learnings |

To use a template:
1. Click **Create**.
2. Browse or search templates.
3. Select a template and click **Use template**.

---

## Common Actions

### @Mentioning Team Members

Type `@` followed by a person's name anywhere in a page to mention them. They will receive a notification and be linked in the content.

### Adding Comments

- **Inline comments**: Highlight text on a published page and click the comment bubble that appears.
- **Page comments**: Scroll to the bottom of a published page and click **Add a comment**.

### Watching a Page or Space

Click the **Watch** icon (bell) on any page or space to receive email notifications when content is updated.

### Searching

Use the **Search** bar (top navigation) to find pages, spaces, or people. You can filter results by space, contributor, and date.

---

## Keyboard Shortcuts

| Action | Shortcut |
|---|---|
| Create a new page | `C` |
| Edit current page | `E` |
| Open search | `/` or `Ctrl+K` |
| Insert a macro | `/` (in editor) |
| Save page | `Ctrl+S` (Win) / `Cmd+S` (Mac) |

---

## Frequently Asked Questions

**Q: Can I restrict who sees a specific page?**  
A: Yes. Open the page, click **•••** > **Restrictions**, and set view/edit permissions per user or group.

**Q: How is Confluence different from Google Docs?**  
A: Confluence is purpose-built for team documentation with features like page hierarchies, space permissions, Jira integration, and powerful macros. Google Docs is better for lightweight document collaboration.

**Q: Can I use Confluence offline?**  
A: Confluence Cloud does not have a native offline mode. However, the Confluence mobile app caches recently visited pages for offline reading.

**Q: How many spaces can I create?**  
A: There is no hard limit on the number of spaces in Confluence Cloud. However, it is best practice to consolidate content and avoid creating too many underused spaces.

---

## Related Articles

- [How to use Confluence templates](./using-templates.md)
- [Setting up space permissions](./space-permissions.md)
- [Linking Confluence pages to Jira issues](../jira/link-confluence-to-jira.md)
- [Using macros in Confluence](./macros-overview.md)

---

*Was this article helpful?* 👍 👎  
*Still need help? [Contact Atlassian Support](https://support.atlassian.com)*
