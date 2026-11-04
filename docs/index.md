# Build Your Application With PhalconKit

PhalconKit adds REST resources, database scaffolding, model relationships,
authentication, permissions, and shared HTTP/CLI/WebSocket infrastructure to
Phalcon. Your application defines its schema, business rules, and public API.

## Start With A Working API

```shell
composer create-project phalcon-kit/app my-api
cd my-api
cp .env.example .env
php -S 127.0.0.1:8080 -t public public/index.php
```

Then request `http://127.0.0.1:8080/api`. The starter responds with HTTP 200.
See [Getting Started](guides/getting-started.md) for PHP/Phalcon requirements,
database configuration, and deployment setup.

Follow [Your First REST Resource](guides/first-rest-resource.md) to turn a table
into a controlled API. The tutorial includes the schema, generated model paths,
controller policies, permissions, requests, and actual response examples.

## Understand How It Fits Together

PhalconKit is still Phalcon: one bootstrap reads your config, registers a DI
service per provider, and runs the same application over HTTP, the CLI, or a
WebSocket worker. [Application Structure](guides/architecture.md) shows where
your code belongs, and [How A Request Runs](guides/request-lifecycle.md)
follows a request from the entrypoint through the permission checks to your
controller.

## What Are You Building?

| Application task | Start here |
| --- | --- |
| A new backend | [Install and run](guides/getting-started.md) |
| Core inside an existing Phalcon project | [Application integration](guides/application-integration.md) |
| Search and list screens | [Filters, pagination, and sorting](guides/rest-filtering.md) |
| Forms and batch editing | [Writes and validation](guides/rest-writes.md) |
| Detail screens with related records | [Relationships](guides/rest-relationships.md) |
| Dashboards and downloads | [Counts, facets, and exports](guides/rest-aggregates.md) |
| Authenticated application users | [Login, refresh, logout, and account commands](guides/authentication.md) |
| Private or tenant-owned resources | [Permissions and row scope](guides/identity-and-permissions.md) |
| A change history for records | [Opt-in audit trail](guides/models-and-eager-loading.md#audit-trail-opt-in) |
| Scheduled tasks | [CLI commands](guides/cli-tasks.md) |
| Live notifications | [WebSockets and application subscriptions](guides/web-server-and-websocket.md) |

## Use The API Confidently

The [REST handbook](guides/rest-api.md) covers built-in actions and their policies.
Use [Requests And Responses](guides/rest-requests-and-responses.md) for client
integration and the [scenario checklist](guides/rest-scenarios.md) to verify
empty results, errors, batches, permissions, and relationship edge cases.

Changing an existing application? Use the [migration index](guides/migrations/README.md)
for package, REST, Core, and App changes.

## Look Something Up

| Question | Reference |
| --- | --- |
| Which variable sets this option, and what is its default? | [Environment variables](guides/reference/environment.md) |
| Which DI service does this, and how do I replace it? | [Services](guides/reference/services.md) |
| Which CLI tasks, actions, and options exist? | [CLI commands](guides/reference/cli.md) |
| What does this class or method do? | [API reference](api/Home.md) |

Browse [all guides](guides/README.md), or ask a usage question in
[Discussions](https://github.com/orgs/phalcon-kit/discussions).
