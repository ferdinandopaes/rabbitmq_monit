#!/bin/bash
##
# Script criado monitorar o RabbitMQ
# Criado por: Ferdinando Paes
# Data de criação 2019-08-30
##

export HOME="/var/lib/rabbitmq"
export PWD="/etc/zabbix/scripts"

ping() {
    sudo rabbitmq-diagnostics ping -q > /dev/null
    echo $?
}

connectivity() {
    # Retorna 0 se todas as portas estiverem respondendo
    # Retorna 1 se alguma porta não estiver respondendo
    sudo rabbitmq-diagnostics -q check_port_connectivity | grep Successfully | grep 5672 | grep 15672 | grep 25672 > /dev/null
    echo $?
}

conn_channels() {
    # Retorna a porcentagem de conexões nos canais do RabbitMQ
    sudo rabbitmq-diagnostics -q memory_breakdown --unit "MB" | grep connection_channels | awk {'print $4'} | sed 's/(//g' | sed 's/)//g' | sed 's/%//g'
}

conn_readers() {
    # Retorna a porcentagem de conexões de leitura nos canais do RabbitMQ
    sudo rabbitmq-diagnostics -q memory_breakdown --unit "MB" | grep connection_readers | awk {'print $4'} | sed 's/(//g' | sed 's/)//g' | sed 's/%//g'
}

conn_writers() {
    # Retorna a porcentagem de conexões de escrita nos canais do RabbitMQ
    sudo rabbitmq-diagnostics -q memory_breakdown --unit "MB" | grep connection_writers | awk {'print $4'} | sed 's/(//g' | sed 's/)//g' | sed 's/%//g'
}

queue_procs() {
    # Retorna a porcentagem de procs nas filas do RabbitMQ
    sudo rabbitmq-diagnostics -q memory_breakdown --unit "MB" | grep queue_procs | awk {'print $4'} | sed 's/(//g' | sed 's/)//g' | sed 's/%//g'
}

disk_alarms() {
    NODE=`sudo rabbitmq-diagnostics server_version | head -1 | awk {'print $3'}`
    JSON=`curl -s -u guest:guest http://localhost:15672/api/nodes/$NODE | jq '.disk_free_alarm'`

    if [ "$JSON" == "false" ]; then
        echo 0
    elif [ "$JSON" =="true" ]; then
        echo 1
    else
        echo 3
    fi
}

mem_alarms() {
    NODE=`sudo rabbitmq-diagnostics server_version | head -1 | awk {'print $3'}`
    JSON=`curl -s -u guest:guest http://localhost:15672/api/nodes/$NODE | jq '.mem_alarm'`

    if [ "$JSON" == "false" ]; then
        echo 0
    elif [ "$JSON" =="true" ]; then
        echo 1
    else
        echo 3
    fi
}

file_descriptor() {
    LIMIT=`sudo rabbitmq-diagnostics -q status | grep total_limit | sed 's/[^0-9]*//g' 2>/dev/null`
    USED=`sudo rabbitmq-diagnostics -q status | grep total_used | sed 's/[^0-9]*//g' 2>/dev/null`

    P_FREE=$(($USED * 100))
    X=$(($P_FREE / $LIMIT))

    echo $X
}

queue_quantity() {
    sudo rabbitmq-diagnostics status | grep run_queue | sed 's/[^0-9]*//g'
}

case "$1" in
    ping)
        ping
        ;;
    connectivity)
        connectivity
        ;;
    conn_channels)
        conn_channels
        ;;
    conn_readers)
        conn_readers
        ;;
    conn_writers)
        conn_writers
        ;;
    queue_procs)
        queue_procs
        ;;
    disk_alarms)
        disk_alarms
        ;;
    mem_alarms)
        mem_alarms
        ;;
    file_descriptor)
        file_descriptor
        ;;
    queue_quantity)
        queue_quantity
        ;;
    *)
        echo $"Usage: $0 {ping|connectivity|conn_channels|conn_readers|conn_writers|queue_procs|disk_alarms|mem_alarms|file_descriptor|queue_quantity}"
        exit
esac
