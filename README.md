# DevOps Pages Lab

Owner: 陳致安 (B11309058) · Course: DevOps

Live site: https://wagyboy.github.io/devops-pages-lab/

## Recent GitHub Activity

<!--START_SECTION:activity-->
1. ✨ Created a new branch main in [wagyboy/devops-pages-lab](https://github.com/wagyboy/devops-pages-lab/tree/main)
2. ✨ Created a new branch chore/test-automation in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/tree/chore/test-automation)
3. 🎉 Merged PR #3 in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/pull/3)
4. 🔀 Opened PR #3 in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/pull/3)
5. 🚀 Committed to chore/test-automation in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/ca913749a29fc65743c1af7f30685d075464392e)
6. 🚀 Committed to chore/test-automation in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/f230c0e3cb570a1fe77d435677630b142dc313c7)
7. 🚀 Committed to chore/a4-demo in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/6e052610ed96aa62a517bdbcad1a4b57725404fd)
8. 🚀 Committed to chore/a4-agent in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/9024e63076724846db8c3b33e8becd4e05039b3b)
9. ✨ Created a new branch chore/a4-agent in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/tree/chore/a4-agent)
10. 🚀 Committed to chore/a4-quality in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/dea63abfe55521172d6a3f81c6be7da323b4d471)
11. ✨ Created a new branch chore/a4-demo in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/tree/chore/a4-demo)
12. 🚀 Committed to chore/a4-demo in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/fc9cceefd6d389e79a3ced9eb78391da8b7bf2c8)
13. 🚀 Committed to master in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/c1bc594483aa13279c2c6b85a6cb393401b7b971)
14. 🚀 Committed to master in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/c5f402124f07026bb10773f657467286ba74ea03)
15. 🚀 Committed to chore/a4-agent in [wagyboy/activity-log-a4](https://github.com/wagyboy/activity-log-a4/commit/b98ff5b04c3cd95661c571bf3f5b3f871aabbc30)
<!--END_SECTION:activity-->

*This section is updated automatically by a scheduled GitHub Actions workflow.*

## How this site works

1. A scheduled workflow (`.github/workflows/activity-log.yml`) runs the `TheDanniCraft/activity-log` action.
2. The action reads my recent GitHub events and rewrites the lines between the two markers above, then commits the new `README.md`.
3. GitHub Pages rebuilds the site. `index.md` includes this README, so the homepage always shows the latest activity.

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
- `.github/workflows/activity-log.yml`: the scheduled update workflow
- `.gitignore`: keeps local Jekyll build output out of the repository
