# AuditEvent

```php
namespace PhalconKit\Models\Enums;

enum AuditEvent: string
```

## Cases

| Case | Value |
| --- | --- |
| `CREATE` | <code>&quot;create&quot;</code> |
| `UPDATE` | <code>&quot;update&quot;</code> |
| `DELETE` | <code>&quot;delete&quot;</code> |
| `RESTORE` | <code>&quot;restore&quot;</code> |
| `OTHER` | <code>&quot;other&quot;</code> |

Use [`cases()`](https://www.php.net/manual/en/unitenum.cases.php) to list cases.
Use [`from()`](https://www.php.net/manual/en/backedenum.from.php) or
[`tryFrom()`](https://www.php.net/manual/en/backedenum.tryfrom.php) to resolve a backing value.
