# GitHub FAQ — Repositories

**Source:** GitHub Docs  
**Category:** Repositories  
**FAQ ID:** GH-REPO  
**Last Updated:** 2024-12-02  

---

## Repository Basics

---

**Q: What is a GitHub repository?**

A: A **repository** (or "repo") is the fundamental unit of storage on GitHub. It contains:
- All files and folders in your project
- The complete **version history** of every change ever made (powered by Git)
- Issues, pull requests, and discussions related to the project
- GitHub Actions workflows
- Project metadata (description, topics, license)

Repositories can be **public** (visible to everyone on the internet) or **private** (visible only to you and people you explicitly grant access to).

---

**Q: How do I create a new repository?**

A: 

**On GitHub.com:**
1. Click the **+** icon in the top-right corner.
2. Select **New repository**.
3. Fill in:
   - **Owner**: Your personal account or an organization
   - **Repository name**: Unique within the owner's namespace
   - **Description** (optional)
   - **Visibility**: Public or Private
4. Optionally initialize with:
   - A **README** file
   - A **.gitignore** template (language-specific)
   - A **license**
5. Click **Create repository**.

**Via GitHub CLI:**
```bash
gh repo create my-project --public --clone
```

**From an existing local project:**
```bash
git init
git add .
git commit -m "Initial commit"
gh repo create my-project --source=. --push
```

---

**Q: What is the difference between a public and private repository?**

A:

| Feature | Public | Private |
|---|---|---|
| Visible to | Anyone on the internet | Only you and invited collaborators |
| Searchable | Yes (on GitHub and search engines) | No |
| Can be forked by | Anyone | Only collaborators (with permission) |
| GitHub Actions minutes | Standard | Standard (free plan has limits) |
| Cost | Free (unlimited) | Free (unlimited on personal; org limits vary) |
| GitHub Pages | Available | Available on paid plans only |

**Converting between public and private:**
- Public → Private: Go to **Settings > Danger Zone > Change repository visibility**
- Private → Public: Same path; note that making a repo public exposes all history and code

**Warning:** Making a private repo public exposes everything in it — including git history. If you accidentally committed sensitive data (passwords, API keys), changing to public would expose it. Rotate any exposed credentials before changing visibility.

---

**Q: How do I clone a repository to my local machine?**

A: Cloning downloads a full copy of the repository to your computer.

**Via HTTPS (recommended for most users):**
```bash
git clone https://github.com/username/repo-name.git
```

