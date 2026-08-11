
Provides explicit accessors for configurable framework model classes.

Applications can replace core PhalconKit model classes through the `models`
config map. This trait lets services resolve those classes without magic
methods and keeps all default class names documented in one place. The
generic mapping helpers are intentionally loose because downstream projects
may map core classes to application-specific subclasses.

***

* Full name: `\PhalconKit\Support\ModelsMap`

## Properties

### modelsMap

Store mapped model classes keyed by the original core class name.

```php
public array<string,string> $modelsMap
```

Values are usually class-string values, but the trait does not validate
them here so applications can load partial maps before class autoloading
is fully available.

***

## Methods

### getDI

Return the DI container used to resolve config-backed mappings.

```php
public getDI(): \Phalcon\Di\DiInterface
```

Implemented by `PhalconKit\Di\Injectable` consumers.

* This method is **abstract**.
***
### getConfig

Resolve the bootstrap config used for model class mappings.

```php
public getConfig(): \PhalconKit\Bootstrap\Config
```

The backing DI must be a PhalconKit DI because model mapping is a
framework-level integration point and should fail consistently when a
native-only container is accidentally used.

**Return Value:**

Bootstrap config service.

**Throws:**

When the DI container or config service cannot
be resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***
### setModelsMap

Replace the model mapping or load it from configuration.

```php
public setModelsMap(array<string,string>|null $modelsMap = null): void
```

Passing an explicit array lets tests and service providers avoid a config
lookup. Passing null loads `models` from the bootstrap config service and
stores an empty array when no mapping is configured.

**Parameters:**

| Parameter    | Type                           | Description                                                                          |
|--------------|--------------------------------|--------------------------------------------------------------------------------------|
| `$modelsMap` | **array<string,string>\|null** | Mapping of core class names
to replacement class names, or null to load from config. |

**Throws:**

When the config-backed mapping cannot be loaded.
- [`ServiceException`](../Exception/ServiceException.md)

***
### getModelsMap

Return the currently configured model class map.

```php
public getModelsMap(): array<string,string>
```

**Return Value:**

Mapping of original core class names to the
class names that should be instantiated or referenced.

***
### setClassMap

Add or replace one model class mapping.

```php
public setClassMap(string $map, string $class): void
```

**Parameters:**

| Parameter | Type       | Description                                    |
|-----------|------------|------------------------------------------------|
| `$map`    | **string** | Original core class name or logical map key.   |
| `$class`  | **string** | Replacement class name to return for that key. |

***
### removeClassMap

Remove one model class mapping.

```php
public removeClassMap(string $map): void
```

After removal, `getClassMap()` falls back to returning the requested
class/key unchanged.

**Parameters:**

| Parameter | Type       | Description                                            |
|-----------|------------|--------------------------------------------------------|
| `$map`    | **string** | Original core class name or logical map key to remove. |

***
### getClassMap

Return the mapped class name for a core class or fallback to itself.

```php
public getClassMap(string $class): string
```

**Parameters:**

| Parameter | Type       | Description                                  |
|-----------|------------|----------------------------------------------|
| `$class`  | **string** | Original core class name or logical map key. |

**Return Value:**

Replacement class name when configured; otherwise the
original value.

***
### getBackupClass

Return the configured backup model class.

```php
public getBackupClass(): string
```

**Return Value:**

Replacement for `Backup::class`, or the core class when
no mapping is configured.

***
### getAuditClass

Return the configured audit model class.

```php
public getAuditClass(): string
```

**Return Value:**

Replacement for `Audit::class`, or the core class when no
mapping is configured.

***
### getAuditDetailClass

Return the configured audit-detail model class.

```php
public getAuditDetailClass(): string
```

**Return Value:**

Replacement for `AuditDetail::class`, or the core class
when no mapping is configured.

***
### getLogClass

Return the configured log model class.

```php
public getLogClass(): string
```

**Return Value:**

Replacement for `Log::class`, or the core class when no
mapping is configured.

***
### getEmailClass

Return the configured email model class.

```php
public getEmailClass(): string
```

**Return Value:**

Replacement for `Email::class`, or the core class when no
mapping is configured.

***
### getJobClass

Return the configured job model class.

```php
public getJobClass(): string
```

**Return Value:**

Replacement for `Job::class`, or the core class when no
mapping is configured.

***
### getFileClass

Return the configured file model class.

```php
public getFileClass(): string
```

**Return Value:**

Replacement for `File::class`, or the core class when no
mapping is configured.

***
### getSessionClass

Return the configured session model class.

```php
public getSessionClass(): string
```

**Return Value:**

Replacement for `Session::class`, or the core class when
no mapping is configured.

***
### getFlagClass

Return the configured flag model class.

```php
public getFlagClass(): string
```

**Return Value:**

Replacement for `Flag::class`, or the core class when no
mapping is configured.

