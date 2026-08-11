
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\With`

## Constants

| Constant         | Visibility | Type   | Value  |
|------------------|------------|--------|--------|
| `WITH_PARAMETER` | public     | string | 'with' |

## Properties

### with

Controller-defined eager-load relation paths.

```php
protected ?\Phalcon\Support\Collection $with
```

The collection is used as the default relationship set for `findWith()`
and `findFirstWith()`. It also acts as the request allow-list when a
frontend sends the

- **See:** \PhalconKit\Mvc\Controller\Traits\Query\WITH_PARAMETER parameter to request a subset of
those relationships.

***

## Methods

### initializeWith

Initialize the default eager-load relationship collection.

```php
public initializeWith(): void
```

The default is null, so `findWith()` and `findFirstWith()` load no
relationships unless a concrete controller sets them. Relationship
request parameters are intentionally closed when no default relationship
graph exists, because eager loading can expose extra data and create
expensive query plans.

***
### setWith

Replace the default eager-load relationship collection.

```php
public setWith(array|\Phalcon\Support\Collection|null $with): void
```

Supported collection shapes match the eager-loading loader:
- `['Author', 'Author.Profile']` loads those relation paths by default.
- `['Author' => $callable]` applies a constraint callback to that
  relation when the default eager-load graph is used.
- `['Author' => false]` or `['Author' => 'off']` keeps the key in
  merged configuration but disables the relation, matching other
  REST enabled-map policies.

When a client sends a `with` request parameter, the same collection
becomes the allow-list. A client may request any configured relation path
or a parent path of one, so a configured `Author.Profile.Avatar` allows a
request for `Author.Profile` without also loading `Avatar`.

**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$with`   | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getWith

Return the default eager-load relationship collection.

```php
public getWith(): ?\Phalcon\Support\Collection
```

A null value means the controller has no default eager-load graph and no
frontend-requestable relationship graph. It does not mean arbitrary
relationships are allowed from request parameters.

***
### mergeWith

Merge additional eager-load relation paths into the current collection.

```php
public mergeWith(array|\Phalcon\Support\Collection $with): void
```

Merging into null creates the first default/allowed relationship graph.
This is useful for base controllers that define common relations and
resource controllers that add their own nested paths.

**Parameters:**

| Parameter | Type                                   | Description |
|-----------|----------------------------------------|-------------|
| `$with`   | **array\|\Phalcon\Support\Collection** |             |

***
### getRequestedWith

Resolve the request-provided eager-load subset for `*WithAction()`.

```php
protected getRequestedWith(): array<string|int,mixed>|null
```

A null return value means the frontend did not send the `with` parameter,
so callers should use the controller's configured default relationship
graph. An empty array means the parameter was present but requested no
relationships. Non-empty arrays contain only relationships allowed by the
configured graph.

Nested paths are first-class: a request for `Author.Profile.Avatar` is
passed to the eager loader as one path, and the loader builds the
required parent paths internally. When configured parent paths have
constraint callbacks, they are preserved in the returned subset.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the request shape is invalid or a relation is
not present in the configured relationship graph.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### normalizeRequestedWith

Normalize the public `with` request parameter to relation paths.

```php
protected normalizeRequestedWith(mixed $requested): list<string>
```

Supported request shapes:
- `?with=Author,Author.Profile` for comma-separated paths.
- `?with[]=Author&with[]=Author.Profile` for list-style paths.
- `?with[Author.Profile]=1` for enabled-map syntax.

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$requested` | **mixed** |             |

**Throws:**

When the parameter has an unsupported type.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### filterRequestedWithRelations

Keep only requested relation paths allowed by the configured graph.

```php
protected filterRequestedWithRelations(list<string> $requested): array<string|int,mixed>
```

**Parameters:**

| Parameter    | Type             | Description                               |
|--------------|------------------|-------------------------------------------|
| `$requested` | **list<string>** | Relation paths requested by the frontend. |

**Throws:**

When a requested relation is outside the configured
relationship graph.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### getWithRelationMap

Normalize configured eager-load relationships to relation => constraint.

```php
protected getWithRelationMap(): array<string,callable|null>
```

The returned map intentionally follows the current eager loader contract:
string keys are relation paths, callable values are constraints, and list
values are plain relation paths. Non-callable string-key values use
PhalconKit's enabled-map normalization so merged configuration can disable
a relation with values such as `false`, `0`, `'0'`, or `'off'`.

***
### getDefaultWithRelations

Return the configured eager-load graph in loader-ready form.

```php
protected getDefaultWithRelations(): array<string|int,mixed>
```

`findWith()` and `findFirstWith()` call this when no request-specific
subset is supplied. Normalizing through

- **See:** \PhalconKit\Mvc\Controller\Traits\Query\getWithRelationMap() keeps
default relationship loading aligned with request-time `with[Relation]`
enabled-map behavior, while still preserving callable constraints on the
exact configured relation paths.

***
### isWithRelationAllowed

Determine whether a requested relation is present in the configured graph.

```php
protected isWithRelationAllowed(string $requested, list<string> $allowedRelations): bool
```

A requested relation may be exactly configured or may be a parent of a
configured nested relation. The inverse is not allowed: configuring
`Author` does not permit a frontend to request `Author.Profile`.

**Parameters:**

| Parameter           | Type             | Description |
|---------------------|------------------|-------------|
| `$requested`        | **string**       |             |
| `$allowedRelations` | **list<string>** |             |

***
### isSameOrParentWithRelation

Check whether one configured relation is the same as or parent of another.

```php
protected isSameOrParentWithRelation(string $candidate, string $relation): bool
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$candidate` | **string** |             |
| `$relation`  | **string** |             |

***
### isWithRelationEnabledValue

Check whether an enabled-map `with[Relation]` value should request a path.

```php
protected isWithRelationEnabledValue(mixed $value): bool
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***
### normalizeWithRelationList

Trim, de-duplicate, and validate relation path fragments.

```php
protected normalizeWithRelationList(array<int,mixed> $relations): list<string>
```

**Parameters:**

| Parameter    | Type                 | Description             |
|--------------|----------------------|-------------------------|
| `$relations` | **array<int,mixed>** | Raw relation fragments. |

**Throws:**

When a relation path is not scalar.
- [`HttpException`](../../../../Exception/HttpException.md)

***
### normalizeWithRelationMap

Convert a relation map back to the eager loader's compact argument shape.

```php
protected normalizeWithRelationMap(array<string,callable|null> $relations): array<string|int,mixed>
```

Relations without constraints are returned as list values so the payload
remains equivalent to the existing `['Author', 'Author.Profile']` style.
Constrained relations keep their string key so the loader receives the
callback on the exact configured path.

**Parameters:**

| Parameter    | Type                             | Description |
|--------------|----------------------------------|-------------|
| `$relations` | **array<string,callable\|null>** |             |

***
