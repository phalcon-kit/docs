
This is an automatically generated documentation for **Phalcon Kit Documentation**.

## Namespaces

### \


| Function                                                          | Description                                                         |
|-------------------------------------------------------------------|---------------------------------------------------------------------|
| [`array_unset_recursive()`](./functions/array_unset_recursive.md) | Remove selected keys from an array at every nesting level.          |
| [`dump()`](./functions/dump.md)                                   | Dump values in a CLI-safe or browser-safe representation.           |
| [`exit_500()`](./functions/exit_500.md)                           | Terminate execution with a 500 Internal Server Error response code. |
| [`dd()`](./functions/dd.md)                                       | Dump values and terminate execution as an error.                    |
| [`vdd()`](./functions/vdd.md)                                     | Dump values through native `var_dump()` and terminate execution.    |
| [`implode_sprintf()`](./functions/implode_sprintf.md)             | Format every non-null array value and join the formatted parts.     |
| [`implode_mb_sprintf()`](./functions/implode_mb_sprintf.md)       | Multibyte-safe variant of `implode_sprintf()`.                      |
| [`sprintfn()`](./functions/sprintfn.md)                           | Format a string with named placeholders backed by `vsprintf()`.     |
| [`mb_sprintf()`](./functions/mb_sprintf.md)                       | Return a formatted multibyte string.                                |
| [`mb_vsprintf()`](./functions/mb_vsprintf.md)                     | Return a formatted string with multibyte-aware `%s` handling.       |

### \PhalconKit


| Class                                            | Description                                                                   |
|--------------------------------------------------|-------------------------------------------------------------------------------|
| [`Bootstrap`](./classes/PhalconKit/Bootstrap.md) | Coordinates PhalconKit runtime setup for MVC, CLI, and WebSocket entrypoints. |
| [`Exception`](./classes/PhalconKit/Exception.md) | Base checked category for general PhalconKit framework exceptions.            |
| [`Locale`](./classes/PhalconKit/Locale.md)       | Allow to manage and lookup the locale for the localisation                    |
| [`Tag`](./classes/PhalconKit/Tag.md)             | This file is part of the Phalcon Kit.                                         |

### \PhalconKit\Acl


| Class                                                          | Description                                                            |
|----------------------------------------------------------------|------------------------------------------------------------------------|
| [`Acl`](./classes/PhalconKit/Acl/Acl.md)                       | Builds native Phalcon ACL instances from PhalconKit permission config. |
| [`PermissionName`](./classes/PhalconKit/Acl/PermissionName.md) | Normalizes controller and action names used by ACL permissions.        |


| Interface                                                  | Description                                                       |
|------------------------------------------------------------|-------------------------------------------------------------------|
| [`AclInterface`](./classes/PhalconKit/Acl/AclInterface.md) | Contract for ACL builders backed by PhalconKit permission arrays. |

### \PhalconKit\Assets


| Class                                               | Description                       |
|-----------------------------------------------------|-----------------------------------|
| [`Manager`](./classes/PhalconKit/Assets/Manager.md) | PhalconKit asset manager wrapper. |

### \PhalconKit\Autoload


| Class                                               | Description                                                 |
|-----------------------------------------------------|-------------------------------------------------------------|
| [`Loader`](./classes/PhalconKit/Autoload/Loader.md) | Phalcon autoloader optimized for framework bootstrap usage. |

### \PhalconKit\Bootstrap


| Class                                                        | Description                                                    |
|--------------------------------------------------------------|----------------------------------------------------------------|
| [`Config`](./classes/PhalconKit/Bootstrap/Config.md)         | Default framework configuration used by PhalconKit bootstraps. |
| [`Deployment`](./classes/PhalconKit/Bootstrap/Deployment.md) | Default database deployment/scaffolding configuration.         |
| [`Devtools`](./classes/PhalconKit/Bootstrap/Devtools.md)     | Config adapter shape expected by Phalcon DevTools.             |
| [`Router`](./classes/PhalconKit/Bootstrap/Router.md)         | Bootstrap router with PhalconKit's default frontend routes.    |

### \PhalconKit\Bootstrap\Permissions


| Class                                                                              | Description                                                |
|------------------------------------------------------------------------------------|------------------------------------------------------------|
| [`ColumnConfig`](./classes/PhalconKit/Bootstrap/Permissions/ColumnConfig.md)       | Default permission fragment for column metadata resources. |
| [`DynamicConfig`](./classes/PhalconKit/Bootstrap/Permissions/DynamicConfig.md)     | Default permission fragment for dynamic-model access.      |
| [`RecordConfig`](./classes/PhalconKit/Bootstrap/Permissions/RecordConfig.md)       | Default permission fragment for generic record resources.  |
| [`TableConfig`](./classes/PhalconKit/Bootstrap/Permissions/TableConfig.md)         | Default permission fragment for table metadata resources.  |
| [`TemplateConfig`](./classes/PhalconKit/Bootstrap/Permissions/TemplateConfig.md)   | Default permission fragment for template resources.        |
| [`WorkspaceConfig`](./classes/PhalconKit/Bootstrap/Permissions/WorkspaceConfig.md) | Default permission fragment for workspace resources.       |

### \PhalconKit\Cache


| Class                                          | Description                    |
|------------------------------------------------|--------------------------------|
| [`Cache`](./classes/PhalconKit/Cache/Cache.md) | PhalconKit cache service type. |

### \PhalconKit\Cli


| Class                                                              | Description                                             |
|--------------------------------------------------------------------|---------------------------------------------------------|
| [`Console`](./classes/PhalconKit/Cli/Console.md)                   | PhalconKit CLI console wrapper.                         |
| [`Dispatcher`](./classes/PhalconKit/Cli/Dispatcher.md)             | CLI dispatcher with PhalconKit diagnostic state export. |
| [`ExceptionHandler`](./classes/PhalconKit/Cli/ExceptionHandler.md) | Minimal CLI exception/message writer.                   |
| [`Module`](./classes/PhalconKit/Cli/Module.md)                     | Default CLI module definition.                          |
| [`Router`](./classes/PhalconKit/Cli/Router.md)                     | CLI router with PhalconKit diagnostic state export.     |
| [`Task`](./classes/PhalconKit/Cli/Task.md)                         | Base class for PhalconKit CLI tasks.                    |


| Interface                                                                | Description                                                  |
|--------------------------------------------------------------------------|--------------------------------------------------------------|
| [`DispatcherInterface`](./classes/PhalconKit/Cli/DispatcherInterface.md) | Combined dispatcher contract for PhalconKit CLI dispatchers. |
| [`TaskInterface`](./classes/PhalconKit/Cli/TaskInterface.md)             | Marker contract for PhalconKit CLI task handlers.            |

### \PhalconKit\Config


| Class                                             | Description                                                            |
|---------------------------------------------------|------------------------------------------------------------------------|
| [`Config`](./classes/PhalconKit/Config/Config.md) | PhalconKit config wrapper with framework merge and typed-path helpers. |


| Interface                                                           | Description                        |
|---------------------------------------------------------------------|------------------------------------|
| [`ConfigInterface`](./classes/PhalconKit/Config/ConfigInterface.md) | PhalconKit configuration contract. |

### \PhalconKit\Db


| Class                                             | Description                                                            |
|---------------------------------------------------|------------------------------------------------------------------------|
| [`Column`](./classes/PhalconKit/Db/Column.md)     |                                                                        |
| [`Profiler`](./classes/PhalconKit/Db/Profiler.md) | Database profiler with null-safe profile access and array diagnostics. |

### \PhalconKit\Db\Adapter\Pdo


| Class                                                   | Description |
|---------------------------------------------------------|-------------|
| [`Mysql`](./classes/PhalconKit/Db/Adapter/Pdo/Mysql.md) |             |

### \PhalconKit\Db\Dialect


| Class                                               | Description                                  |
|-----------------------------------------------------|----------------------------------------------|
| [`Mysql`](./classes/PhalconKit/Db/Dialect/Mysql.md) | MySQL dialect with PhalconKit query helpers. |

### \PhalconKit\Db\Events


| Class                                                    | Description                                                            |
|----------------------------------------------------------|------------------------------------------------------------------------|
| [`Logger`](./classes/PhalconKit/Db/Events/Logger.md)     | Responsible for logging database query events.                         |
| [`Profiler`](./classes/PhalconKit/Db/Events/Profiler.md) | Database event listener that feeds executed queries into the profiler. |

### \PhalconKit\Di


| Class                                                           | Description                                                                  |
|-----------------------------------------------------------------|------------------------------------------------------------------------------|
| [`Di`](./classes/PhalconKit/Di/Di.md)                           | Minimal PhalconKit DI container.                                             |
| [`FactoryDefault`](./classes/PhalconKit/Di/FactoryDefault.md)   | MVC/default-service PhalconKit DI container.                                 |
| [`Injectable`](./classes/PhalconKit/Di/Injectable.md)           |                                                                              |
| [`ServiceResolver`](./classes/PhalconKit/Di/ServiceResolver.md) | Shared typed service resolver for static helpers and native Phalcon bridges. |


| Trait                                                                     | Description                                                                                 |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [`AbstractInjectable`](./classes/PhalconKit/Di/AbstractInjectable.md)     | Trait AbstractInjectable                                                                    |
| [`InjectableProperties`](./classes/PhalconKit/Di/InjectableProperties.md) |                                                                                             |
| [`InjectableTrait`](./classes/PhalconKit/Di/InjectableTrait.md)           | The InjectableTrait trait provides methods for using dependency injection within an object. |
| [`TypedServicesTrait`](./classes/PhalconKit/Di/TypedServicesTrait.md)     | Implements typed service lookups for PhalconKit DI containers.                              |


| Interface                                               | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [`DiInterface`](./classes/PhalconKit/Di/DiInterface.md) | PhalconKit dependency injection contract. |

### \PhalconKit\Di\FactoryDefault


| Class                                                  | Description                                  |
|--------------------------------------------------------|----------------------------------------------|
| [`Cli`](./classes/PhalconKit/Di/FactoryDefault/Cli.md) | CLI default-service PhalconKit DI container. |

### \PhalconKit\Dispatcher


| Class                                                                         | Description                           |
|-------------------------------------------------------------------------------|---------------------------------------|
| [`AbstractDispatcher`](./classes/PhalconKit/Dispatcher/AbstractDispatcher.md) | Generic PhalconKit dispatcher helper. |


| Trait                                                                   | Description                                             |
|-------------------------------------------------------------------------|---------------------------------------------------------|
| [`DispatcherTrait`](./classes/PhalconKit/Dispatcher/DispatcherTrait.md) | Shared dispatcher behavior for MVC and CLI dispatchers. |


| Interface                                                                       | Description                                                                    |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [`DispatcherInterface`](./classes/PhalconKit/Dispatcher/DispatcherInterface.md) | Shared dispatcher contract for PhalconKit MVC, CLI, and WebSocket dispatchers. |

### \PhalconKit\Encryption


| Class                                                     | Description                                                             |
|-----------------------------------------------------------|-------------------------------------------------------------------------|
| [`Security`](./classes/PhalconKit/Encryption/Security.md) | Security service with PhalconKit random generation and Argon2 defaults. |

### \PhalconKit\Encryption\Security


| Class                                                          | Description |
|----------------------------------------------------------------|-------------|
| [`Random`](./classes/PhalconKit/Encryption/Security/Random.md) |             |

### \PhalconKit\Events


| Class                                                                                 | Description                                                     |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [`ConfiguredEventListeners`](./classes/PhalconKit/Events/ConfiguredEventListeners.md) | Attaches config-declared listeners to a Phalcon events manager. |


| Trait                                                                 | Description                                                               |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`EventsAwareTrait`](./classes/PhalconKit/Events/EventsAwareTrait.md) | The EventsAwareTrait provides methods for managing events within a class. |

### \PhalconKit\Exception


| Class                                                                                    | Description                                                                   |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`CliException`](./classes/PhalconKit/Exception/CliException.md)                         | Raised for command-line task and console dispatch failures.                   |
| [`ConfigurationException`](./classes/PhalconKit/Exception/ConfigurationException.md)     | Raised when framework configuration is present but invalid.                   |
| [`HttpException`](./classes/PhalconKit/Exception/HttpException.md)                       | Raised for HTTP/request-level failures handled by PhalconKit controllers.     |
| [`InvalidArgumentException`](./classes/PhalconKit/Exception/InvalidArgumentException.md) | Raised when a caller passes an invalid argument to PhalconKit code.           |
| [`LogicException`](./classes/PhalconKit/Exception/LogicException.md)                     | Raised when PhalconKit detects an impossible or inconsistent framework state. |
| [`RuntimeException`](./classes/PhalconKit/Exception/RuntimeException.md)                 | Raised when a PhalconKit operation fails at runtime outside DI resolution.    |
| [`ServiceException`](./classes/PhalconKit/Exception/ServiceException.md)                 | Raised when a framework service cannot be resolved or used safely.            |
| [`WsException`](./classes/PhalconKit/Exception/WsException.md)                           | Raised for WebSocket bootstrap, routing, or request-handling failures.        |


| Interface                                                                    | Description                                                         |
|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`ExceptionInterface`](./classes/PhalconKit/Exception/ExceptionInterface.md) | Marker contract for exceptions raised by PhalconKit framework code. |

### \PhalconKit\Filter


| Class                                                           | Description                                                              |
|-----------------------------------------------------------------|--------------------------------------------------------------------------|
| [`Filter`](./classes/PhalconKit/Filter/Filter.md)               | Phalcon filter service with PhalconKit sanitizers registered by default. |
| [`FilterFactory`](./classes/PhalconKit/Filter/FilterFactory.md) | Factory for filter locators that include PhalconKit sanitizer aliases.   |
| [`Validation`](./classes/PhalconKit/Filter/Validation.md)       | PhalconKit validation service type.                                      |

### \PhalconKit\Filter\Sanitize


