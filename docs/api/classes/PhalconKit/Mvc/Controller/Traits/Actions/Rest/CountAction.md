
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\CountAction`

## Constants

| Constant                       | Visibility | Type   | Value          |
|--------------------------------|------------|--------|----------------|
| `COUNT_ACTION_COUNT_PARAMETER` | public     | string | 'count'        |
| `COUNT_RESPONSE_GROUPED_COUNT` | public     | string | 'groupedCount' |
| `COUNT_RESPONSE_BUCKET_TOTAL`  | public     | string | 'bucketTotal'  |
| `COUNT_RESPONSE_TOTAL_COUNT`   | public     | string | 'totalCount'   |

## Properties

### countActionResponseFields

Opt-in extra response fields added by {@see countAction()}.

```php
protected ?\Phalcon\Support\Collection $countActionResponseFields
```

***

## Methods

### countAction

Return the count for the current REST query.

```php
public countAction(): \Phalcon\Http\ResponseInterface
```

The response variable is named `count`. When the underlying query uses a
group clause, native Phalcon may return grouped count rows instead of a
scalar total; callers should treat this action as a thin REST wrapper
around the controller query contract.

***
### initializeCountActionResponseFields

Initialize extra count response fields during the REST controller setup.

```php
public initializeCountActionResponseFields(): void
```

The default keeps the public `count` response unchanged. Concrete
controllers can override this initializer and call


- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\setCountActionResponseFields() or

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\mergeCountActionResponseFields() with the `COUNT_RESPONSE_*`
constants when they need dashboard/facet metadata.

***
### setCountActionResponseFields

Replace the extra response fields emitted by {@see countAction()}.

```php
public setCountActionResponseFields(array|\Phalcon\Support\Collection|null $countActionResponseFields): void
```

Passing null means no extra fields, preserving the legacy count response.

**Parameters:**

| Parameter                    | Type                                         | Description |
|------------------------------|----------------------------------------------|-------------|
| `$countActionResponseFields` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getCountActionResponseFields

Return the configured extra count response fields.

```php
public getCountActionResponseFields(): ?\Phalcon\Support\Collection
```

***
### hasCountActionResponseFields

Check whether the controller has opted into extra count response fields.

```php
public hasCountActionResponseFields(): bool
```

***
### mergeCountActionResponseFields

Merge extra count response fields with the current field collection.

```php
public mergeCountActionResponseFields(array|\Phalcon\Support\Collection $countActionResponseFields): void
```

**Parameters:**

| Parameter                    | Type                                   | Description                                                                           |
|------------------------------|----------------------------------------|---------------------------------------------------------------------------------------|
| `$countActionResponseFields` | **array\|\Phalcon\Support\Collection** | array or Collection containing field
names, usually the `COUNT_RESPONSE_*` constants. |

***
### setCountActionResponseFieldValues

Add opt-in grouped-count fields to the response view.

```php
protected setCountActionResponseFieldValues(\Phalcon\Mvc\Model\ResultsetInterface|int|false $count): void
```

`groupedCount` is the raw result returned by the normal count query,
`bucketTotal` is only the sum of those returned buckets, and `totalCount`
runs a second count query with the group clause removed. Keeping these as
separate names prevents bucket totals from being mistaken for unique root
record totals on joined/grouped endpoints.

**Parameters:**

| Parameter | Type                                                  | Description |
|-----------|-------------------------------------------------------|-------------|
| `$count`  | **\Phalcon\Mvc\Model\ResultsetInterface\|int\|false** |             |

**Throws:**

When the client requests an unsupported or
disallowed count field.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### getCountActionResponseFieldNames

Normalize the enabled extra count response field names.

```php
protected getCountActionResponseFieldNames(): list<string>
```

Collections can be configured either as value lists, for example
`[self::COUNT_RESPONSE_TOTAL_COUNT]`, or as enabled maps, for example
`[self::COUNT_RESPONSE_TOTAL_COUNT => true]`. Enabled-map values are
interpreted with

- **See:** \PhalconKit\Support\CollectionPolicy::isEnabledValue(), so config
values such as `1`, `'1'`, and `'yes'` enable the key while `0`, `'0'`,
`'false'`, `'no'`, and `'off'` disable it.

***
### getCountActionSelectedResponseFieldNames

Return the configured and requested extra count response fields.

```php
protected getCountActionSelectedResponseFieldNames(): list<string>
```

The native `count` field is always emitted by

- **See:** \PhalconKit\Mvc\Controller\Traits\Actions\Rest\countAction(), so
client requests for `count` are valid but do not add another response
field. Requests for optional metadata are checked against the configured
policy. A null policy is unrestricted across supported count fields,
while an empty collection blocks every optional requested field.

**Throws:**

When the client requests a disallowed count field.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### getCountActionAllowedResponseFieldNames

Return count fields accepted by the current count-action policy.

```php
protected getCountActionAllowedResponseFieldNames(): list<string>
```

***
### getCountActionSupportedResponseFieldNames

Return the built-in count response field names that can be requested.

```php
protected getCountActionSupportedResponseFieldNames(): list<string>
```

***
### getCountActionRequestedResponseFieldNames

Return count response fields requested through the `count` parameter.

```php
protected getCountActionRequestedResponseFieldNames(): list<string>
```

Supported request shapes:
- `?count=1` or `?count=true` requests the native `count` field.
- `?count=count,totalCount` requests named fields.
- `?count[]=count&count[]=totalCount` requests named fields as a list.
- `?count[totalCount]=1` requests named fields as an enabled map.

**Throws:**

When the parameter has an unsupported type.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### normalizeCountActionRequestedCountFields

Normalize a client `count` request value to field names.

```php
protected normalizeCountActionRequestedCountFields(mixed $requested): list<string>
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$requested` | **mixed** |             |

**Throws:**

When the parameter has an unsupported type.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### normalizeCountActionRequestedCountString

Normalize a scalar `count` request value.

```php
protected normalizeCountActionRequestedCountString(string $requested): list<string>
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$requested` | **string** |             |

***
### isCountActionCountEnabledValue

Check whether an enabled-map `count[field]` value should request a field.

```php
protected isCountActionCountEnabledValue(mixed $value): bool
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***
### isCountActionCountTruthyString

