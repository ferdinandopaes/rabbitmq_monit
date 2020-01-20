# -*- coding: utf-8 -*-

"""
Script criado monitorar o RabbitMQ
Criado por: Ferdinando Paes
Data de criação 2020-01-17
"""

import subprocess, requests, json, sys, socket

def getNodeJson():
    command = subprocess.check_output("sudo rabbitmq-diagnostics server_version | head -1 | awk {'print $3'}", shell=True)
    node = command.rstrip('\n')
    uri = 'http://guest:guest@localhost:15672/api/nodes/{NODE}'.format(NODE=node)
    request = requests.get(uri)
    dumpedJson = json.dumps(request.json())
    loadedJson = json.loads(dumpedJson)
    return loadedJson

def getOverviewJson():
    uri = 'http://guest:guest@localhost:15672/api/overview/'
    request = requests.get(uri)
    dumpedJson = json.dumps(request.json())
    loadedJson = json.loads(dumpedJson)
    return loadedJson

def getStatusPort(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r = s.connect_ex(('127.0.0.1', port))
    print (r)

def getMemAlarm():
    data = getNodeJson()
    print (data['mem_alarm'])

def getDiskAlarm():
    data = getNodeJson()
    print (data['disk_free_alarm'])

def getQueueDel():
    data = getNodeJson()
    print (data['queue_deleted'])

def getChannelCreated():
    data = getNodeJson()
    print (data['channel_created'])

def getMemLimit():
    data = getNodeJson()
    print (data['mem_limit'])

def getMemUsed():
    data = getNodeJson()
    print (data['mem_used'])

def getUpTime():
    data = getNodeJson()
    print (data['uptime'])

def getDiskFreeAlarm():
    data = getNodeJson()
    print (data['disk_free_limit'])

def getRateConnCreated():
    data = getNodeJson()
    print (data['connection_created_details']['rate'])

def getFileDescriptorsTotal():
    data = getNodeJson()
    print (data['fd_total'])

def getFileDescriptorsInUse():
    data = getNodeJson()
    print (data['fd_used'])

def getSocketsUsed():
    data = getNodeJson()
    print (data['sockets_used'])

def getChannels():
    data = getOverviewJson()
    print (data['object_totals']['channels'])

def getConnections():
    data = getOverviewJson()
    print (data['object_totals']['connections'])

def getQueue():
    data = getOverviewJson()
    print (data['object_totals']['queues'])

def getTotalExchanges():
    data = getOverviewJson()
    print (data['object_totals']['exchanges'])

def getRateChurns():
    data = getOverviewJson()
    print (data['churn_rates']['channel_created_details']['rate'])

def getRatePublish():
    data = getOverviewJson()
    print (data['message_stats']['publish_details'])

def getRateConsumerAck():
    data = getOverviewJson()
    print (data['message_stats']['ack_details']['rate'])

def getTotalMessages():
    data = getOverviewJson()
    print (data['queue_totals']['messages'])

def getTotalMessagesUnack():
    data = getOverviewJson()
    print (data['queue_totals']['messages_unacknowledged'])

def getDeliverGet():
    data = getOverviewJson()
    print (data['message_stats']['deliver_get'])

def argument(option):
    if option == 'mem_alarm':
        getMemAlarm()
    elif option == 'port_5672':
        getStatusPort(5672)
    elif option == 'port_15672':
        getStatusPort(15672)
    elif option == 'port_25672':
        getStatusPort(25672)
    elif option == 'disk_alarm':
        getDiskAlarm()
    elif option == 'queue_del':
        getQueueDel()
    elif option == 'channel_created':
        getChannelCreated()
    elif option == 'mem_limit':
        getMemLimit()
    elif option == 'mem_used':
        getMemUsed()
    elif option == 'uptime':
        getUpTime()
    elif option == 'disk_free_alarm':
        getDiskFreeAlarm()
    elif option == 'rate_conn_created':
        getRateConnCreated()
    elif option == 'file_descriptor_total':
        getFileDescriptorsTotal()
    elif option == 'file_descriptor_in_use':
        getFileDescriptorsInUse()
    elif option == 'sockets_in_use':
        getSocketsUsed()
    elif option == 'channels':
        getChannels()
    elif option == 'connections':
        getConnections()
    elif option == 'queue':
        getQueue()
    elif option == 'exchanges':
        getTotalExchanges()
    elif option == 'churn_rates':
        getRateChurns()
    elif option == 'publish_rates':
        getRatePublish()
    elif option == 'consumer_ack_rate':
        getRateConsumerAck()
    elif option == 'total_enqueued':
        getTotalMessages()
    elif option == 'unacked':
        getTotalMessagesUnack()
    elif option == 'delivered':
        getDeliverGet()
    else:
        print ('Paramêtro Inválido!!!')

if __name__ == '__main__':
    arg = sys.argv[1]
    argument(arg)
