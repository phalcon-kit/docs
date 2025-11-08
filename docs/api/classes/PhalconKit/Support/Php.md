
Class Php

Provides utility methods for working with PHP settings and environment.

***

* Full name: `\PhalconKit\Support\Php`

## Methods

### isCli

Check if the script is running in a command-line interface (CLI) environment.

```php
public static isCli(string $sapi = PHP_SAPI): bool
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$sapi`   | **string** |             |

**Return Value:**

Returns true if the script is running in a CLI environment, false otherwise.

***

### trustForwardedProto

Trust the forwarded protocol from the reverse proxy server.

```php
public static trustForwardedProto(): void
```

If trusted and HTTP_X_FORWARDED_PROTO is https force $_SERVER['https'] to 'on'

* This method is **static**.
***

### debug

Enable or disable debug mode

```php
public static debug(bool|null $debug = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type           | Description                                                                                   |
|-----------|----------------|-----------------------------------------------------------------------------------------------|
| `$debug`  | **bool\|null** | Set to true to enable debug mode, false to disable it. If null, debug mode remains unchanged. |

***

### set

Set the configuration options for the application.

```php
public static set(array $config = []): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description                                    |
|-----------|-----------|------------------------------------------------|
| `$config` | **array** | The configuration options for the application. |

***
