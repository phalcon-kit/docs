
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\ReplicationInterface`

## Methods

### getReplicationLag

```php
public static getReplicationLag(): ?int
```

* This method is **static**.
***

### setReplicationLag

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

```php
public static getReplicationReadyAt(): ?int
```

* This method is **static**.
***

### setReplicationReadyAt

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

```php
public initializeReplication(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### selectReadConnection

```php
public selectReadConnection(): \Phalcon\Db\Adapter\AdapterInterface
```

***

### addReadWriteConnectionBehavior

```php
public addReadWriteConnectionBehavior(): void
```

***

### isReplicationReady

```php
public isReplicationReady(): bool
```

***
