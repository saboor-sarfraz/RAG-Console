# GitHub FAQ — GitHub Actions & CI/CD

**Source:** GitHub Docs  
**Category:** GitHub Actions  
**FAQ ID:** GH-ACTIONS  
**Last Updated:** 2024-11-25  

---

## GitHub Actions Basics

---

**Q: What is GitHub Actions?**

A: **GitHub Actions** is GitHub's built-in CI/CD (Continuous Integration / Continuous Delivery) platform. It allows you to automate workflows triggered by events in your repository — like pushing code, opening a pull request, creating a release, or on a schedule.

Common use cases:
- Run tests on every push or pull request
- Build and deploy applications
- Publish packages to npm, PyPI, Docker Hub
- Lint and format code
- Send Slack or email notifications
- Auto-label issues and PRs
- Generate and publish documentation

---

**Q: How is a GitHub Actions workflow structured?**

A: Workflows are defined in **YAML files** stored in `.github/workflows/` in your repository. A workflow file has this structure:

```yaml
name: CI Pipeline                    # Workflow name (shown in Actions tab)

on:                                  # Trigger events
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:                                # One or more jobs to run
  test:                              # Job ID
    runs-on: ubuntu-latest           # Runner OS
    
    steps:                           # Ordered list of steps in the job
      - name: Checkout code
        uses: actions/checkout@v4    # Use an action

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt  # Run a shell command

      - name: Run tests
        run: pytest tests/
```

