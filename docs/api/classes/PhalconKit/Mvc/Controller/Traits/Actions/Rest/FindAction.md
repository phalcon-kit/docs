
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\FindAction`

## Constants

| Constant                      | Visibility | Type   | Value   |
|-------------------------------|------------|--------|---------|
| `FIND_ACTION_COUNT_PARAMETER` | public     | string | 'count' |

## Properties

### findActionCountFields

Controller-owned policy for count fields embeddable in list actions.

```php
protected ?\Phalcon\Support\Collection $findActionCountFields
```

A null policy mirrors the other REST field policies and means clients may
request any supported framework count field. A non-null collection turns
on explicit allow-list mode, where an empty collection blocks every
embedded list-count field.

***

## Methods

### getAllAction

Legacy alias for `findAction()`.

```php
public getAllAction(): \Phalcon\Http\ResponseInterface
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
***
### getAllWithAction

Legacy alias for `findWithAction()`.

```php
public getAllWithAction(): \Phalcon\Http\ResponseInterface
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
***
### findAction

Find and expose records matching the prepared REST query.

```php
public findAction(): \Phalcon\Http\ResponseInterface
```

The `data` response variable receives the exposed result list. Query
preparation is delegated to the shared query trait, so filters, fields,
permissions, identity constraints, ordering, limits, and joins stay
consistent across REST list endpoints.

***
### findWithAction

Find records with eager-loaded relationships and expose the result list.

```php
public findWithAction(): \Phalcon\Http\ResponseInterface
```

When the client does not send the `with` parameter, relationships are
resolved from the controller's configured eager-load graph. When the
client sends `with`, only the requested, controller-approved subset is
loaded. The exposed response shape remains the same as `findAction()`,
with related data included where the eager-load graph permits it.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When a requested relationship is not allowed.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### initializeFindActionCountFields

Initialize list-action count metadata policy.

```php
public initializeFindActionCountFields(): void
```

The default is null, which preserves normal list payloads until a client
asks for count metadata through

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\FIND_ACTION_COUNT_PARAMETER. When
requested, null allows any supported framework count field, matching the
unrestricted behavior used by other REST field policies.

***
### setFindActionCountFields

Replace the count fields that list actions may embed.

```php
public setFindActionCountFields(array|\Phalcon\Support\Collection|null $findActionCountFields): void
```

Supported field names are:
- `count`: the native count query result, matching

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\countAction().
- `groupedCount`: the raw grouped count result.
- `bucketTotal`: the sum of recognized grouped count buckets.
- `totalCount`: a separate ungrouped count query.

Passing null leaves the policy unrestricted for supported framework count
fields. Passing an empty collection enables allow-list mode but allows no
embedded list counts, which is useful for controllers that must reject
every client-requested list count.

**Parameters:**

| Parameter                | Type                                         | Description |
|--------------------------|----------------------------------------------|-------------|
| `$findActionCountFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getFindActionCountFields

Return the configured list-action count field policy.

```php
public getFindActionCountFields(): ?\Phalcon\Support\Collection
```

A null return value means unrestricted supported count fields. A non-null
collection is normalized by

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\getFindActionCountFieldNames() before
request fields are accepted.

***
### hasFindActionCountFields

Check whether list-action count allow-list mode is configured.

```php
public hasFindActionCountFields(): bool
```

This reports policy presence, not whether counts are available. A false
result means the policy is unrestricted for supported count fields, while
an empty non-null collection means every requested count field is denied.

***
### mergeFindActionCountFields

Merge additional list-action count fields with the current policy.

```php
public mergeFindActionCountFields(array|\Phalcon\Support\Collection $findActionCountFields): void
```

The collection accepts the same value-list and enabled-map shapes as
count action response fields, for example `[self::REST_VIEW_COUNT]` or
`[self::COUNT_RESPONSE_TOTAL_COUNT => true]`. Merging into a null policy
creates the first explicit allow-list; it does not need a separate setter
call in controller initialization.

**Parameters:**

| Parameter                | Type                                   | Description |
|--------------------------|----------------------------------------|-------------|
| `$findActionCountFields` | **array\|\Phalcon\Support\Collection** |             |

***
### setFindActionCountFieldValues

Add requested, allowed count metadata to the list response view.

```php
protected setFindActionCountFieldValues(): void
```

Normal `count`, `groupedCount`, and `bucketTotal` use the standard count
query, which honors filters/search/joins/permissions and removes
pagination through the shared query helper. `totalCount` runs the
ungrouped count query used by

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\countAction().

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the client requests an unsupported or
disallowed count field.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### getFindActionRequestedCountFieldNames

Return the requested count fields accepted by the current policy.

```php
protected getFindActionRequestedCountFieldNames(): list<string>
```

A null policy is intentionally unrestricted across supported framework
count fields, so clients can opt in to list counts without every
controller declaring boilerplate. Non-null policies restrict the accepted
names, and unsupported or disallowed requests fail instead of silently
doing surprising work.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the client requests a disallowed count field.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### getFindActionAllowedCountFieldNames

Return the count fields accepted by the current list-action policy.

```php
protected getFindActionAllowedCountFieldNames(): list<string>
```

Null means unrestricted across the finite set of framework-supported
count fields. Non-null policies are normalized through the controller
collection so empty collections and disabled entries can intentionally
deny every requested field.

***
### getFindActionSupportedCountFieldNames

Return the built-in list-count field names that PhalconKit can emit.

```php
protected getFindActionSupportedCountFieldNames(): list<string>
```

This finite set is the boundary for unrestricted mode. It allows
consumers to skip boilerplate policy declarations without turning
arbitrary request strings into dynamic response variables.

***
### getFindActionCountFieldNames

Normalize the controller allow-list to count response field names.

```php
protected getFindActionCountFieldNames(): list<string>
```

Count-field policies do not support public-to-query aliases, so string
keys are treated as enabled-map entries. This keeps PHP config,
environment-derived config, and request-map semantics aligned for count
fields without changing alias-capable policies such as distinct/order
fields.

***
### normalizeFindActionRequestedCountFields

Normalize the client `count` request parameter to field names.

```php
protected normalizeFindActionRequestedCountFields(mixed $requested): list<string>
```

Supported request shapes:
- `?count=1` or `?count=true` requests the native `count` field.
- `?count=count,totalCount` requests named fields.
- `?count[]=count&count[]=totalCount` requests named fields as a list.
- `?count[totalCount]=1` requests named fields as an enabled map.

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$requested` | **mixed** |             |

**Throws:**

When the parameter has an unsupported type.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### normalizeFindActionRequestedCountString

Normalize a scalar `count` request value.

```php
protected normalizeFindActionRequestedCountString(string $requested): list<string>
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$requested` | **string** |             |

***
### isFindActionCountEnabledValue

Check whether an enabled-map `count[field]` value should request a field.

```php
protected isFindActionCountEnabledValue(mixed $value): bool
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***
### isFindActionCountTruthyString

Check whether a scalar string requests the default native count field.

```php
protected isFindActionCountTruthyString(string $value): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$value`  | **string** |             |

***
### normalizeFindActionCountFieldList

Trim, de-duplicate, and drop empty count field names.

```php
protected normalizeFindActionCountFieldList(array<int,mixed> $fields): list<string>
```

**Parameters:**

| Parameter | Type                 | Description          |
|-----------|----------------------|----------------------|
| `$fields` | **array<int,mixed>** | Raw field fragments. |

***
