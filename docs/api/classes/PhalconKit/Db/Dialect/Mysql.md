
MySQL dialect with PhalconKit query helpers.

The dialect registers custom PHQL functions that are commonly used by the
framework query builders:

- `regexp(left, right)` renders `left REGEXP right`
- `ST_Distance_Sphere(left, right)` renders MySQL spherical distance SQL
- `point(left, right)` renders a MySQL point expression

It also keeps a compatibility fallback for binary column definitions affected
by upstream Phalcon behavior.

***

* Full name: `\PhalconKit\Db\Dialect\Mysql`
* Parent class: [`Mysql`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

Register PhalconKit custom SQL functions on construction.

```php
public __construct(): mixed
```

***

### registerRegexpFunction

Register the PHQL `regexp()` helper for MySQL `REGEXP` comparisons.

```php
public registerRegexpFunction(): void
```

***

### registerDistanceSphereFunction

Register the PHQL `ST_Distance_Sphere()` helper for geospatial queries.

```php
public registerDistanceSphereFunction(): void
```

The SQL function expects two point expressions and returns the spherical
distance in meters on supported MySQL/MariaDB versions.

***

### registerPointFunction

Register the PHQL `point()` helper for MySQL point expressions.

```php
public registerPointFunction(): void
```

***

### getColumnDefinition

Return a SQL column definition with a binary-type compatibility fallback.

```php
public getColumnDefinition(\Phalcon\Db\ColumnInterface $column): string
```

Phalcon can throw while rendering binary and varbinary columns in versions
affected by upstream issue https://github.com/phalcon/cphalcon/issues/16532.
For every other column type the native implementation remains authoritative.

**Parameters:**

| Parameter | Type                            | Description                |
|-----------|---------------------------------|----------------------------|
| `$column` | **\Phalcon\Db\ColumnInterface** | Column metadata to render. |

**Return Value:**

SQL fragment for the column type and size.

***
