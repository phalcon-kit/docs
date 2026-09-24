
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\Traits\DatabaseTrait`

## Properties

### drop

```php
public array $drop
```

***
### truncate

```php
public array $truncate
```

***
### engine

```php
public array $engine
```

***
### insert

```php
public array $insert
```

***
### optimize

```php
public array $optimize
```

***
### analyze

```php
public array $analyze
```

***

## Methods

### mainAction

Default action

```php
public mainAction(): ?array
```

***
### resetAction

The resetAction method is responsible for resetting the state of the application by performing
the following actions:

```php
public resetAction(): array
```

1. Truncate database tables using the truncateAction method.
2. Insert initial data into the database using the insertAction method.

Use Case:

This method can be used when you need to reset the state of the application to its initial state.
It is commonly used for testing or when you want to re-populate the database with initial data.

**Throws:**

- [`CliException`](../../../../Exception/CliException.md)

***
### truncateAction

The truncateAction method is responsible for truncating (emptying) database tables specified in the
$this->truncate array. Truncating a table removes all of its data, effectively resetting it to an
empty state. This method iterates through a list of table names and executes an SQL TRUNCATE TABLE
command for each of them.

```php
public truncateAction(): array
```

Use Case:
This method is often used when you need to reset the data in database tables without deleting
the table itself. Truncating tables is a quicker alternative to deleting all rows one by one.

***
### dropAction

Permanently drop every table listed in the configured $drop array.

```php
public dropAction(): array<string,bool>
```

IF EXISTS suppresses errors for absent tables; an existing table and its data
are still removed. Table identifiers are escaped through the shared db service.

**Return Value:**

Execution result keyed by configured table name.

**Throws:**

When the adapter rejects a statement.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the database rejects a statement.
- [`PDOException`](https://www.php.net/manual/en/class.pdoexception.php){:target="_blank"}

***
### fixEngineAction

The fixEngineAction method is responsible for fixing or changing the storage engine for database tables
specified in the $this->engine array. A storage engine determines how data is stored and managed within
a database table. This method iterates through a list of table names and their corresponding desired
storage engines and executes SQL ALTER TABLE commands to make the necessary changes.

```php
public fixEngineAction(): array
```

Use Case:
This method is useful when you need to adjust the storage engine of database tables to optimize performance,
compatibility, or for other specific requirements. Different storage engines have different characteristics,
and choosing the right one can impact table performance and functionality.

***
### insertAction

Insert records

```php
public insertAction(?string $models = null): array
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$models` | **?string** |             |

**Throws:**

- [`CliException`](../../../../Exception/CliException.md)

***
### optimizeAction

The optimizeAction method is responsible for optimizing database tables specified in the
$this->optimize array. Database table optimization is a maintenance task aimed at improving
the performance and storage efficiency of database tables. This method iterates through a
list of table names and executes an SQL OPTIMIZE TABLE command for each of them.

```php
public optimizeAction(): array
```

Use Case:
This method is typically used in the context of database maintenance and optimization routines.
It allows you to automate the process of optimizing database tables, which can help reclaim storage
space and improve query performance by reorganizing table data and indexes.

***
### analyzeAction

This method is responsible for analyzing database tables specified in the $this->analyse array.

```php
public analyzeAction(): array
```

Table analysis is an essential database maintenance task that helps optimize the performance
of database queries. Analyzing a table refreshes statistics and metadata about the table's
structure, which can lead to improved query execution plans.

Use Case:
This method can be used in the context of database optimization and maintenance scripts.
It allows you to automate the process of analyzing database tables, ensuring that the database's
query optimizer has up-to-date statistics to make informed decisions about query execution plans.

***
### addModelsPermissions

```php
public addModelsPermissions(?array $tables = null): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$tables` | **?array** |             |

**Throws:**

When permission configuration cannot be merged.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
