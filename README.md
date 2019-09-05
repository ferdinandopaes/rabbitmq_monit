# RabbitMQ Monit

RabbitMQ Monit is a shell script that help to monitoring RabbitMQ.

### Setup

- Install `jq` - [How to install jq](https://stedolan.github.io/jq/download/)
- Add `zabbix` user on `/etc/sudoers`
```
# Permission to zabbix run rabbit diagnostics
zabbix	ALL=(ALL) NOPASSWD: /usr/sbin/rabbitmq-diagnostics
```
- Add `rabbitmq.sh` on `/etc/zabbix/scripts/`
- Added `userparameter_rabbitmq.conf` on `/etc/zabbix/zabbix_agentd.d/`
- Import Template
