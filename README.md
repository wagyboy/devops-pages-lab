# DevOps Pages Lab

Owner: 陳致安 (B11309058) · Course: DevOps

Live site: https://wagyboy.github.io/devops-pages-lab/

## Recent GitHub Activity

<!--START_SECTION:activity-->
1. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/e95dc62ffe2e051211be8fb0e7b93a94e6a32e0a)
2. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/6af3c3b989d1de24d8721923d6049304bc0975a5)
3. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/a70de3522eb51cfdf3da584eb8c9a6e528bcf827)
4. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/a79487607f4a1e8c1c7e12fecaef07c454c96860)
5. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/ee89e278590aa9d5224f76d35b4e1e51b0b16aa4)
6. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/4926f1ac41fcb6836540cf16f05ba7e6e10a6d5d)
7. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/2722b3645ed50697ac6466faaadc0307d32a12d3)
8. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/4aee8de42d2fb1c1380e0da628adf52b436d8b7e)
9. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/2f96ec9ced65b3a5a6f88ef2c14523cc528488c0)
10. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/040ba6b893f60cd80af830dcfe0175685f7e2d0d)
11. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/a0313355416fd718454ae416c0c2593169b4bf9d)
12. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/f4c534fc29351274363b22ba319732a0987cdcb1)
13. 🚀 Committed to main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/commit/8567c03ff5d265e23acc39f0c50f1c1bb20abb7d)
14. ✨ Created a new branch main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/tree/main)
15. ✨ Created a new branch chore/test-automation in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/tree/chore/test-automation)
<!--END_SECTION:activity-->

*This section is updated automatically by a scheduled GitHub Actions workflow.*

## How this site works

1. A scheduled workflow (`.github/workflows/activity-log.yml`) runs the `TheDanniCraft/activity-log` action.
2. The action reads my recent GitHub events and rewrites the lines between the two markers above, then commits the new `README.md`.
3. That commit triggers the release workflow (`.github/workflows/pages.yml`), which builds the site with Jekyll. `index.md` includes this README, so the homepage always shows the latest activity.
4. A release gate checks the build before anything goes live: the activity markers are present, every page has a doctype, a language and a title, no raw Liquid leaked into the output, and every internal link and asset exists. If any check fails, the site is not deployed and the previous version stays online.
5. After the deploy, a smoke test fetches `version.txt` from the live site and fails unless it matches the commit that was just built.

## Release safety

| Stage | What it does | What it protects against |
| --- | --- | --- |
| Build | Jekyll builds the site and stamps the commit SHA into `version.txt` | Knowing exactly which version is live |
| Gate | `.github/scripts/check_site.py` validates the built site | Broken links, missing activity section, template errors reaching visitors |
| Deploy | Runs only if the gate passed; pull requests run the gate but never deploy | Unchecked changes going live |
| Smoke test | Live `version.txt` must equal the built commit | A deploy that "succeeded" but is not actually being served |

## Configuration

| Setting | Value | Why |
| --- | --- | --- |
| `EVENT_LIMIT` | 15 | Enough to show about a week of work without an overly long page |
| `EVENT_EMOJI_MAP` | custom | One emoji per event type; PRs, issues and releases are mapped per action (opened / merged / closed) |
| `HIDE_DETAILS_ON_PRIVATE_REPOS` | true | Never expose private repository names on a public site |
| `COMMIT_MESSAGE` | `docs(activity): ...` | A conventional-commit prefix makes bot commits easy to filter in history |
| Token scope | `public_repo` only | Least privilege: the token cannot read or write any private repository |

## Schedule rationale

The workflow runs at minute 17 every 6 hours (`17 */6 * * *`, UTC), plus manual runs via `workflow_dispatch`.

- **Fresh enough:** my activity changes a few times a day, so four updates a day keep the page current.
- **Budget:** the action's default 30-minute schedule means 48 runs a day; every 6 hours means 4, which keeps the commit history readable and stays well inside GitHub API rate limits and Actions minutes.
- **Off the hour:** GitHub may delay scheduled runs at the top of the hour when load peaks; minute 17 avoids that queue.
- **No overlap:** `concurrency` makes sure two updates never race to commit `README.md`.

## Repository layout

- `index.md`: the homepage; it includes this README
- `README.md`: page content plus the auto-updated activity section
- `_config.yml`: site title, description and theme
- `_layouts/default.html`: custom page layout (hero panel, content card, footer)
- `assets/css/style.scss`: custom styles (colors, fonts, activity timeline, mobile layout)
- `.github/workflows/activity-log.yml`: the scheduled update workflow
- `.github/workflows/pages.yml`: the release workflow (build, gate, deploy, smoke test)
- `.github/scripts/check_site.py`: the release gate's checks
- `.gitignore`: keeps local Jekyll build output out of the repository
