# mqtt_from_scratch
mqtt like protocol from scratch

Simple protocol working like mqtt. 


To run Broker
```python
python3 main.py
```

To subscribe a topic 
```python
python3 cli_subscribe.py topic
```

To publish message under a topic
```python
python3 cli_publish.py topic message
```

Server port and ip address is defined under server_config.yaml file

Requirements is only PyYaml library.
