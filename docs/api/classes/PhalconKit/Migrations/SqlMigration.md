
Phalcon migration base for application-owned SQL files.

Requires the optional phalcon/migrations package (^3.0.1). Extend this class
and call the SQL helpers from morph(), up(), or down(); the standard runner
still configures the connection and records successful migration versions.

Use one complete SQL statement per file and resolve paths with __DIR__. Files
are executed verbatim, in the supplied order, without splitting SQL or changing
transaction/foreign-key settings. Do not interpolate request data into SQL.
MySQL DDL commits implicitly; supply an appropriate rollback/data recovery plan
in each application migration. The helpers cannot make DDL transactional.

***

* Full name: `\PhalconKit\Migrations\SqlMigration`
* Parent class: [`Migration`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class is an **Abstract class**

## Methods

### executeSqlFile

Read and execute one SQL statement using the runner's active connection.

```php
protected executeSqlFile(string $path): void
```

**Parameters:**

| Parameter | Type       | Description                                                       |
|-----------|------------|-------------------------------------------------------------------|
| `$path`   | **string** | Local SQL file; an absolute path based on __DIR__ is recommended. |

**Throws:**

If the file is missing, unreadable, empty, or execution returns false.
- [`RuntimeException`](../Exception/RuntimeException.md)
If the database rejects the statement.
- [`PDOException`](https://www.php.net/manual/en/class.pdoexception.php){:target="_blank"}

***

### executeSqlFiles

Read every file first, then execute statements in the given order.

```php
protected executeSqlFiles(list<string> $paths): void
```

A missing or empty file prevents the entire batch from starting. A database
error stops subsequent statements; earlier statements may already be committed.
Neither migration history nor database integrity settings are changed here.

**Parameters:**

| Parameter | Type             | Description                                              |
|-----------|------------------|----------------------------------------------------------|
| `$paths`  | **list<string>** | Local SQL files, each containing one complete statement. |

**Throws:**

If any file is missing, unreadable, empty, or execution returns false.
- [`RuntimeException`](../Exception/RuntimeException.md)
If the database rejects a statement.
- [`PDOException`](https://www.php.net/manual/en/class.pdoexception.php){:target="_blank"}

***
