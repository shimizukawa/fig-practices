===============
How to work
===============


Used containers
===============

- `python:2.7`_:
   to execute FlaskApp

- `redis:2`_:
   KeyValue storage for FlaskApp

- `nginx:latest`_:
   Web frontend for FlaskApp and Kibana4

- `shimizukawa/fluentd:latest`_:
   simple fluentd to collect nginx log and transfer it to elasticsearch.

- `devdb/kibana:latest`_:
   Kibana4 beta3 with ElasticSearch


.. _python:2.7: https://registry.hub.docker.com/_/python/
.. _redis:2: https://registry.hub.docker.com/_/redis/
.. _nginx:latest: https://registry.hub.docker.com/_/nginx/
.. _shimizukawa/fluentd:latest:
https://registry.hub.docker.com/u/shimizukawa/fluentd/
.. _devdb/kibana:latest: https://registry.hub.docker.com/devdb/kibana


Container Structures
====================

Browser access flow::

  Browser
    |
    |
    v
   Nginx   ----> FlaskApp ---> Redis
        \
         \
          \
           ------------------\
                              \
                               \
   fluentd                        kibana4
                               elasticsearch


Log data flow::

   Nginx         FlaskApp      Redis
     |
     |access.log
     |
     |
     v (fluentd-elasticsearch-plugin)
   fluentd  -------------------------> elasticsearch
                                         kibana4


