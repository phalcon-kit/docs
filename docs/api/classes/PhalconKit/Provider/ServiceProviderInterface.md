
Contract for services that register PhalconKit runtime dependencies.

Providers are the boundary between configuration and concrete services in
the DI container. They receive a PhalconKit DI implementation, not a native
Phalcon-only container, so implementations can use `getConfig()`,
`getTyped()`, and other framework-level container guarantees while wiring
services.

***

* Full name: `\PhalconKit\Provider\ServiceProviderInterface`
* Parent interfaces:
  `InjectionAwareInterface`

## Methods

### register

Registers one or more services in the DI container.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

Implementations normally register the main service under `getName()` and
should preserve the configured service contract when replacing a core
provider. Invalid configuration should fail with explicit exceptions so
application startup reports the real problem.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

***

### boot

Optional post-registration hook for provider-owned initialization.

```php
public boot(): void
```

The default `Bootstrap` currently registers providers directly and does
not iterate provider instances after registration. Applications or custom
bootstraps that need this hook may call it explicitly.

***

### configure

Configures the provider before services are registered.

```php
public configure(): void
```

`AbstractServiceProvider` calls this method from its constructor after
storing the DI container. Use it for provider-local setup that should run
before `register()`, not for creating DI services.

***

### getName

Returns the stable DI service name managed by this provider.

```php
public getName(): string
```

Downstream injectables and config overrides rely on this name, so provider
replacements should keep the same name unless they intentionally introduce
a new service.

***
