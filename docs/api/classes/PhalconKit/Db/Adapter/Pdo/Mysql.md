
***

* Full name: `\PhalconKit\Db\Adapter\Pdo\Mysql`
* Parent class: [`Mysql`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### executePrepared

Overrides the executePrepared method to rewrite duplicate placeholders.

```php
public executePrepared(\PDOStatement $statement, array $placeholders, array $dataTypes): \PDOStatement
```

**Parameters:**

| Parameter       | Type              | Description                 |
|-----------------|-------------------|-----------------------------|
| `$statement`    | **\PDOStatement** | The original PDO statement. |
| `$placeholders` | **array**         | An array of bind values.    |
| `$dataTypes`    | **array**         | An array of bind types.     |

***

### rewriteQueryPlaceholders

Rewrites an SQL query by replacing duplicate named placeholders with unique ones.

```php
public rewriteQueryPlaceholders(string $sql, array $bind, array $bindTypes): array
```

This function scans the SQL for named placeholders (like :paramName) and for every
duplicate occurrence (beyond the first), it appends a unique suffix (e.g. :paramName_2)
and duplicates the corresponding bind value and type.

It also handles cases where the bind arrays use keys without a leading colon.

**Parameters:**

| Parameter    | Type       | Description             |
|--------------|------------|-------------------------|
| `$sql`       | **string** | The original SQL query. |
| `$bind`      | **array**  | The bind values array.  |
| `$bindTypes` | **array**  | The bind types array.   |

**Return Value:**

An array containing the new SQL, the new bind values, and the new bind types.

***
