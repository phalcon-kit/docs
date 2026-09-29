# Contributing To The Documentation

Write for developers building applications with PhalconKit. Lead with the task,
then prerequisites, file locations/configuration, a complete example, and the
expected result. Describe current behavior; release history belongs in tagged
history and changelogs. Keep upgrade instructions under `guides/migrations/`
using its common scope, preparation, changes, verification, rollback, and related
guides sections. Use neutral examples and never include private project
identifiers, domains, credentials, or proprietary workflows.

## Narrative Guides

The canonical source is `phalcon-kit/core/guides/`. Edit there, then synchronize
from a sibling checkout:

```shell
python bin/sync-guides.py --core ../core
python bin/sync-guides.py --core ../core --check
```

The script recursively mirrors Markdown guides (including the migrations directory), removes stale mirrored guide pages, and
rewrites Core-root policy links for this site. It does not touch generated API
pages. Edit this repository's README, homepage, and narrative navigation here.
Keep the App README aligned with setup commands and guide links. The site edit
link opens Core for mirrored guides, Docs for site-owned pages, and is hidden
for generated API pages; `hooks/edit_links.py` applies that ownership rule.

Before accepting an example, verify actual parameter names, response fields,
permissions, and database effects. Distinguish partial snippets from complete
files and application services from built-in capabilities. Test CLI, auth,
relationships, and serialization against the native runtime when relevant.

## Build And Preview

Using the repository Dockerfile:

```shell
docker build -t phalcon-kit-mkdocs .
docker run --rm -e CD=false -v "$PWD:/docs" phalcon-kit-mkdocs build --strict
docker run --rm -e CD=false -p 8000:8000 -v "$PWD:/docs" phalcon-kit-mkdocs serve -a 0.0.0.0:8000
```

Open `http://localhost:8000`. Podman can run the same image/commands. `CD=false`
disables publication-only plugins that need GitHub/network context; the guide
navigation, search, Markdown rendering, and API pages still build. The publication
workflow uses complete Git history for author/revision metadata and grants only
`contents: write` to the job that pushes the generated `gh-pages` branch.
The optional GitHub committer plugin reads `phalcon-kit/docs` on `main`; without
`MKDOCS_GIT_COMMITTERS_APIKEY`, it stays disabled and local Git author metadata
remains available. Use the publication workflow to verify the complete deployed
plugin configuration.

Run `git diff --check` and check local links/anchors. Confirm that every new
reader-facing guide is linked from the guide index and `mkdocs.yml`.

## Generated API Reference

When intentionally updating the API reference, run `composer docs` in Core,
then synchronize Core's generated `docs/` into this repository's `docs/api/`.
Replace only the API reference subtree in `mkdocs.yml` from Core's generated
`docs/mkdocs_menu.yml`; preserve narrative navigation. Remove stale generated
pages as part of that intentional sync. Do not hand-edit generated class/function
pages during a narrative documentation change.

See [Core contribution guidance](https://github.com/phalcon-kit/core/blob/master/CONTRIBUTING.md)
for code changes and [release procedures](https://github.com/phalcon-kit/core/blob/master/guides/release.md)
for publication. A local build does not publish the site.
