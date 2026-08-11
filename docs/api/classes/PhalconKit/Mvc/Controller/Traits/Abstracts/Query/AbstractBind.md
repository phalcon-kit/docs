
Abstract contract for query bind values and bind types.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractBind`

## Methods

### initializeBind

Initialize query bind values.

```php
public initializeBind(): void
```

* This method is **abstract**.
***
### initializeBindTypes

Initialize query bind types.

```php
public initializeBindTypes(): void
```

* This method is **abstract**.
***
### setBind

Replace bind values used by compiled query options.

```php
public setBind(array|\Phalcon\Support\Collection|null $bind): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$bind`   | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getBind

Return bind values used by compiled query options.

```php
public getBind(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### setBindTypes

Replace bind types used by compiled query options.

```php
public setBindTypes(array|\Phalcon\Support\Collection|null $bindTypes): void
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type                                         | Description |
|--------------|----------------------------------------------|-------------|
| `$bindTypes` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getBindTypes

Return bind types used by compiled query options.

```php
public getBindTypes(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
