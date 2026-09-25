# Phalcon Kit Documentation

This repository publishes the consumer documentation for
[phalcon-kit/core](https://github.com/phalcon-kit/core).

The maintained documentation has two sources:

- Narrative guides synchronized from the core repository.
- API reference generated from the current core source with phpDocumentor.

The site follows **Core 4.0.0 and App 4.0.0**, then ongoing work on the maintained
4.x line. All earlier versions are end of life; historical tags preserve older
documentation. Installation examples use tagged stable releases.

Runtime and dependency requirements come from the current Core package. App
intentionally skips 3.x to align its major version with Core.

## Build Locally

Build the documentation image:

    docker build -t phalcon-kit-mkdocs .

Build the site:

    docker run -e CD=true --rm -it -v $PWD:/docs phalcon-kit-mkdocs build

Serve it locally:

    docker run -e CI=true --rm -it -p 8000:8000 -v $PWD:/docs phalcon-kit-mkdocs

Open http://localhost:8000.

## Updating From Core

Regenerate the API reference in the core repository with:

    composer docs

Then synchronize core/docs into docs/api and core/guides into docs/guides.
Review and build the complete MkDocs site before publishing.

Replace the API navigation in `mkdocs.yml` with Core's generated
`docs/mkdocs_menu.yml`, preserving the narrative guide navigation. Remove stale
generated files for retired classes during synchronization. Links from guides
to Core's root policies, roadmap, and excluded planning guide
(`to-be-discussed.md`) should target the Core repository.

Core's documentation command supplements phpDocumentor with model-enum pages
and includes their cases, backing values, and namespace in the generated API
navigation. Regenerate through `composer docs`; do not maintain those pages by
hand. See the [Core maintenance guide](https://github.com/phalcon-kit/core/blob/master/guides/quality-and-maintenance.md).

When publishing releases, synchronize the final Core source and verify that
App's installation instructions use the tested stable Core constraint and lockfile. See the [Core release process](https://github.com/phalcon-kit/core/blob/master/guides/release.md).

## Contributing

Documentation changes should reflect public behavior already present in
phalcon-kit/core. Keep generated API files separate from hand-written guide
changes when practical.

See the
[core contribution guide](https://github.com/phalcon-kit/core/blob/master/CONTRIBUTING.md).

## License

Phalcon Kit documentation is available under the
[BSD 3-Clause License](LICENSE).
