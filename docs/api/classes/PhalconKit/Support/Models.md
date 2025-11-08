
Allow to get mapped classes without using magic methods

***

* Full name: `\PhalconKit\Support\Models`
* Parent class: [`\PhalconKit\Di\Injectable`](../Di/Injectable.md)

## Properties

### instances

Store an array of instances

```php
public array $instances
```

***

## Methods

### __construct

```php
public __construct(?array $mapping = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$mapping` | **?array** |             |

***

### getInstances

Get an array of mapped models

```php
public getInstances(): array
```

***

### setInstance

Set the instance for a class

```php
public setInstance(string $class, \PhalconKit\Mvc\Model $instance): void
```

**Parameters:**

| Parameter   | Type                      | Description |
|-------------|---------------------------|-------------|
| `$class`    | **string**                |             |
| `$instance` | **\PhalconKit\Mvc\Model** |             |

***

### unsetInstance

Remove an existing class

```php
public unsetInstance(string $map): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$map`    | **string** |             |

***

### getInstance

Return an instance of a specified class implementing Model interface

```php
public getInstance(string $class): \PhalconKit\Mvc\Model
```

**Parameters:**

| Parameter | Type       | Description                    |
|-----------|------------|--------------------------------|
| `$class`  | **string** | The fully qualified class name |

**Return Value:**

An instance of the specified class

***

### getBackup

Return an instance of \PhalconKit\Models\Interfaces\BackupInterface

```php
public getBackup(): \PhalconKit\Models\Interfaces\BackupInterface
```

***

### getAudit

Return an instance of \PhalconKit\Models\Interfaces\AuditInterface

```php
public getAudit(): \PhalconKit\Models\Interfaces\AuditInterface
```

***

### getAuditDetail

Return an instance of \PhalconKit\Models\Interfaces\AuditDetailInterface

```php
public getAuditDetail(): \PhalconKit\Models\Interfaces\AuditDetailInterface
```

***

### getLog

Return an instance of \PhalconKit\Models\Interfaces\LogInterface

```php
public getLog(): \PhalconKit\Models\Interfaces\LogInterface
```

***

### getEmail

Return an instance of \PhalconKit\Models\Interfaces\EmailInterface

```php
public getEmail(): \PhalconKit\Models\Interfaces\EmailInterface
```

***

### getJob

Return an instance of \PhalconKit\Models\Interfaces\JobInterface

```php
public getJob(): \PhalconKit\Models\Interfaces\JobInterface
```

***

### getFile

Return an instance of \PhalconKit\Models\Interfaces\FileInterface

```php
public getFile(): \PhalconKit\Models\Interfaces\FileInterface
```

***

### getSession

Return an instance of \PhalconKit\Models\Interfaces\SessionInterface

```php
public getSession(): \PhalconKit\Models\Interfaces\SessionInterface
```

***

### getFlag

Return an instance of \PhalconKit\Models\Interfaces\FlagInterface

```php
public getFlag(): \PhalconKit\Models\Interfaces\FlagInterface
```

***

### getSetting

Return an instance of \PhalconKit\Models\Interfaces\SettingInterface

```php
public getSetting(): \PhalconKit\Models\Interfaces\SettingInterface
```

***

### getLang

Return an instance of \PhalconKit\Models\Interfaces\LangInterface

```php
public getLang(): \PhalconKit\Models\Interfaces\LangInterface
```

***

### getTranslate

Return an instance of \PhalconKit\Models\Interfaces\TranslateInterface

```php
public getTranslate(): \PhalconKit\Models\Interfaces\TranslateInterface
```

***

### getWorkspace

Return an instance of \PhalconKit\Models\Interfaces\WorkspaceInterface

```php
public getWorkspace(): \PhalconKit\Models\Interfaces\WorkspaceInterface
```

***

### getWorkspaceLang

Return an instance of \PhalconKit\Models\Interfaces\WorkspaceInterface

```php
public getWorkspaceLang(): \PhalconKit\Models\Interfaces\WorkspaceLangInterface
```

***

### getPage

Return an instance of \PhalconKit\Models\Interfaces\PageInterface

```php
public getPage(): \PhalconKit\Models\Interfaces\PageInterface
```

***

### getPost

Return an instance of \PhalconKit\Models\Interfaces\PostInterface

```php
public getPost(): \PhalconKit\Models\Interfaces\PostInterface
```

***

### getTemplate

Return an instance of \PhalconKit\Models\Interfaces\TemplateInterface

