
   Nginx       ----> FlaskApp ----------------> Redis
     |
     v
   access.log
     |
     v
   fluentd     ----> fluentd  ----------------> elasticsearch
                    (fluentd-elasticsearch)        kibana4
