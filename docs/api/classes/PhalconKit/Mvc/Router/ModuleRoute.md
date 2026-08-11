
Route group for one MVC module, optionally scoped by hostname and locale.

The group registers the conventional PhalconKit routes for:
- module root
- controller index
- controller/action/params

When locales are provided, it also registers locale-prefixed variants using
both one regex route and concrete per-locale route names. Hostname groups use
host-derived route names so generated routes do not collide with path-based
module routes.

***

* Full name: `\PhalconKit\Mvc\Router\ModuleRoute`
* Parent class: [`Group`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/latest/routing/

## Properties

### locale

Allowed locale prefixes for this module route group.

```php
public list<string> $locale
```

***

## Methods

### __construct

Create a module route group.

```php
public __construct(array<string,mixed>|string|null $paths = null, list<string> $locale = [], string|null $hostname = null): mixed
```

**Parameters:**

| Parameter   | Type                                  | Description                                                                              |
|-------------|---------------------------------------|------------------------------------------------------------------------------------------|
| `$paths`    | **array<string,mixed>\|string\|null** | Native Phalcon route
paths. PhalconKit expects at least `module` in normal module usage. |
| `$locale`   | **list<string>**                      | Locale prefixes to register.                                                             |
| `$hostname` | **string\|null**                      | Optional hostname constraint.                                                            |

***

### initialize

Register default, controller, action, and locale-aware routes.

```php
public initialize(): void
```

The method is called by Phalcon's router group lifecycle after
construction. Route names are deterministic so applications can generate
URLs for either plain module routes or locale/hostname-specific routes.

***
