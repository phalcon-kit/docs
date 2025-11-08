# RESTful System

## Overview

### RESTful `v1` VS `v2`

!!! success "RESTful `v1` (Current)"
    The current **RESTful v1 system** integrates seamlessly with native Models methods, offering an efficient and intuitive
    experience. The methods
    include `with`, `withFirst`, `find`, `findFirst`, `count`, `average`, `sum`, `maximum`, `minimum`, `save`, `create`,
    and `update`. This setup ensures a balance between ease of use and performance through the following features:

    - **Lazy Loading and Eager Loading**: We employ lazy loading for records, complemented by eager loading for relationships, optimizing data retrieval without compromising on performance.
    - **Fully Constructed Responses**: The objects and lists retrieved are complete with meta-data and merged relationships, simplifying consumption and return processes.

!!! info "RESTful `v2` Enhancements (Planned)"
    Looking ahead, the upcoming RESTful v2 system aims to elevate flexibility and performance:

    - **QueryBuilder Integration**: v2 will leverage a query builder mechanism, enhancing the adaptability of data handling and retrieval.
    - **Optimized Data Structure**: The relationships and meta-data will be segregated from the main dataset. This strategic separation is aimed at boosting processing speed and reducing the payload size, thereby optimizing overall performance.
    
    Stay tuned for the upcoming launch of the RESTful v2 system, set to redefine data management efficiency in Phalcon Kit.

## Default RESTful Parameters

### Query Parameters

| **Parameter** | **Type**           | **Default** | **Behavior**                       |
|---------------|--------------------|-------------|------------------------------------|
| `limit`       | `Absolute Integer` | `10`        | Limit records to retrieve          |
| `offset`      | `Absolute Integer` | `null`      | Starting position                  |
| `order`       | `String`           | `null`      | Fields to order by                 |
| `group`       | `String`           | `null`      | Fields to group by                 |
| `distinct`    | `String`           | `null`      | Fields to select distinct          |
| `search`      | `String`           | `null`      | Match on search fields             |
| `filters`     | `Object`           | `null`      | Build the query conditions         |
| `fields`      | `Array`            | `null`      | List of fields to retrieve         |
| `lifetime`    | `Absolute Integer` | `null`      | Lifetime to cache the query result |

### Fields Parameters

| **Parameter**  | **Type** | **Default** | **Behavior**     |
|----------------|----------|-------------|------------------|
| `exposeFields` | `Array`  | `null`      | Fields to expose |
| `filterFields` | `Array`  | `null`      | Fields to filter |
| `searchFields` | `Array`  | `null`      | Fields to search |
| `saveFields`   | `Array`  | `null`      | Fields to save   |
| `createFields` | `Array`  | `null`      | Fields to create |
| `updateFields` | `Array`  | `null`      | Fields to update |
| `mapFields`    | `Array`  | `null`      | Fields mapping   |

## Default RESTful Methods

The default RESTful actions provide comprehensive coverage for most data handling needs in an application:

| **Request**                       | **Path**              | **Action**         | **Behavior**                      |
|-----------------------------------|-----------------------|--------------------|-----------------------------------|
| `GET`                             | /:controller/get/:id  | `getAction()`      | Retrieve a single record          |
| `GET`, `POST`                     | /:controller/find     | `findAction()`     | Retrieve a list of record         |
| `GET`, `POST`                     | /:controller/distinct | `distinctAction()` | Retrieve a distinct list of value |
| `GET`, `POST`                     | /:controller/export   | `exportAction()`   | Export a list of record           |
| `GET`, `POST`                     | /:controller/new      | `newAction()`      | Prepare a new record object       |
| `GET`, `POST`                     | /:controller/create   | `createAction()`   | Validate and create records       |
| `GET`, `POST` <br/>`PUT`, `PATCH` | /:controller/update   | `updateAction()`   | Validate and update records       |
| `GET`, `POST` <br/>`PUT`, `PATCH` | /:controller/save     | `saveAction()`     | Validate and save records         |
| `GET`, `POST`                     | /:controller/count    | `countAction()`    | Count the records                 |
| `GET`, `POST`                     | /:controller/sum      | `sumAction()`      | Calculate the sum                 |
| `GET`, `POST`                     | /:controller/average  | `averageAction()`  | Calculate the average             |
| `GET`, `POST`                     | /:controller/maximum  | `maximumAction()`  | Retrieve the maximum              |
| `GET`, `POST`                     | /:controller/minimum  | `minimumAction()`  | Retrieve the minimum              |
| `GET`, `POST`                     | /:controller/reorder  | `reorderAction()`  | Re-order a list of record         |
| `GET`, `POST` <br/>`DELETE`       | /:controller/delete   | `deleteAction()`   | Delete records                    |
| `GET`, `POST`                     | /:controller/restore  | `restoreAction()`  | Restore soft-deleted records      |

### Forwards: `indexAction()`

 Phalcon kit's RESTful System provides a standardized approach to handling HTTP requests and mapping them to specific actions
within controllers. This system ensures efficient and logical routing for CRUD operations and other RESTful
interactions.

#### Forwarded Actions Based on Request Method

Each HTTP request method is intelligently mapped to a corresponding controller action, streamlining request handling.
The table below outlines these mappings (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`):

| **Request** | **Path**           | **Action**      | **Forward to**   |
|-------------|--------------------|-----------------|------------------|
| `GET`       | `/:controller/`    | `indexAction()` | `findAction()`   |
| `GET`       | `/:controller/:id` | `indexAction()` | `getAction()`    |
| `POST`      | `/:controller/:id` | `indexAction()` | `saveAction()`   |
| `PUT`       | `/:controller/:id` | `indexAction()` | `saveAction()`   |
| `PATCH`     | `/:controller/:id` | `indexAction()` | `updateAction()` |
| `DELETE`    | `/:controller/:id` | `indexAction()` | `deleteAction()` |

### Average: averageAction()

Calculates and returns the average of a specified field.

### Count: countAction()

Counts the number of records that meet the specified criteria.


### Delete: deleteAction()

Permanently removes specified records.


### Distinct: distinctAction()

Retrieves a distinct list of values based on a specified field.


### Export: exportAction()

Exports a list of records in a specified format.


### Find: findAction()

Retrieves a list of records based on query parameters.


### FindFirst findFirstAction()

Fetches the first record that matches the specified criteria.


### Maximum: maximumAction()

Finds the maximum value of a specified field.


### Minimum: minimumAction()

Determines the minimum value of a specified field.


### New: newAction()

Prepares and returns a new record object.


### Reorder: reorderAction()

Adjusts the order of a list of records.


### Restore: restoreAction()

Restores soft-deleted records.


### Save: saveAction()

Validates and saves records, creating or updating them as necessary.


### Sum: sumAction()

Calculates the sum of a specified field across records.

