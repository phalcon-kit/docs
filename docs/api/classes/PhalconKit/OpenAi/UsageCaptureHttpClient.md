
PSR-18 decorator capturing Responses usage without changing SDK response objects.

***

* Full name: `\PhalconKit\OpenAi\UsageCaptureHttpClient`
* This class is marked as **final** and can't be subclassed
* This class implements:
  `ClientInterface`
* This class is a **Final class**

## Properties

### client

```php
private \Psr\Http\Client\ClientInterface $client
```

***

### capture

```php
private \PhalconKit\OpenAi\UsageCapture $capture
```

***

## Methods

### __construct

```php
public __construct(\Psr\Http\Client\ClientInterface $client, \PhalconKit\OpenAi\UsageCapture $capture): mixed
```

**Parameters:**

| Parameter  | Type                                 | Description                                      |
|------------|--------------------------------------|--------------------------------------------------|
| `$client`  | **\Psr\Http\Client\ClientInterface** | Application-owned HTTP transport.                |
| `$capture` | **\PhalconKit\OpenAi\UsageCapture**  | Shared billing store; also use it for streaming. |

***

### sendRequest

Send through the original client and observe eligible response bodies lazily.

```php
public sendRequest(\Psr\Http\Message\RequestInterface $request): \Psr\Http\Message\ResponseInterface
```

Requests, including uploads, are not read or modified. Client exceptions
propagate unchanged; the caller's reads determine when usage is available.

**Parameters:**

| Parameter  | Type                                   | Description |
|------------|----------------------------------------|-------------|
| `$request` | **\Psr\Http\Message\RequestInterface** |             |

***
