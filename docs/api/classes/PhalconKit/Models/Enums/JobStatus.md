# JobStatus

```php
namespace PhalconKit\Models\Enums;

enum JobStatus: string
```

## Cases

| Case | Value |
| --- | --- |
| `NEW` | <code>&quot;new&quot;</code> |
| `PROGRESS` | <code>&quot;progress&quot;</code> |
| `FAILED` | <code>&quot;failed&quot;</code> |
| `FINISHED` | <code>&quot;finished&quot;</code> |

Use [`cases()`](https://www.php.net/manual/en/unitenum.cases.php) to list cases.
Use [`from()`](https://www.php.net/manual/en/backedenum.from.php) or
[`tryFrom()`](https://www.php.net/manual/en/backedenum.tryfrom.php) to resolve a backing value.
