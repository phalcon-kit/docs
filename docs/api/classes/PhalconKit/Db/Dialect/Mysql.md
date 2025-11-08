
Class MySQL

Mysql class extends \Phalcon\Db\Dialect\Mysql to provide additional functionalities for MySQL database dialect.
- Regexp: " %%s REGEXP $s"
- Distance: " ST_Distance_Sphere(%%s, %%s) "
- point: " point(%%s, %%s) "

***

* Full name: `\PhalconKit\Db\Dialect\Mysql`
* Parent class: [`Mysql`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

```php
public __construct(): mixed
```

***

### registerRegexpFunction

Register a custom REGEXP function for the database dialect.

```php
public registerRegexpFunction(): void
```

***

### registerDistanceSphereFunction

Register a custom distance sphere function to be used in SQL queries.

```php
public registerDistanceSphereFunction(): void
```

This method registers the "ST_Distance_Sphere" function, which calculates the spherical distance between two points.

***

### registerPointFunction

Register a point function for SQL dialect.

```php
public registerPointFunction(): void
```

***

### getColumnDefinition

Get the SQL column definition for a given column.

```php
public getColumnDefinition(\Phalcon\Db\ColumnInterface $column): string
```

This is a temporary fix in regard to this github issue:
- https://github.com/phalcon/cphalcon/issues/16532

**Parameters:**

| Parameter | Type                            | Description                           |
|-----------|---------------------------------|---------------------------------------|
| `$column` | **\Phalcon\Db\ColumnInterface** | The column to get the definition for. |

**Return Value:**

The SQL column definition.

***
