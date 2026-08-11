# Phalcon Kit Documentation

This repository publishes the consumer documentation for
[phalcon-kit/core](https://github.com/phalcon-kit/core).

The maintained documentation has two sources:

- Narrative guides synchronized from the core repository.
- API reference generated from the current core source with phpDocumentor.

The site is rolling documentation for the latest stable Phalcon Kit release.
Runtime and dependency requirements come from the current core package rather
than being duplicated as version labels throughout the site.

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

## Contributing

Documentation changes should reflect public behavior already present in
phalcon-kit/core. Keep generated API files separate from hand-written guide
changes when practical.

See the
[core contribution guide](https://github.com/phalcon-kit/core/blob/master/CONTRIBUTING.md).

## License

Phalcon Kit documentation is available under the
[BSD 3-Clause License](LICENSE).
