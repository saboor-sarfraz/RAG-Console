# Understanding and Configuring Jira Workflows

**Product:** Jira Software Cloud  
**Category:** Project Configuration  
**Article ID:** JIRA-028  
**Last Updated:** 2024-11-15  

---

## Overview

A workflow in Jira defines the lifecycle of an issue — the **statuses** it can be in and the **transitions** that move it between those statuses. Every issue type in every project is governed by a workflow. This article explains how workflows work and how project admins can configure them.

---

## Core Concepts

### Status

A **status** represents the current state of an issue. Examples:
- `To Do` – Work hasn't started
- `In Progress` – Work is actively being done
- `In Review` – Awaiting review or QA
- `Blocked` – Work is stuck pending external input
- `Done` – Work is complete

### Transition

A **transition** is an allowed movement from one status to another. For example, `Start Progress` might be a transition that moves an issue from `To Do` to `In Progress`.

Transitions can be:
- **Unidirectional** – Can only move in one direction (e.g., from `In Progress` → `Done`)
- **Bidirectional** – Can move back and forth (e.g., between `In Review` and `In Progress`)

### Resolution

A **resolution** is a field set when an issue is closed, explaining why it moved to a final status. Common resolutions include:
- Fixed
- Won't Fix
- Duplicate
- Cannot Reproduce
- Done

---

## Default Jira Software Workflow

Out of the box, Jira Software uses a simplified workflow:

```
To Do  →  In Progress  →  Done
```

All three statuses are available on the board as columns, and transitions happen by dragging cards or clicking status buttons in the issue view.

---

## Viewing the Workflow for a Project

1. Go to your project.
2. Click **Project settings** in the left sidebar.
3. Click **Workflows**.
4. You'll see a list of workflows and which issue types they apply to.
5. Click the workflow name to see a visual diagram.

---

## Creating a Custom Workflow (Team-Managed Projects)

> **Note:** In company-managed projects, workflows are managed by Jira administrators at the site level. In team-managed projects, project admins have direct control.

### Adding a New Status

1. Go to **Project settings > Workflows**.
2. Click **Add status**.
3. Enter a **status name** (e.g., `In Review`).
4. Choose a **status category**:
   - **To Do** (grey)
   - **In Progress** (blue)
   - **Done** (green)
5. Click **Add**.

The status category determines how it appears on reports and how Jira counts work-in-progress.

### Editing the Column Order on the Board

1. Go to **Project settings > Workflows**.
2. Drag and drop statuses to reorder them.
3. Click **Save**.

---

## Company-Managed Projects: Workflow Schemes

In company-managed projects, workflows are configured at the **site admin** level and applied via **workflow schemes**.

### Workflow Scheme

A workflow scheme maps issue types to specific workflows:

| Issue Type | Workflow |
|---|---|
| Bug | Bug Tracking Workflow |
| Story | Software Development Workflow |
| Task | Default Jira Workflow |
| Epic | Epic Workflow |

### Editing a Workflow (Site Admin)

1. Go to **Jira Settings** (gear icon, top right) > **Issues** > **Workflows**.
2. Find the workflow you want to edit.
3. Click **Edit** (or copy it first if it's a shared workflow).
4. Use the workflow editor to:
   - Add or remove statuses
   - Add or remove transitions
   - Add conditions, validators, and post-functions to transitions
5. Click **Publish** to make changes live.

> **Warning:** Publishing a workflow may migrate existing issues. Always test in a non-production project first.

---

## Transition Conditions, Validators, and Post-Functions

Advanced workflow transitions can include logic that controls behavior:

### Conditions

Conditions **restrict who can trigger a transition**. Examples:
- Only the assignee can move an issue to `In Review`
- Only users in the `QA-Team` group can transition to `Done`

### Validators

Validators **check that required criteria are met** before a transition completes. Examples:
- The `Resolution` field must be set before moving to `Done`
- At least one comment must exist before moving to `In Review`

### Post-Functions

Post-functions **execute actions automatically after a transition**. Examples:
- Assign the issue to a specific user when moved to `In Review`
- Clear the `Assignee` field when moved back to `To Do`
- Fire a webhook to notify an external system

---

## Board Columns vs. Workflow Statuses

Boards in Jira display **columns** that map to one or more workflow statuses.

- A column can contain **multiple statuses** (useful when you want a simplified board view)
- Not all statuses need to be displayed as separate columns

### Mapping Statuses to Columns

1. Go to **Project settings > Kanban board** (or **Scrum board**).
2. Click **Columns**.
3. Drag statuses from the **Unmapped statuses** section into the appropriate column.
4. Add or rename columns as needed.
5. Click **Save**.

---

## Workflow Best Practices

- **Keep it simple** – Avoid creating more statuses than your team will actually use. Each extra status adds cognitive overhead.
- **Match your real process** – Workflows should reflect what actually happens, not what you wish would happen.
- **Use status categories correctly** – Jira uses categories for reports, burndown charts, and velocity metrics. Miscategorized statuses skew data.
- **Document transitions** – Add descriptions to transitions so team members understand when to use each one.
- **Test before publishing** – Use a test project to verify complex workflow logic before applying it to production projects.
- **Avoid too many conditions** – Over-restricting transitions can block legitimate work and cause frustration.

---

## Common Workflow Patterns

### Software Development (Scrum)

```
To Do → In Progress → Code Review → QA Testing → Ready for Release → Done
```

### Bug Tracking

```
Open → In Progress → Fixed → Verification → Closed
         ↓
       Won't Fix / Duplicate / Cannot Reproduce → Closed
```

### Content Publishing

```
Draft → In Review → Approved → Published → Archived
          ↓
        Rejected → Draft
```

---

## Troubleshooting

### I can't transition an issue to a certain status

Possible causes:
- A **condition** on the transition restricts who can use it
- You don't have the required permission
- A **validator** is failing (e.g., a required field is empty)

**Resolution:** Check the workflow diagram in Project Settings, or ask your Jira admin to inspect the transition's conditions and validators.

### A status is missing from the board

The status exists in the workflow but may not be mapped to a board column.

**Resolution:** Go to **Project settings > Board > Columns** and drag the unmapped status into a column.

### Issues are stuck in a status with no transitions

The workflow may not have an outgoing transition from that status.

**Resolution:** A site admin needs to add a transition in the workflow editor.

---

## Related Articles

- [Creating and managing issues in Jira](./creating-and-managing-issues.md)
- [Jira board configuration](./board-configuration.md)
- [Jira project types: team-managed vs company-managed](./project-types.md)
- [Using automation rules in Jira](./automation-rules.md)

---

*Was this article helpful?* 👍 👎  
*Still need help? [Contact Atlassian Support](https://support.atlassian.com)*
