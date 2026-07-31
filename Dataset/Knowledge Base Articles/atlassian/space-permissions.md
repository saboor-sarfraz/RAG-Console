# Managing Space Permissions in Confluence

**Product:** Confluence Cloud  
**Category:** Permissions & Security  
**Article ID:** CONF-045  
**Last Updated:** 2024-10-22  

---

## Overview

Space permissions in Confluence control who can view, edit, export, and administer content within a specific space. This article explains the permission model, available permission levels, and how to configure them for your team.

---

## How Confluence Permissions Work

Confluence uses a **layered permissions model**:

1. **Site-level permissions** – Set by the Confluence site admin. Controls who can log in and access Confluence at all.
2. **Space-level permissions** – Set by space admins. Controls what users/groups can do within a specific space.
3. **Page-level restrictions** – Set by page editors. Controls who can view or edit individual pages (overrides space permissions in a restrictive direction).

> **Important:** Space permissions can only grant access up to what site-level permissions allow. They cannot grant access to users who have been blocked at the site level.

---

## Permission Groups

Within a space, permissions are assigned to:

- **Individual users** – A named person with a Confluence account
- **Groups** – A collection of users managed in your Atlassian organization (e.g., `developers`, `marketing-team`)
- **Anonymous users** – People without a Confluence login (only applicable if your site allows public access)

Using groups is strongly recommended over individual user assignments for easier long-term management.

---

## Available Space Permissions

The following permissions can be toggled per user or group:

### Page Permissions

| Permission | Description |
|---|---|
| **View pages** | Can read all pages in the space (unless restricted at page level) |
| **Add pages** | Can create new pages in the space |
| **Edit pages** | Can modify existing pages |
| **Delete pages** | Can permanently delete pages |

### Blog Permissions

| Permission | Description |
|---|---|
| **View blog posts** | Can read blog entries in the space |
| **Add blog posts** | Can create blog entries |
| **Delete blog posts** | Can delete blog entries |

### Comment Permissions

| Permission | Description |
|---|---|
| **Add comments** | Can add inline and page-level comments |
| **Delete comments** | Can delete own or others' comments (depending on role) |

### Attachment Permissions

| Permission | Description |
|---|---|
| **Add attachments** | Can upload files to pages |
| **Delete attachments** | Can remove uploaded files |

### Space Admin Permission

| Permission | Description |
|---|---|
| **Space admin** | Full control: manage permissions, look-and-feel, page tree, and space settings |

---

## How to View Space Permissions

1. Go to the space where you want to check permissions.
2. In the left sidebar, click **Space settings** (gear icon at the bottom).
3. Under the **Permissions** section, click **Space permissions**.
4. Review the table showing users, groups, and their assigned permissions.

> **Note:** Only space admins and Confluence site admins can view the Space Permissions page.

---

## How to Edit Space Permissions

### Add a User or Group

1. Go to **Space settings > Space permissions**.
2. Scroll to the **Users** or **Groups** section.
3. In the input field, type the name of the user or group to add.
4. Check the boxes for the permissions you want to grant.
5. Click **Save all**.

### Remove a User or Group

1. On the Space Permissions page, find the user or group row.
2. Uncheck all permission boxes for that row.
3. Click **Save all**.

The user or group will no longer appear in the permissions list once all permissions are removed.

### Grant Space Admin Access

1. Find the user or group row on the Space Permissions page.
2. Check the **Space admin** checkbox.
3. Click **Save all**.

> **Warning:** Space admins can change all settings for the space, including removing other admins. Grant this permission carefully.

---

## Page-Level Restrictions

Page restrictions allow more granular access control beyond space permissions.

To restrict a page:
1. Open the page.
2. Click the **lock icon** in the top-right corner (next to the Share button), or go to **•••** > **Restrictions**.
3. Choose a restriction type:
   - **Viewing restricted** – Only specified users/groups can view the page
   - **Editing restricted** – Only specified users/groups can edit the page
4. Add users or groups.
5. Click **Apply**.

> **Note:** Page restrictions only narrow access — they cannot expand access beyond what space permissions allow. If a user cannot view a space, restricting a page to them still won't grant access.

---

## Anonymous Access

By default, spaces require login. If your Confluence site has anonymous access enabled by a site admin, you can allow non-logged-in users to view your space:

1. Go to **Space settings > Space permissions**.
2. Scroll to the **Anonymous access** section.
3. Check **View** to allow public viewing.
4. Click **Save all**.

> **Caution:** Anonymous access is not recommended for spaces containing sensitive or internal-only content.

---

## Common Permission Scenarios

### Scenario 1: Read-only space for external stakeholders

- Add the users/group with only the **View pages** permission checked.
- Ensure no edit, add, or delete permissions are granted.

### Scenario 2: Team collaboration space

- Grant **View pages**, **Add pages**, **Edit pages**, **Add comments**, and **Add attachments** to all team members.
- Grant **Space admin** to team leads only.

### Scenario 3: Archive a space

- Remove all edit, add, and delete permissions from all users/groups.
- Keep **View pages** for those who need historical reference.
- This effectively makes the space read-only.

### Scenario 4: Private personal space

- Remove all permissions from the default groups (e.g., `confluence-users`).
- Add only yourself with full permissions.

---

## Permission Troubleshooting

### "You don't have permission to view this page"

This error means either:
- You don't have **View pages** permission in that space, or
- The page has a **View restriction** that excludes you.

**Resolution:** Ask the space admin to grant you access, or ask a page editor to remove the restriction.

### "You don't have permission to edit this page"

Possible causes:
- Your group/user doesn't have **Edit pages** permission in the space.
- The page has an **Edit restriction** applied.
- The page is archived or in a space that has been set to read-only.

### A group I added doesn't appear in permissions

- Verify the group exists in your Atlassian organization (site admin can check under **Admin > User management > Groups**).
- Groups must have at least one member to appear correctly.

---

## Best Practices

- **Use groups, not individuals** – Easier to manage when people join or leave.
- **Principle of least privilege** – Only grant the minimum permissions needed.
- **Avoid giving everyone space admin** – Reserve it for one or two trusted people per space.
- **Review permissions quarterly** – Audit spaces regularly to remove stale access.
- **Document your permission structure** – Use a Confluence page itself to maintain a record of who has what access and why.

---

## Related Articles

- [Getting started with Confluence](./getting-started-with-confluence.md)
- [Understanding Confluence site-level permissions](./site-permissions.md)
- [Restricting access to individual pages](./page-restrictions.md)
- [Archiving a Confluence space](./archive-space.md)

---

*Was this article helpful?* 👍 👎  
*Still need help? [Contact Atlassian Support](https://support.atlassian.com)*
