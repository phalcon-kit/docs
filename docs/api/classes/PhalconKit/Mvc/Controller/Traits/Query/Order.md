
Parses REST `order` parameters into Phalcon-compatible query expressions.

By default the parser preserves the historical PhalconKit behavior and
accepts any field name that passes identifier normalization. Controllers can
opt in to explicit order-field allow-lists through `initializeOrderFields()`
/ `setOrderFields()`, usually provided by the aggregate Query field policy
initialization.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Order`

## Properties

### defaultOrder

Controller-owned fallback order used when the request has no `order`.

```php
protected array|string|null $defaultOrder
```

***
### order

Parsed ORDER BY expressions keyed by public field name.

```php
protected ?\Phalcon\Support\Collection $order
```

***

## Methods

### initializeDefaultOrder

Initialize the default order used by the REST query.

```php
public initializeDefaultOrder(): void
```

Concrete controllers can override this method and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Query\setDefaultOrder() when a resource should always use a stable sort
unless the client provides one. The default remains null so existing
controllers keep Phalcon's natural model ordering.

***
### initializeOrder

Parse the request `order` parameter into model-qualified expressions.

```php
public initializeOrder(): void
```

Accepted request forms:
- `?order=title desc,createdAt asc`
- `order[title]=desc`
- `order[]=title desc`
- `order[][0]=title&order[][1]=desc`

Direction handling is intentionally small and deterministic: only `desc`
is treated as descending, every other value falls back to ascending. When
an order-field policy is configured, the public field name must resolve
through that policy before it is formatted for PHQL.

**Throws:**

When the root value, an element shape, or a
restricted field is invalid for REST query ordering.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### setOrder

Replace the parsed order collection for the query.

```php
public setOrder(array|\Phalcon\Support\Collection|null $order): void
```

Values are compiled later by

- **See:** \PhalconKit\Mvc\Controller\Traits\Query::prepareFind().
Use null when no ORDER BY clause should be sent to Phalcon.

**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$order`  | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getOrder

Return the parsed order collection, or null when no ordering is active.

```php
public getOrder(): ?\Phalcon\Support\Collection
```

Keys are public REST field names. Values are PHQL-ready field expressions
with normalized direction suffixes.

***
### setDefaultOrder

Replace the default order used when the request has no `order` parameter.

```php
public setDefaultOrder(array|string|null $defaultOrder): void
```

The value accepts the same shapes as the public `order` parameter so
controller-owned defaults and request-supplied order definitions compile
through the same path.

**Parameters:**

| Parameter       | Type                    | Description |
|-----------------|-------------------------|-------------|
| `$defaultOrder` | **array\|string\|null** |             |

***
### getDefaultOrder

Return the default order definition for the current request.

```php
public getDefaultOrder(): array|string|null
```

A null return value means no default order will be applied.

***
### resolveOrderField

Resolve a public order field to the query field used in PHQL.

```php
protected resolveOrderField(string $field): string
```

Null order fields preserve legacy unrestricted ordering. Once a policy is
configured, only public names in the normalized field map are accepted.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

**Throws:**

When the field is not enabled by the configured
order-field policy.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### getSide

Normalize the requested order direction.

```php
protected getSide(string $side): string
```

REST ordering accepts only one explicit descending token. Unknown,
omitted, or empty values intentionally fall back to ascending so malformed
directions do not become SQL fragments.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$side`   | **string** |             |

***
