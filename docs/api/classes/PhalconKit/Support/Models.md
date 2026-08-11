
Resolves configured PhalconKit model instances without magic methods.

Applications can replace core model classes through the `models` config map.
This service turns those configured class names into cached model instances
while validating the contracts expected by each typed getter. Invalid app
mappings are reported as `ServiceException` failures so production runtimes
behave consistently even when PHP assertions are disabled.

The service intentionally constructs models directly instead of resolving
them from the DI container because Phalcon models normally receive their
runtime services through the model manager and default DI integration.

***

* Full name: `\PhalconKit\Support\Models`
* Parent class: [`\PhalconKit\Di\Injectable`](../Di/Injectable.md)

## Properties

### instances

Cached model instances keyed by the original core model class name.

```php
public array<string,\PhalconKit\Mvc\Model> $instances
```

The cache key remains the core class requested by the framework, not the
mapped replacement class. This lets callers swap implementations through
config while preserving stable lookup and `unsetInstance()` semantics.

***

## Methods

### __construct

Build the model resolver with an optional explicit model class map.

```php
public __construct(array<string,string>|null $mapping = null): mixed
```

Passing null loads the `models` map from the bootstrap config service via
`ModelsMap::setModelsMap()`. Tests and service providers can pass an
explicit array to bypass the config lookup and validate local mappings.

**Parameters:**

| Parameter  | Type                           | Description                                                                                  |
|------------|--------------------------------|----------------------------------------------------------------------------------------------|
| `$mapping` | **array<string,string>\|null** | Core model class names mapped
to replacement model class names, or null to load from config. |

**Throws:**

When the config-backed model map cannot be
loaded from the DI container.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getInstances

Return every model instance that has already been resolved.

```php
public getInstances(): array<string,\PhalconKit\Mvc\Model>
```

**Return Value:**

Cached instances keyed by the original core
model class name requested by the framework.

***

### setInstance

Store a resolved model instance for a core model class.

```php
public setInstance(string $class, \PhalconKit\Mvc\Model $instance): void
```

This method is public so tests or advanced applications can pre-seed the
cache with custom instances. The supplied instance is not revalidated
against a typed getter contract until that getter is called.

**Parameters:**

| Parameter   | Type                      | Description                                      |
|-------------|---------------------------|--------------------------------------------------|
| `$class`    | **string**                | Original core model class used as the cache key. |
| `$instance` | **\PhalconKit\Mvc\Model** | Model instance to reuse for future lookups.      |

***

### unsetInstance

Remove a cached model instance for a core model class.

```php
public unsetInstance(string $map): void
```

The configured class map is left intact. The next lookup for the same
class will instantiate the currently configured mapped model again.

**Parameters:**

| Parameter | Type       | Description                                      |
|-----------|------------|--------------------------------------------------|
| `$map`    | **string** | Original core model class used as the cache key. |

***

### getInstance

Return a cached instance of the configured model class for a core class.

```php
public getInstance(string $class): \PhalconKit\Mvc\Model
```

The requested class is first translated through the model map. The mapped
class must exist, be instantiable with its default constructor, and extend
`PhalconKit\Mvc\Model`; otherwise a stable framework exception is thrown
before a native PHP error or disabled assertion can leak to callers.

**Parameters:**

| Parameter | Type       | Description                     |
|-----------|------------|---------------------------------|
| `$class`  | **string** | Original core model class name. |

**Return Value:**

Instance of the configured mapped model class.

**Throws:**

When the mapped class cannot be loaded,
instantiated, or does not extend the PhalconKit base model.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getTypedInstance

Return a mapped model instance that implements a specific framework contract.

```php
private getTypedInstance(string $class, class-string<\PhalconKit\Support\T> $expectedType): \PhalconKit\Support\T
```

Typed getters call this helper after resolving the mapped model. This
keeps every public getter concise while ensuring a wrong-but-valid model
class, such as mapping `User::class` to `Backup::class`, fails with a
precise `ServiceException` instead of a late PHP return-type error.

**Parameters:**

| Parameter       | Type                                    | Description                        |
|-----------------|-----------------------------------------|------------------------------------|
| `$class`        | **string**                              | Original core model class name.    |
| `$expectedType` | **class-string<\PhalconKit\Support\T>** | Required model interface or class. |

**Return Value:**

Model instance implementing the requested contract.

**Throws:**