| Class                                                  | Description                                                 |
|--------------------------------------------------------|-------------------------------------------------------------|
| [`IPv4`](./classes/PhalconKit/Filter/Sanitize/IPv4.md) | Sanitizer that accepts only valid IPv4 address strings.     |
| [`IPv6`](./classes/PhalconKit/Filter/Sanitize/IPv6.md) | Sanitizer that accepts only valid IPv6 address strings.     |
| [`Json`](./classes/PhalconKit/Filter/Sanitize/Json.md) | Sanitizer that keeps only syntactically valid JSON strings. |
| [`Md5`](./classes/PhalconKit/Filter/Sanitize/Md5.md)   | Sanitizer for md5-style lowercase hexadecimal strings.      |

### \PhalconKit\Filter\Validation\Validator


| Class                                                                | Description                                                       |
|----------------------------------------------------------------------|-------------------------------------------------------------------|
| [`Color`](./classes/PhalconKit/Filter/Validation/Validator/Color.md) | Validate CSS-style hexadecimal color strings.                     |
| [`Json`](./classes/PhalconKit/Filter/Validation/Validator/Json.md)   | Validate that a field contains a syntactically valid JSON string. |

### \PhalconKit\Fractal


| Class                                                                  | Description                                                      |
|------------------------------------------------------------------------|------------------------------------------------------------------|
| [`Manager`](./classes/PhalconKit/Fractal/Manager.md)                   | Framework-scoped League Fractal manager.                         |
| [`ModelTransformer`](./classes/PhalconKit/Fractal/ModelTransformer.md) | Default Fractal transformer for Phalcon models.                  |
| [`Transformer`](./classes/PhalconKit/Fractal/Transformer.md)           | Base transformer for Fractal resources backed by Phalcon models. |

### \PhalconKit\Fractal\Serializer


| Class                                                                                 | Description                                                                 |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`RawArraySerializer`](./classes/PhalconKit/Fractal/Serializer/RawArraySerializer.md) | Fractal serializer that returns payload arrays without a resource envelope. |

### \PhalconKit\Html


| Class                                                   | Description                                          |
|---------------------------------------------------------|------------------------------------------------------|
| [`Escaper`](./classes/PhalconKit/Html/Escaper.md)       | HTML escaper with PhalconKit JSON-attribute support. |
| [`TagFactory`](./classes/PhalconKit/Html/TagFactory.md) | Framework HTML tag factory.                          |

### \PhalconKit\Html\Escaper


| Interface                                                                   | Description                                                        |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------|
| [`EscaperInterface`](./classes/PhalconKit/Html/Escaper/EscaperInterface.md) | Escaper contract with PhalconKit's JSON attribute escaping helper. |

### \PhalconKit\Http


| Class                                                   | Description                                                  |
|---------------------------------------------------------|--------------------------------------------------------------|
| [`Request`](./classes/PhalconKit/Http/Request.md)       | HTTP request implementation with PhalconKit request helpers. |
| [`Response`](./classes/PhalconKit/Http/Response.md)     | HTTP response implementation used by PhalconKit services.    |
| [`StatusCode`](./classes/PhalconKit/Http/StatusCode.md) | HTTP status-code constants and reason-phrase lookup helpers. |


| Interface                                                             | Description                                                     |
|-----------------------------------------------------------------------|-----------------------------------------------------------------|
| [`RequestInterface`](./classes/PhalconKit/Http/RequestInterface.md)   | HTTP request contract extended with PhalconKit request helpers. |
| [`ResponseInterface`](./classes/PhalconKit/Http/ResponseInterface.md) | HTTP response contract used by PhalconKit services.             |

### \PhalconKit\Identity


| Class                                                 | Description                                                   |
|-------------------------------------------------------|---------------------------------------------------------------|
| [`Manager`](./classes/PhalconKit/Identity/Manager.md) | Coordinates authentication state for PhalconKit applications. |


| Interface                                                               | Description                                                  |
|-------------------------------------------------------------------------|--------------------------------------------------------------|
| [`ManagerInterface`](./classes/PhalconKit/Identity/ManagerInterface.md) | Public contract for the default PhalconKit identity manager. |

### \PhalconKit\Identity\Traits


| Trait                                                                    | Description                                                                    |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [`Acl`](./classes/PhalconKit/Identity/Traits/Acl.md)                     | Builds the ACL role objects used by PhalconKit permission checks.              |
| [`Impersonation`](./classes/PhalconKit/Identity/Traits/Impersonation.md) | Implements session-based user impersonation.                                   |
| [`Jwt`](./classes/PhalconKit/Identity/Traits/Jwt.md)                     | Resolves identity claims from JWTs, bearer authorization, or session fallback. |
| [`Oauth2`](./classes/PhalconKit/Identity/Traits/Oauth2.md)               | Links provider OAuth2 identities to local users.                               |
| [`Role`](./classes/PhalconKit/Identity/Traits/Role.md)                   | Provides role matching and configured role inheritance.                        |
| [`Session`](./classes/PhalconKit/Identity/Traits/Session.md)             | Stores the lightweight identity payload for the active manager.                |
| [`User`](./classes/PhalconKit/Identity/Traits/User.md)                   | Resolves identity users from the configured user model.                        |

### \PhalconKit\Identity\Traits\Abstracts


| Trait                                                                                              | Description                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [`AbstractAcl`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractAcl.md)                     | Declares ACL role methods required by traits composed into the identity manager. |
| [`AbstractImpersonation`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractImpersonation.md) | Declares impersonation methods required by composed identity traits.             |
| [`AbstractJwt`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractJwt.md)                     | Declares JWT claim methods required by session and identity helpers.             |
| [`AbstractOauth2`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractOauth2.md)               | Declares OAuth2 linking methods required by composed identity traits.            |
| [`AbstractRole`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractRole.md)                   | Declares role matching methods required by ACL and impersonation helpers.        |
| [`AbstractSession`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractSession.md)             | Declares identity session methods required by JWT, OAuth2, and user helpers.     |
| [`AbstractUser`](./classes/PhalconKit/Identity/Traits/Abstracts/AbstractUser.md)                   | Declares user-resolution methods required by identity behavior traits.           |

### \PhalconKit\Identity\Traits\Interfaces


