
Coordinates read/write connection selection around replica lag.

When MySQL read replicas are enabled in config, the trait records a short
cooldown after write events. During that cooldown reads continue using the
write connection so application code does not immediately read stale replica
state after creating, updating, deleting, restoring, or reordering a model.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Replication`

## Properties

### replicationLag

Replica lag window in milliseconds.

```php
protected static ?int $replicationLag
```

A null value means replication behavior has not been initialized yet.

* This property is **static**.

***
### replicationReadyAt

Unix timestamp in milliseconds after which replica reads may resume.

```php
protected static ?int $replicationReadyAt
```

A null value means the replica is considered ready immediately.

* This property is **static**.

***
### readWriteConnectionBehaviorEventsManager

Events manager that already received the read/write replication listeners.

```php
protected ?\Phalcon\Contracts\Events\Manager $readWriteConnectionBehaviorEventsManager
```

Models can be initialized more than once in tests, long-running workers,
or application code that refreshes feature options. Tracking the manager
instance keeps listener attachment idempotent while still allowing a new
manager to receive the listeners if the model swaps managers.

***

## Methods

### setConnectionService

Set the default connection service used by Phalcon for this model.

```php
public setConnectionService(string $connectionService): void
```

Implemented by Phalcon's model base class.

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description                                 |
|----------------------|------------|---------------------------------------------|
| `$connectionService` | **string** | DI service name for the default
connection. |

***
### setReadConnectionService

Set the read connection service used by Phalcon for this model.

```php
public setReadConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description                          |
|----------------------|------------|--------------------------------------|
| `$connectionService` | **string** | DI service name for read operations. |

***
### setWriteConnectionService

Set the write connection service used by Phalcon for this model.

```php
public setWriteConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description                           |
|----------------------|------------|---------------------------------------|
| `$connectionService` | **string** | DI service name for write operations. |

***
### getWriteConnectionService

Return the configured write connection service name.

```php
public getWriteConnectionService(): string
```

* This method is **abstract**.
**Return Value:**

DI service name for write operations.

***
### getReadConnectionService

Return the configured read connection service name.

```php
public getReadConnectionService(): string
```

* This method is **abstract**.
**Return Value:**

DI service name for read operations.

***
### getReplicationLag

Return the configured replica lag window in milliseconds.

```php
public static getReplicationLag(): int|null
```

* This method is **static**.
**Return Value:**

Lag window, or null before replication initialization.

***
### setReplicationLag

Set the replica lag window in milliseconds.

```php
public static setReplicationLag(int|null $replicationLag = null): void
```

* This method is **static**.
**Parameters:**

| Parameter         | Type          | Description                                                       |
|-------------------|---------------|-------------------------------------------------------------------|
| `$replicationLag` | **int\|null** | Lag window to use after write events, or
null to clear the value. |

***
### getReplicationReadyAt

Return the timestamp after which replica reads may resume.

```php
public static getReplicationReadyAt(): int|null
```

* This method is **static**.
**Return Value:**

Unix timestamp in milliseconds, or null when reads are
not currently pinned to the write connection.

***
### setReplicationReadyAt

Set the timestamp after which replica reads may resume.

```php
public static setReplicationReadyAt(int|null $replicationReadyAt = null): void
```

* This method is **static**.
**Parameters:**

| Parameter             | Type          | Description                                                           |
|-----------------------|---------------|-----------------------------------------------------------------------|
| `$replicationReadyAt` | **int\|null** | Unix timestamp in milliseconds, or
null to mark the replica as ready. |

***
### initializeReplication

Initialize read/write connection services for replica-aware models.

```php
public initializeReplication(array<array-key,mixed>|null $options = null): void
```

The trait reads `database.drivers.mysql.readonly.enable` from the config
service. When enabled, it configures connection service names and attaches
write-event listeners that temporarily pin reads to the write connection.

**Parameters:**

| Parameter  | Type                             | Description                                                                                                                         |
|------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `$options` | **array<array-key,mixed>\|null** | Optional replication
options. Supported keys are `lag`, `connectionService`,
`readConnectionService`, and `writeConnectionService`. |

**Throws:**

When the config service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### selectReadConnection

Select the connection used for model reads.

```php
public selectReadConnection(): \Phalcon\Db\Adapter\AdapterInterface
```

When there is no active replica-cooldown window, the configured read
connection service is returned. Immediately after write-like events,
reads are pinned back to the write connection until the lag window
expires, which avoids stale reads from asynchronous replicas.

**Return Value:**

Read connection when replicas are ready; write
connection while reads are pinned after a mutation.

**Throws:**

When the read or write connection service cannot
be resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### addReadWriteConnectionBehavior

Attach lifecycle listeners that pin reads to the write connection.

```php
public addReadWriteConnectionBehavior(): void
```

Each write-like event updates `replicationReadyAt` to `now + lag`. Native
Phalcon requires a compatible events manager to attach these callbacks.

**Throws:**

When the model events manager is missing or does
not implement Phalcon's events manager contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### isReplicationReady

Determine whether reads may use a replica again.

```php
public isReplicationReady(): bool
```

When the cooldown has expired, the ready timestamp is cleared so future
calls remain ready until another write event updates it.

**Return Value:**

True when the replica cooldown is absent or expired.

***
### nowMs

Return the current process time in milliseconds.

```php
protected static nowMs(): int
```

This helper keeps replication timestamps integer-based and easy to
compare without leaking floating-point microtime values into public
replication state.

* This method is **static**.
**Return Value:**

Unix timestamp in milliseconds.

***