```php
public getTemplate(): \PhalconKit\Models\Interfaces\TemplateInterface
```

***

### getTable

Return an instance of \PhalconKit\Models\Interfaces\TableInterface

```php
public getTable(): \PhalconKit\Models\Interfaces\TableInterface
```

***

### getProfile

Return an instance of \PhalconKit\Models\Interfaces\ProfileInterface

```php
public getProfile(): \PhalconKit\Models\Interfaces\ProfileInterface
```

***

### getOauth2

Return an instance of \PhalconKit\Models\Interfaces\UserInterface

```php
public getOauth2(): \PhalconKit\Models\Interfaces\Oauth2Interface
```

***

### getUser

Return an instance of \PhalconKit\Models\Interfaces\UserInterface

```php
public getUser(): \PhalconKit\Models\Interfaces\UserInterface
```

***

### getUserType

Return an instance of \PhalconKit\Models\Interfaces\UserTypeInterface

```php
public getUserType(): \PhalconKit\Models\Interfaces\UserTypeInterface
```

***

### getUserGroup

Return an instance of \PhalconKit\Models\Interfaces\UserGroupInterface

```php
public getUserGroup(): \PhalconKit\Models\Interfaces\UserGroupInterface
```

***

### getUserRole

Return an instance of \PhalconKit\Models\Interfaces\UserRoleInterface

```php
public getUserRole(): \PhalconKit\Models\Interfaces\UserRoleInterface
```

***

### getUserFeature

Return an instance of \PhalconKit\Models\Interfaces\UserFeatureInterface

```php
public getUserFeature(): \PhalconKit\Models\Interfaces\UserFeatureInterface
```

***

### getRole

Return an instance of \PhalconKit\Models\Interfaces\RoleInterface

```php
public getRole(): \PhalconKit\Models\Interfaces\RoleInterface
```

***

### getRoleRole

Return an instance of \PhalconKit\Models\Interfaces\RoleRoleInterface

```php
public getRoleRole(): \PhalconKit\Models\Interfaces\RoleRoleInterface
```

***

### getRoleFeature

Return an instance of \PhalconKit\Models\Interfaces\RoleFeatureInterface

```php
public getRoleFeature(): \PhalconKit\Models\Interfaces\RoleFeatureInterface
```

***

### getGroup

Return an instance of \PhalconKit\Models\Interfaces\GroupInterface

```php
public getGroup(): \PhalconKit\Models\Interfaces\GroupInterface
```

***

### getGroupRole

Return an instance of \PhalconKit\Models\Interfaces\GroupRoleInterface

```php
public getGroupRole(): \PhalconKit\Models\Interfaces\GroupRoleInterface
```

***

### getGroupType

Return an instance of \PhalconKit\Models\Interfaces\GroupTypeInterface

```php
public getGroupType(): \PhalconKit\Models\Interfaces\GroupTypeInterface
```

***

### getGroupFeature

Return an instance of \PhalconKit\Models\Interfaces\GroupFeatureInterface

```php
public getGroupFeature(): \PhalconKit\Models\Interfaces\GroupFeatureInterface
```

***

### getType

Return an instance of \PhalconKit\Models\Interfaces\TypeInterface

```php
public getType(): \PhalconKit\Models\Interfaces\TypeInterface
```

***

### getFeature

Return an instance of \PhalconKit\Models\Interfaces\FeatureInterface

```php
public getFeature(): \PhalconKit\Models\Interfaces\FeatureInterface
```

***

## Inherited methods

### getDI

```php
public getDI(): \Phalcon\Di\DiInterface
```

* This method is **abstract**.
***

### getConfig

Retrieve the config from DI

```php
public getConfig(): \PhalconKit\Bootstrap\Config
```

***

### setModelsMap

Set the models mapping or retrieve the mapped models from the config

```php
public setModelsMap(?array $modelsMap = null): void
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$modelsMap` | **?array** |             |

***

### getModelsMap

Get an array of mapped models

```php
public getModelsMap(): array
```

***

### setClassMap

Map a new class

```php
public setClassMap(string $map, string $class): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$map`    | **string** |             |
| `$class`  | **string** |             |

***

### removeClassMap

Remove an existing class

```php
public removeClassMap(string $map): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$map`    | **string** |             |

***

### getClassMap

Return the class mapping

