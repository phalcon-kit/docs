
Replica Lag Workaround
Prevents Phalcon to use read connection while
it might be lagging behind the master db

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Replication`

## Properties

### replicationLag

Replica Lag in milliseconds

```php
protected static ?int $replicationLag
```

* This property is **static**.

***
### replicationReadyAt

Timestamp until we can use replication

```php
protected static ?int $replicationReadyAt
```

* This property is **static**.

***

## Methods

### setConnectionService

```php
public setConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description |
|----------------------|------------|-------------|
| `$connectionService` | **string** |             |

***
### setReadConnectionService

```php
public setReadConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description |
|----------------------|------------|-------------|
| `$connectionService` | **string** |             |

***
### setWriteConnectionService

```php
public setWriteConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description |
|----------------------|------------|-------------|
| `$connectionService` | **string** |             |

***
### getWriteConnectionService

```php
public getWriteConnectionService(): string
```

* This method is **abstract**.
***
### getReadConnectionService

```php
public getReadConnectionService(): string
```

* This method is **abstract**.
***
### getReplicationLag

Get the replication lag value in milliseconds

```php
public static getReplicationLag(): ?int
```

* This method is **static**.
***
### setReplicationLag

Set the replication lag value in milliseconds

```php
public static setReplicationLag(?int $replicationLag = null): void
```

* This method is **static**.
**Parameters:**

| Parameter         | Type     | Description |
|-------------------|----------|-------------|
| `$replicationLag` | **?int** |             |

***
### getReplicationReadyAt

Get the replication lag value in milliseconds

```php
public static getReplicationReadyAt(): ?int
```

* This method is **static**.
***
### setReplicationReadyAt

Set the replication lag value in milliseconds

```php
public static setReplicationReadyAt(?int $replicationReadyAt = null): void
```

* This method is **static**.
**Parameters:**

| Parameter             | Type     | Description |
|-----------------------|----------|-------------|
| `$replicationReadyAt` | **?int** |             |

***
### initializeReplication

Replication Trait Initialization
- Set Read & Write Connection Service
- Add Replication Behavior

```php
public initializeReplication(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***
### selectReadConnection

Dynamically selects a shard
- Prefer to read on the write master during the replica delay

```php
public selectReadConnection(): \Phalcon\Db\Adapter\AdapterInterface
```

Possible parameters which can be added if required
?array $intermediate = null, array $bindParams = [], array $bindTypes = []

***
### addReadWriteConnectionBehavior

Force write connection service to master if the model was previously saved

```php
public addReadWriteConnectionBehavior(): void
```

***
### isReplicationReady

Check whether the replica should be ready or not

```php
public isReplicationReady(): bool
```

**Return Value:**

true if replica should be ready

***
### nowMs

```php
protected static nowMs(): int
```

* This method is **static**.
***