| Interface                                                                                             | Description                                                                    |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [`AclInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/AclInterface.md)                     | Contract for building the effective ACL roles of an identity.                  |
| [`ImpersonationInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/ImpersonationInterface.md) | Contract for switching an authenticated session into and out of impersonation. |
| [`JwtInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/JwtInterface.md)                     | Contract for JWT-backed identity claims and token generation.                  |
| [`Oauth2Interface`](./classes/PhalconKit/Identity/Traits/Interfaces/Oauth2Interface.md)               | Contract for linking OAuth2 identities to local PhalconKit users.              |
| [`RoleInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/RoleInterface.md)                   | Contract for role matching and configured role inheritance.                    |
| [`SessionInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/SessionInterface.md)             | Contract for storing identity payloads under the current claim key.            |
| [`UserInterface`](./classes/PhalconKit/Identity/Traits/Interfaces/UserInterface.md)                   | Contract for resolving the effective and impersonating identity users.         |

### \PhalconKit\Locales


| Class                                      | Description                                                  |
|--------------------------------------------|--------------------------------------------------------------|
| [`En`](./classes/PhalconKit/Locales/En.md) | Built-in English translation adapter for framework messages. |
| [`Fr`](./classes/PhalconKit/Locales/Fr.md) | Built-in French translation adapter for framework messages.  |

### \PhalconKit\Logger


| Class                                               | Description                                              |
|-----------------------------------------------------|----------------------------------------------------------|
| [`Loggers`](./classes/PhalconKit/Logger/Loggers.md) | Factory and registry for named Phalcon logger instances. |

### \PhalconKit\Models


| Class                                                                   | Description                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`AbstractModel`](./classes/PhalconKit/Models/AbstractModel.md)         | Events
- afterCreate
- afterDelete
- afterFetch
- afterSave
- afterUpdate
- afterValidation
- afterValidationOnCreate
- afterValidationOnUpdate
- beforeDelete
- beforeCreate
- beforeSave
- beforeUpdate
- beforeValidation
- beforeValidationOnCreate
- beforeValidationOnUpdate
- notDeleted
- notSaved
- onValidationFails
- prepareSave
- validation |
| [`Audit`](./classes/PhalconKit/Models/Audit.md)                         | Class Audit                                                                                                                                                                                                                                                                                                                                               |
| [`AuditDetail`](./classes/PhalconKit/Models/AuditDetail.md)             | Class AuditDetail                                                                                                                                                                                                                                                                                                                                         |
| [`Backup`](./classes/PhalconKit/Models/Backup.md)                       | Class Backup                                                                                                                                                                                                                                                                                                                                              |
| [`Category`](./classes/PhalconKit/Models/Category.md)                   | Class Category                                                                                                                                                                                                                                                                                                                                            |
| [`Column`](./classes/PhalconKit/Models/Column.md)                       | Class Column                                                                                                                                                                                                                                                                                                                                              |
| [`Data`](./classes/PhalconKit/Models/Data.md)                           | Class Data                                                                                                                                                                                                                                                                                                                                                |
| [`Email`](./classes/PhalconKit/Models/Email.md)                         | Class Email                                                                                                                                                                                                                                                                                                                                               |
| [`EmailFile`](./classes/PhalconKit/Models/EmailFile.md)                 | Class EmailFile                                                                                                                                                                                                                                                                                                                                           |
| [`Feature`](./classes/PhalconKit/Models/Feature.md)                     | Class Feature                                                                                                                                                                                                                                                                                                                                             |
| [`File`](./classes/PhalconKit/Models/File.md)                           | Class File                                                                                                                                                                                                                                                                                                                                                |
| [`FileRelation`](./classes/PhalconKit/Models/FileRelation.md)           | Class FileRelation                                                                                                                                                                                                                                                                                                                                        |
| [`Flag`](./classes/PhalconKit/Models/Flag.md)                           | Class Flag                                                                                                                                                                                                                                                                                                                                                |
| [`Group`](./classes/PhalconKit/Models/Group.md)                         | Class Group                                                                                                                                                                                                                                                                                                                                               |
| [`GroupFeature`](./classes/PhalconKit/Models/GroupFeature.md)           | Class GroupFeature                                                                                                                                                                                                                                                                                                                                        |
| [`GroupRole`](./classes/PhalconKit/Models/GroupRole.md)                 | Class GroupRole                                                                                                                                                                                                                                                                                                                                           |
| [`GroupType`](./classes/PhalconKit/Models/GroupType.md)                 | Class GroupType                                                                                                                                                                                                                                                                                                                                           |
| [`Job`](./classes/PhalconKit/Models/Job.md)                             | Class Job                                                                                                                                                                                                                                                                                                                                                 |
| [`JobScheduler`](./classes/PhalconKit/Models/JobScheduler.md)           | Class JobScheduler                                                                                                                                                                                                                                                                                                                                        |
| [`Lang`](./classes/PhalconKit/Models/Lang.md)                           | Class Lang                                                                                                                                                                                                                                                                                                                                                |
| [`Log`](./classes/PhalconKit/Models/Log.md)                             | Class Log                                                                                                                                                                                                                                                                                                                                                 |
| [`Menu`](./classes/PhalconKit/Models/Menu.md)                           | Class Menu                                                                                                                                                                                                                                                                                                                                                |
| [`Meta`](./classes/PhalconKit/Models/Meta.md)                           | Class Meta                                                                                                                                                                                                                                                                                                                                                |
| [`Oauth2`](./classes/PhalconKit/Models/Oauth2.md)                       | Class Oauth2                                                                                                                                                                                                                                                                                                                                              |
| [`Page`](./classes/PhalconKit/Models/Page.md)                           | Class Page                                                                                                                                                                                                                                                                                                                                                |
| [`PhalconMigrations`](./classes/PhalconKit/Models/PhalconMigrations.md) | Class PhalconMigrations                                                                                                                                                                                                                                                                                                                                   |
| [`Post`](./classes/PhalconKit/Models/Post.md)                           | Class Post                                                                                                                                                                                                                                                                                                                                                |
| [`PostCategory`](./classes/PhalconKit/Models/PostCategory.md)           | Class PostCategory                                                                                                                                                                                                                                                                                                                                        |
| [`Profile`](./classes/PhalconKit/Models/Profile.md)                     | Class Profile                                                                                                                                                                                                                                                                                                                                             |
| [`Record`](./classes/PhalconKit/Models/Record.md)                       | Class Record                                                                                                                                                                                                                                                                                                                                              |
| [`Role`](./classes/PhalconKit/Models/Role.md)                           | Class Role                                                                                                                                                                                                                                                                                                                                                |
| [`RoleFeature`](./classes/PhalconKit/Models/RoleFeature.md)             | Class RoleFeature                                                                                                                                                                                                                                                                                                                                         |
| [`RoleRole`](./classes/PhalconKit/Models/RoleRole.md)                   | Class RoleRole                                                                                                                                                                                                                                                                                                                                            |
| [`Session`](./classes/PhalconKit/Models/Session.md)                     | Class Session                                                                                                                                                                                                                                                                                                                                             |
| [`Setting`](./classes/PhalconKit/Models/Setting.md)                     | Class Setting                                                                                                                                                                                                                                                                                                                                             |
| [`Site`](./classes/PhalconKit/Models/Site.md)                           | Class Site                                                                                                                                                                                                                                                                                                                                                |
| [`SiteLang`](./classes/PhalconKit/Models/SiteLang.md)                   | Class SiteLang                                                                                                                                                                                                                                                                                                                                            |
| [`Table`](./classes/PhalconKit/Models/Table.md)                         | Class Table                                                                                                                                                                                                                                                                                                                                               |
| [`Template`](./classes/PhalconKit/Models/Template.md)                   | Class Template                                                                                                                                                                                                                                                                                                                                            |
| [`Translate`](./classes/PhalconKit/Models/Translate.md)                 | Class Translate                                                                                                                                                                                                                                                                                                                                           |
| [`Type`](./classes/PhalconKit/Models/Type.md)                           | Class Type                                                                                                                                                                                                                                                                                                                                                |
| [`User`](./classes/PhalconKit/Models/User.md)                           | Class User                                                                                                                                                                                                                                                                                                                                                |
| [`UserFeature`](./classes/PhalconKit/Models/UserFeature.md)             | Class UserFeature                                                                                                                                                                                                                                                                                                                                         |
| [`UserGroup`](./classes/PhalconKit/Models/UserGroup.md)                 | Class UserGroup                                                                                                                                                                                                                                                                                                                                           |
| [`UserRole`](./classes/PhalconKit/Models/UserRole.md)                   | Class UserRole                                                                                                                                                                                                                                                                                                                                            |
| [`UserType`](./classes/PhalconKit/Models/UserType.md)                   | Class UserType                                                                                                                                                                                                                                                                                                                                            |
| [`Validator`](./classes/PhalconKit/Models/Validator.md)                 | Class Validator                                                                                                                                                                                                                                                                                                                                           |
| [`Workspace`](./classes/PhalconKit/Models/Workspace.md)                 | Class Workspace                                                                                                                                                                                                                                                                                                                                           |
| [`WorkspaceLang`](./classes/PhalconKit/Models/WorkspaceLang.md)         | Class WorkspaceLang                                                                                                                                                                                                                                                                                                                                       |

### \PhalconKit\Models\Abstracts


| Class                                                                                             | Description                     |
|---------------------------------------------------------------------------------------------------|---------------------------------|
| [`AuditAbstract`](./classes/PhalconKit/Models/Abstracts/AuditAbstract.md)                         | Class AuditAbstract             |
| [`AuditDetailAbstract`](./classes/PhalconKit/Models/Abstracts/AuditDetailAbstract.md)             | Class AuditDetailAbstract       |
| [`BackupAbstract`](./classes/PhalconKit/Models/Abstracts/BackupAbstract.md)                       | Class BackupAbstract            |
| [`CategoryAbstract`](./classes/PhalconKit/Models/Abstracts/CategoryAbstract.md)                   | Class CategoryAbstract          |
| [`ColumnAbstract`](./classes/PhalconKit/Models/Abstracts/ColumnAbstract.md)                       | Class ColumnAbstract            |
| [`DataAbstract`](./classes/PhalconKit/Models/Abstracts/DataAbstract.md)                           | Class DataAbstract              |
| [`EmailAbstract`](./classes/PhalconKit/Models/Abstracts/EmailAbstract.md)                         | Class EmailAbstract             |
| [`EmailFileAbstract`](./classes/PhalconKit/Models/Abstracts/EmailFileAbstract.md)                 | Class EmailFileAbstract         |
| [`FeatureAbstract`](./classes/PhalconKit/Models/Abstracts/FeatureAbstract.md)                     | Class FeatureAbstract           |
| [`FileAbstract`](./classes/PhalconKit/Models/Abstracts/FileAbstract.md)                           | Class FileAbstract              |
| [`FileRelationAbstract`](./classes/PhalconKit/Models/Abstracts/FileRelationAbstract.md)           | Class FileRelationAbstract      |
| [`FlagAbstract`](./classes/PhalconKit/Models/Abstracts/FlagAbstract.md)                           | Class FlagAbstract              |
| [`GroupAbstract`](./classes/PhalconKit/Models/Abstracts/GroupAbstract.md)                         | Class GroupAbstract             |
| [`GroupFeatureAbstract`](./classes/PhalconKit/Models/Abstracts/GroupFeatureAbstract.md)           | Class GroupFeatureAbstract      |
| [`GroupRoleAbstract`](./classes/PhalconKit/Models/Abstracts/GroupRoleAbstract.md)                 | Class GroupRoleAbstract         |
| [`GroupTypeAbstract`](./classes/PhalconKit/Models/Abstracts/GroupTypeAbstract.md)                 | Class GroupTypeAbstract         |
| [`JobAbstract`](./classes/PhalconKit/Models/Abstracts/JobAbstract.md)                             | Class JobAbstract               |
| [`JobSchedulerAbstract`](./classes/PhalconKit/Models/Abstracts/JobSchedulerAbstract.md)           | Class JobSchedulerAbstract      |
| [`LangAbstract`](./classes/PhalconKit/Models/Abstracts/LangAbstract.md)                           | Class LangAbstract              |
| [`LogAbstract`](./classes/PhalconKit/Models/Abstracts/LogAbstract.md)                             | Class LogAbstract               |
| [`MenuAbstract`](./classes/PhalconKit/Models/Abstracts/MenuAbstract.md)                           | Class MenuAbstract              |
| [`MetaAbstract`](./classes/PhalconKit/Models/Abstracts/MetaAbstract.md)                           | Class MetaAbstract              |
| [`Oauth2Abstract`](./classes/PhalconKit/Models/Abstracts/Oauth2Abstract.md)                       | Class Oauth2Abstract            |
| [`PageAbstract`](./classes/PhalconKit/Models/Abstracts/PageAbstract.md)                           | Class PageAbstract              |
| [`PhalconMigrationsAbstract`](./classes/PhalconKit/Models/Abstracts/PhalconMigrationsAbstract.md) | Class PhalconMigrationsAbstract |
| [`PostAbstract`](./classes/PhalconKit/Models/Abstracts/PostAbstract.md)                           | Class PostAbstract              |
| [`PostCategoryAbstract`](./classes/PhalconKit/Models/Abstracts/PostCategoryAbstract.md)           | Class PostCategoryAbstract      |
| [`ProfileAbstract`](./classes/PhalconKit/Models/Abstracts/ProfileAbstract.md)                     | Class ProfileAbstract           |
| [`RecordAbstract`](./classes/PhalconKit/Models/Abstracts/RecordAbstract.md)                       | Class RecordAbstract            |
| [`RoleAbstract`](./classes/PhalconKit/Models/Abstracts/RoleAbstract.md)                           | Class RoleAbstract              |
| [`RoleFeatureAbstract`](./classes/PhalconKit/Models/Abstracts/RoleFeatureAbstract.md)             | Class RoleFeatureAbstract       |
| [`RoleRoleAbstract`](./classes/PhalconKit/Models/Abstracts/RoleRoleAbstract.md)                   | Class RoleRoleAbstract          |
| [`SessionAbstract`](./classes/PhalconKit/Models/Abstracts/SessionAbstract.md)                     | Class SessionAbstract           |
| [`SettingAbstract`](./classes/PhalconKit/Models/Abstracts/SettingAbstract.md)                     | Class SettingAbstract           |
| [`SiteAbstract`](./classes/PhalconKit/Models/Abstracts/SiteAbstract.md)                           | Class SiteAbstract              |
| [`SiteLangAbstract`](./classes/PhalconKit/Models/Abstracts/SiteLangAbstract.md)                   | Class SiteLangAbstract          |
| [`TableAbstract`](./classes/PhalconKit/Models/Abstracts/TableAbstract.md)                         | Class TableAbstract             |
| [`TemplateAbstract`](./classes/PhalconKit/Models/Abstracts/TemplateAbstract.md)                   | Class TemplateAbstract          |
| [`TranslateAbstract`](./classes/PhalconKit/Models/Abstracts/TranslateAbstract.md)                 | Class TranslateAbstract         |
| [`TypeAbstract`](./classes/PhalconKit/Models/Abstracts/TypeAbstract.md)                           | Class TypeAbstract              |
| [`UserAbstract`](./classes/PhalconKit/Models/Abstracts/UserAbstract.md)                           | Class UserAbstract              |
| [`UserFeatureAbstract`](./classes/PhalconKit/Models/Abstracts/UserFeatureAbstract.md)             | Class UserFeatureAbstract       |
| [`UserGroupAbstract`](./classes/PhalconKit/Models/Abstracts/UserGroupAbstract.md)                 | Class UserGroupAbstract         |
| [`UserRoleAbstract`](./classes/PhalconKit/Models/Abstracts/UserRoleAbstract.md)                   | Class UserRoleAbstract          |
| [`UserTypeAbstract`](./classes/PhalconKit/Models/Abstracts/UserTypeAbstract.md)                   | Class UserTypeAbstract          |
| [`ValidatorAbstract`](./classes/PhalconKit/Models/Abstracts/ValidatorAbstract.md)                 | Class ValidatorAbstract         |
| [`WorkspaceAbstract`](./classes/PhalconKit/Models/Abstracts/WorkspaceAbstract.md)                 | Class WorkspaceAbstract         |
| [`WorkspaceLangAbstract`](./classes/PhalconKit/Models/Abstracts/WorkspaceLangAbstract.md)         | Class WorkspaceLangAbstract     |

### \PhalconKit\Models\Abstracts\Interfaces


| Interface                                                                                                                      | Description |
|--------------------------------------------------------------------------------------------------------------------------------|-------------|
| [`AuditAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/AuditAbstractInterface.md)                         |             |
| [`AuditDetailAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/AuditDetailAbstractInterface.md)             |             |
| [`BackupAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/BackupAbstractInterface.md)                       |             |
| [`CategoryAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/CategoryAbstractInterface.md)                   |             |
| [`ColumnAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/ColumnAbstractInterface.md)                       |             |
| [`DataAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/DataAbstractInterface.md)                           |             |
| [`EmailAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/EmailAbstractInterface.md)                         |             |
| [`EmailFileAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/EmailFileAbstractInterface.md)                 |             |
| [`FeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FeatureAbstractInterface.md)                     |             |
| [`FileAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FileAbstractInterface.md)                           |             |
| [`FileRelationAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FileRelationAbstractInterface.md)           |             |
| [`FlagAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/FlagAbstractInterface.md)                           |             |
| [`GroupAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupAbstractInterface.md)                         |             |
| [`GroupFeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupFeatureAbstractInterface.md)           |             |
| [`GroupRoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupRoleAbstractInterface.md)                 |             |
| [`GroupTypeAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/GroupTypeAbstractInterface.md)                 |             |
| [`JobAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/JobAbstractInterface.md)                             |             |
| [`JobSchedulerAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/JobSchedulerAbstractInterface.md)           |             |
| [`LangAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/LangAbstractInterface.md)                           |             |
| [`LogAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/LogAbstractInterface.md)                             |             |
| [`MenuAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/MenuAbstractInterface.md)                           |             |
| [`MetaAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/MetaAbstractInterface.md)                           |             |
| [`Oauth2AbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/Oauth2AbstractInterface.md)                       |             |
| [`PageAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PageAbstractInterface.md)                           |             |
| [`PhalconMigrationsAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PhalconMigrationsAbstractInterface.md) |             |
| [`PostAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PostAbstractInterface.md)                           |             |
| [`PostCategoryAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/PostCategoryAbstractInterface.md)           |             |
| [`ProfileAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/ProfileAbstractInterface.md)                     |             |
| [`RecordAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RecordAbstractInterface.md)                       |             |
| [`RoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RoleAbstractInterface.md)                           |             |
| [`RoleFeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RoleFeatureAbstractInterface.md)             |             |
| [`RoleRoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/RoleRoleAbstractInterface.md)                   |             |
| [`SessionAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SessionAbstractInterface.md)                     |             |
| [`SettingAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SettingAbstractInterface.md)                     |             |
| [`SiteAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SiteAbstractInterface.md)                           |             |
| [`SiteLangAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/SiteLangAbstractInterface.md)                   |             |
| [`TableAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TableAbstractInterface.md)                         |             |
| [`TemplateAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TemplateAbstractInterface.md)                   |             |
| [`TranslateAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TranslateAbstractInterface.md)                 |             |
| [`TypeAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/TypeAbstractInterface.md)                           |             |
| [`UserAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserAbstractInterface.md)                           |             |
| [`UserFeatureAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserFeatureAbstractInterface.md)             |             |
| [`UserGroupAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserGroupAbstractInterface.md)                 |             |
| [`UserRoleAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserRoleAbstractInterface.md)                   |             |
| [`UserTypeAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/UserTypeAbstractInterface.md)                   |             |
| [`ValidatorAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/ValidatorAbstractInterface.md)                 |             |
| [`WorkspaceAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/WorkspaceAbstractInterface.md)                 |             |
| [`WorkspaceLangAbstractInterface`](./classes/PhalconKit/Models/Abstracts/Interfaces/WorkspaceLangAbstractInterface.md)         |             |

### \PhalconKit\Models\Behaviors


| Interface                                                                             | Description |
|---------------------------------------------------------------------------------------|-------------|
| [`BlameableInterface`](./classes/PhalconKit/Models/Behaviors/BlameableInterface.md)   |             |
| [`SoftDeleteInterface`](./classes/PhalconKit/Models/Behaviors/SoftDeleteInterface.md) |             |

### \PhalconKit\Models\Behaviors\Blameable


