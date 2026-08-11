# Phalcon Kit

Phalcon Kit is a database-first toolkit for building Phalcon applications and
REST APIs with consistent scaffolding, model relationships, eager loading,
identity, permissions, CLI tasks, and WebSocket support.

The current stable documentation targets:

- Phalcon Kit Core 3.9.0
- PHP 8.5 or newer
- Phalcon 5.18.2

Phalcon Kit extends Phalcon rather than replacing it. Use the official
[Phalcon 5.18 documentation](https://docs.phalcon.io/5.18/) for native framework
behavior and these guides for Phalcon Kit conventions.

## Start Here

- [Getting Started](guides/getting-started.md): install, configure, and run an
  application.
- [Build Your First REST Resource](guides/first-rest-resource.md): go from a
  database table to a model-backed API resource.
- [Architecture](guides/architecture.md): understand bootstrap, modules,
  generated models, and application-owned code.
- [Configuration](guides/configuration.md): configure modules, providers,
  aliases, permissions, and integrations.

## Core Workflows

- [Database And Scaffolding](guides/database-scaffolding.md)
- [Models And Eager Loading](guides/models-and-eager-loading.md)
- [REST APIs](guides/rest-api.md)
- [Identity And Permissions](guides/identity-and-permissions.md)
- [Web Server And WebSocket](guides/web-server-and-websocket.md)

## Reference

- [API Reference](api/Home.md): generated directly from the current
  phalcon-kit/core source.
- [Phalcon Runtime Upgrades](guides/phalcon-runtime-upgrades.md): keep the
  native extension, Composer requirements, IDE stubs, Docker, and CI aligned.
- [Migration From zemit-cms/core](guides/migration-from-zemit.md): guidance for
  historical applications.

Install the stable core package with:

    composer require phalcon-kit/core:^3.9

For a new project:

    composer create-project phalcon-kit/app my-api