Check whether a scalar string requests the default native count field.

```php
protected isCountActionCountTruthyString(string $value): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$value`  | **string** |             |

***
### normalizeCountActionCountFieldList

Trim, de-duplicate, and drop empty count field names.

```php
protected normalizeCountActionCountFieldList(array<int,mixed> $fields): list<string>
```

**Parameters:**

| Parameter | Type                 | Description          |
|-----------|----------------------|----------------------|
| `$fields` | **array<int,mixed>** | Raw field fragments. |

***
### getCountActionTotalFind

Build the ungrouped count query used by `totalCount`.

```php
protected getCountActionTotalFind(): array<string|int,mixed>
```

The query keeps the same filters, joins, permissions, binds, and bind
types as the normal count query, but removes the group clause so Phalcon
returns an ungrouped total. Controllers with custom aggregate columns can
override this method if their total query needs a different column.

***
### getCountActionBucketTotal

Sum the row-count buckets returned by a grouped count query.

```php
protected getCountActionBucketTotal(\Phalcon\Mvc\Model\ResultsetInterface|int|false $count): int|float|false
```

This value is deliberately named `bucketTotal`, not `total`, because
joined grouped counts can count the same root record in several buckets.
If a row does not expose a recognizable numeric count column, the method
returns false instead of guessing.

**Parameters:**

| Parameter | Type                                                  | Description |
|-----------|-------------------------------------------------------|-------------|
| `$count`  | **\Phalcon\Mvc\Model\ResultsetInterface\|int\|false** |             |

***
### getCountActionBucketValue

Read one numeric count value from a grouped count row.

```php
protected getCountActionBucketValue(mixed $row): int|float|null
```

Phalcon commonly exposes grouped `count()` values as `rowcount`, but
hydration mode and custom columns can produce arrays with another count
key. Known count keys are preferred; a one-column numeric row is accepted
as a fallback for custom result rows. Multi-column rows without a known
count key are rejected so numeric group keys are not accidentally summed.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$row`    | **mixed** |             |

***
### normalizeCountActionBucketNumber

Normalize one grouped count bucket value.

```php
protected normalizeCountActionBucketNumber(mixed $value): int|float|null
```

Numeric strings are common when database drivers hydrate aggregate
columns. Preserve integer-like values as integers and decimal/scientific
values as floats so API payloads stay natural without relying on implicit
arithmetic casts.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***