| Interface                                                                                   | Description |
|---------------------------------------------------------------------------------------------|-------------|
| [`CreatedInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/CreatedInterface.md)   |             |
| [`DeletedInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/DeletedInterface.md)   |             |
| [`RestoredInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/RestoredInterface.md) |             |
| [`UpdateInterface`](./classes/PhalconKit/Models/Behaviors/Blameable/UpdateInterface.md)     |             |

### \PhalconKit\Models\Interfaces


| Interface                                                                                            | Description |
|------------------------------------------------------------------------------------------------------|-------------|
| [`AuditDetailInterface`](./classes/PhalconKit/Models/Interfaces/AuditDetailInterface.md)             |             |
| [`AuditInterface`](./classes/PhalconKit/Models/Interfaces/AuditInterface.md)                         |             |
| [`BackupInterface`](./classes/PhalconKit/Models/Interfaces/BackupInterface.md)                       |             |
| [`CategoryInterface`](./classes/PhalconKit/Models/Interfaces/CategoryInterface.md)                   |             |
| [`ColumnInterface`](./classes/PhalconKit/Models/Interfaces/ColumnInterface.md)                       |             |
| [`DataInterface`](./classes/PhalconKit/Models/Interfaces/DataInterface.md)                           |             |
| [`EmailFileInterface`](./classes/PhalconKit/Models/Interfaces/EmailFileInterface.md)                 |             |
| [`EmailInterface`](./classes/PhalconKit/Models/Interfaces/EmailInterface.md)                         |             |
| [`FeatureInterface`](./classes/PhalconKit/Models/Interfaces/FeatureInterface.md)                     |             |
| [`FileInterface`](./classes/PhalconKit/Models/Interfaces/FileInterface.md)                           |             |
| [`FileRelationInterface`](./classes/PhalconKit/Models/Interfaces/FileRelationInterface.md)           |             |
| [`FlagInterface`](./classes/PhalconKit/Models/Interfaces/FlagInterface.md)                           |             |
| [`GroupFeatureInterface`](./classes/PhalconKit/Models/Interfaces/GroupFeatureInterface.md)           |             |
| [`GroupInterface`](./classes/PhalconKit/Models/Interfaces/GroupInterface.md)                         |             |
| [`GroupRoleInterface`](./classes/PhalconKit/Models/Interfaces/GroupRoleInterface.md)                 |             |
| [`GroupTypeInterface`](./classes/PhalconKit/Models/Interfaces/GroupTypeInterface.md)                 |             |
| [`JobInterface`](./classes/PhalconKit/Models/Interfaces/JobInterface.md)                             |             |
| [`JobSchedulerInterface`](./classes/PhalconKit/Models/Interfaces/JobSchedulerInterface.md)           |             |
| [`LangInterface`](./classes/PhalconKit/Models/Interfaces/LangInterface.md)                           |             |
| [`LogInterface`](./classes/PhalconKit/Models/Interfaces/LogInterface.md)                             |             |
| [`MenuInterface`](./classes/PhalconKit/Models/Interfaces/MenuInterface.md)                           |             |
| [`MetaInterface`](./classes/PhalconKit/Models/Interfaces/MetaInterface.md)                           |             |
| [`Oauth2Interface`](./classes/PhalconKit/Models/Interfaces/Oauth2Interface.md)                       |             |
| [`PageInterface`](./classes/PhalconKit/Models/Interfaces/PageInterface.md)                           |             |
| [`PhalconMigrationsInterface`](./classes/PhalconKit/Models/Interfaces/PhalconMigrationsInterface.md) |             |
| [`PostCategoryInterface`](./classes/PhalconKit/Models/Interfaces/PostCategoryInterface.md)           |             |
| [`PostInterface`](./classes/PhalconKit/Models/Interfaces/PostInterface.md)                           |             |
| [`ProfileInterface`](./classes/PhalconKit/Models/Interfaces/ProfileInterface.md)                     |             |
| [`RecordInterface`](./classes/PhalconKit/Models/Interfaces/RecordInterface.md)                       |             |
| [`RoleFeatureInterface`](./classes/PhalconKit/Models/Interfaces/RoleFeatureInterface.md)             |             |
| [`RoleInterface`](./classes/PhalconKit/Models/Interfaces/RoleInterface.md)                           |             |
| [`RoleRoleInterface`](./classes/PhalconKit/Models/Interfaces/RoleRoleInterface.md)                   |             |
| [`SessionInterface`](./classes/PhalconKit/Models/Interfaces/SessionInterface.md)                     |             |
| [`SettingInterface`](./classes/PhalconKit/Models/Interfaces/SettingInterface.md)                     |             |
| [`SiteInterface`](./classes/PhalconKit/Models/Interfaces/SiteInterface.md)                           |             |
| [`SiteLangInterface`](./classes/PhalconKit/Models/Interfaces/SiteLangInterface.md)                   |             |
| [`TableInterface`](./classes/PhalconKit/Models/Interfaces/TableInterface.md)                         |             |
| [`TemplateInterface`](./classes/PhalconKit/Models/Interfaces/TemplateInterface.md)                   |             |
| [`TranslateInterface`](./classes/PhalconKit/Models/Interfaces/TranslateInterface.md)                 |             |
| [`TypeInterface`](./classes/PhalconKit/Models/Interfaces/TypeInterface.md)                           |             |
| [`UserFeatureInterface`](./classes/PhalconKit/Models/Interfaces/UserFeatureInterface.md)             |             |
| [`UserGroupInterface`](./classes/PhalconKit/Models/Interfaces/UserGroupInterface.md)                 |             |
| [`UserInterface`](./classes/PhalconKit/Models/Interfaces/UserInterface.md)                           |             |
| [`UserRoleInterface`](./classes/PhalconKit/Models/Interfaces/UserRoleInterface.md)                   |             |
| [`UserTypeInterface`](./classes/PhalconKit/Models/Interfaces/UserTypeInterface.md)                   |             |
| [`ValidatorInterface`](./classes/PhalconKit/Models/Interfaces/ValidatorInterface.md)                 |             |
| [`WorkspaceInterface`](./classes/PhalconKit/Models/Interfaces/WorkspaceInterface.md)                 |             |
| [`WorkspaceLangInterface`](./classes/PhalconKit/Models/Interfaces/WorkspaceLangInterface.md)         |             |

### \PhalconKit\Modules\Admin


| Class                                                            | Description                                                |
|------------------------------------------------------------------|------------------------------------------------------------|
| [`Controller`](./classes/PhalconKit/Modules/Admin/Controller.md) | Base MVC controller for PhalconKit applications.           |
| [`Module`](./classes/PhalconKit/Modules/Admin/Module.md)         | Base MVC module definition used by PhalconKit web modules. |

### \PhalconKit\Modules\Admin\Controllers


| Class                                                                                        | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Admin/Controllers/AbstractController.md) | Base MVC controller for PhalconKit applications. |
| [`ErrorController`](./classes/PhalconKit/Modules/Admin/Controllers/ErrorController.md)       | Base MVC controller for PhalconKit applications. |
| [`IndexController`](./classes/PhalconKit/Modules/Admin/Controllers/IndexController.md)       | Base MVC controller for PhalconKit applications. |

### \PhalconKit\Modules\Api


| Class                                                          | Description                                                |
|----------------------------------------------------------------|------------------------------------------------------------|
| [`Controller`](./classes/PhalconKit/Modules/Api/Controller.md) | Base MVC controller for PhalconKit applications.           |
| [`Module`](./classes/PhalconKit/Modules/Api/Module.md)         | Base MVC module definition used by PhalconKit web modules. |

### \PhalconKit\Modules\Api\Controllers


| Class                                                                                                        | Description                                           |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Api/Controllers/AbstractController.md)                   | Base MVC controller for PhalconKit applications.      |
| [`AuditController`](./classes/PhalconKit/Modules/Api/Controllers/AuditController.md)                         | Base MVC controller for PhalconKit applications.      |
| [`AuditDetailController`](./classes/PhalconKit/Modules/Api/Controllers/AuditDetailController.md)             | Base MVC controller for PhalconKit applications.      |
| [`AuthController`](./classes/PhalconKit/Modules/Api/Controllers/AuthController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`CategoryController`](./classes/PhalconKit/Modules/Api/Controllers/CategoryController.md)                   | Base MVC controller for PhalconKit applications.      |
| [`ClamavController`](./classes/PhalconKit/Modules/Api/Controllers/ClamavController.md)                       | Base MVC controller for PhalconKit applications.      |
| [`ColumnController`](./classes/PhalconKit/Modules/Api/Controllers/ColumnController.md)                       | Base MVC controller for PhalconKit applications.      |
| [`DataController`](./classes/PhalconKit/Modules/Api/Controllers/DataController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`EmailController`](./classes/PhalconKit/Modules/Api/Controllers/EmailController.md)                         | Base MVC controller for PhalconKit applications.      |
| [`ErrorController`](./classes/PhalconKit/Modules/Api/Controllers/ErrorController.md)                         | API error endpoint without model-backed REST actions. |
| [`FieldController`](./classes/PhalconKit/Modules/Api/Controllers/FieldController.md)                         | Base MVC controller for PhalconKit applications.      |
| [`FileController`](./classes/PhalconKit/Modules/Api/Controllers/FileController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`FlagController`](./classes/PhalconKit/Modules/Api/Controllers/FlagController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`GroupController`](./classes/PhalconKit/Modules/Api/Controllers/GroupController.md)                         | Base MVC controller for PhalconKit applications.      |
| [`IndexController`](./classes/PhalconKit/Modules/Api/Controllers/IndexController.md)                         | Base MVC controller for PhalconKit applications.      |
| [`LangController`](./classes/PhalconKit/Modules/Api/Controllers/LangController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`LogController`](./classes/PhalconKit/Modules/Api/Controllers/LogController.md)                             | Base MVC controller for PhalconKit applications.      |
| [`MenuController`](./classes/PhalconKit/Modules/Api/Controllers/MenuController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`MetaController`](./classes/PhalconKit/Modules/Api/Controllers/MetaController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`PageController`](./classes/PhalconKit/Modules/Api/Controllers/PageController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`PhalconMigrationsController`](./classes/PhalconKit/Modules/Api/Controllers/PhalconMigrationsController.md) | Base MVC controller for PhalconKit applications.      |
| [`PostController`](./classes/PhalconKit/Modules/Api/Controllers/PostController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`ProfileController`](./classes/PhalconKit/Modules/Api/Controllers/ProfileController.md)                     | Base MVC controller for PhalconKit applications.      |
| [`RecordController`](./classes/PhalconKit/Modules/Api/Controllers/RecordController.md)                       | Base MVC controller for PhalconKit applications.      |
| [`RoleController`](./classes/PhalconKit/Modules/Api/Controllers/RoleController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`SessionController`](./classes/PhalconKit/Modules/Api/Controllers/SessionController.md)                     | Base MVC controller for PhalconKit applications.      |
| [`SettingController`](./classes/PhalconKit/Modules/Api/Controllers/SettingController.md)                     | Base MVC controller for PhalconKit applications.      |
| [`TableController`](./classes/PhalconKit/Modules/Api/Controllers/TableController.md)                         | Base MVC controller for PhalconKit applications.      |
| [`TemplateController`](./classes/PhalconKit/Modules/Api/Controllers/TemplateController.md)                   | Base MVC controller for PhalconKit applications.      |
| [`TestController`](./classes/PhalconKit/Modules/Api/Controllers/TestController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`TranslateController`](./classes/PhalconKit/Modules/Api/Controllers/TranslateController.md)                 | Base MVC controller for PhalconKit applications.      |
| [`TranslateFieldController`](./classes/PhalconKit/Modules/Api/Controllers/TranslateFieldController.md)       | Base MVC controller for PhalconKit applications.      |
| [`TranslateTableController`](./classes/PhalconKit/Modules/Api/Controllers/TranslateTableController.md)       | Base MVC controller for PhalconKit applications.      |
| [`TypeController`](./classes/PhalconKit/Modules/Api/Controllers/TypeController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`UserController`](./classes/PhalconKit/Modules/Api/Controllers/UserController.md)                           | Base MVC controller for PhalconKit applications.      |
| [`WorkspaceController`](./classes/PhalconKit/Modules/Api/Controllers/WorkspaceController.md)                 | Base MVC controller for PhalconKit applications.      |

### \PhalconKit\Modules\Api\Transformers


| Class                                                                                     | Description                                                      |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [`RecordTransformer`](./classes/PhalconKit/Modules/Api/Transformers/RecordTransformer.md) | Base transformer for Fractal resources backed by Phalcon models. |

### \PhalconKit\Modules\Cli


| Class                                                  | Description                          |
|--------------------------------------------------------|--------------------------------------|
| [`Module`](./classes/PhalconKit/Modules/Cli/Module.md) | Default CLI module definition.       |
| [`Task`](./classes/PhalconKit/Modules/Cli/Task.md)     | Base class for PhalconKit CLI tasks. |

### \PhalconKit\Modules\Cli\Tasks


| Class                                                                              | Description                          |
|------------------------------------------------------------------------------------|--------------------------------------|
| [`AbstractTask`](./classes/PhalconKit/Modules/Cli/Tasks/AbstractTask.md)           | Base class for PhalconKit CLI tasks. |
| [`CacheTask`](./classes/PhalconKit/Modules/Cli/Tasks/CacheTask.md)                 | Base class for PhalconKit CLI tasks. |
| [`CronTask`](./classes/PhalconKit/Modules/Cli/Tasks/CronTask.md)                   | Base class for PhalconKit CLI tasks. |
| [`DatabaseTask`](./classes/PhalconKit/Modules/Cli/Tasks/DatabaseTask.md)           | Base class for PhalconKit CLI tasks. |
| [`DataLifeCycleTask`](./classes/PhalconKit/Modules/Cli/Tasks/DataLifeCycleTask.md) | Base class for PhalconKit CLI tasks. |
| [`ErrorTask`](./classes/PhalconKit/Modules/Cli/Tasks/ErrorTask.md)                 | Base class for PhalconKit CLI tasks. |
| [`FakerTask`](./classes/PhalconKit/Modules/Cli/Tasks/FakerTask.md)                 | Base class for PhalconKit CLI tasks. |
| [`HelpTask`](./classes/PhalconKit/Modules/Cli/Tasks/HelpTask.md)                   | Base class for PhalconKit CLI tasks. |
| [`ScaffoldTask`](./classes/PhalconKit/Modules/Cli/Tasks/ScaffoldTask.md)           | Base class for PhalconKit CLI tasks. |
| [`TsScaffoldTask`](./classes/PhalconKit/Modules/Cli/Tasks/TsScaffoldTask.md)       | Base class for PhalconKit CLI tasks. |
| [`UserTask`](./classes/PhalconKit/Modules/Cli/Tasks/UserTask.md)                   | Base class for PhalconKit CLI tasks. |

### \PhalconKit\Modules\Cli\Tasks\Traits


| Trait                                                                               | Description          |
|-------------------------------------------------------------------------------------|----------------------|
| [`DatabaseTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/DatabaseTrait.md)   |                      |
| [`DescribesTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/DescribesTrait.md) | Trait DescribesTrait |
| [`ScaffoldTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/ScaffoldTrait.md)   | Trait DescribesTrait |
| [`UserTrait`](./classes/PhalconKit/Modules/Cli/Tasks/Traits/UserTrait.md)           |                      |

