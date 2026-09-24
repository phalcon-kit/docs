
WebSocket task with overridable Swoole event hooks.

Requires the shared `swoole` DI service to provide a WebSocket server using
positional event arguments (`event_object` disabled). Request/message callbacks
reset model connection state before invoking application hooks. Subscriptions
belong to the current worker process; applications coordinate other workers.

***

* Full name: `\PhalconKit\Modules\Ws\Tasks\AbstractTask`
* Parent class: [`\PhalconKit\Modules\Ws\Task`](../Task.md)
* This class is an **Abstract class**

## Properties

### subscriptions

```php
public static array $subscriptions
```

* This property is **static**.

***

### onOpen

```php
public \Closure $onOpen
```

***

### onClose

```php
public \Closure $onClose
```

***

### onMessage

```php
public \Closure $onMessage
```

***

### onWorkerError

```php
public \Closure $onWorkerError
```

***

### onStart

```php
public \Closure $onStart
```

***

### onWorkerStart

```php
public \Closure $onWorkerStart
```

***

### onShutdown

```php
public \Closure $onShutdown
```

***

### onRequest

```php
public \Closure $onRequest
```

***

### onPipeMessage

```php
public \Closure $onPipeMessage
```

***

### server

```php
public \Swoole\WebSocket\Server $server
```

***

## Methods

### initialize

Resolve the shared `swoole` service, build callbacks, and register them.

```php
public initialize(): void
```

Call the parent when overriding initialization to retain event dispatch.

***

### handleWebSocket

Register the initialized callbacks on the server without starting its event loop.

```php
public handleWebSocket(): void
```

***

### listenAction

Start the configured server event loop; returns after the server stops.

```php
public listenAction(): void
```

***

### initializeOpen

Install the open callback, resetting model connection state before the hook.

```php
public initializeOpen(): void
```

***

### initializeMessage

Install the message callback, resetting model connection state before the hook.

```php
public initializeMessage(): void
```

***

### initializeClose

Install the close callback, resetting model connection state before the hook.

```php
public initializeClose(): void
```

***

### initializeWorkerError

Adapt Swoole's five worker-error arguments to the existing four-argument hook.

```php
public initializeWorkerError(): void
```

Keep onWorkerError() overrides compatible while passing the actual exit code
and retaining both the worker PID and termination signal in the reason text.

***

### initializeStart

Install the master-process startup callback.

```php
public initializeStart(): void
```

***

### initializeWorkerStart

Install the worker startup callback with its worker ID.

```php
public initializeWorkerStart(): void
```

***

### initializeShutdown

Install the server shutdown callback.

```php
public initializeShutdown(): void
```

***

### initializeRequest

Install the HTTP callback, resetting model connection state before the hook.

```php
public initializeRequest(): void
```

***

### initializePipeMessage

Install the inter-worker message callback, resetting model connection state first.

```php
public initializePipeMessage(): void
```

***

### onOpen

Handle a completed WebSocket handshake; the default logs the client descriptor.

```php
public onOpen(\Swoole\WebSocket\Server $server, \Swoole\Http\Request $request): void
```

**Parameters:**

| Parameter  | Type                         | Description |
|------------|------------------------------|-------------|
| `$server`  | **\Swoole\WebSocket\Server** |             |
| `$request` | **\Swoole\Http\Request**     |             |

***

### onMessage

Handle a received WebSocket frame; the default logs its descriptor and payload.

```php
public onMessage(\Swoole\WebSocket\Server $server, \Swoole\WebSocket\Frame $frame): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |
| `$frame`  | **\Swoole\WebSocket\Frame**  |             |

***

### onClose

Handle a closed client descriptor; override to clean application subscription state.

```php
public onClose(\Swoole\WebSocket\Server $server, int $fd): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |
| `$fd`     | **int**                      |             |

***

### onWorkerError

Handle a failed worker; override to integrate application monitoring.

```php
public onWorkerError(\Swoole\WebSocket\Server $server, int $fd, int $code, string $reason): void
```

**Parameters:**

| Parameter | Type                         | Description                                                                |
|-----------|------------------------------|----------------------------------------------------------------------------|
| `$server` | **\Swoole\WebSocket\Server** | Server whose worker failed.                                                |
| `$fd`     | **int**                      | Worker ID, despite the historical parameter name; not a client descriptor. |
| `$code`   | **int**                      | Worker exit code.                                                          |
| `$reason` | **string**                   | Worker process details, formatted as "pid=<pid>, signal=<signal>".         |

