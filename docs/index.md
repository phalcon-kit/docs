# Build With Phalcon Kit

Phalcon Kit is a database-first toolkit for building Phalcon applications and
REST APIs with consistent scaffolding, model relationships, eager loading,
identity, permissions, CLI tasks, and WebSocket support.

[Get Started](guides/getting-started.md){ .md-button .md-button--primary }
[Browse The Cookbook](guides/cookbook.md){ .md-button }

!!! info "Core 4.0 and App 4.0 development"

    This site follows the upcoming **Core 4.0.0 and App 4.0.0** releases. Only
    4.x is maintained; all earlier versions are end of life, with no fixes or
    backports. Both releases are still unreleased, so there is currently no
    supported stable release. Read the [Core 4.0 upgrade guide](guides/upgrading-4.0.md)
    before evaluating the development preview. Older tags preserve historical
    documentation.

Phalcon Kit extends Phalcon rather than replacing it. Refer to the
[latest Phalcon documentation](https://docs.phalcon.io/latest/){:target="_blank"}
for native framework behavior, and use this site for Phalcon Kit conventions.

The current source baseline requires PHP 8.5 or newer and Phalcon 5.22.0 or
newer on the 5.x release line.

## Jump Right In

Choose the path closest to what you want to build.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Get Started**

    ---

    Install Phalcon Kit, understand the application layout, and boot your first
    project.

    [:octicons-arrow-right-24: Getting Started](guides/getting-started.md)

-   :material-api:{ .lg .middle } **Build A REST Resource**

    ---

    Turn a database table into a model-backed API resource using the current
    controller conventions.

    [:octicons-arrow-right-24: First REST Resource](guides/first-rest-resource.md)

-   :material-sitemap:{ .lg .middle } **Understand The Architecture**

    ---

    Learn how bootstrap, modules, providers, configuration, and application
    ownership fit together.

    [:octicons-arrow-right-24: Architecture](guides/architecture.md)

-   :material-database-cog:{ .lg .middle } **Work With Data**

    ---

    Scaffold models, configure relationships, and load related records without
    N+1 queries.

    [:octicons-arrow-right-24: Models And Eager Loading](guides/models-and-eager-loading.md)

-   :material-shield-account:{ .lg .middle } **Secure The Application**

    ---

    Connect identities, roles, permissions, sessions, JWT, and controller
    attributes.

    [:octicons-arrow-right-24: Identity And Permissions](guides/identity-and-permissions.md)

-   :material-console-line:{ .lg .middle } **Run Beyond HTTP**

    ---

    Use the shared bootstrap and dependency injection model for CLI tasks and
    WebSocket runtimes.

    [:octicons-arrow-right-24: CLI And WebSocket](guides/web-server-and-websocket.md)

-   :material-lightbulb-on-outline:{ .lg .middle } **Solve A Common Task**

    ---

    Copy focused recipes for endpoints, services, eager loading, workflow
    actions, transformers, CLI tasks, and tests.

    [:octicons-arrow-right-24: Developer Cookbook](guides/cookbook.md)

-   :material-code-braces:{ .lg .middle } **Browse The API**

    ---

    Explore the generated class, interface, trait, and function reference for
    the current source tree.

    [:octicons-arrow-right-24: API Reference](api/Home.md)

</div>

## Install

=== "Add To A Project"

    ```bash
    composer require phalcon-kit/core
    ```

=== "Create An Application"

    ```bash
    composer create-project phalcon-kit/app my-api
    ```

## Keep Exploring

- [Configuration](guides/configuration.md) covers modules, providers, aliases,
  permissions, and integrations.
- [Database And Scaffolding](guides/database-scaffolding.md) explains the
  database-first development workflow.
- [REST APIs](guides/rest-api.md) documents controllers, query composition,
  responses, and extension points.
- [Troubleshooting](guides/troubleshooting.md) maps common symptoms back to the
  runtime, configuration, routing, model, or REST layer that owns them.
- [Migration Guides](guides/migration-from-zemit.md) help older Zemit and
  PhalconKit applications move onto current namespaces and contracts.
- [Guide Index](guides/README.md) lists every maintained guide by workflow.