**Via SSH (recommended if you've set up SSH keys):**
```bash
git clone git@github.com:username/repo-name.git
```

**Via GitHub CLI:**
```bash
gh repo clone username/repo-name
```

**Via GitHub Desktop:** Click the green **Code** button on the repo page > **Open with GitHub Desktop**.

After cloning, you'll have a local copy with the full history. Changes you make locally don't affect the remote repository until you `git push`.

---

**Q: What is a README file and why is it important?**

A: A **README.md** file is the front page of your repository. GitHub displays it automatically on the repository's main page. It should tell visitors:

- **What** the project is and what it does
- **Why** it exists / the problem it solves
- **How to install** and run it
- **How to use** it (with examples)
- **How to contribute**
- **License** information

**README best practices:**
- Write in Markdown (`.md`) for proper formatting on GitHub
- Include a badge section (build status, coverage, version)
- Keep the getting-started section short and clear
- Add screenshots or GIFs for UI projects
- Keep it updated as the project evolves

A good README is often the deciding factor in whether someone uses your project or moves on.

---

**Q: How do branches work in GitHub?**

A: A **branch** is an independent line of development within a repository. Branches allow you to work on new features or bug fixes without affecting the main codebase.

**Default branch:** When you create a repository, a default branch is created (typically named `main`). This is usually the "production-ready" branch.

**Common branching strategies:**

**Feature branching (most common):**
```
main
├── feature/user-authentication
├── feature/payment-integration
└── bugfix/login-error
```

**Git Flow:**
```
main (production)
└── develop (integration)
    ├── feature/* branches
    ├── release/* branches
    └── hotfix/* branches
```

**Creating a branch:**
```bash
git checkout -b feature/new-feature
# or
git switch -c feature/new-feature
```

**Pushing a branch to GitHub:**
```bash
git push origin feature/new-feature
```

**Deleting a merged branch:**
```bash
git branch -d feature/new-feature          # local
git push origin --delete feature/new-feature  # remote
```

---

**Q: What is a fork and how is it different from a branch?**

A:

**Fork:**
- A **personal copy** of someone else's repository under your own GitHub account
- Creates a completely separate repository linked back to the original ("upstream")
- Used for: Contributing to open source projects you don't have write access to; experimenting with someone else's code without affecting the original

**Branch:**
- A parallel line of development **within the same repository**
- Used for: Feature development, bug fixes, experiments within a project you own or collaborate on

**Fork workflow (contributing to open source):**
1. Fork the repository → you now have `your-username/project-name`
2. Clone your fork locally
3. Create a branch for your changes
4. Make and commit changes
5. Push to your fork
6. Open a Pull Request from your fork to the original repository

---

**Q: What is a .gitignore file?**

A: A **.gitignore** file tells Git which files and directories to ignore — they won't be tracked, staged, or committed.

Common things to ignore:
- Build output (`dist/`, `build/`, `*.pyc`, `*.class`)
- Dependencies (`node_modules/`, `venv/`, `.env`)
- IDE files (`.vscode/`, `.idea/`, `*.swp`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Secrets and credentials (`.env`, `secrets.json`, `*.pem`)

**Example .gitignore for a Python project:**
```
# Virtual environment
venv/
.env

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Distribution
dist/
build/
*.egg-info/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

GitHub maintains a collection of starter `.gitignore` templates for popular languages and frameworks at [github.com/github/gitignore](https://github.com/github/gitignore). You can also select one when creating a new repository.

**Important:** Files already tracked by Git are NOT ignored even if you add them to `.gitignore`. To stop tracking a previously committed file:
```bash
git rm --cached filename
git commit -m "Remove tracked file"
```

---

**Q: How do I rename or delete a repository?**

A:

**Rename a repository:**
1. Go to the repository on GitHub.
2. Click **Settings** (near the top of the repo page).
3. Under **Repository name**, enter the new name.
4. Click **Rename**.

**After renaming:** GitHub automatically creates redirects from the old URL to the new one. However, update any local clone remotes:
```bash
git remote set-url origin https://github.com/username/new-name.git
```

**Delete a repository:**
1. Go to **Settings** > **Danger Zone**.
2. Click **Delete this repository**.
3. Type the repository name to confirm.
4. Click **I understand the consequences, delete this repository**.

**Warning:** Deletion is permanent and cannot be undone. GitHub does not have a repository restore feature for deleted repos (only GitHub Support in very limited circumstances can assist). **Archive** the repository instead if you want to preserve it without accepting new changes.

---

**Q: What are repository topics and how do they help?**

A: **Topics** are tags you add to a repository to make it more discoverable on GitHub. They appear as blue labels on the repository page.

**Adding topics:**
1. On the repository page, click the gear icon next to **About** (top right of the repo page).
2. Enter topics in the **Topics** field (e.g., `python`, `machine-learning`, `rag`, `nlp`).
3. Click **Save changes**.

**Benefits of topics:**
- Your repo appears in GitHub's topic search (e.g., `github.com/topics/rag`)
- Helps other developers find your project
- Signals the technology stack and purpose at a glance

**Good topic practices:**
- Use lowercase, hyphenated terms (`machine-learning` not `MachineLearning`)
- Include: language, framework, domain, purpose
- Limit to 10–15 relevant topics; avoid keyword stuffing

---

**Q: How do I transfer a repository to another user or organization?**

A:
1. Go to **Settings > Danger Zone > Transfer**.
2. Enter the name of the new owner (GitHub username or organization name).
3. Confirm by typing the repository name.
4. Click **I understand, transfer this repository**.

**What happens after transfer:**
- The repo moves to the new owner's namespace
- GitHub redirects the old URL to the new one
- You lose admin access (unless the new owner re-invites you)
- Stars, forks, and issues are preserved
- Webhooks, secrets, and integrations may need to be reconfigured

---

## Related FAQ Sections

- [GitHub FAQ — Pull Requests & Code Review](./github-faq-pull-requests.md)
- [GitHub FAQ — GitHub Actions & CI/CD](../actions/github-faq-actions.md)
- [GitHub FAQ — Security](../security/github-faq-security.md)
- [GitHub FAQ — Billing & Plans](../billing/github-faq-billing.md)

---

*Couldn't find your answer? Visit [GitHub Docs](https://docs.github.com)*
