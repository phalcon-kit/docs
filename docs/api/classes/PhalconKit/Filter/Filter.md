
Phalcon filter service with PhalconKit sanitizers registered by default.

The service keeps Phalcon's native filter behavior and adds named sanitizers
for md5-style lowercase hexadecimal tokens, JSON strings, and IP address
normalization. Consumers can use the declared magic methods through Phalcon's
filter API, or request the named filters directly through
`sanitize($value, [Filter::FILTER_JSON])`.

Invalid values follow the sanitizer contract for their data type: JSON keeps
`null` as `null`, invalid JSON becomes `null`, and invalid IP addresses become
an empty string so form/request sanitization can collapse them to "no value".

***

* Full name: `\PhalconKit\Filter\Filter`
* Parent class: [`Filter`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/latest/filter/

## Constants

| Constant      | Visibility | Type   | Value  |
|---------------|------------|--------|--------|
| `FILTER_MD5`  | public     | string | 'md5'  |
| `FILTER_JSON` | public     | string | 'json' |
| `FILTER_IPV4` | public     | string | 'ipv4' |
| `FILTER_IPV6` | public     | string | 'ipv6' |

## Methods

### init

Register PhalconKit sanitizers after Phalcon initializes its mapper.

```php
protected init(array<string,string> $mapper): void
```

Phalcon passes its service mapper during construction. Calling the parent
first preserves native filters, then the framework aliases are layered on
top so the DI `filter` service and standalone `FilterFactory` instances
expose the same custom sanitizers.

**Parameters:**

| Parameter | Type                     | Description                     |
|-----------|--------------------------|---------------------------------|
| `$mapper` | **array<string,string>** | Existing Phalcon filter mapper. |

***
