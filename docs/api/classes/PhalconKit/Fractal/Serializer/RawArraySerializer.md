
Fractal serializer that returns payload arrays without a resource envelope.

League Fractal's default array serializers may wrap data under resource keys.
This serializer is used when PhalconKit endpoints need the transformed data
itself as the response body. The resource key is accepted for Fractal
compatibility, but it is intentionally ignored.

This is the default serializer used by PhalconKit REST helpers, so controller
responses remain shaped like the transformed model/item arrays instead of
being wrapped under a `data` or resource-name envelope.

***

* Full name: `\PhalconKit\Fractal\Serializer\RawArraySerializer`
* Parent class: [`ArraySerializer`](https://fractal.thephpleague.com/){:target="_blank"}

**See Also:**

* https://fractal.thephpleague.com/serializers/

## Methods

### collection

Return collection data exactly as transformed by Fractal.

```php
public collection(string|null $resourceKey, array<int|string,mixed> $data): array<int|string,mixed>
```

The collection resource key is ignored on purpose. Use a different
serializer when an API contract requires collection envelopes,
pagination wrappers, or top-level metadata.

**Parameters:**

| Parameter      | Type                         | Description                                           |
|----------------|------------------------------|-------------------------------------------------------|
| `$resourceKey` | **string\|null**             | Fractal resource key, ignored by this raw
serializer. |
| `$data`        | **array<int\|string,mixed>** | Transformed collection payload.                       |

**Return Value:**

Unwrapped collection payload.

***

### item

Return item data exactly as transformed by Fractal.

```php
public item(string|null $resourceKey, array<array-key,mixed> $data): array<array-key,mixed>
```

The item resource key is ignored on purpose so single-record responses
keep the same top-level fields emitted by their transformer.

**Parameters:**

| Parameter      | Type                       | Description                                           |
|----------------|----------------------------|-------------------------------------------------------|
| `$resourceKey` | **string\|null**           | Fractal resource key, ignored by this raw
serializer. |
| `$data`        | **array<array-key,mixed>** | Transformed item payload.                             |

**Return Value:**

Unwrapped item payload.

***

### null

Serialize null resources as an empty array.

```php
public null(): ?array
```

This keeps API responses shape-stable for callers that expect JSON
objects or arrays instead of literal null bodies.

Fractal allows serializers to choose the representation of null
resources. PhalconKit chooses `[]` here to match the raw-array response
style used by collection and item resources.

***
