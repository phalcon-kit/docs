
Registers the OpenAI API client service.

The provider builds an `openai-php/client` instance from the `openai` config
section. Supported values include API key, organization, project, and base
URI. The canonical config keys are `apiKey`, `organization`, `project`, and
`baseUri`; legacy bootstrap aliases such as `secretKey`, `organizationId`,
and `projectId` are accepted as fallbacks so older app config can keep
resolving the shared service while it migrates. A Guzzle client is supplied
explicitly so streaming responses use the same HTTP stack as normal requests.

***

* Full name: `\PhalconKit\Provider\OpenAi\ServiceProvider`
* Parent class: [`\PhalconKit\Provider\AbstractServiceProvider`](../AbstractServiceProvider.md)

## Properties

### serviceName

Stable DI service name managed by this provider.

```php
protected string $serviceName
```

This value is part of the provider contract because controllers, tasks,
other injectables, and replacement providers resolve services by name.
Concrete providers must set it to a non-empty value.

***

## Methods

### register

Register the shared `openAi` service.

```php
public register(\PhalconKit\Di\DiInterface $di): void
```

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

***

### normalizeOpenAiConfig

Normalize supported OpenAI provider config aliases.

```php
protected static normalizeOpenAiConfig(array<string,mixed> $openAiConfig): array{apiKey: string, organization: string|null, project: string|null, baseUri: string}
```

`apiKey`, `organization`, `project`, and `baseUri` are the canonical
provider-facing keys. The legacy bootstrap keys are still read as
fallbacks because applications may have copied the default `secretKey` or
`organizationId` names before the provider contract was clarified.

* This method is **static**.
**Parameters:**

| Parameter       | Type                    | Description                  |
|-----------------|-------------------------|------------------------------|
| `$openAiConfig` | **array<string,mixed>** | Raw `openai` config section. |

***

### stringConfigOption

Return the first non-empty string value from a list of config aliases.

```php
private static stringConfigOption(array<string,mixed> $config, list<string> $keys, string $default = ''): string
```

Canonical keys are passed first and legacy aliases follow them. Empty
strings are ignored so partially migrated environment files can leave a
canonical key blank while still relying on the older configured alias.

* This method is **static**.
**Parameters:**

| Parameter  | Type                    | Description                     |
|------------|-------------------------|---------------------------------|
| `$config`  | **array<string,mixed>** | Raw provider config.            |
| `$keys`    | **list<string>**        | Ordered config keys to inspect. |
| `$default` | **string**              |                                 |

***

### nullableStringConfigOption

Return an optional string config value from canonical and alias keys.

```php
private static nullableStringConfigOption(array<string,mixed> $config, list<string> $keys): ?string
```

* This method is **static**.
**Parameters:**

| Parameter | Type                    | Description                     |
|-----------|-------------------------|---------------------------------|
| `$config` | **array<string,mixed>** | Raw provider config.            |
| `$keys`   | **list<string>**        | Ordered config keys to inspect. |

***

### stringConfigValue

Cast a provider config value to the string expected by `openai-php/client`.

```php
private static stringConfigValue(mixed $value): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

## Inherited methods

### __construct

Stores the DI container and prepares the provider for registration.

```php
public __construct(\PhalconKit\Di\DiInterface $di): mixed
```

The constructor intentionally requires `PhalconKit\Di\DiInterface` so
providers can rely on typed service helpers during configuration and
registration.

**Parameters:**

| Parameter | Type                           | Description |
|-----------|--------------------------------|-------------|
| `$di`     | **\PhalconKit\Di\DiInterface** |             |

**Throws:**

When a concrete provider does not define a
non-empty service name.
- [`LogicException`](../../Exception/LogicException.md)

***

### getName

Returns the DI service name managed by this provider.

```php
public getName(): string
```

***

### boot

Optional post-registration hook.

```php
public boot(): void
```

The base implementation is intentionally empty. Custom bootstraps or
application code may call this method for provider-specific startup work
after all services have been registered.

***

### configure

Optional provider-local configuration hook.

```php
public configure(): void
```

This runs during construction after DI has been stored and before
`register()` is called. Use it to normalize provider options or prepare
lightweight state; service creation belongs in `register()`.

***
