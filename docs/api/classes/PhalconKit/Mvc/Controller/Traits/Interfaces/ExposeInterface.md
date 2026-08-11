
Contract for controller payload exposure helpers.

Exposure rules are passed to the shared exposer so REST actions can return
stable public arrays without leaking protected or internal fields.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ExposeInterface`

## Methods

### expose

Expose one item according to an optional rule map.

```php
public expose(mixed $item, array<string|int,mixed>|null $expose = null): array<string,mixed>
```

**Parameters:**

| Parameter | Type                               | Description               |
|-----------|------------------------------------|---------------------------|
| `$item`   | **mixed**                          | Item to expose.           |
| `$expose` | **array<string\|int,mixed>\|null** | Exposure rule definition. |

***

### listExpose

Expose each item in a list response.

```php
public listExpose(iterable<array-key,mixed> $items, array<string|int,mixed>|null $expose = null): array<int|string,mixed>
```

**Parameters:**

| Parameter | Type                               | Description          |
|-----------|------------------------------------|----------------------|
| `$items`  | **iterable<array-key,mixed>**      | Items to expose.     |
| `$expose` | **array<string\|int,mixed>\|null** | List exposure rules. |

***

### exportExpose

Expose each item in an export response.

```php
public exportExpose(iterable<array-key,mixed> $items, array<string|int,mixed>|null $expose = null): array<int|string,mixed>
```

**Parameters:**

| Parameter | Type                               | Description            |
|-----------|------------------------------------|------------------------|
| `$items`  | **iterable<array-key,mixed>**      | Items to expose.       |
| `$expose` | **array<string\|int,mixed>\|null** | Export exposure rules. |

***
