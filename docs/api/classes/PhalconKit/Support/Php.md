
Small PHP runtime helpers used during bootstrap.

These helpers centralize runtime concerns that must be configured before the
application handles a request, such as SAPI checks, proxy HTTPS detection,
debugging INI flags, locale, encoding, memory limit, and execution timeout.

***

* Full name: `\PhalconKit\Support\Php`

## Methods

### isCli

Determine whether a SAPI value represents a command-line runtime.

```php
public static isCli(string $sapi = \PhalconKit\Support\PHP_SAPI): bool
```

`phpdbg` is treated as CLI so test runners and debuggers follow the same
bootstrap path as normal console commands.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description                                          |
|-----------|------------|------------------------------------------------------|
| `$sapi`   | **string** | PHP SAPI name. Defaults to the current process SAPI. |

**Return Value:**

True for CLI-like SAPIs, false for web SAPIs.

***

### trustForwardedProto

Promote trusted proxy HTTPS information into `$_SERVER['HTTPS']`.

```php
public static trustForwardedProto(): void
```

Applications behind a reverse proxy can call this during bootstrap after
deciding that `HTTP_X_FORWARDED_PROTO` is trustworthy. When the forwarded
protocol starts with `https`, Phalcon and PHP helpers that inspect
`$_SERVER['HTTPS']` will see the request as secure.

* This method is **static**.
***

### debug

Enable or disable PHP error display for the current process.

```php
public static debug(bool|null $debug = null): void
```

Passing true enables full error reporting and display. Passing false or
null disables display while keeping `error_reporting(-1)`, which preserves
reporting for logs without exposing errors in responses.

* This method is **static**.
**Parameters:**

| Parameter | Type           | Description                                              |
|-----------|----------------|----------------------------------------------------------|
| `$debug`  | **bool\|null** | Whether response-visible debug output should be
enabled. |

***

### set

Apply process-wide PHP defaults used by PhalconKit applications.

```php
public static set(array{timezone?: non-empty-string, encoding?: non-empty-string, locale?: non-empty-string, memoryLimit?: non-empty-string, timeoutLimit?: int|string} $config = []): void
```

Missing values are filled with conservative framework defaults. This
method changes global PHP runtime state, so applications should call it
once during bootstrap before handling requests or starting long-running
workers.

* This method is **static**.
**Parameters:**

| Parameter | Type                                                                                                                                                       | Description               |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| `$config` | **array{timezone?: non-empty-string, encoding?: non-empty-string, locale?: non-empty-string, memoryLimit?: non-empty-string, timeoutLimit?: int\|string}** | Runtime options to apply. |

***