### \PhalconKit\Modules\Frontend


| Class                                                               | Description                                                |
|---------------------------------------------------------------------|------------------------------------------------------------|
| [`Controller`](./classes/PhalconKit/Modules/Frontend/Controller.md) | Base MVC controller for PhalconKit applications.           |
| [`Module`](./classes/PhalconKit/Modules/Frontend/Module.md)         | Base MVC module definition used by PhalconKit web modules. |

### \PhalconKit\Modules\Frontend\Controllers


| Class                                                                                           | Description                                      |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Frontend/Controllers/AbstractController.md) | Base MVC controller for PhalconKit applications. |
| [`ErrorController`](./classes/PhalconKit/Modules/Frontend/Controllers/ErrorController.md)       | Base MVC controller for PhalconKit applications. |
| [`IndexController`](./classes/PhalconKit/Modules/Frontend/Controllers/IndexController.md)       | Base MVC controller for PhalconKit applications. |

### \PhalconKit\Modules\Oauth2


| Class                                                             | Description                                                |
|-------------------------------------------------------------------|------------------------------------------------------------|
| [`Controller`](./classes/PhalconKit/Modules/Oauth2/Controller.md) | Base MVC controller for PhalconKit applications.           |
| [`Module`](./classes/PhalconKit/Modules/Oauth2/Module.md)         | Base MVC module definition used by PhalconKit web modules. |

### \PhalconKit\Modules\Oauth2\Controllers


| Class                                                                                           | Description                                      |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [`AbstractController`](./classes/PhalconKit/Modules/Oauth2/Controllers/AbstractController.md)   | Base MVC controller for PhalconKit applications. |
| [`ClientController`](./classes/PhalconKit/Modules/Oauth2/Controllers/ClientController.md)       | Base MVC controller for PhalconKit applications. |
| [`FacebookController`](./classes/PhalconKit/Modules/Oauth2/Controllers/FacebookController.md)   | Base MVC controller for PhalconKit applications. |
| [`GithubController`](./classes/PhalconKit/Modules/Oauth2/Controllers/GithubController.md)       | Base MVC controller for PhalconKit applications. |
| [`GoogleController`](./classes/PhalconKit/Modules/Oauth2/Controllers/GoogleController.md)       | Base MVC controller for PhalconKit applications. |
| [`InstagramController`](./classes/PhalconKit/Modules/Oauth2/Controllers/InstagramController.md) | Base MVC controller for PhalconKit applications. |
| [`LinkedinController`](./classes/PhalconKit/Modules/Oauth2/Controllers/LinkedinController.md)   | Base MVC controller for PhalconKit applications. |

### \PhalconKit\Modules\Ws


| Class                                                 | Description                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------|
| [`Module`](./classes/PhalconKit/Modules/Ws/Module.md) | WebSocket module definition backed by Phalcon's CLI-style dispatcher. |
| [`Task`](./classes/PhalconKit/Modules/Ws/Task.md)     | Base class for WebSocket tasks.                                       |

### \PhalconKit\Modules\Ws\Tasks


| Class                                                                   | Description                     |
|-------------------------------------------------------------------------|---------------------------------|
| [`AbstractTask`](./classes/PhalconKit/Modules/Ws/Tasks/AbstractTask.md) | Base class for WebSocket tasks. |
| [`ErrorTask`](./classes/PhalconKit/Modules/Ws/Tasks/ErrorTask.md)       | Base class for WebSocket tasks. |

### \PhalconKit\Mvc


| Class                                                    | Description                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`Application`](./classes/PhalconKit/Mvc/Application.md) | MVC application with PhalconKit's typed DI boundary and HMVC helper.                                                                                                                                                                                                                                                                                      |
| [`Controller`](./classes/PhalconKit/Mvc/Controller.md)   | Base MVC controller for PhalconKit applications.                                                                                                                                                                                                                                                                                                          |
| [`Dispatcher`](./classes/PhalconKit/Mvc/Dispatcher.md)   | MVC dispatcher with PhalconKit's shared dispatcher safeguards.                                                                                                                                                                                                                                                                                            |
| [`Model`](./classes/PhalconKit/Mvc/Model.md)             | Events
- afterCreate
- afterDelete
- afterFetch
- afterSave
- afterUpdate
- afterValidation
- afterValidationOnCreate
- afterValidationOnUpdate
- beforeDelete
- beforeCreate
- beforeSave
- beforeUpdate
- beforeValidation
- beforeValidationOnCreate
- beforeValidationOnUpdate
- notDeleted
- notSaved
- onValidationFails
- prepareSave
- validation |
| [`Module`](./classes/PhalconKit/Mvc/Module.md)           | Base MVC module definition used by PhalconKit web modules.                                                                                                                                                                                                                                                                                                |
| [`Router`](./classes/PhalconKit/Mvc/Router.md)           | Framework router with config-backed module and locale route registration.                                                                                                                                                                                                                                                                                 |
| [`Url`](./classes/PhalconKit/Mvc/Url.md)                 | URL service that normalizes generated local paths.                                                                                                                                                                                                                                                                                                        |
| [`View`](./classes/PhalconKit/Mvc/View.md)               | MVC view wrapper with PhalconKit path normalization and optional minification.                                                                                                                                                                                                                                                                            |


| Interface                                                      | Description |
|----------------------------------------------------------------|-------------|
| [`ModelInterface`](./classes/PhalconKit/Mvc/ModelInterface.md) |             |

### \PhalconKit\Mvc\Controller


| Class                                                       | Description                                      |
|-------------------------------------------------------------|--------------------------------------------------|
| [`Error`](./classes/PhalconKit/Mvc/Controller/Error.md)     | Base MVC controller for PhalconKit applications. |
| [`Rest`](./classes/PhalconKit/Mvc/Controller/Rest.md)       | Base MVC controller for PhalconKit applications. |
| [`Restful`](./classes/PhalconKit/Mvc/Controller/Restful.md) | Base MVC controller for PhalconKit applications. |


| Interface                                                                     | Description                                    |
|-------------------------------------------------------------------------------|------------------------------------------------|
| [`RestfulInterface`](./classes/PhalconKit/Mvc/Controller/RestfulInterface.md) | Contract for full resource controllers.        |
| [`RestInterface`](./classes/PhalconKit/Mvc/Controller/RestInterface.md)       | Base contract for PhalconKit REST controllers. |

### \PhalconKit\Mvc\Controller\Attributes


| Class                                                                                                          | Description                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [`AllowRoles`](./classes/PhalconKit/Mvc/Controller/Attributes/AllowRoles.md)                                   | Grants controller actions directly to one or more ACL roles.                 |
| [`AttachBehavior`](./classes/PhalconKit/Mvc/Controller/Attributes/AttachBehavior.md)                           | Attaches controller behaviors through role or feature permissions.           |
| [`PermissionAttributeResolver`](./classes/PhalconKit/Mvc/Controller/Attributes/PermissionAttributeResolver.md) | Compiles controller PHP attributes into PhalconKit permission config arrays. |
| [`PermissionFeature`](./classes/PhalconKit/Mvc/Controller/Attributes/PermissionFeature.md)                     | Declares controller actions that belong to one or more permission features.  |

### \PhalconKit\Mvc\Controller\Behavior\Model


| Class                                                                      | Description                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`Create`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Create.md)   | Reserved controller behavior marker for create-oriented model workflows.  |
| [`Delete`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Delete.md)   | Reserved controller behavior marker for delete-oriented model workflows.  |
| [`Restore`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Restore.md) | Reserved controller behavior marker for restore-oriented model workflows. |
| [`Update`](./classes/PhalconKit/Mvc/Controller/Behavior/Model/Update.md)   | Reserved controller behavior marker for update-oriented model workflows.  |

### \PhalconKit\Mvc\Controller\Behavior\Query


| Class                                                                                            | Description                                                                     |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [`RemoveBind`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveBind.md)                 | Clears all prepared bind values after REST bind initialization.                 |
| [`RemoveCacheConfig`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveCacheConfig.md)   | Clears REST cache options after cache configuration is initialized.             |
| [`RemoveColumn`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveColumn.md)             | Clears configured query columns after column initialization.                    |
| [`RemoveConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveConditions.md)     | Clears the combined condition collection after REST conditions are initialized. |
| [`RemoveDefaultLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveDefaultLimit.md) | Disables default pagination before REST query initialization.                   |
| [`RemoveDistinct`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveDistinct.md)         | Clears distinct query expressions after distinct initialization.                |
| [`RemoveGroup`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveGroup.md)               | Clears group-by expressions after group initialization.                         |
| [`RemoveHaving`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveHaving.md)             | Clears HAVING predicates after HAVING initialization.                           |
| [`RemoveJoins`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveJoins.md)               | Clears configured and dynamic joins after join initialization.                  |
| [`RemoveLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveLimit.md)               | Resets the current limit to the configured maximum after limit initialization.  |
| [`RemoveMaxLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveMaxLimit.md)         | Disables the maximum pagination limit before REST query initialization.         |
| [`RemoveOffset`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveOffset.md)             | Resets request/configured pagination offset after offset initialization.        |
| [`RemoveWith`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/RemoveWith.md)                 | Clears eager-loading relation requests after `with` initialization.             |

### \PhalconKit\Mvc\Controller\Behavior\Query\Conditions


| Class                                                                                                                                                               | Description                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [`RemoveDefaultFilterCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultFilterCondition.md)                                     | Removes only the default request-filter condition after condition initialization.          |
| [`RemoveDefaultIdentityCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultIdentityCondition.md)                                 | Removes only the default identity-scope condition after initialization.                    |
| [`RemoveDefaultPermissionCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultPermissionCondition.md)                             | Removes only the default permission condition after initialization.                        |
| [`RemoveDefaultSearchCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultSearchCondition.md)                                     | Removes only the default search condition after initialization.                            |
| [`RemoveDefaultSoftDeleteCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultSoftDeleteCondition.md)                             | Removes only the default soft-delete condition after initialization.                       |
| [`RemoveDefaultSoftDeleteConditionWhileFiltering`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveDefaultSoftDeleteConditionWhileFiltering.md) | Removes the default soft-delete condition only when the request filters by deletion state. |
| [`RemoveFilterConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveFilterConditions.md)                                                 | Clears all request-filter conditions after condition initialization.                       |
| [`RemoveIdentityConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveIdentityConditions.md)                                             | Clears all identity-scope conditions after condition initialization.                       |
| [`RemovePermissionConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemovePermissionConditions.md)                                         | Clears all permission conditions after condition initialization.                           |
| [`RemoveSearchConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveSearchConditions.md)                                                 | Clears all search conditions after condition initialization.                               |
| [`RemoveSoftDeleteConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveSoftDeleteConditions.md)                                         | Clears all soft-delete conditions after condition initialization.                          |
| [`RemoveSoftDeleteConditionsWhileFiltering`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Conditions/RemoveSoftDeleteConditionsWhileFiltering.md)             | Clears all soft-delete conditions only when the request filters by deletion state.         |

### \PhalconKit\Mvc\Controller\Behavior\Query\Fields


| Class                                                                                                   | Description                                                         |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`RemoveExposeFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveExposeFields.md) | Clears exposed-field rules after REST field initialization.         |
| [`RemoveFilterFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveFilterFields.md) | Clears filterable-field rules after REST field initialization.      |
| [`RemoveMapFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveMapFields.md)       | Clears API-to-model field mapping rules after field initialization. |
| [`RemoveSaveFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveSaveFields.md)     | Clears saveable-field rules after REST field initialization.        |
| [`RemoveSearchFields`](./classes/PhalconKit/Mvc/Controller/Behavior/Query/Fields/RemoveSearchFields.md) | Clears searchable-field rules after REST field initialization.      |

### \PhalconKit\Mvc\Controller\Behavior\Skip


| Class                                                                                                     | Description                                                               |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`SkipBind`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipBind.md)                               | Behavior flag that disables REST query bind initialization for an action. |
| [`SkipBindTypes`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipBindTypes.md)                     | Behavior flag that disables REST query bind-type initialization.          |
| [`SkipCache`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipCache.md)                             | Behavior flag that disables REST query cache-option initialization.       |
| [`SkipColumns`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipColumns.md)                         | Behavior flag that disables selected-column initialization.               |
| [`SkipConditions`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipConditions.md)                   | Behavior flag that disables the combined REST condition collection.       |
| [`SkipDistinct`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipDistinct.md)                       | Behavior flag that disables distinct-expression initialization.           |
| [`SkipFilterCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipFilterCondition.md)         | Behavior flag that disables request-filter condition initialization.      |
| [`SkipGroup`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipGroup.md)                             | Behavior flag that disables group-by initialization.                      |
| [`SkipHaving`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipHaving.md)                           | Behavior flag that disables HAVING-clause initialization.                 |
| [`SkipIdentityCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipIdentityCondition.md)     | Behavior flag that disables identity-scope condition initialization.      |
| [`SkipJoins`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipJoins.md)                             | Behavior flag that disables REST join initialization.                     |
| [`SkipLimit`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipLimit.md)                             | Behavior flag that disables limit initialization.                         |
| [`SkipOffset`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipOffset.md)                           | Behavior flag that disables offset initialization.                        |
| [`SkipOrder`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipOrder.md)                             | Behavior flag that disables order-by initialization.                      |
| [`SkipPermissionCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipPermissionCondition.md) | Behavior flag that disables permission condition initialization.          |
| [`SkipSearchCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipSearchCondition.md)         | Behavior flag that disables search condition initialization.              |
| [`SkipSoftDeleteCondition`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipSoftDeleteCondition.md) | Removes the default soft-delete condition after condition assembly.       |
| [`SkipWhiteList`](./classes/PhalconKit/Mvc/Controller/Behavior/Skip/SkipWhiteList.md)                     | Behavior flag that disables whitelist initialization.                     |

### \PhalconKit\Mvc\Controller\Traits


