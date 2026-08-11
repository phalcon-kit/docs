
Minimal CLI exception/message writer.

The handler is intentionally small: it writes a string, Exception, or any
Throwable to a stream and appends one trailing newline. It is useful during
early CLI bootstrap where a full logger service may not be available yet.

***

* Full name: `\PhalconKit\Cli\ExceptionHandler`

## Properties

### e

```php
private string|\Exception|\Throwable $e
```

***

### outputStream

```php
private mixed $outputStream
```

***

## Methods

### __construct

```php
public __construct(string|\Exception|\Throwable $e, mixed $outputStream = \PhalconKit\Cli\STDERR): mixed
```

**Parameters:**

| Parameter       | Type                               | Description                                     |
|-----------------|------------------------------------|-------------------------------------------------|
| `$e`            | **string\|\Exception\|\Throwable** | Message or throwable to render.                 |
| `$outputStream` | **mixed**                          | Writable stream resource, defaulting to
STDERR. |

***

### write

Write the configured message/throwable to the output stream.

```php
public write(): void
```

***
