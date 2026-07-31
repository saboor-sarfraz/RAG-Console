# GitHub FAQ — Security

**Source:** GitHub Docs  
**Category:** Security  
**FAQ ID:** GH-SEC  
**Last Updated:** 2024-11-18  

---

## Repository & Account Security

---

**Q: How do I enable two-factor authentication (2FA) on GitHub?**

A: Two-factor authentication adds a second layer of security to your account beyond your password.

**Setting up 2FA:**
1. Go to **Settings > Password and authentication**.
2. Under **Two-factor authentication**, click **Enable two-factor authentication**.
3. Choose your preferred method:
   - **Authenticator app** (recommended): Use apps like Google Authenticator, Authy, 1Password, or Bitwarden
   - **SMS text message**: Less secure; use only if an authenticator app isn't available
   - **Security key (hardware)**: Most secure; requires a physical key (YubiKey, etc.)
   - **GitHub Mobile app**: Use the GitHub app on your phone to approve logins

4. Save your **recovery codes** somewhere secure. These are one-time codes to access your account if you lose your 2FA device.

**Note:** As of 2023, GitHub requires 2FA for all accounts that contribute to code on GitHub.com. If you don't enable it, your account may have restricted functionality.

---

**Q: What is Dependabot and how does it help with security?**

A: **Dependabot** is GitHub's automated dependency management tool. It monitors your project's dependencies for known security vulnerabilities and outdated versions.

**Dependabot features:**

**Security alerts:** When a dependency in your project has a known vulnerability (CVE), GitHub notifies you via:
- A notification on the repository's **Security** tab
- Email notifications (configurable)

**Dependabot security updates:** Automatically opens a pull request to update the vulnerable dependency to a fixed version.

**Dependabot version updates:** Automatically opens PRs to keep your dependencies up to date (not just security-related updates). Configure in `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
```

**Enabling Dependabot:**
1. Go to **Settings > Security > Code security and analysis**.
2. Enable **Dependency graph**, **Dependabot alerts**, and **Dependabot security updates**.

---

**Q: What is GitHub's Secret Scanning feature?**

A: **Secret Scanning** automatically detects when secrets (API keys, tokens, passwords, certificates) are committed to a GitHub repository.

**How it works:**
- GitHub scans all commits pushed to a repository for patterns matching known secret formats
- Patterns include: AWS access keys, Stripe API keys, Google credentials, GitHub tokens, Slack webhooks, and 200+ other formats
- When detected, GitHub alerts the repository owner and may notify the service provider (some partners auto-revoke exposed secrets)

**Push protection:** Blocks pushes that contain secrets *before* they reach the repository — preventing exposure entirely. Available for GitHub Advanced Security users and all public repositories.

**Enabling Secret Scanning:**
- **Public repos:** Enabled by default
- **Private/internal repos:** Go to **Settings > Code security and analysis > Secret scanning** (requires GitHub Advanced Security for private repos)

**What to do if a secret is detected:**
1. **Immediately rotate** the exposed secret (revoke and generate a new one)
2. Check your git history — the secret exists in every commit since it was introduced
3. Consider using `git filter-branch` or `git-filter-repo` to remove secrets from history (if the repo is private and history is manageable)
4. Never assume a briefly exposed secret is safe — automated scrapers monitor GitHub in real time

---

**Q: How do I remove a secret I accidentally committed to GitHub?**

A: This is a serious situation. Even a few seconds of exposure can mean a secret has been scraped. Always assume exposure occurred.

**Step 1: Rotate the secret immediately**
Before doing anything else, invalidate the exposed key with the service provider (AWS, Stripe, etc.) and generate a new one.

**Step 2: Remove from git history**

For a file that was committed with secrets:
```bash
# Using git-filter-repo (recommended over filter-branch)
pip install git-filter-repo
git filter-repo --path secrets.env --invert-paths

# Or to replace a specific string in all commits:
git filter-repo --replace-text <(echo 'EXPOSED_KEY==>REPLACED')
```

**Step 3: Force push to GitHub**
```bash
git push origin --force --all
git push origin --force --tags
```

**Step 4: Contact GitHub Support** (optional but recommended for public repos)
Ask them to clear cached views of the old commits.

**Step 5: Update all services using the old key**
Update your application, CI/CD secrets, and any team members' local environments.

**Going forward:**
- Use `.gitignore` to prevent committing `.env` files
- Use pre-commit hooks (e.g., `detect-secrets`, `git-secrets`) to catch secrets before commit
- Use GitHub's push protection to block accidental pushes

