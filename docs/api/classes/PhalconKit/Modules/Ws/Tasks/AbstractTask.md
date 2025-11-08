
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

```php
public initialize(): void
```

***

### handleWebSocket

```php
public handleWebSocket(): void
```

***

### listenAction

```php
public listenAction(): void
```

***

### initializeOpen

```php
public initializeOpen(): void
```

***

### initializeMessage

```php
public initializeMessage(): void
```

***

### initializeClose

```php
public initializeClose(): void
```

***

### initializeWorkerError

```php
public initializeWorkerError(): void
```

***

### initializeStart

```php
public initializeStart(): void
```

***

### initializeWorkerStart

```php
public initializeWorkerStart(): void
```

***

### initializeShutdown

```php
public initializeShutdown(): void
```

***

### initializeRequest

```php
public initializeRequest(): void
```

***

### initializePipeMessage

```php
public initializePipeMessage(): void
```

***

### onOpen

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

```php
public onWorkerError(\Swoole\WebSocket\Server $server, int $fd, int $code, string $reason): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |
| `$fd`     | **int**                      |             |
| `$code`   | **int**                      |             |
| `$reason` | **string**                   |             |

***

### onStart

```php
public onStart(\Swoole\WebSocket\Server $server): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |

***

### onWorkerStart

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

```php
public onShutdown(\Swoole\WebSocket\Server $server): void
```

**Parameters:**

| Parameter | Type                         | Description |
|-----------|------------------------------|-------------|
| `$server` | **\Swoole\WebSocket\Server** |             |

***

### onRequest

```php
public onRequest(\Swoole\Http\Request $request, \Swoole\Http\Response $response): void
```

**Parameters:**

| Parameter   | Type                      | Description |
|-------------|---------------------------|-------------|
| `$request`  | **\Swoole\Http\Request**  |             |
| `$response` | **\Swoole\Http\Response** |             |

***

### onPipeMessage

```php
public onPipeMessage(\Swoole\WebSocket\Server $server, int $srcWorkerId, mixed $data): void
```

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