| Trait                                                                        | Description                                                                                       |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [`Behavior`](./classes/PhalconKit/Mvc/Controller/Traits/Behavior.md)         |                                                                                                   |
| [`Debug`](./classes/PhalconKit/Mvc/Controller/Traits/Debug.md)               |                                                                                                   |
| [`Export`](./classes/PhalconKit/Mvc/Controller/Traits/Export.md)             | Provides some utility methods to export data                                                      |
| [`Expose`](./classes/PhalconKit/Mvc/Controller/Traits/Expose.md)             |                                                                                                   |
| [`Fractal`](./classes/PhalconKit/Mvc/Controller/Traits/Fractal.md)           | This trait provides methods for working with Fractal, a library for transforming data structures. |
| [`Model`](./classes/PhalconKit/Mvc/Controller/Traits/Model.md)               |                                                                                                   |
| [`Params`](./classes/PhalconKit/Mvc/Controller/Traits/Params.md)             |                                                                                                   |
| [`Query`](./classes/PhalconKit/Mvc/Controller/Traits/Query.md)               | Shared REST query builder for PhalconKit controllers.                                             |
| [`RestResponse`](./classes/PhalconKit/Mvc/Controller/Traits/RestResponse.md) |                                                                                                   |
| [`StatusCode`](./classes/PhalconKit/Mvc/Controller/Traits/StatusCode.md)     | Set the status code to the response                                                               |

### \PhalconKit\Mvc\Controller\Traits\Abstracts


| Trait                                                                                                  | Description                                                                 |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`AbstractBehavior`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractBehavior.md)         |                                                                             |
| [`AbstractDebug`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractDebug.md)               |                                                                             |
| [`AbstractExport`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractExport.md)             |                                                                             |
| [`AbstractExpose`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractExpose.md)             |                                                                             |
| [`AbstractFractal`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractFractal.md)           |                                                                             |
| [`AbstractInjectable`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractInjectable.md)     | Trait AbstractInjectable                                                    |
| [`AbstractModel`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractModel.md)               |                                                                             |
| [`AbstractParams`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractParams.md)             |                                                                             |
| [`AbstractQuery`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractQuery.md)               | Abstract contract consumed by traits that delegate to the REST query layer. |
| [`AbstractRestResponse`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractRestResponse.md) |                                                                             |
| [`AbstractStatusCode`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/AbstractStatusCode.md)     |                                                                             |

### \PhalconKit\Mvc\Controller\Traits\Abstracts\Query


| Trait                                                                                                    | Description                                                          |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [`AbstractBind`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractBind.md)             | Abstract contract for query bind values and bind types.              |
| [`AbstractCache`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractCache.md)           | Abstract contract for query result cache options.                    |
| [`AbstractColumn`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractColumn.md)         | Abstract contract for aggregate column selection.                    |
| [`AbstractConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractConditions.md) | Abstract contract for the composed REST query condition collections. |
| [`AbstractDistinct`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractDistinct.md)     | Abstract contract for SELECT DISTINCT configuration.                 |
| [`AbstractFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractFields.md)         | Abstract contract that groups all REST field-policy collections.     |
| [`AbstractGroup`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractGroup.md)           | Abstract contract for GROUP BY query configuration.                  |
| [`AbstractHaving`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractHaving.md)         | Abstract contract for HAVING query conditions.                       |
| [`AbstractJoins`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractJoins.md)           | Abstract contract for configured PHQL join definitions.              |
| [`AbstractLimit`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractLimit.md)           | Abstract contract for REST query limit policy.                       |
| [`AbstractOffset`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractOffset.md)         | Abstract contract for REST query offset configuration.               |
| [`AbstractOrder`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractOrder.md)           | Abstract contract for ORDER BY query configuration.                  |
| [`AbstractSave`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractSave.md)             | Abstract contract for REST persistence helpers.                      |
| [`AbstractWith`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/AbstractWith.md)             | Abstract contract for eager-loading relation configuration.          |

### \PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions


| Trait                                                                                                                                   | Description                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [`AbstractFilterConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractFilterConditions.md)         | Abstract contract for request-filter query conditions.   |
| [`AbstractIdentityConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractIdentityConditions.md)     | Abstract contract for identity-based query conditions.   |
| [`AbstractPermissionConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractPermissionConditions.md) | Abstract contract for permission-based query conditions. |
| [`AbstractSearchConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractSearchConditions.md)         | Abstract contract for search-based query conditions.     |
| [`AbstractSoftDeleteConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Conditions/AbstractSoftDeleteConditions.md) | Abstract contract for soft-delete query conditions.      |

### \PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields


| Trait                                                                                                               | Description                                                               |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`AbstractExposeFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractExposeFields.md) | Abstract contract for list/detail exposure field policies.                |
| [`AbstractFilterFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractFilterFields.md) | Abstract contract for fields that may appear in request filters.          |
| [`AbstractMapFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractMapFields.md)       | Abstract contract for public-field to model-field mapping.                |
| [`AbstractOrderFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractOrderFields.md)   | Abstract contract for REST order-field policy configuration.              |
| [`AbstractSaveFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractSaveFields.md)     | Abstract contract for fields that may be assigned during save operations. |
| [`AbstractSearchFields`](./classes/PhalconKit/Mvc/Controller/Traits/Abstracts/Query/Fields/AbstractSearchFields.md) | Abstract contract for fields that may participate in text search.         |

### \PhalconKit\Mvc\Controller\Traits\Actions


| Trait                                                                                  | Description           |
|----------------------------------------------------------------------------------------|-----------------------|
| [`AuthActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/AuthActions.md)     |                       |
| [`ClamavActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/ClamavActions.md) |                       |
| [`ErrorActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/ErrorActions.md)   | Default Error Actions |
| [`RestActions`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/RestActions.md)     |                       |

### \PhalconKit\Mvc\Controller\Traits\Actions\Rest


| Trait                                                                                           | Description                          |
|-------------------------------------------------------------------------------------------------|--------------------------------------|
| [`AverageAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/AverageAction.md)     |                                      |
| [`CountAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/CountAction.md)         |                                      |
| [`DeleteAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/DeleteAction.md)       |                                      |
| [`DistinctAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/DistinctAction.md)   |                                      |
| [`ExportAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/ExportAction.md)       |                                      |
| [`FindAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/FindAction.md)           |                                      |
| [`FindFirstAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/FindFirstAction.md) |                                      |
| [`IndexAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/IndexAction.md)         |                                      |
| [`MaximumAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/MaximumAction.md)     |                                      |
| [`MinimumAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/MinimumAction.md)     |                                      |
| [`NewAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/NewAction.md)             |                                      |
| [`ReorderAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/ReorderAction.md)     |                                      |
| [`RestoreAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/RestoreAction.md)     |                                      |
| [`SaveAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/SaveAction.md)           | REST save / create / update actions. |
| [`SumAction`](./classes/PhalconKit/Mvc/Controller/Traits/Actions/Rest/SumAction.md)             |                                      |

### \PhalconKit\Mvc\Controller\Traits\Interfaces


| Interface                                                                                                 | Description                                                     |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [`BehaviorInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/BehaviorInterface.md)         | Contract for attaching controller behavior listeners.           |
| [`CacheInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/CacheInterface.md)               | Contract for REST query cache-key helpers.                      |
| [`DebugInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/DebugInterface.md)               | Contract for controller debug-mode checks.                      |
| [`ExportInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ExportInterface.md)             | Contract for REST file export helpers.                          |
| [`ExposeInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ExposeInterface.md)             | Contract for controller payload exposure helpers.               |
| [`FractalInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/FractalInterface.md)           | Contract for Fractal-backed REST response transformation.       |
| [`ModelInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ModelInterface.md)               | Contract for resolving the model managed by a REST controller.  |
| [`ParamsInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/ParamsInterface.md)             | Contract for filtered REST request parameter access.            |
| [`RestResponseInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/RestResponseInterface.md) | Contract for normalizing REST response payloads.                |
| [`StatusCodeInterface`](./classes/PhalconKit/Mvc/Controller/Traits/Interfaces/StatusCodeInterface.md)     | Contract for setting HTTP status codes on controller responses. |

### \PhalconKit\Mvc\Controller\Traits\Query


| Trait                                                                              | Description                                                                   |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`Bind`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Bind.md)                 |                                                                               |
| [`Cache`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Cache.md)               | This trait provides methods for caching data for the query.                   |
| [`Column`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Column.md)             |                                                                               |
| [`Compiler`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Compiler.md)         | Find-definition compiler.                                                     |
| [`Conditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions.md)     |                                                                               |
| [`Distinct`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Distinct.md)         |                                                                               |
| [`DynamicJoins`](./classes/PhalconKit/Mvc/Controller/Traits/Query/DynamicJoins.md) |                                                                               |
| [`Fields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields.md)             | Groups REST field-policy initialization for query controllers.                |
| [`Group`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Group.md)               |                                                                               |
| [`Having`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Having.md)             |                                                                               |
| [`Joins`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Joins.md)               |                                                                               |
| [`Limit`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Limit.md)               | The Limit trait provides methods to handle query limits.                      |
| [`Offset`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Offset.md)             | This trait provides functionality to set and get an offset value for a query. |
| [`Order`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Order.md)               | Parses REST `order` parameters into Phalcon-compatible query expressions.     |
| [`Save`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Save.md)                 | REST persistence trait (controller-side).                                     |
| [`With`](./classes/PhalconKit/Mvc/Controller/Traits/Query/With.md)                 |                                                                               |

### \PhalconKit\Mvc\Controller\Traits\Query\Conditions


| Trait                                                                                                           | Description                                |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| [`ExistentialConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/ExistentialConditions.md) |                                            |
| [`FilterConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/FilterConditions.md)           |                                            |
| [`FilterSemantics`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/FilterSemantics.md)             |                                            |
| [`IdentityConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/IdentityConditions.md)       | IdentityConditions                         |
| [`PermissionConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/PermissionConditions.md)   | Permission-based query condition provider. |
| [`SearchConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/SearchConditions.md)           | Search-based query condition provider.     |
| [`SoftDeleteConditions`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Conditions/SoftDeleteConditions.md)   | Soft-delete query condition provider.      |

### \PhalconKit\Mvc\Controller\Traits\Query\Fields


| Trait                                                                                     | Description                                                            |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [`ExposeFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/ExposeFields.md) |                                                                        |
| [`FilterFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/FilterFields.md) |                                                                        |
| [`MapFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/MapFields.md)       |                                                                        |
| [`OrderFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/OrderFields.md)   | Stores the REST order-field allow-list used by the query order parser. |
| [`SaveFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/SaveFields.md)     |                                                                        |
| [`SearchFields`](./classes/PhalconKit/Mvc/Controller/Traits/Query/Fields/SearchFields.md) |                                                                        |

### \PhalconKit\Mvc\Dispatcher


| Class                                                               | Description                                                                   |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`Camelize`](./classes/PhalconKit/Mvc/Dispatcher/Camelize.md)       | Normalizes dispatched controller and action names to framework method names.  |
| [`Error`](./classes/PhalconKit/Mvc/Dispatcher/Error.md)             | Dispatcher listener that maps request and runtime exceptions to error routes. |
| [`Logger`](./classes/PhalconKit/Mvc/Dispatcher/Logger.md)           | Dispatcher listener that logs route resolution metadata.                      |
| [`Maintenance`](./classes/PhalconKit/Mvc/Dispatcher/Maintenance.md) | Dispatcher listener that redirects traffic while maintenance mode is enabled. |
| [`Module`](./classes/PhalconKit/Mvc/Dispatcher/Module.md)           | Dispatcher listener that keeps the module name synchronized during forwards.  |
| [`Preflight`](./classes/PhalconKit/Mvc/Dispatcher/Preflight.md)     | Dispatcher listener for CORS and preflight requests.                          |
| [`Rest`](./classes/PhalconKit/Mvc/Dispatcher/Rest.md)               | Pass-through dispatcher listener reserved for REST dispatch customization.    |
| [`Security`](./classes/PhalconKit/Mvc/Dispatcher/Security.md)       | Dispatcher listener that enforces configured ACL permissions.                 |

### \PhalconKit\Mvc\Model


| Class                                                  | Description                                                      |
|--------------------------------------------------------|------------------------------------------------------------------|
| [`Dynamic`](./classes/PhalconKit/Mvc/Model/Dynamic.md) | Runtime model whose source and metadata can change per instance. |
| [`Manager`](./classes/PhalconKit/Mvc/Model/Manager.md) |                                                                  |


| Interface                                                                | Description |
|--------------------------------------------------------------------------|-------------|
| [`ManagerInterface`](./classes/PhalconKit/Mvc/Model/ManagerInterface.md) |             |

### \PhalconKit\Mvc\Model\Behavior


| Class                                                                       | Description                                                                 |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`Action`](./classes/PhalconKit/Mvc/Model/Behavior/Action.md)               |                                                                             |
| [`Blameable`](./classes/PhalconKit/Mvc/Model/Behavior/Blameable.md)         | Blameable Behavior                                                          |
| [`Conditional`](./classes/PhalconKit/Mvc/Model/Behavior/Conditional.md)     | PhalconKit\Mvc\Model\Traits\Behavior\Conditional                            |
| [`Position`](./classes/PhalconKit/Mvc/Model/Behavior/Position.md)           |                                                                             |
| [`Security`](./classes/PhalconKit/Mvc/Model/Behavior/Security.md)           | Enforces ACL permissions for model lifecycle operations.                    |
| [`Snapshot`](./classes/PhalconKit/Mvc/Model/Behavior/Snapshot.md)           |                                                                             |
| [`SoftDelete`](./classes/PhalconKit/Mvc/Model/Behavior/SoftDelete.md)       | {@inheritDoc}                                                               |
| [`Transformable`](./classes/PhalconKit/Mvc/Model/Behavior/Transformable.md) | Applies configured attribute transformations during model lifecycle events. |