---

**Q: What are branch protection rules?**

A: **Branch protection rules** restrict what can be done to specific branches, ensuring code quality and preventing accidental or unauthorized changes.

**Setting up branch protection:**
1. Go to **Settings > Branches**.
2. Click **Add rule** (or **Add branch protection rule**).
3. Enter the **branch name pattern** (e.g., `main`, `release/*`).
4. Configure protections:

**Common protection settings:**

| Setting | Description |
|---|---|
| **Require a pull request before merging** | Prevent direct pushes; require PRs |
| **Require approvals** | Minimum number of approving reviews before merge |
| **Dismiss stale reviews** | Re-review required when new commits are pushed |
| **Require review from code owners** | CODEOWNERS file determines who must review specific paths |
| **Require status checks to pass** | CI/CD checks must succeed before merging |
| **Require branches to be up to date** | PR must be rebased/merged with base before merging |
| **Require signed commits** | Only GPG/SSH-signed commits can be pushed |
| **Restrict who can push** | Only specific users/teams can push to this branch |
| **Require linear history** | Disallow merge commits; enforce squash or rebase merge |

**Recommended settings for `main`:**
- Require PR with at least 1 approval
- Require status checks (tests must pass)
- Restrict who can push (only admins directly)
- Enable "Include administrators" to apply rules even to admins

---

**Q: What is a CODEOWNERS file?**

A: A **CODEOWNERS** file defines which users or teams are responsible for reviewing changes to specific files or directories. When a PR modifies files covered by CODEOWNERS, those owners are automatically requested as reviewers.

**Location:** `.github/CODEOWNERS` (or `CODEOWNERS` in root or `docs/`)

**Syntax:**
```
# Each line: pattern  @owner

# Catch-all: any file not covered below
*                         @global-team

# Specific directory
/src/payments/            @payments-team @security-team

# Specific file type
*.tf                      @devops-team

# Specific file
/docs/CONTRIBUTING.md     @docs-team

# Multiple owners
/api/                     @backend-lead @api-reviewers
```

**How it works:**
- When a PR changes files matching a CODEOWNERS pattern, the listed owners are auto-requested for review
- If branch protection requires "code owner review", the PR cannot merge until a code owner approves
- Code owners can be users (`@username`) or teams (`@org/team-name`)

---

**Q: How do I set up SSH keys for GitHub?**

A: SSH keys let you authenticate to GitHub without entering your username and password each time.

**Generating an SSH key:**
```bash
# Generate a new key (Ed25519 recommended)
ssh-keygen -t ed25519 -C "your_email@example.com"

# When prompted:
# - File location: press Enter for default (~/.ssh/id_ed25519)
# - Passphrase: add one for extra security (optional but recommended)
```

**Adding the public key to GitHub:**
1. Copy your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
2. Go to **Settings > SSH and GPG keys > New SSH key**.
3. Paste the public key content.
4. Give it a descriptive title (e.g., "Personal Laptop").
5. Click **Add SSH key**.

**Testing the connection:**
```bash
ssh -T git@github.com
# Expected: "Hi username! You've successfully authenticated..."
```

**SSH vs HTTPS:**
- **SSH:** No password prompts after setup; uses key file; great for regular contributors
- **HTTPS:** Works everywhere; prompts for credentials (mitigated with credential managers); better for occasional contributors or environments where SSH is blocked

---

**Q: What permissions do repository collaborators get?**

A: GitHub has predefined **roles** for repository collaborators:

| Role | Read | Write (push) | Triage issues/PRs | Manage settings | Admin |
|---|---|---|---|---|---|
| **Read** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Triage** | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Write** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Maintain** | ✅ | ✅ | ✅ | Partial | ❌ |
| **Admin** | ✅ | ✅ | ✅ | ✅ | ✅ |

**Adding a collaborator:**
1. Go to **Settings > Collaborators and teams**.
2. Click **Add people**.
3. Search by username or email.
4. Select a role.

**For organizations:** Permissions can be managed at the team level via **Organization > Teams**, which scales better than per-user repository settings.

---

## Related FAQ Sections

- [GitHub FAQ — Repositories](../repositories/github-faq-repositories.md)
- [GitHub FAQ — GitHub Actions & CI/CD](../actions/github-faq-actions.md)
- [GitHub FAQ — Billing & Plans](../billing/github-faq-billing.md)

---

*Couldn't find your answer? Visit [GitHub Docs](https://docs.github.com)*
