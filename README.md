# RabbitMQ Monit

RabbitMQ Monit is a python script that help to monitoring RabbitMQ with Zabbix.

### Minimum requirements

- Zabbix 4.0
- Python 2.7

### Setup

- Add `zabbix` user on `/etc/sudoers`
```
# Permission to zabbix run rabbit diagnostics
zabbix	ALL=(ALL) NOPASSWD: /usr/sbin/rabbitmq-diagnostics
```
- Add `rabbitmq.py` on `/etc/zabbix/scripts/`
- Add `userparameter_rabbitmq.conf` on `/etc/zabbix/zabbix_agentd.d/`
- Import Template
- Restart Zabbix agent
