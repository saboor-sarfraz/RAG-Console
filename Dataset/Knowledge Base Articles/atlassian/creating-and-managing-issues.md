# Creating and Managing Issues in Jira

**Product:** Jira Software Cloud  
**Category:** Issues  
**Article ID:** JIRA-012  
**Last Updated:** 2024-12-01  

---

## Overview

Issues are the core unit of work in Jira. An issue can represent a task, bug, story, epic, or any other type of work item depending on how your project is configured. This article explains how to create, update, assign, and manage issues in Jira Software Cloud.

---

## What is a Jira Issue?

A Jira issue is a single piece of trackable work. Issues belong to **projects** and have a set of **fields** that describe and categorize them. Common issue fields include:

- **Summary** – A short description of the work
- **Issue type** – The category of work (e.g., Bug, Story, Task, Epic)
- **Status** – Where the issue currently is in the workflow (e.g., To Do, In Progress, Done)
- **Priority** – Urgency level (Highest, High, Medium, Low, Lowest)
- **Assignee** – The team member responsible for completing the work
- **Reporter** – The person who created the issue
- **Labels** – Free-text tags for filtering
- **Components** – Logical sub-areas of the project
- **Story points / Estimate** – Effort estimation for planning
- **Sprint** – Which sprint the issue belongs to (Scrum projects)
- **Description** – Detailed explanation, acceptance criteria, steps to reproduce, etc.
- **Attachments** – Screenshots, logs, or documents
- **Linked issues** – Relationships to other issues (blocks, is blocked by, relates to, duplicates)

---

## Issue Types

Jira supports customizable issue types. The default types in Jira Software are:

| Issue Type | Description |
|---|---|
| **Epic** | A large body of work spanning multiple sprints or releases |
| **Story** | A user-facing feature or requirement from the end-user's perspective |
| **Task** | A unit of technical or internal work, not necessarily user-facing |
| **Bug** | A defect or problem that needs to be fixed |
| **Subtask** | A smaller piece of work that belongs to a parent issue |

> **Note:** Project admins can add, rename, or remove issue types depending on the team's workflow.

---

## Creating an Issue

### Method 1: Using the Create Button

1. Click the **Create** button in the top navigation bar (keyboard shortcut: `C`).
2. Fill in the required fields:
   - **Project** – Select the project this issue belongs to
   - **Issue type** – Choose Bug, Story, Task, etc.
   - **Summary** – Enter a clear, concise title
3. Fill in optional fields as needed (assignee, priority, description, etc.).
4. Click **Create** to submit.

### Method 2: Creating from the Board

1. On your Scrum or Kanban board, scroll to the bottom of any column.
2. Click **+ Create issue** beneath the column.
3. Enter a summary and press `Enter`.
4. Click the new issue card to open and complete the full details.

### Method 3: Creating a Child Issue (Subtask)

1. Open the parent issue.
2. Scroll to the **Child issues** section.
3. Click **Create child issue**.
4. Enter a summary and configure the fields.
5. Click **Create**.

---

## Viewing and Editing an Issue

### Opening an Issue

Click any issue key (e.g., `PROJ-42`) or issue title from the board, backlog, or search results to open the issue detail view.

### Editing Fields

Most fields in Jira are **inline-editable**:
- Click on any field value to edit it directly.
- Press `Enter` or click away to save.

Fields like description and comments use a rich text editor supporting headings, lists, code blocks, images, and mentions.

### Editing the Summary

1. Open the issue.
2. Click the summary (title) at the top.
3. Make your changes.
4. Press `Enter` to save.

---

## Transitioning Issue Status

Issues move through statuses as work progresses. The available statuses depend on your project's **workflow**.

### From the Board

Drag and drop issue cards between columns on the board to update their status.

### From the Issue View

1. Open the issue.
2. Click the **Status** button (e.g., **To Do**, **In Progress**).
3. Select the next status from the dropdown transition menu.

### Common Workflow Transitions

- **To Do → In Progress**: Work has started
- **In Progress → In Review**: Work is ready for code review or QA
- **In Review → Done**: Work is approved and complete
- **Any Status → Blocked**: Issue is stuck (can be handled via a flag or custom status)