### \PhalconKit\Mvc\Model\Behavior\Traits


| Trait                                                                                | Description                                                                                                                       |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [`ProgressTrait`](./classes/PhalconKit/Mvc/Model/Behavior/Traits/ProgressTrait.md)   | Allow to enable or disable trait
on the current model instance ($progress)
or globally for every model instance ($staticProgress) |
| [`SkippableTrait`](./classes/PhalconKit/Mvc/Model/Behavior/Traits/SkippableTrait.md) | Allow to enable or disable trait
on the current model instance ($enabled)
or globally for every model instance ($staticEnabled)   |

### \PhalconKit\Mvc\Model\EagerLoading


| Class                                                                         | Description                                                   |
|-------------------------------------------------------------------------------|---------------------------------------------------------------|
| [`EagerLoad`](./classes/PhalconKit/Mvc/Model/EagerLoading/EagerLoad.md)       | Represents a level in the relations tree to be eagerly loaded |
| [`Loader`](./classes/PhalconKit/Mvc/Model/EagerLoading/Loader.md)             |                                                               |
| [`QueryBuilder`](./classes/PhalconKit/Mvc/Model/EagerLoading/QueryBuilder.md) |                                                               |

### \PhalconKit\Mvc\Model\Interfaces


| Interface                                                                                     | Description                                                       |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [`AttributeInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/AttributeInterface.md)       |                                                                   |
| [`BehaviorInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/BehaviorInterface.md)         |                                                                   |
| [`BlameableInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/BlameableInterface.md)       |                                                                   |
| [`EagerLoadInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/EagerLoadInterface.md)       |                                                                   |
| [`ExposeInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/ExposeInterface.md)             |                                                                   |
| [`HashInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/HashInterface.md)                 |                                                                   |
| [`IdentityInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/IdentityInterface.md)         |                                                                   |
| [`InstanceInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/InstanceInterface.md)         |                                                                   |
| [`JsonInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/JsonInterface.md)                 |                                                                   |
| [`LocaleInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/LocaleInterface.md)             |                                                                   |
| [`MetaDataInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/MetaDataInterface.md)         |                                                                   |
| [`OptionsInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/OptionsInterface.md)           |                                                                   |
| [`PositionInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/PositionInterface.md)         |                                                                   |
| [`RelationshipInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/RelationshipInterface.md) | Defines PhalconKit's relationship assignment and export contract. |
| [`ReplicationInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/ReplicationInterface.md)   |                                                                   |
| [`SecurityInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SecurityInterface.md)         |                                                                   |
| [`SlugInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SlugInterface.md)                 |                                                                   |
| [`SnapshotInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SnapshotInterface.md)         |                                                                   |
| [`SoftDeleteInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/SoftDeleteInterface.md)     |                                                                   |
| [`ValidateInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/ValidateInterface.md)         |                                                                   |

### \PhalconKit\Mvc\Model\Interfaces\Blameable


| Interface                                                                                       | Description |
|-------------------------------------------------------------------------------------------------|-------------|
| [`BlameAtInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/BlameAtInterface.md)   |             |
| [`CreatedInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/CreatedInterface.md)   |             |
| [`DeletedInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/DeletedInterface.md)   |             |
| [`RestoredInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/RestoredInterface.md) |             |
| [`UpdatedInterface`](./classes/PhalconKit/Mvc/Model/Interfaces/Blameable/UpdatedInterface.md)   |             |

### \PhalconKit\Mvc\Model\Traits


| Trait                                                                   | Description                                                                                      |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [`Attribute`](./classes/PhalconKit/Mvc/Model/Traits/Attribute.md)       | This trait provides methods to get and set attributes in a model using the get/set methods       |
| [`Behavior`](./classes/PhalconKit/Mvc/Model/Traits/Behavior.md)         | Adds named behavior registration helpers to PhalconKit models.                                   |
| [`Blameable`](./classes/PhalconKit/Mvc/Model/Traits/Blameable.md)       | Installs audit/user attribution behavior and user relationships on models.                       |
| [`Cache`](./classes/PhalconKit/Mvc/Model/Traits/Cache.md)               | Registers model-cache flushing behavior for mutable models.                                      |
| [`Count`](./classes/PhalconKit/Mvc/Model/Traits/Count.md)               | Provides count helpers for queries that need a subquery wrapper.                                 |
| [`EagerLoad`](./classes/PhalconKit/Mvc/Model/Traits/EagerLoad.md)       |                                                                                                  |
| [`Events`](./classes/PhalconKit/Mvc/Model/Traits/Events.md)             |                                                                                                  |
| [`Expose`](./classes/PhalconKit/Mvc/Model/Traits/Expose.md)             |                                                                                                  |
| [`FindIn`](./classes/PhalconKit/Mvc/Model/Traits/FindIn.md)             | Provides small `IN (...)` helpers for models with an integer `id` column.                        |
| [`Hash`](./classes/PhalconKit/Mvc/Model/Traits/Hash.md)                 |                                                                                                  |
| [`Identity`](./classes/PhalconKit/Mvc/Model/Traits/Identity.md)         | Provides model-level access to the current PhalconKit identity service.                          |
| [`Instance`](./classes/PhalconKit/Mvc/Model/Traits/Instance.md)         |                                                                                                  |
| [`Json`](./classes/PhalconKit/Mvc/Model/Traits/Json.md)                 | Trait Json                                                                                       |
| [`LifeCycle`](./classes/PhalconKit/Mvc/Model/Traits/LifeCycle.md)       | Provides static query helpers for data-retention lifecycle tasks.                                |
| [`Locale`](./classes/PhalconKit/Mvc/Model/Traits/Locale.md)             | Adds locale-aware field and method fallbacks to models.                                          |
| [`MetaData`](./classes/PhalconKit/Mvc/Model/Traits/MetaData.md)         | The MetaData trait provides methods for retrieving metadata information about a model or entity. |
| [`Options`](./classes/PhalconKit/Mvc/Model/Traits/Options.md)           | The Options trait provides methods for managing options using an options manager.                |
| [`Position`](./classes/PhalconKit/Mvc/Model/Traits/Position.md)         | The Position trait is used to manage the position behavior of an object.                         |
| [`Relationship`](./classes/PhalconKit/Mvc/Model/Traits/Relationship.md) | Adds relationship-aware assignment, persistence, and export helpers.                             |
| [`Replication`](./classes/PhalconKit/Mvc/Model/Traits/Replication.md)   | Coordinates read/write connection selection around replica lag.                                  |
| [`Security`](./classes/PhalconKit/Mvc/Model/Traits/Security.md)         | The Security trait provides methods to handle security-related functionalities.                  |
| [`Slug`](./classes/PhalconKit/Mvc/Model/Traits/Slug.md)                 |                                                                                                  |
| [`Snapshot`](./classes/PhalconKit/Mvc/Model/Traits/Snapshot.md)         | Trait that provides snapshot functionality for a model.                                          |
| [`SoftDelete`](./classes/PhalconKit/Mvc/Model/Traits/SoftDelete.md)     | This trait provides soft delete functionality to a model class.                                  |
| [`Uuid`](./classes/PhalconKit/Mvc/Model/Traits/Uuid.md)                 | Installs UUID generation behavior for model create operations.                                   |
| [`Validate`](./classes/PhalconKit/Mvc/Model/Traits/Validate.md)         |                                                                                                  |

### \PhalconKit\Mvc\Model\Traits\Abstracts


| Trait                                                                                               | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`AbstractBehavior`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractBehavior.md)           |                                                                             |
| [`AbstractBlameable`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractBlameable.md)         |                                                                             |
| [`AbstractEntity`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractEntity.md)               |                                                                             |
| [`AbstractEventsManager`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractEventsManager.md) |                                                                             |
| [`AbstractIdentity`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractIdentity.md)           | Abstract identity contract required by model traits that need user context. |
| [`AbstractInjectable`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractInjectable.md)       |                                                                             |
| [`AbstractInstance`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractInstance.md)           |                                                                             |
| [`AbstractLocale`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractLocale.md)               |                                                                             |
| [`AbstractMetaData`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractMetaData.md)           |                                                                             |
| [`AbstractModelsCache`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractModelsCache.md)     | Shared typed accessor for the model cache service.                          |
| [`AbstractModelsManager`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractModelsManager.md) | Shared models-manager contract helpers for model traits.                    |
| [`AbstractOptions`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractOptions.md)             |                                                                             |
| [`AbstractSave`](./classes/PhalconKit/Mvc/Model/Traits/Abstracts/AbstractSave.md)                   |                                                                             |

### \PhalconKit\Mvc\Model\Traits\Blameable


| Trait                                                                     | Description |
|---------------------------------------------------------------------------|-------------|
| [`BlameAt`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/BlameAt.md)   |             |
| [`Created`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Created.md)   |             |
| [`Deleted`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Deleted.md)   |             |
| [`Restored`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Restored.md) |             |
| [`Updated`](./classes/PhalconKit/Mvc/Model/Traits/Blameable/Updated.md)   |             |

### \PhalconKit\Mvc\Router


| Class                                                           | Description                                                               |
|-----------------------------------------------------------------|---------------------------------------------------------------------------|
| [`ModuleRoute`](./classes/PhalconKit/Mvc/Router/ModuleRoute.md) | Route group for one MVC module, optionally scoped by hostname and locale. |

### \PhalconKit\Mvc\View


| Class                                             | Description                                                   |
|---------------------------------------------------|---------------------------------------------------------------|
| [`Error`](./classes/PhalconKit/Mvc/View/Error.md) | View event listener reserved for framework-level view errors. |

### \PhalconKit\Provider


| Class                                                                                 | Description                                              |
|---------------------------------------------------------------------------------------|----------------------------------------------------------|
| [`AbstractServiceProvider`](./classes/PhalconKit/Provider/AbstractServiceProvider.md) | Base implementation for PhalconKit DI service providers. |


| Interface                                                                               | Description                                                          |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [`ServiceProviderInterface`](./classes/PhalconKit/Provider/ServiceProviderInterface.md) | Contract for services that register PhalconKit runtime dependencies. |

### \PhalconKit\Provider\Acl


| Class                                                                     | Description                           |
|---------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Acl/ServiceProvider.md) | Registers the access-control service. |

### \PhalconKit\Provider\Annotations


| Class                                                                             | Description                               |
|-----------------------------------------------------------------------------------|-------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Annotations/ServiceProvider.md) | Registers the annotations reader service. |

### \PhalconKit\Provider\Application


| Class                                                                             | Description                            |
|-----------------------------------------------------------------------------------|----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Application/ServiceProvider.md) | Registers the MVC application service. |

### \PhalconKit\Provider\Assets


| Class                                                                        | Description                           |
|------------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Assets/ServiceProvider.md) | Registers the assets manager service. |

### \PhalconKit\Provider\Aws


| Class                                                                     | Description                    |
|---------------------------------------------------------------------------|--------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Aws/ServiceProvider.md) | Registers the AWS SDK service. |

### \PhalconKit\Provider\Cache


| Class                                                                       | Description                              |
|-----------------------------------------------------------------------------|------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Cache/ServiceProvider.md) | Registers the application cache service. |

### \PhalconKit\Provider\Clamav


| Class                                                                        | Description                          |
|------------------------------------------------------------------------------|--------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Clamav/ServiceProvider.md) | Registers the ClamAV client service. |

### \PhalconKit\Provider\Config


| Class                                                                        | Description                                    |
|------------------------------------------------------------------------------|------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Config/ServiceProvider.md) | Registers the framework configuration service. |

### \PhalconKit\Provider\Console


| Class                                                                         | Description                        |
|-------------------------------------------------------------------------------|------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Console/ServiceProvider.md) | Registers the CLI console service. |

### \PhalconKit\Provider\Cookies


| Class                                                                         | Description                             |
|-------------------------------------------------------------------------------|-----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Cookies/ServiceProvider.md) | Registers the response cookies service. |

### \PhalconKit\Provider\Crypt


| Class                                                                       | Description                       |
|-----------------------------------------------------------------------------|-----------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Crypt/ServiceProvider.md) | Registers the encryption service. |

### \PhalconKit\Provider\Database


| Class                                                                          | Description                                     |
|--------------------------------------------------------------------------------|-------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Database/ServiceProvider.md) | Registers a configured PDO database connection. |

### \PhalconKit\Provider\DatabaseDynamic


| Class                                                                                 | Description                                              |
|---------------------------------------------------------------------------------------|----------------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/DatabaseDynamic/ServiceProvider.md) | Registers the dynamic-model database connection service. |

### \PhalconKit\Provider\DatabaseReadOnly


| Class                                                                                  | Description                                          |
|----------------------------------------------------------------------------------------|------------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/DatabaseReadOnly/ServiceProvider.md) | Registers the read-only database connection service. |

### \PhalconKit\Provider\Debug


| Class                                                                       | Description                         |
|-----------------------------------------------------------------------------|-------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Debug/ServiceProvider.md) | Registers the debug helper service. |

### \PhalconKit\Provider\Dispatcher


| Class                                                                            | Description                                                         |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Dispatcher/ServiceProvider.md) | Registers the mode-specific dispatcher and core dispatch listeners. |

### \PhalconKit\Provider\Env


| Class                                                                     | Description                               |
|---------------------------------------------------------------------------|-------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Env/ServiceProvider.md) | Registers the environment helper service. |

### \PhalconKit\Provider\Escaper


| Class                                                                         | Description                         |
|-------------------------------------------------------------------------------|-------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Escaper/ServiceProvider.md) | Registers the HTML escaper service. |

### \PhalconKit\Provider\EventsManager


| Class                                                                               | Description                                  |
|-------------------------------------------------------------------------------------|----------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/EventsManager/ServiceProvider.md) | Registers the shared events manager service. |

### \PhalconKit\Provider\FileSystem


| Class                                                                            | Description                             |
|----------------------------------------------------------------------------------|-----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/FileSystem/ServiceProvider.md) | Registers the local filesystem service. |

