# Build With Phalcon Kit

Phalcon Kit is a database-first toolkit for building Phalcon applications and
REST APIs with consistent scaffolding, model relationships, eager loading,
identity, permissions, CLI tasks, and WebSocket support.

!!! info "Latest-version documentation"

    This site documents the latest stable release of `phalcon-kit/core` and
    the runtime requirements declared by that release. Historical behavior
    belongs in the changelog and GitHub releases rather than a versioned copy
    of this site.

Phalcon Kit extends Phalcon rather than replacing it. Refer to the
[latest Phalcon documentation](https://docs.phalcon.io/latest/){:target="_blank"}
for native framework behavior, and use this site for Phalcon Kit conventions.

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

-   :material-swap-horizontal:{ .lg .middle } **Migrate An Existing App**

    ---

    Move older Zemit or PhalconKit applications onto the current namespaces and
    REST conventions.

    [:octicons-arrow-right-24: Migration Guides](guides/migration-from-zemit.md)

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
- [Guide Index](guides/README.md) lists every maintained guide by workflow.
