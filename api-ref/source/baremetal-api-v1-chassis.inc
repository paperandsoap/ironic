.. -*- rst -*-

=================
Chassis (chassis)
=================

The Chassis resource type was originally conceived as a means to group Node
resources. Support for this continues to exist in the REST API, however, it is
very minimal. The Chassis object does not provide any functionality today
aside from a means to list a group of Nodes.

Use of this resource is discouraged, and may be deprecated and removed in a
future release.


List chassis with details
=========================

.. rest_method::  GET /v1/chassis/detail

Lists all chassis with details.

Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,

Request
-------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort_dir: sort_dir
   - sort_key: sort_key

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - uuid: uuid
   - chassis: chassis
   - description: description
   - extra: extra

Response Example
----------------

.. literalinclude:: samples/chassis-list-details-response.json
   :language: javascript


Show chassis details
====================

.. rest_method::  GET /v1/chassis/{chassis_id}

Shows details for a chassis.

Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,

Request
-------

.. rest_parameters:: parameters.yaml

   - fields: fields

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - uuid: uuid
   - chassis: chassis
   - description: description
   - extra: extra

Response Example
----------------

.. literalinclude:: samples/chassis-show-response.json
   :language: javascript

Update chassis
==============

.. rest_method::  PATCH /v1/chassis/{chassis_id}

Updates a chassis.

Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,

Request
-------

.. rest_parameters:: parameters.yaml

   - chassis: chassis
   - description: description
   - extra: extra

Request Example
---------------

.. literalinclude:: samples/chassis-update-request.json
   :language: javascript

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - extra: extra
   - created_at: created_at
   - updated_at: updated_at
   - chassis: chassis
   - nodes: nodes
   - uuid: uuid

Response Example
----------------

.. literalinclude:: samples/chassis-show-response.json
   :language: javascript


Delete chassis
==============

.. rest_method::  DELETE /v1/chassis/{chassis_id}

Deletes a chassis.

Error response codes:204,413,415,405,404,403,401,400,503,409,

Request
-------

Create chassis
==============

.. rest_method::  POST /v1/chassis

Creates a chassis.

Error response codes:201,413,415,405,404,403,401,400,503,409,

Request
-------

.. rest_parameters:: parameters.yaml

   - chassis: chassis
   - description: description
   - extra: extra

Request Example
---------------

.. literalinclude:: samples/chassis-create-request.json
   :language: javascript

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - extra: extra
   - created_at: created_at
   - updated_at: updated_at
   - nodes: nodes
   - uuid: uuid

List chassis
============

.. rest_method::  GET /v1/chassis

Lists all chassis.

Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,

Request
-------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort_dir: sort_dir
   - sort_key: sort_key
   - fields: fields

Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - uuid: uuid
   - chassis: chassis
   - description: description
   - extra: extra

Response Example
----------------

.. literalinclude:: samples/chassis-list-response.json
   :language: javascript
