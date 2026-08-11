
Stores the REST order-field allow-list used by the query order parser.

A null policy preserves the legacy behavior and allows any client-supplied
order field to be normalized by the model query compiler. A non-null
collection enables explicit allow-list mode, where only configured public
field names can be used by the `order` request parameter.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields\OrderFields`

## Properties

### orderFields

Controller-owned order-field policy.

```php
protected ?\Phalcon\Support\Collection $orderFields
```

Supported collection shapes:
- `['status', 'createdAt']` exposes the same public and query fields.
- `['status' => true]` enables a field map entry.
- `['ownerEmail' => 'Owner.email']` exposes a stable public alias that
  orders by a model-qualified or relationship-qualified query field.
- false, null, and empty-string values are ignored so inherited entries
  can be disabled through merge policy.

String values are aliases, not boolean-like flags. For example,
`['legacySort' => 'off']` maps `legacySort` to the query field `off`; it
does not disable the entry.

***

## Methods

### initializeOrderFields

Initialize the order-field allow-list for REST queries.

```php
public initializeOrderFields(): void
```

The default is null for backward compatibility: controllers keep their
existing unrestricted ordering behavior until they opt in by overriding
this method and calling

- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\setOrderFields().

***
### setOrderFields

Replace the fields that clients may use in the `order` parameter.

```php
public setOrderFields(array|\Phalcon\Support\Collection|null $orderFields): void
```

Passing null disables allow-list enforcement and preserves legacy
behavior. Passing an empty collection enables allow-list mode but allows
no fields, which can be useful for controllers that must reject every
client-controlled sort key.

**Parameters:**

| Parameter      | Type                                         | Description                                                                                          |
|----------------|----------------------------------------------|------------------------------------------------------------------------------------------------------|
| `$orderFields` | **array\|\Phalcon\Support\Collection\|null** | Field policy collection, null for
unrestricted ordering, or an empty collection for a closed policy. |

***
### getOrderFields

Return the configured order-field policy.

```php
public getOrderFields(): \Phalcon\Support\Collection|null
```

A null return value means unrestricted ordering. A non-null collection is
normalized by

- **See:** \PhalconKit\Mvc\Controller\Traits\Query\Fields\getOrderFieldMap() before the request `order`
parameter is accepted.

**Return Value:**

Field policy collection or null for unrestricted
ordering.

***
### hasOrderFields

Check whether order-field allow-list mode is configured.

```php
public hasOrderFields(): bool
```

This reports policy presence, not whether the policy currently enables at
least one field. An empty collection still means allow-list mode is active
and every requested order field will be rejected.

***
### mergeOrderFields

Merge additional order-field entries into the current policy.

```php
public mergeOrderFields(array|\Phalcon\Support\Collection $orderFields): void
```

Merge semantics match the other REST field-policy collections: null
starts from the incoming collection, string keys can override previous
entries, and false/null values can disable inherited entries.

**Parameters:**

| Parameter      | Type                                   | Description                      |
|----------------|----------------------------------------|----------------------------------|
| `$orderFields` | **array\|\Phalcon\Support\Collection** | Additional field policy entries. |

***
### getOrderFieldMap

Normalize the configured order policy to public => query field names.

```php
protected getOrderFieldMap(): array<string,string>
```

The public name is what clients send in `order`. The query field is what
the framework passes to

- **See:** \PhalconKit\Mvc\Controller\Traits\Model::appendModelName()
when building the PHQL `ORDER BY` expression.

***