```php
public getClassMap(string $class): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **string** |             |

***

### getBackupClass

Return the mapped class name of \PhalconKit\Models\Backup::class

```php
public getBackupClass(): string
```

***

### getAuditClass

Return the mapped class name of \PhalconKit\Models\Audit::class

```php
public getAuditClass(): string
```

***

### getAuditDetailClass

Return the mapped class name of \PhalconKit\Models\AuditDetail::class

```php
public getAuditDetailClass(): string
```

***

### getLogClass

Return the mapped class name of \PhalconKit\Models\Log::class

```php
public getLogClass(): string
```

***

### getEmailClass

Return the mapped class name of \PhalconKit\Models\Email::class

```php
public getEmailClass(): string
```

***

### getJobClass

Return the mapped class name of \PhalconKit\Models\Job::class

```php
public getJobClass(): string
```

***

### getFileClass

Return the mapped class name of \PhalconKit\Models\File::class

```php
public getFileClass(): string
```

***

### getSessionClass

Return the mapped class name of \PhalconKit\Models\Session::class

```php
public getSessionClass(): string
```

***

### getFlagClass

Return the mapped class name of \PhalconKit\Models\Flag::class

```php
public getFlagClass(): string
```

***

### getSettingClass

Return the mapped class name of \PhalconKit\Models\Setting::class

```php
public getSettingClass(): string
```

***

### getLangClass

Return the mapped class name of \PhalconKit\Models\Lang::class

```php
public getLangClass(): string
```

***

### getTranslateClass

Return the mapped class name of \PhalconKit\Models\Translate::class

```php
public getTranslateClass(): string
```

***

### getWorkspaceClass

Return the mapped class name of \PhalconKit\Models\Workspace::class

```php
public getWorkspaceClass(): string
```

***

### getWorkspaceLangClass

Return the mapped class name of \PhalconKit\Models\WorkspaceLang::class

```php
public getWorkspaceLangClass(): string
```

***

### getPageClass

Return the mapped class name of \PhalconKit\Models\Page::class

```php
public getPageClass(): string
```

***

### getPostClass

Return the mapped class name of \PhalconKit\Models\Post::class

```php
public getPostClass(): string
```

***

### getTemplateClass

Return the mapped class name of \PhalconKit\Models\Template::class

```php
public getTemplateClass(): string
```

***

### getTableClass

Return the mapped class name of \PhalconKit\Models\Table::class

```php
public getTableClass(): string
```

***

### getProfileClass

Return the mapped class name of \PhalconKit\Models\Profile::class

```php
public getProfileClass(): string
```

***

### getOauth2Class

Return the mapped class name of \PhalconKit\Models\Oauth2::class

```php
public getOauth2Class(): string
```

***

### getUserClass

Return the mapped class name of \PhalconKit\Models\User::class

```php
public getUserClass(): string
```

***

### getUserTypeClass

Return the mapped class name of \PhalconKit\Models\UserType::class

```php
public getUserTypeClass(): string
```

***

### getUserGroupClass

Return the mapped class name of \PhalconKit\Models\UserGroup::class

```php
public getUserGroupClass(): string
```

***

### getUserRoleClass

Return the mapped class name of \PhalconKit\Models\UserRole::class

```php
public getUserRoleClass(): string
```

***

### getUserFeatureClass

Return the mapped class name of \PhalconKit\Models\UserFeature::class

```php
public getUserFeatureClass(): string
```

***

### getRoleClass

Return the mapped class name of \PhalconKit\Models\Role::class

```php
public getRoleClass(): string
```

***

### getRoleRoleClass

Return the mapped class name of \PhalconKit\Models\RoleRole::class

```php
public getRoleRoleClass(): string
```

***

### getRoleFeatureClass

Return the mapped class name of \PhalconKit\Models\RoleFeature::class

```php
public getRoleFeatureClass(): string
```

***

### getGroupClass

Return the mapped class name of \PhalconKit\Models\Group::class

```php
public getGroupClass(): string
```

***

### getGroupRoleClass

Return the mapped class name of \PhalconKit\Models\GroupRole::class

```php
public getGroupRoleClass(): string
```

***

### getGroupTypeClass

Return the mapped class name of \PhalconKit\Models\GroupType::class

```php
public getGroupTypeClass(): string
```

***

### getGroupFeatureClass

Return the mapped class name of \PhalconKit\Models\GroupFeature::class

```php
public getGroupFeatureClass(): string
```

***

### getTypeClass

Return the mapped class name of \PhalconKit\Models\Type::class

```php
public getTypeClass(): string
```

***

### getFeatureClass

Return the mapped class name of \PhalconKit\Models\Feature::class

```php
public getFeatureClass(): string
```

***
