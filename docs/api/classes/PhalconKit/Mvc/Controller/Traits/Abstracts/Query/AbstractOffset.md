
Abstract contract for REST query offset configuration.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractOffset`

## Methods

### initializeOffset

Initialize offset configuration.

```php
public initializeOffset(): void
```

* This method is **abstract**.
***
### setOffset

Replace the requested offset.

```php
public setOffset(?int $offset): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$offset` | **?int** |             |

***
### getOffset

Return the requested offset.

```php
public getOffset(): ?int
```

* This method is **abstract**.
***
### defaultOffset

Return the default offset.

```php
public defaultOffset(): ?int
```

* This method is **abstract**.
***
