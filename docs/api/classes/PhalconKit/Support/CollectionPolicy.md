
Merge/intersection helpers for nullable collection policy sets.

Several controller query policies use `null` to mean "unrestricted" and an
empty collection to mean "explicitly empty". These helpers preserve that
distinction when feature, role, and controller policies are combined.

***

* Full name: `\PhalconKit\Support\CollectionPolicy`
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Methods

### normalize

Normalize REST/query policy input to the framework's internal collection.

```php
public static normalize(array<array-key,mixed>|\Phalcon\Support\Collection $value): \Phalcon\Support\Collection
```

Public REST controllers may accept plain arrays for ergonomic
initialization, but internal query compilation still works with
`Collection` instances so null, empty, list, map, and enabled-map
policies keep one consistent shape after assignment.

* This method is **static**.
**Parameters:**

| Parameter | Type                                                    | Description                                                          |
|-----------|---------------------------------------------------------|----------------------------------------------------------------------|
| `$value`  | **array<array-key,mixed>\|\Phalcon\Support\Collection** | Raw policy array or an
existing collection supplied by a controller. |

**Return Value:**

Collection value ready for storage or merging.

***

### normalizeNullable

Normalize nullable REST/query policy input.

```php
public static normalizeNullable(array<array-key,mixed>|\Phalcon\Support\Collection|null $value): \Phalcon\Support\Collection|null
```

Null is intentionally preserved because REST policies use it as a
distinct state from an explicit empty collection. For example, null may
mean unrestricted filtering while an empty collection means filtering is
configured but closed.

* This method is **static**.
**Parameters:**

| Parameter | Type                                                          | Description                                        |
|-----------|---------------------------------------------------------------|----------------------------------------------------|
| `$value`  | **array<array-key,mixed>\|\Phalcon\Support\Collection\|null** | Raw policy input or
null to keep the policy unset. |

**Return Value:**

Normalized collection or null.

***

### isEnabledValue

Interpret a collection map value as an enabled/disabled flag.

```php
public static isEnabledValue(mixed $value): bool
```

Several public REST policies accept "enabled map" syntax where the array
key is the field or relation name and the value decides whether that key
is active, for example `['totalCount' => true]` or values coming from a
query string such as `['totalCount' => '1']`.

Use this helper only when the value is meant to be a boolean-like flag.
Do not use it for policy maps where string values are aliases or query
field names, such as `['ownerEmail' => 'Owner.email']`.

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description                                                                  |
|-----------|-----------|------------------------------------------------------------------------------|
| `$value`  | **mixed** | Raw collection value from PHP config, merged config,
request maps, or tests. |

**Return Value:**

True when the map entry should be considered enabled.

***

### mergeNullable

Merge an incoming constrained collection into an optional base policy.

```php
public static mergeNullable(?\Phalcon\Support\Collection $base, \Phalcon\Support\Collection $incoming): \Phalcon\Support\Collection
```

`null` means the base policy is unrestricted, so the incoming policy
becomes the first real constraint. An empty incoming collection leaves an
existing constrained base unchanged.

* This method is **static**.
**Parameters:**

| Parameter   | Type                             | Description |
|-------------|----------------------------------|-------------|
| `$base`     | **?\Phalcon\Support\Collection** |             |
| `$incoming` | **\Phalcon\Support\Collection**  |             |

***

### intersectNullable

Intersect an incoming collection with an optional base policy.

```php
public static intersectNullable(?\Phalcon\Support\Collection $base, \Phalcon\Support\Collection $incoming): \Phalcon\Support\Collection
```

`null` means unrestricted, so the incoming collection is returned as the
first real constraint. Non-null bases are intersected with incoming
values and returned as a new collection.

* This method is **static**.
**Parameters:**

| Parameter   | Type                             | Description |
|-------------|----------------------------------|-------------|
| `$base`     | **?\Phalcon\Support\Collection** |             |
| `$incoming` | **\Phalcon\Support\Collection**  |             |

***
