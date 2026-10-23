
Optional, bounded capture of Responses billing fields omitted by SDK decoders.

Share one instance between UsageCaptureHttpClient and wrapStreamHandler().
Entries contain only whitelisted usage counters and model/service-tier identifiers;
prompts, output, headers, and arbitrary metadata are never stored here. Applications
own pricing and persistence and must check usage_valid before using captured counters.

***

* Full name: `\PhalconKit\OpenAi\UsageCapture`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Properties

### responses

```php
private array<string,array{usage: array<string,mixed>, usage_valid: bool, model?: string, service_tier?: string}> $responses
```

***

### capacity

```php
private int $capacity
```

***

## Methods

### __construct

```php
public __construct(int $capacity = 128): mixed
```

**Parameters:**

| Parameter   | Type    | Description                                                  |
|-------------|---------|--------------------------------------------------------------|
| `$capacity` | **int** | Maximum unconsumed response IDs; oldest entries are evicted. |

**Throws:**

If capacity is less than one.
- [`InvalidArgumentException`](https://www.php.net/manual/en/class.invalidargumentexception.php){:target="_blank"}

***

### reset

Discard unconsumed counters, for example at the end of a worker job.

```php
public reset(): void
```

***

### takeForResponseId

Consume billing fields for exactly this provider response ID, once.

```php
public takeForResponseId(string $responseId): array{usage: array<string,mixed>, usage_valid: bool, model?: string, service_tier?: string}|array{}
```

Call after consuming the JSON body or terminal stream event. Missing counters
remain missing; invalid supplied counters are omitted and set usage_valid=false.
An empty result means no capture is available, not that the request was free.

**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$responseId` | **string** |             |

***

### wrapStreamHandler

Decorate a transport without reading ahead or buffering the entire stream.

```php
public wrapStreamHandler(callable $handler): callable
```

Register the returned closure as the openAiStreamHandler DI service through
a factory returning it. Transport and body-read exceptions remain unchanged.

**Parameters:**

| Parameter  | Type         | Description         |
|------------|--------------|---------------------|
| `$handler` | **callable** | Existing transport. |

***

### wrapResponse

Observe successful Responses create/retrieve bodies as the caller reads them.

```php
public wrapResponse(\Psr\Http\Message\RequestInterface $request, \Psr\Http\Message\ResponseInterface $response): \Psr\Http\Message\ResponseInterface
```

Other endpoints, errors, unsupported media types, and unreadable bodies are
returned unchanged. JSON bodies and individual SSE data lines have an 8 MiB
transient parsing limit; oversized or malformed data yields no capture.
Seek, close, and detach retain the underlying stream's behavior. Re-reading
an observed body does not recreate consumed records. GET captures must match
the response ID in the requested path. No network or body reads occur here.

**Parameters:**

| Parameter   | Type                                    | Description |
|-------------|-----------------------------------------|-------------|
| `$request`  | **\Psr\Http\Message\RequestInterface**  |             |
| `$response` | **\Psr\Http\Message\ResponseInterface** |             |

***

### captureJson

```php
private captureJson(string $json, ?string $expectedId, array<string,true>& $seen): void
```

**Parameters:**

| Parameter     | Type                   | Description |
|---------------|------------------------|-------------|
| `$json`       | **string**             |             |
| `$expectedId` | **?string**            |             |
| `$seen`       | **array<string,true>** |             |

***

### filterCounters

```php
private filterCounters(mixed $raw, array<string,mixed> $schema, bool& $valid): array<string,mixed>
```

**Parameters:**

| Parameter | Type                    | Description |
|-----------|-------------------------|-------------|
| `$raw`    | **mixed**               |             |
| `$schema` | **array<string,mixed>** |             |
| `$valid`  | **bool**                |             |

***