***

### onStart

Handle master-process startup; the default logs the listening address.

```php
public onStart(\Swoole\WebSocket\Server $server): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |

***

### onWorkerStart

Handle worker startup; override for resources owned by this worker process.

```php
public onWorkerStart(\Swoole\WebSocket\Server $server, int $workerId): void
```

**Parameters:**

| Parameter   | Type                         | Description |
|-------------|------------------------------|-------------|
| `$server`   | **\Swoole\WebSocket\Server** |             |
| `$workerId` | **int**                      |             |

***

### onShutdown

Handle server shutdown; the default logs completion.

```php
public onShutdown(\Swoole\WebSocket\Server $server): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |

***

### onRequest

Handle an HTTP request on the WebSocket server.

```php
public onRequest(\Swoole\Http\Request $request, \Swoole\Http\Response $response): void
```

The default logs the path and ends the response with a placeholder body.

**Parameters:**

| Parameter   | Type                      | Description |
|-------------|---------------------------|-------------|
| `$request`  | **\Swoole\Http\Request**  |             |
| `$response` | **\Swoole\Http\Response** |             |

***

### onPipeMessage

Handle data sent by another worker.

```php
public onPipeMessage(\Swoole\WebSocket\Server $server, int $srcWorkerId, mixed $data): void
```

The default logs string-compatible data; override for structured messages.

**Parameters:**

| Parameter      | Type                         | Description |
|----------------|------------------------------|-------------|
| `$server`      | **\Swoole\WebSocket\Server** |             |
| `$srcWorkerId` | **int**                      |             |
| `$data`        | **mixed**                    |             |

***

### subscribeClientToChannel

Subscribes a client, identified by its file descriptor, to a specific channel.

```php
public subscribeClientToChannel(int $fd, string $channel): void
```

**Parameters:**

| Parameter  | Type       | Description                                         |
|------------|------------|-----------------------------------------------------|
| `$fd`      | **int**    | The file descriptor identifying the client.         |
| `$channel` | **string** | The name of the channel to subscribe the client to. |

***

### unsubscribeClientFromChannel

Unsubscribes a client, identified by its file descriptor, from a specific channel.

```php
public unsubscribeClientFromChannel(int $fd, string $channel): void
```

**Parameters:**

| Parameter  | Type       | Description                                             |
|------------|------------|---------------------------------------------------------|
| `$fd`      | **int**    | The file descriptor identifying the client.             |
| `$channel` | **string** | The name of the channel to unsubscribe the client from. |

***

### broadcastToChannel

Broadcasts a message to all active subscribers of a specified channel. Optionally, the broadcast
can target a specific list of file descriptors.

```php
public broadcastToChannel(\Swoole\WebSocket\Server $server, string $channel, array $data, array|null $fdList = null): void
```

**Parameters:**

| Parameter  | Type                         | Description                                                                      |
|------------|------------------------------|----------------------------------------------------------------------------------|
| `$server`  | **\Swoole\WebSocket\Server** | The server instance used to handle broadcasting and validating connections.      |
| `$channel` | **string**                   | The channel name to which the message should be broadcasted.                     |
| `$data`    | **array**                    | The message payload to be sent to the subscribers.                               |
| `$fdList`  | **array\|null**              | Optional list of file descriptors to restrict the broadcast to specific clients. |

***

### unsubscribeClient

Unsubscribes a client, identified by its file descriptor, from all subscribed channels.

```php
public unsubscribeClient(int $fd): void
```

**Parameters:**

| Parameter | Type    | Description                                 |
|-----------|---------|---------------------------------------------|
| `$fd`     | **int** | The file descriptor identifying the client. |

***

### log

Logs a message with the worker ID of the specified server instance or the default server instance.

```php
public log(string $message, \Swoole\WebSocket\Server|null $server = null): void
```

**Parameters:**

| Parameter  | Type                               | Description                                                                                                 |
|------------|------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `$message` | **string**                         | The message to log.                                                                                         |
| `$server`  | **\Swoole\WebSocket\Server\|null** | The server instance to use for retrieving the worker ID. If null, the default server instance will be used. |

***

## Inherited methods

### resetConnectionState

Clear request-scoped model connection state in a long-running worker.

```php
public resetConnectionState(): void
```

Call this before custom WebSocket callbacks that perform model reads or
writes. The built-in abstract task invokes it for open, message, close,
HTTP request, and pipe-message callbacks.

***
