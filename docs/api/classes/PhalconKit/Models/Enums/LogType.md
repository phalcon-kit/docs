# LogType

```php
namespace PhalconKit\Models\Enums;

enum LogType: string
```

## Cases

| Case | Value |
| --- | --- |
| `CRITICAL` | <code>&quot;critical&quot;</code> |
| `ALERT` | <code>&quot;alert&quot;</code> |
| `ERROR` | <code>&quot;error&quot;</code> |
| `WARNING` | <code>&quot;warning&quot;</code> |
| `NOTICE` | <code>&quot;notice&quot;</code> |
| `INFO` | <code>&quot;info&quot;</code> |
| `DEBUG` | <code>&quot;debug&quot;</code> |
| `EMERGENCY` | <code>&quot;emergency&quot;</code> |
| `OTHER` | <code>&quot;other&quot;</code> |

Use [`cases()`](https://www.php.net/manual/en/unitenum.cases.php) to list cases.
Use [`from()`](https://www.php.net/manual/en/backedenum.from.php) or
[`tryFrom()`](https://www.php.net/manual/en/backedenum.tryfrom.php) to resolve a backing value.