When the configured model does not implement
the contract required by the typed getter.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getBackup

Return the configured backup model instance.

```php
public getBackup(): \PhalconKit\Models\Interfaces\BackupInterface
```

**Return Value:**

Cached instance for `Backup::class`.

**Throws:**

When the configured model does not implement
the backup model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getAudit

Return the configured audit model instance.

```php
public getAudit(): \PhalconKit\Models\Interfaces\AuditInterface
```

**Return Value:**

Cached instance for `Audit::class`.

**Throws:**

When the configured model does not implement
the audit model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getAuditDetail

Return the configured audit-detail model instance.

```php
public getAuditDetail(): \PhalconKit\Models\Interfaces\AuditDetailInterface
```

**Return Value:**

Cached instance for `AuditDetail::class`.

**Throws:**

When the configured model does not implement
the audit-detail model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getLog

Return the configured log model instance.

```php
public getLog(): \PhalconKit\Models\Interfaces\LogInterface
```

**Return Value:**

Cached instance for `Log::class`.

**Throws:**

When the configured model does not implement
the log model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getEmail

Return the configured email model instance.

```php
public getEmail(): \PhalconKit\Models\Interfaces\EmailInterface
```

**Return Value:**

Cached instance for `Email::class`.

**Throws:**

When the configured model does not implement
the email model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getJob

Return the configured job model instance.

```php
public getJob(): \PhalconKit\Models\Interfaces\JobInterface
```

**Return Value:**

Cached instance for `Job::class`.

**Throws:**

When the configured model does not implement
the job model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getFile

Return the configured file model instance.

```php
public getFile(): \PhalconKit\Models\Interfaces\FileInterface
```

**Return Value:**

Cached instance for `File::class`.

**Throws:**

When the configured model does not implement
the file model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getSession

Return the configured persisted-session model instance.

```php
public getSession(): \PhalconKit\Models\Interfaces\SessionInterface
```

**Return Value:**

Cached instance for `Session::class`.

**Throws:**

When the configured model does not implement
the persisted-session model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getFlag

Return the configured feature-flag model instance.

```php
public getFlag(): \PhalconKit\Models\Interfaces\FlagInterface
```

**Return Value:**

Cached instance for `Flag::class`.

**Throws:**

When the configured model does not implement
the feature-flag model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getSetting

Return the configured setting model instance.

```php
public getSetting(): \PhalconKit\Models\Interfaces\SettingInterface
```

**Return Value:**

Cached instance for `Setting::class`.

**Throws:**

When the configured model does not implement
the setting model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getLang

Return the configured language model instance.

```php
public getLang(): \PhalconKit\Models\Interfaces\LangInterface
```

**Return Value:**

Cached instance for `Lang::class`.

**Throws:**

When the configured model does not implement
the language model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getTranslate

Return the configured translation model instance.

```php
public getTranslate(): \PhalconKit\Models\Interfaces\TranslateInterface
```

**Return Value:**

Cached instance for `Translate::class`.

**Throws:**

When the configured model does not implement
the translation model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getWorkspace

Return the configured workspace model instance.

```php
public getWorkspace(): \PhalconKit\Models\Interfaces\WorkspaceInterface
```

**Return Value:**

Cached instance for `Workspace::class`.

**Throws:**

When the configured model does not implement
the workspace model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getWorkspaceLang

Return the configured workspace-language model instance.

```php
public getWorkspaceLang(): \PhalconKit\Models\Interfaces\WorkspaceLangInterface
```

**Return Value:**

Cached instance for `WorkspaceLang::class`.

**Throws:**

When the configured model does not implement
the workspace-language model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getPage

Return the configured page model instance.

```php
public getPage(): \PhalconKit\Models\Interfaces\PageInterface
```

**Return Value:**

Cached instance for `Page::class`.

**Throws:**

When the configured model does not implement
the page model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getPost

Return the configured post model instance.

```php
public getPost(): \PhalconKit\Models\Interfaces\PostInterface
```

**Return Value:**

Cached instance for `Post::class`.

**Throws:**

When the configured model does not implement
the post model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getTemplate

Return the configured template model instance.

```php
public getTemplate(): \PhalconKit\Models\Interfaces\TemplateInterface
```

**Return Value:**

Cached instance for `Template::class`.

**Throws:**

When the configured model does not implement
the template model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getTable

Return the configured table model instance.

```php
public getTable(): \PhalconKit\Models\Interfaces\TableInterface
```