---

## Assigning Issues

To assign an issue to a team member:
1. Open the issue.
2. Click the **Assignee** field.
3. Search for and select a team member.
4. The assignee is saved automatically.

To assign an issue to yourself:
- Click **Assign to me** below the Assignee field.

---

## Adding Comments

1. Open the issue.
2. Scroll to the **Activity** section.
3. Click in the **Add a comment** box.
4. Type your comment (supports rich text, @mentions, and emoji).
5. Click **Save**.

To edit or delete a comment, hover over it and click the **Edit** or **Delete** icon.

---

## Linking Issues

Issue links help show relationships between issues.

1. Open the issue.
2. Click **Link** (in the detail panel or via **•••** > **Link issue**).
3. Choose a link type:
   - **blocks** / **is blocked by**
   - **clones** / **is cloned by**
   - **duplicates** / **is duplicated by**
   - **relates to**
4. Search for the related issue by key or summary.
5. Click **Save**.

---

## Using Labels and Components

### Labels

Labels are informal tags for grouping issues. To add a label:
1. Open the issue.
2. Click the **Labels** field.
3. Type a label name or select from existing labels.
4. Press `Enter`.

### Components

Components are defined at the project level by a project admin. To assign a component:
1. Open the issue.
2. Click the **Component/s** field.
3. Select one or more components.

---

## Watching and Notifications

Click the **Watch** icon (eye) on any issue to receive notifications when:
- A comment is added
- The status changes
- A field is updated

You are automatically added as a watcher when you create or are assigned an issue.

---

## Logging Work

In Jira Software with time tracking enabled:
1. Open the issue.
2. Click **Log work** (in the Time Tracking section).
3. Enter:
   - **Time spent** (e.g., `2h 30m`)
   - **Date started**
   - **Work description** (optional)
4. Adjust the **Remaining estimate** if needed.
5. Click **Save**.

---

## Closing and Resolving Issues

An issue is considered **done** when it reaches the final status in its workflow (typically **Done** or **Closed**).

To close an issue:
1. Open the issue.
2. Transition the status to **Done**.
3. If prompted, fill in the **Resolution** field (e.g., Fixed, Won't Fix, Duplicate, Cannot Reproduce).

> **Tip:** Even after closing an issue, you can reopen it by transitioning the status back to an earlier state.

---

## Deleting an Issue

> **Warning:** Deleting an issue is permanent and cannot be undone. Consider closing or archiving instead.

To delete an issue:
1. Open the issue.
2. Click **•••** > **Delete**.
3. Confirm deletion in the dialog.

Only project admins and users with the **Delete Issues** permission can delete issues.

---

## Keyboard Shortcuts

| Action | Shortcut |
|---|---|
| Create a new issue | `C` |
| Assign issue to me | `I` |
| Comment on issue | `M` |
| Edit summary | `E` |
| Log work | `L` |
| Label an issue | `L` (on board) |
| Open issue search | `/` |

---

## Frequently Asked Questions

**Q: Can I change the issue type after creation?**  
A: Yes. Click the **Issue type** icon/field in the issue view and select a different type. Note that some fields may not transfer between issue types.

**Q: Why can't I delete an issue?**  
A: You need the **Delete Issues** project permission. Contact your project admin to grant it.

**Q: How do I move an issue to a different project?**  
A: Open the issue, click **•••** > **Move**, select the destination project and issue type, then confirm the field mappings.

**Q: What happens to subtasks if I delete the parent issue?**  
A: Subtasks are deleted along with the parent issue. This action cannot be undone.

---

## Related Articles

- [Understanding Jira workflows](./jira-workflows.md)
- [Using the Jira backlog](./backlog-management.md)
- [Jira board configuration](./board-configuration.md)
- [Linking Confluence pages to Jira issues](../confluence/link-confluence-to-jira.md)

---

*Was this article helpful?* 👍 👎  
*Still need help? [Contact Atlassian Support](https://support.atlassian.com)*
