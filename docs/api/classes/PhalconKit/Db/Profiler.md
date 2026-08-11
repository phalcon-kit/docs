
Database profiler with null-safe profile access and array diagnostics.

Phalcon's profiler can throw type errors when no profile data has been
collected in some runtime states. This wrapper normalizes those cases to
empty profile lists and zero elapsed time so debug endpoints can inspect the
profiler without defensive try/catch blocks.

***

* Full name: `\PhalconKit\Db\Profiler`
* Parent class: [`Profiler`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### getProfiles

Return collected query profiles or an empty list when none are available.

```php
public getProfiles(): array<int,\Phalcon\Db\Profiler\Item>
```

***

### getTotalElapsedNanoseconds

Return total elapsed profile time in nanoseconds.

```php
public getTotalElapsedNanoseconds(): float
```

***

### getTotalElapsedSeconds

Return total elapsed profile time as reported by Phalcon.

```php
public getTotalElapsedSeconds(): float
```

***

### toArray

Export profiler data for debug responses.

```php
public toArray(): array{profiles: array<int,array<string,mixed>>, numberTotalStatements: int, totalElapsedSeconds: float}
```

***
