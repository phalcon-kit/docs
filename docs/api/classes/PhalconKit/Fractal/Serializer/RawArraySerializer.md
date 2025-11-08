
Class RawArraySerializer

This class is responsible for serializing data in the form of arrays.
It extends the ArraySerializer class and provides methods for serializing
collections, items, and null values.

***

* Full name: `\PhalconKit\Fractal\Serializer\RawArraySerializer`
* Parent class: [`ArraySerializer`](https://fractal.thephpleague.com/){:target="_blank"}

## Methods

### collection

{@inheritDoc}

```php
public collection(?string $resourceKey, array $data): array
```

**Parameters:**

| Parameter      | Type        | Description |
|----------------|-------------|-------------|
| `$resourceKey` | **?string** |             |
| `$data`        | **array**   |             |

***

### item

{@inheritDoc}

```php
public item(?string $resourceKey, array $data): array
```

**Parameters:**

| Parameter      | Type        | Description |
|----------------|-------------|-------------|
| `$resourceKey` | **?string** |             |
| `$data`        | **array**   |             |

***

### null

{@inheritDoc}

```php
public null(): ?array
```

***