***
### getSettingClass

Return the configured setting model class.

```php
public getSettingClass(): string
```

**Return Value:**

Replacement for `Setting::class`, or the core class when
no mapping is configured.

***
### getLangClass

Return the configured language model class.

```php
public getLangClass(): string
```

**Return Value:**

Replacement for `Lang::class`, or the core class when no
mapping is configured.

***
### getTranslateClass

Return the configured translate model class.

```php
public getTranslateClass(): string
```

**Return Value:**

Replacement for `Translate::class`, or the core class
when no mapping is configured.

***
### getWorkspaceClass

Return the configured workspace model class.

```php
public getWorkspaceClass(): string
```

**Return Value:**

Replacement for `Workspace::class`, or the core class
when no mapping is configured.

***
### getWorkspaceLangClass

Return the configured workspace-language model class.

```php
public getWorkspaceLangClass(): string
```

**Return Value:**

Replacement for `WorkspaceLang::class`, or the core class
when no mapping is configured.

***
### getPageClass

Return the configured page model class.

```php
public getPageClass(): string
```

**Return Value:**

Replacement for `Page::class`, or the core class when no
mapping is configured.

***
### getPostClass

Return the configured post model class.

```php
public getPostClass(): string
```

**Return Value:**

Replacement for `Post::class`, or the core class when no
mapping is configured.

***
### getTemplateClass

Return the configured template model class.

```php
public getTemplateClass(): string
```

**Return Value:**

Replacement for `Template::class`, or the core class when
no mapping is configured.

***
### getTableClass

Return the configured table model class.

```php
public getTableClass(): string
```

**Return Value:**

Replacement for `Table::class`, or the core class when no
mapping is configured.

***
### getProfileClass

Return the configured profile model class.

```php
public getProfileClass(): string
```

**Return Value:**

Replacement for `Profile::class`, or the core class when
no mapping is configured.

***
### getOauth2Class

Return the configured OAuth2 model class.

```php
public getOauth2Class(): string
```

**Return Value:**

Replacement for `Oauth2::class`, or the core class when
no mapping is configured.

***
### getUserClass

Return the configured user model class.

```php
public getUserClass(): string
```

**Return Value:**

Replacement for `User::class`, or the core class when no
mapping is configured.

***
### getUserTypeClass

Return the configured user-type model class.

```php
public getUserTypeClass(): string
```

**Return Value:**

Replacement for `UserType::class`, or the core class when
no mapping is configured.

***
### getUserGroupClass

Return the configured user-group model class.

```php
public getUserGroupClass(): string
```

**Return Value:**

Replacement for `UserGroup::class`, or the core class
when no mapping is configured.

***
### getUserRoleClass

Return the configured user-role model class.

```php
public getUserRoleClass(): string
```

**Return Value:**

Replacement for `UserRole::class`, or the core class when
no mapping is configured.

***
### getUserFeatureClass

Return the configured user-feature model class.

```php
public getUserFeatureClass(): string
```

**Return Value:**

Replacement for `UserFeature::class`, or the core class
when no mapping is configured.

***
### getRoleClass

Return the configured role model class.

```php
public getRoleClass(): string
```

**Return Value:**

Replacement for `Role::class`, or the core class when no
mapping is configured.

***
### getRoleRoleClass

Return the configured role-role model class.

```php
public getRoleRoleClass(): string
```

**Return Value:**

Replacement for `RoleRole::class`, or the core class when
no mapping is configured.

***
### getRoleFeatureClass

Return the configured role-feature model class.

```php
public getRoleFeatureClass(): string
```

**Return Value:**

Replacement for `RoleFeature::class`, or the core class
when no mapping is configured.

***
### getGroupClass

Return the configured group model class.

```php
public getGroupClass(): string
```

**Return Value:**

Replacement for `Group::class`, or the core class when no
mapping is configured.

***
### getGroupRoleClass

Return the configured group-role model class.

```php
public getGroupRoleClass(): string
```

**Return Value:**

Replacement for `GroupRole::class`, or the core class
when no mapping is configured.

***
### getGroupTypeClass

Return the configured group-type model class.

```php
public getGroupTypeClass(): string
```

**Return Value:**

Replacement for `GroupType::class`, or the core class
when no mapping is configured.

***
### getGroupFeatureClass

Return the configured group-feature model class.

```php
public getGroupFeatureClass(): string
```

**Return Value:**

Replacement for `GroupFeature::class`, or the core class
when no mapping is configured.

***
### getTypeClass

Return the configured type model class.

```php
public getTypeClass(): string
```

**Return Value:**

Replacement for `Type::class`, or the core class when no
mapping is configured.

***
### getFeatureClass

Return the configured feature model class.

```php
public getFeatureClass(): string
```

**Return Value:**

Replacement for `Feature::class`, or the core class when
no mapping is configured.

***