**Return Value:**

Cached instance for `Table::class`.

**Throws:**

When the configured model does not implement
the table model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getProfile

Return the configured profile model instance.

```php
public getProfile(): \PhalconKit\Models\Interfaces\ProfileInterface
```

**Return Value:**

Cached instance for `Profile::class`.

**Throws:**

When the configured model does not implement
the profile model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getOauth2

Return the configured OAuth2 identity model instance.

```php
public getOauth2(): \PhalconKit\Models\Interfaces\Oauth2Interface
```

**Return Value:**

Cached instance for `Oauth2::class`.

**Throws:**

When the configured model does not implement
the OAuth2 identity model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getUser

Return the configured user model instance.

```php
public getUser(): \PhalconKit\Models\Interfaces\UserInterface
```

**Return Value:**

Cached instance for `User::class`.

**Throws:**

When the configured model does not implement
the user model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getUserType

Return the configured user-type model instance.

```php
public getUserType(): \PhalconKit\Models\Interfaces\UserTypeInterface
```

**Return Value:**

Cached instance for `UserType::class`.

**Throws:**

When the configured model does not implement
the user-type model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getUserGroup

Return the configured user-group model instance.

```php
public getUserGroup(): \PhalconKit\Models\Interfaces\UserGroupInterface
```

**Return Value:**

Cached instance for `UserGroup::class`.

**Throws:**

When the configured model does not implement
the user-group model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getUserRole

Return the configured user-role model instance.

```php
public getUserRole(): \PhalconKit\Models\Interfaces\UserRoleInterface
```

**Return Value:**

Cached instance for `UserRole::class`.

**Throws:**

When the configured model does not implement
the user-role model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getUserFeature

Return the configured user-feature model instance.

```php
public getUserFeature(): \PhalconKit\Models\Interfaces\UserFeatureInterface
```

**Return Value:**

Cached instance for `UserFeature::class`.

**Throws:**

When the configured model does not implement
the user-feature model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getRole

Return the configured role model instance.

```php
public getRole(): \PhalconKit\Models\Interfaces\RoleInterface
```

**Return Value:**

Cached instance for `Role::class`.

**Throws:**

When the configured model does not implement
the role model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getRoleRole

Return the configured role-inheritance model instance.

```php
public getRoleRole(): \PhalconKit\Models\Interfaces\RoleRoleInterface
```

**Return Value:**

Cached instance for `RoleRole::class`.

**Throws:**

When the configured model does not implement
the role-inheritance model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getRoleFeature

Return the configured role-feature model instance.

```php
public getRoleFeature(): \PhalconKit\Models\Interfaces\RoleFeatureInterface
```

**Return Value:**

Cached instance for `RoleFeature::class`.

**Throws:**

When the configured model does not implement
the role-feature model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getGroup

Return the configured group model instance.

```php
public getGroup(): \PhalconKit\Models\Interfaces\GroupInterface
```

**Return Value:**

Cached instance for `Group::class`.

**Throws:**

When the configured model does not implement
the group model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getGroupRole

Return the configured group-role model instance.

```php
public getGroupRole(): \PhalconKit\Models\Interfaces\GroupRoleInterface
```

**Return Value:**

Cached instance for `GroupRole::class`.

**Throws:**

When the configured model does not implement
the group-role model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getGroupType

Return the configured group-type model instance.

```php
public getGroupType(): \PhalconKit\Models\Interfaces\GroupTypeInterface
```

**Return Value:**

Cached instance for `GroupType::class`.

**Throws:**

When the configured model does not implement
the group-type model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getGroupFeature

Return the configured group-feature model instance.

```php
public getGroupFeature(): \PhalconKit\Models\Interfaces\GroupFeatureInterface
```

**Return Value:**

Cached instance for `GroupFeature::class`.

**Throws:**

When the configured model does not implement
the group-feature model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getType

Return the configured type model instance.

```php
public getType(): \PhalconKit\Models\Interfaces\TypeInterface
```

**Return Value:**

Cached instance for `Type::class`.

**Throws:**

When the configured model does not implement
the type model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getFeature

Return the configured feature model instance.

```php
public getFeature(): \PhalconKit\Models\Interfaces\FeatureInterface
```

**Return Value:**

Cached instance for `Feature::class`.

**Throws:**

When the configured model does not implement
the feature model contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

## Inherited methods

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
