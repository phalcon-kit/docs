# JobSchedulerFrequency

```php
namespace PhalconKit\Models\Enums;

enum JobSchedulerFrequency: string
```

## Cases

| Case | Value |
| --- | --- |
| `MANUALLY` | <code>&quot;manually&quot;</code> |
| `MINUTELY` | <code>&quot;minutely&quot;</code> |
| `HOURLY` | <code>&quot;hourly&quot;</code> |
| `DAILY` | <code>&quot;daily&quot;</code> |
| `WEEKDAYS` | <code>&quot;weekdays&quot;</code> |
| `WEEKENDS` | <code>&quot;weekends&quot;</code> |
| `WEEKLY` | <code>&quot;weekly&quot;</code> |
| `BI_WEEKLY` | <code>&quot;bi-weekly&quot;</code> |
| `MONTHLY` | <code>&quot;monthly&quot;</code> |
| `BI_MONTHLY` | <code>&quot;bi-monthly&quot;</code> |
| `QUARTERLY` | <code>&quot;quarterly&quot;</code> |
| `SEMI_ANNUALLY` | <code>&quot;semi-annually&quot;</code> |
| `YEARLY` | <code>&quot;yearly&quot;</code> |

Use [`cases()`](https://www.php.net/manual/en/unitenum.cases.php) to list cases.
Use [`from()`](https://www.php.net/manual/en/backedenum.from.php) or
[`tryFrom()`](https://www.php.net/manual/en/backedenum.tryfrom.php) to resolve a backing value.
