# alpine-skills

A collection of [Claude Skills](https://docs.claude.com/en/docs/claude-code/skills), packaged as a Claude Code plugin.

## Layout

```
.
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # lets this repo be added as a marketplace
└── skills/
    └── <skill-name>/
        ├── SKILL.md         # required: frontmatter + instructions
        ├── references/      # optional: docs loaded on demand
        ├── scripts/         # optional: code the skill runs
        └── assets/          # optional: templates and output files
```

## Installing

As a plugin (skills are namespaced as `alpine-skills:<skill-name>`):

```
/plugin marketplace add <path-or-git-url-of-this-repo>
/plugin install alpine-skills@alpine-skills
```

Or symlink a single skill for local use:

```sh
ln -s "$PWD/skills/<skill-name>" ~/.claude/skills/<skill-name>
```

## Adding a skill

1. Create `skills/<skill-name>/SKILL.md`, where `<skill-name>` is kebab-case.
2. Give it frontmatter whose `name` matches the directory name:

   ```markdown
   ---
   name: <skill-name>
   description: What the skill does and when to use it. This is what triggers the skill, so be specific.
   ---

   Instructions for Claude go here.
   ```

3. Keep `SKILL.md` lean; move long material into `references/` and link to it from the body.
4. Keep each skill self-contained: no files shared between skill directories.