**Key concepts:**
- **Workflow:** The entire YAML file — the top-level automation
- **Job:** A set of steps that run on the same runner (VM)
- **Step:** A single task — either a shell command (`run`) or a pre-built action (`uses`)
- **Action:** A reusable unit of automation (from GitHub's marketplace or your own repo)
- **Runner:** The virtual machine that executes the job (GitHub-hosted or self-hosted)

---

**Q: What triggers can start a GitHub Actions workflow?**

A: Workflows can be triggered by dozens of events. Common ones:

**Code events:**
```yaml
on:
  push:                          # On push to any branch
  push:
    branches: [main, develop]    # On push to specific branches
  pull_request:                  # On PR open, sync, reopen
    types: [opened, synchronize]
  pull_request_review:           # When a PR review is submitted
```

**Schedule:**
```yaml
on:
  schedule:
    - cron: '0 8 * * 1-5'       # Every weekday at 8 AM UTC
```

**Manual trigger:**
```yaml
on:
  workflow_dispatch:             # Run manually from Actions tab
    inputs:
      environment:
        description: 'Deploy target'
        required: true
        default: 'staging'
```

**Other repository events:**
- `issues` – When an issue is opened, closed, labeled
- `release` – When a release is published
- `workflow_run` – When another workflow completes
- `repository_dispatch` – Triggered via API call (useful for cross-repo triggers)

---

**Q: What are GitHub-hosted runners and what are their specs?**

A: GitHub provides hosted virtual machines that run your workflows. You don't need to set up or maintain any infrastructure.

**Available GitHub-hosted runners:**

| Runner Label | OS | Specs |
|---|---|---|
| `ubuntu-latest` | Ubuntu 22.04 | 2-core CPU, 7 GB RAM, 14 GB SSD |
| `ubuntu-22.04` | Ubuntu 22.04 | Same as above |
| `ubuntu-20.04` | Ubuntu 20.04 | Same as above |
| `windows-latest` | Windows Server 2022 | 2-core CPU, 7 GB RAM, 14 GB SSD |
| `macos-latest` | macOS 13 (Ventura) | 3-core CPU, 14 GB RAM, 14 GB SSD |
| `macos-14` | macOS 14 (Sonoma) | M1 chip, 3-core CPU, 7 GB RAM |

Runners come pre-installed with many common tools: Git, Python, Node.js, Java, Docker, AWS CLI, Azure CLI, and more. See the full pre-installed software list in GitHub's documentation.

**Larger runners (GitHub Team/Enterprise):** GitHub offers 4-core, 8-core, 16-core, 32-core, and 64-core machines for CPU-intensive workloads like large builds or ML training.

---

**Q: What is the difference between GitHub-hosted and self-hosted runners?**

A:

| | GitHub-hosted | Self-hosted |
|---|---|---|
| **Setup** | None required | You install the runner agent |
| **Maintenance** | Managed by GitHub | You manage OS, updates, software |
| **Cost** | Included minutes per plan; per-minute after | Your hardware costs only |
| **Security** | Ephemeral (fresh VM per job) | Persistent (state carries between jobs) |
| **Network access** | Public internet | Your private network (can access internal resources) |
| **Custom software** | Limited (pre-install via steps) | Pre-installed on the machine |
| **Best for** | Most public/small repos | Private network access, custom hardware, high volume |

**When to use self-hosted runners:**
- Your workflow needs access to on-premise databases or internal services
- You need GPU runners for ML workloads
- You have very high workflow volume and want to reduce costs
- You need a custom operating system or environment

**Security warning:** Do **not** use self-hosted runners with public repositories. A malicious pull request from a fork could execute arbitrary code on your self-hosted runner.

---

**Q: How do I store and use secrets in GitHub Actions?**

A: **Secrets** are encrypted environment variables stored in GitHub. They're used for API keys, passwords, and other sensitive values.

**Adding a secret:**
1. Go to the repository on GitHub.
2. Click **Settings > Secrets and variables > Actions**.
3. Click **New repository secret**.
4. Enter a name (e.g., `STRIPE_SECRET_KEY`) and value.
5. Click **Add secret**.

**Using a secret in a workflow:**
```yaml
steps:
  - name: Deploy to production
    env:
      STRIPE_KEY: ${{ secrets.STRIPE_SECRET_KEY }}
    run: python deploy.py
```

**Secret scoping:**
- **Repository secrets:** Available in all workflows in that repo
- **Environment secrets:** Available only when a job targets a specific deployment environment (e.g., `production`)
- **Organization secrets:** Available in all repos within the organization (with permission)

**Security rules:**
- Secrets are **never printed in logs** — GitHub masks them automatically
- Secrets are not passed to workflows triggered by forks (for security)
- Secret values are not visible after creation — only the name appears in the UI
- Rotate secrets regularly, especially after team member departures

---

**Q: How do I cache dependencies to speed up workflows?**

A: Caching saves downloaded dependencies so they don't have to be re-downloaded on every run.

**Using `actions/cache`:**
```yaml
- name: Cache pip packages
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

**How it works:**
- On the first run, the cache is **saved** after the step with the specified `path`
- On subsequent runs, if the `key` matches, the cache is **restored** before the step
- The `hashFiles()` function generates a hash of your dependency file — if the file changes, a new cache is created
- `restore-keys` provides fallback keys to restore a partial cache when the exact key doesn't match

**Language-specific setup actions often include caching:**
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'          # Automatically caches pip packages
```

Effective caching can reduce workflow time by **50–80%** for dependency-heavy projects.

---

**Q: How do I deploy to a cloud provider using GitHub Actions?**

A: GitHub has official or well-maintained actions for all major cloud providers:

**AWS:**
```yaml
- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: us-east-1

- name: Deploy to S3
  run: aws s3 sync ./dist s3://my-bucket --delete
```

**Azure:**
```yaml
- name: Deploy to Azure Web App
  uses: azure/webapps-deploy@v3
  with:
    app-name: 'my-web-app'
    publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
    package: '.'
```

**Google Cloud:**
```yaml
- name: Authenticate to Google Cloud
  uses: google-github-actions/auth@v2
  with:
    credentials_json: ${{ secrets.GCP_CREDENTIALS }}

- name: Deploy to Cloud Run
  uses: google-github-actions/deploy-cloudrun@v2
  with:
    service: 'my-service'
    region: 'us-central1'
    image: 'gcr.io/my-project/my-image'
```

**Best practice:** Use **OpenID Connect (OIDC)** token-based authentication instead of long-lived access keys where possible. This eliminates the need to store cloud credentials as secrets in GitHub.

---

**Q: How do I view and debug failed workflow runs?**

A: 

**Viewing logs:**
1. Go to the **Actions** tab in your repository.
2. Click the failed workflow run.
3. Click the failed job.
4. Expand individual steps to see their log output.

**Common debugging approaches:**

**Enable debug logging:** Add a secret `ACTIONS_RUNNER_DEBUG` = `true` to your repository. This outputs verbose runner logs.

**Enable step debug logging:** Add a secret `ACTIONS_STEP_DEBUG` = `true` for more detailed step output.

**Add echo statements:**
```yaml
- name: Debug environment
  run: |
    echo "Current directory: $(pwd)"
    echo "Files: $(ls -la)"
    echo "Python version: $(python --version)"
    env
```

**Use `tmate` for SSH debugging (development use):**
```yaml
- name: Setup tmate session
  uses: mxschmitt/action-tmate@v3
  if: ${{ failure() }}   # Only open SSH session on failure
```

**Re-run failed jobs:** On the failed run page, click **Re-run failed jobs** to retry without re-running successful jobs.

---

**Q: How much do GitHub Actions cost?**

A: GitHub Actions pricing is based on **compute minutes** used on GitHub-hosted runners:

**Free minutes per plan:**

| Plan | Free Minutes/Month |
|---|---|
| GitHub Free | 2,000 minutes |
| GitHub Pro | 3,000 minutes |
| GitHub Team | 3,000 minutes |
| GitHub Enterprise | 50,000 minutes |

**Minute multipliers (relative to Linux):**

| Runner OS | Multiplier |
|---|---|
| Linux (ubuntu-*) | 1× |
| Windows (windows-*) | 2× |
| macOS (macos-*) | 10× |

Example: 1 minute on macOS = 10 minutes deducted from your free allotment.

**Storage:** Artifacts and caches stored by Actions use your account's GitHub Actions storage quota (500 MB free on Free plan; 2 GB on Pro).

**Public repositories:** GitHub Actions is **free for public repositories** with no minute limits.

**Self-hosted runners:** No per-minute charge from GitHub (you pay for your own infrastructure).

---

## Related FAQ Sections

- [GitHub FAQ — Repositories](../repositories/github-faq-repositories.md)
- [GitHub FAQ — Security](../security/github-faq-security.md)
- [GitHub FAQ — Billing & Plans](../billing/github-faq-billing.md)

---

*Couldn't find your answer? Visit [GitHub Docs](https://docs.github.com)*