### \PhalconKit\Provider\Filter


| Class                                                                        | Description                              |
|------------------------------------------------------------------------------|------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Filter/ServiceProvider.md) | Registers the PhalconKit filter locator. |

### \PhalconKit\Provider\Flash


| Class                                                                       | Description                                   |
|-----------------------------------------------------------------------------|-----------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Flash/ServiceProvider.md) | Registers the direct flash messaging service. |

### \PhalconKit\Provider\Helper


| Class                                                                        | Description                           |
|------------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Helper/ServiceProvider.md) | Registers the helper factory service. |

### \PhalconKit\Provider\Identity


| Class                                                                          | Description                             |
|--------------------------------------------------------------------------------|-----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Identity/ServiceProvider.md) | Registers the identity manager service. |

### \PhalconKit\Provider\Imap


| Class                                                                      | Description                         |
|----------------------------------------------------------------------------|-------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Imap/ServiceProvider.md) | Registers the IMAP mailbox service. |

### \PhalconKit\Provider\Jwt


| Class                                                                     | Description                                                                  |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [`Jwt`](./classes/PhalconKit/Provider/Jwt/Jwt.md)                         | Helper around Phalcon's JWT builder, parser, signer, and validator services. |
| [`ServiceProvider`](./classes/PhalconKit/Provider/Jwt/ServiceProvider.md) | Registers the JWT helper service.                                            |

### \PhalconKit\Provider\Locale


| Class                                                                        | Description                            |
|------------------------------------------------------------------------------|----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Locale/ServiceProvider.md) | Registers the locale resolver service. |

### \PhalconKit\Provider\Logger


| Class                                                                        | Description                           |
|------------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Logger/ServiceProvider.md) | Registers the default logger service. |

### \PhalconKit\Provider\Loggers


| Class                                                                         | Description                                  |
|-------------------------------------------------------------------------------|----------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Loggers/ServiceProvider.md) | Registers the named logger registry service. |

### \PhalconKit\Provider\LoremIpsum


| Class                                                                            | Description                                  |
|----------------------------------------------------------------------------------|----------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/LoremIpsum/ServiceProvider.md) | Registers the lorem ipsum generator service. |

### \PhalconKit\Provider\Mailer


| Class                                                                        | Description                           |
|------------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Mailer/ServiceProvider.md) | Registers the mailer manager service. |

### \PhalconKit\Provider\Models


| Class                                                                        | Description                                      |
|------------------------------------------------------------------------------|--------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Models/ServiceProvider.md) | Registers the framework model class-map service. |

### \PhalconKit\Provider\ModelsCache


| Class                                                                             | Description                               |
|-----------------------------------------------------------------------------------|-------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ModelsCache/ServiceProvider.md) | Registers the model-result cache service. |

### \PhalconKit\Provider\ModelsManager


| Class                                                                               | Description                          |
|-------------------------------------------------------------------------------------|--------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ModelsManager/ServiceProvider.md) | Registers the model manager service. |

### \PhalconKit\Provider\ModelsMetadata


| Class                                                                                | Description                           |
|--------------------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ModelsMetadata/ServiceProvider.md) | Registers the model metadata service. |

### \PhalconKit\Provider\OCR


| Class                                                                     | Description                |
|---------------------------------------------------------------------------|----------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/OCR/ServiceProvider.md) | Registers the OCR service. |

### \PhalconKit\Provider\Oauth2Client


| Class                                                                              | Description                                 |
|------------------------------------------------------------------------------------|---------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Oauth2Client/ServiceProvider.md) | Registers a generic OAuth2 client provider. |

### \PhalconKit\Provider\Oauth2Facebook


| Class                                                                                | Description                             |
|--------------------------------------------------------------------------------------|-----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Oauth2Facebook/ServiceProvider.md) | Registers the Facebook OAuth2 provider. |

### \PhalconKit\Provider\Oauth2Google


| Class                                                                              | Description                           |
|------------------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Oauth2Google/ServiceProvider.md) | Registers the Google OAuth2 provider. |

### \PhalconKit\Provider\OpenAi


| Class                                                                        | Description                              |
|------------------------------------------------------------------------------|------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/OpenAi/ServiceProvider.md) | Registers the OpenAI API client service. |

### \PhalconKit\Provider\Profiler


| Class                                                                          | Description                              |
|--------------------------------------------------------------------------------|------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Profiler/ServiceProvider.md) | Registers the database profiler service. |

### \PhalconKit\Provider\ReCaptcha


| Class                                                                           | Description                               |
|---------------------------------------------------------------------------------|-------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/ReCaptcha/ServiceProvider.md) | Registers the ReCaptcha verifier service. |

### \PhalconKit\Provider\Redis


| Class                                                                       | Description                                |
|-----------------------------------------------------------------------------|--------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Redis/ServiceProvider.md) | Registers the native Redis client service. |

### \PhalconKit\Provider\Request


| Class                                                                         | Description                         |
|-------------------------------------------------------------------------------|-------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Request/ServiceProvider.md) | Registers the HTTP request service. |

### \PhalconKit\Provider\Response


| Class                                                                          | Description                          |
|--------------------------------------------------------------------------------|--------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Response/ServiceProvider.md) | Registers the HTTP response service. |

### \PhalconKit\Provider\Router


| Class                                                                        | Description                                 |
|------------------------------------------------------------------------------|---------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Router/ServiceProvider.md) | Registers the mode-specific router service. |

### \PhalconKit\Provider\Security


| Class                                                                          | Description                                                |
|--------------------------------------------------------------------------------|------------------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Security/ServiceProvider.md) | Registers the password hashing and token security service. |

### \PhalconKit\Provider\Session


| Class                                                                         | Description                            |
|-------------------------------------------------------------------------------|----------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Session/ServiceProvider.md) | Registers the session manager service. |

### \PhalconKit\Provider\Swoole


| Class                                                                        | Description                                    |
|------------------------------------------------------------------------------|------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Swoole/ServiceProvider.md) | Registers the Swoole WebSocket server service. |

### \PhalconKit\Provider\Tag


| Class                                                                     | Description                                  |
|---------------------------------------------------------------------------|----------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Tag/ServiceProvider.md) | Registers the PhalconKit tag helper service. |

### \PhalconKit\Provider\Translate


| Class                                                                           | Description                                |
|---------------------------------------------------------------------------------|--------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Translate/ServiceProvider.md) | Registers the translation adapter service. |

### \PhalconKit\Provider\Url


| Class                                                                     | Description                           |
|---------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Url/ServiceProvider.md) | Registers the URL generation service. |

### \PhalconKit\Provider\Utils


| Class                                                                       | Description                           |
|-----------------------------------------------------------------------------|---------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Utils/ServiceProvider.md) | Registers the utility helper service. |

### \PhalconKit\Provider\Version


| Class                                                                         | Description                                     |
|-------------------------------------------------------------------------------|-------------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Version/ServiceProvider.md) | Registers the framework version helper service. |

### \PhalconKit\Provider\View


| Class                                                                      | Description                     |
|----------------------------------------------------------------------------|---------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/View/ServiceProvider.md) | Registers the MVC view service. |

### \PhalconKit\Provider\Volt


| Class                                                                      | Description                                 |
|----------------------------------------------------------------------------|---------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/Volt/ServiceProvider.md) | Registers the Volt template engine service. |

### \PhalconKit\Provider\WebSocket


| Class                                                                           | Description                                  |
|---------------------------------------------------------------------------------|----------------------------------------------|
| [`ServiceProvider`](./classes/PhalconKit/Provider/WebSocket/ServiceProvider.md) | Registers the WebSocket application service. |

### \PhalconKit\Router


| Interface                                                           | Description                             |
|---------------------------------------------------------------------|-----------------------------------------|
| [`RouterInterface`](./classes/PhalconKit/Router/RouterInterface.md) | Shared contract for PhalconKit routers. |

### \PhalconKit\Support


| Class                                                                  | Description                                                                  |
|------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [`CollectionPolicy`](./classes/PhalconKit/Support/CollectionPolicy.md) | Merge/intersection helpers for nullable collection policy sets.              |
| [`Debug`](./classes/PhalconKit/Support/Debug.md)                       | Customizes Phalcon's debug renderer for PhalconKit applications.             |
| [`Env`](./classes/PhalconKit/Support/Env.md)                           | Loads dotenv files and exposes normalized environment values.                |
| [`Helper`](./classes/PhalconKit/Support/Helper.md)                     | Static facade for native Phalcon and PhalconKit helper services.             |
| [`HelperFactory`](./classes/PhalconKit/Support/HelperFactory.md)       | Helper factory with PhalconKit-specific array/string helpers.                |
| [`Models`](./classes/PhalconKit/Support/Models.md)                     | Resolves configured PhalconKit model instances without magic methods.        |
| [`Php`](./classes/PhalconKit/Support/Php.md)                           | Small PHP runtime helpers used during bootstrap.                             |
| [`Slug`](./classes/PhalconKit/Support/Slug.md)                         |                                                                              |
| [`Utils`](./classes/PhalconKit/Support/Utils.md)                       | Miscellaneous low-level utility helpers.                                     |
| [`Version`](./classes/PhalconKit/Support/Version.md)                   | Exposes the installed PhalconKit core version through Phalcon's version API. |


| Trait                                                    | Description                                                           |
|----------------------------------------------------------|-----------------------------------------------------------------------|
| [`ModelsMap`](./classes/PhalconKit/Support/ModelsMap.md) | Provides explicit accessors for configurable framework model classes. |

### \PhalconKit\Support\Debug\Renderer


| Class                                                                         | Description                                                         |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`HtmlRenderer`](./classes/PhalconKit/Support/Debug/Renderer/HtmlRenderer.md) | Renders Phalcon 5.16+ debug reports with PhalconKit's inline theme. |

### \PhalconKit\Support\Exposer


| Class                                                        | Description                                                               |
|--------------------------------------------------------------|---------------------------------------------------------------------------|
| [`Builder`](./classes/PhalconKit/Support/Exposer/Builder.md) | Mutable state container used by {@see Exposer} during exposure traversal. |
| [`Exposer`](./classes/PhalconKit/Support/Exposer/Exposer.md) | Deterministic exposure engine built on top of a mutable Builder.          |


| Interface                                                                      | Description                                                        |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [`BuilderInterface`](./classes/PhalconKit/Support/Exposer/BuilderInterface.md) | Contract for the mutable state carrier used by the Exposer engine. |

### \PhalconKit\Support\Helper\Arr


| Class                                                                                   | Description                                               |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [`FlattenKeys`](./classes/PhalconKit/Support/Helper/Arr/FlattenKeys.md)                 | Flatten nested arrays into dot-path keyed rule maps.      |
| [`RecursiveMap`](./classes/PhalconKit/Support/Helper/Arr/RecursiveMap.md)               | Apply a callback to every scalar value in a nested array. |
| [`RecursiveStrReplace`](./classes/PhalconKit/Support/Helper/Arr/RecursiveStrReplace.md) | Replace string fragments throughout a nested array.       |

### \PhalconKit\Support\Helper\Str


| Class                                                                                   | Description                                                  |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [`NormalizeLineBreaks`](./classes/PhalconKit/Support/Helper/Str/NormalizeLineBreaks.md) | Normalize line-break sequences in text.                      |
| [`RemoveNonPrintable`](./classes/PhalconKit/Support/Helper/Str/RemoveNonPrintable.md)   | Remove non-printable characters from text.                   |
| [`SanitizeUTF8`](./classes/PhalconKit/Support/Helper/Str/SanitizeUTF8.md)               | Normalize input text to UTF-8 and remove invalid characters. |
| [`Slugify`](./classes/PhalconKit/Support/Helper/Str/Slugify.md)                         | Create URL-friendly slugs through the shared slug generator. |

### \PhalconKit\Support\Options


| Class                                                        | Description                       |
|--------------------------------------------------------------|-----------------------------------|
| [`Manager`](./classes/PhalconKit/Support/Options/Manager.md) | Default in-memory option manager. |


| Trait                                                        | Description                                                 |
|--------------------------------------------------------------|-------------------------------------------------------------|
| [`Options`](./classes/PhalconKit/Support/Options/Options.md) | Reusable implementation for mutable service/object options. |


| Interface                                                                      | Description                                               |
|--------------------------------------------------------------------------------|-----------------------------------------------------------|
| [`ManagerInterface`](./classes/PhalconKit/Support/Options/ManagerInterface.md) | Minimal mutable key/value option manager contract.        |
| [`OptionsInterface`](./classes/PhalconKit/Support/Options/OptionsInterface.md) | Contract for objects that expose mutable runtime options. |

### \PhalconKit\Translate\Adapter


| Class                                                                              | Description                                       |
|------------------------------------------------------------------------------------|---------------------------------------------------|
| [`NestedNativeArray`](./classes/PhalconKit/Translate/Adapter/NestedNativeArray.md) | Translation adapter backed by a nested PHP array. |

### \PhalconKit\Ws


| Class                                                 | Description                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------|
| [`Dispatcher`](./classes/PhalconKit/Ws/Dispatcher.md) | WebSocket task dispatcher.                                            |
| [`Module`](./classes/PhalconKit/Ws/Module.md)         | WebSocket module definition backed by Phalcon's CLI-style dispatcher. |
| [`Router`](./classes/PhalconKit/Ws/Router.md)         | WebSocket router built on Phalcon's CLI routing model.                |
| [`Task`](./classes/PhalconKit/Ws/Task.md)             | Base class for WebSocket tasks.                                       |
| [`WebSocket`](./classes/PhalconKit/Ws/WebSocket.md)   | Console runtime used for WebSocket task dispatching.                  |


| Interface                                                               | Description                                 |
|-------------------------------------------------------------------------|---------------------------------------------|
| [`DispatcherInterface`](./classes/PhalconKit/Ws/DispatcherInterface.md) | Contract for WebSocket task dispatchers.    |
| [`TaskInterface`](./classes/PhalconKit/Ws/TaskInterface.md)             | Marker contract for WebSocket task classes. |
