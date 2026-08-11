
Deterministic exposure engine built on top of a mutable Builder.

The exposer converts objects/arrays into public payloads according to a
flattened rule map. It is used by models and response helpers that need
consistent allow/deny behavior for nested values without tying that behavior
to one model class or serializer.

Design goals (all preserved):
- Deny-by-default or allow-by-default behavior controlled explicitly by rules.
- Support deep dot-path rules (flattened internally).
- Support anonymous functions (closures) as dynamic callbacks.
- Support value transformation via string formatters.
- Support parent inheritance and child-activation semantics.
- Support protected fields (underscore-prefixed) opt-out.

Core rule types:
- bool
  - true  → expose
  - false → hide

- string
  - Expose and transform value using mb_vsprintf()

- callable(Builder $builder)
  - Return BuilderInterface → caller mutates builder directly
  - Return string           → formatter
  - Return bool             → expose toggle
  - Return iterable         → additional column rules (merged)

- iterable
  - Nested column definitions (flattened recursively)

Root behavior:
- A boolean at index 0 (e.g. `[false, 'id', 'email']`)
  is treated as a rule on the ROOT path (`''`).
- This enables strict deny-by-default semantics with explicit allow-lists.

***

* Full name: `\PhalconKit\Support\Exposer\Exposer`

## Methods

### createBuilder

Create and initialize a Builder for an exposure run.

```php
public static createBuilder(mixed $object, array<string|int,mixed>|null $columns = null, bool|null $expose = null, bool|null $protected = null): \PhalconKit\Support\Exposer\Builder
```

Column definitions are parsed into the flattened rule map consumed by the
traversal engine. `$expose` controls the default visibility when no
matching rule exists, and `$protected` controls whether underscore-prefixed
keys may be returned.

* This method is **static**.
**Parameters:**

| Parameter    | Type                               | Description                                        |
|--------------|------------------------------------|----------------------------------------------------|
| `$object`    | **mixed**                          | Root object, array, scalar, or iterable to expose. |
| `$columns`   | **array<string\|int,mixed>\|null** | Exposure rule definition.                          |
| `$expose`    | **bool\|null**                     | Default visibility. Null uses allow-by-default.    |
| `$protected` | **bool\|null**                     | Whether underscore-prefixed keys are allowed.      |

**Return Value:**

Initialized mutable traversal state.

***

### formatValue

Apply string formatting to a value.

```php
private static formatValue(string $format, mixed $value): string
```

String rules use `mb_vsprintf()` with the current value as the only
argument. This keeps formatter rules compact while still supporting
multibyte-safe formatting.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$format` | **string** |             |
| `$value`  | **mixed**  |             |

***

### checkExpose

Determine whether the current builder node should be exposed.

```php
private static checkExpose(\PhalconKit\Support\Exposer\Builder $builder): void
```

Resolution order:
1. Exact rule match (including root: '')
2. Nearest parent rule
3. Child-activation (a deeper rule === true)
4. Protected-field enforcement

* This method is **static**.
**Parameters:**

| Parameter  | Type                                    | Description                                                                                               |
|------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `$builder` | **\PhalconKit\Support\Exposer\Builder** | Current traversal state. The method mutates the
builder's expose flag, value, and column rules as needed. |

***

### applyRule

Apply a single rule to the builder.

```php
private static applyRule(\PhalconKit\Support\Exposer\Builder $builder, mixed $rule, string $ruleKey, mixed $currentValue, bool $isParentRule = false): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type                                    | Description                                                                                          |
|-----------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|
| `$builder`      | **\PhalconKit\Support\Exposer\Builder** | Current traversal state.                                                                             |
| `$rule`         | **mixed**                               | Rule value resolved from the flattened column map.                                                   |
| `$ruleKey`      | **string**                              | Dot-path key that supplied the rule.                                                                 |
| `$currentValue` | **mixed**                               | Current value before the rule is applied.                                                            |
| `$isParentRule` | **bool**                                | Whether this rule was inherited from a parent
path instead of matching the current full key exactly. |

***

### expose

Expose a value graph according to builder state.

```php
public static expose(\PhalconKit\Support\Exposer\Builder $builder): mixed
```

Objects with `toArray()` are converted through that method before
traversal; other objects are cast to arrays. The same builder instance is
reused through recursion, so the method restores context after each
nested traversal before returning.

* This method is **static**.
**Parameters:**

| Parameter  | Type                                    | Description                                                                                                    |
|------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `$builder` | **\PhalconKit\Support\Exposer\Builder** | Prepared builder from {@see \PhalconKit\Support\Exposer\createBuilder()} or a
compatible custom builder state. |

**Return Value:**

Public value, nested array, or null when the current scalar
is hidden.

***

### parseColumnsRecursive

Parse column definitions into a flattened dot-path rule map.

```php
public static parseColumnsRecursive(iterable<string|int|bool,mixed>|null $columns = null, string|null $context = null): array<string,mixed>|null
```

Root semantics:
- A boolean without a key becomes a rule on the root path ('').
- Root context never produces ".field" keys.

* This method is **static**.
**Parameters:**

| Parameter  | Type                                        | Description                                                          |
|------------|---------------------------------------------|----------------------------------------------------------------------|
| `$columns` | **iterable<string\|int\|bool,mixed>\|null** | Nested column/rule
definition, or null to keep expose defaults only. |
| `$context` | **string\|null**                            | Current recursion path.                                              |

**Return Value:**

Flattened rule map, or null when no
column definition was provided.

***
