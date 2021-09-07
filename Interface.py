from __future__ import print_function

import obd
from CloudStorage import store


deviceId = "4548c207-41cf-46ac-b58b-78af80c54409"
auth = ""



def connect():
    ports = obd.scan_serial()  # return list of valid USB or RF ports
    print(ports)
    obd.logger.setLevel(obd.logging.DEBUG)

    device = ports[0]
    speed = 38400
    protocol = '5'

    connection = obd.OBD(fast=False, portstr=device, baudrate=speed, protocol=protocol)
    i = 1
    while len(connection.supported_commands) < 10:
        connection = obd.OBD(fast=False, portstr=device, baudrate=speed, protocol=protocol)
        i += 1
        if i > 10:
            break

    return connection


def collect(connection):
    results = {}
    resultsStr = {}
#     cmd = obd.commands.SPEED  # select an OBD command (sensor)
#     response = connection.query(cmd)  # send the command, and parse the responses

    for sc in connection.supported_commands:
        try:
            res = connection.query(sc)
            results[sc.name] = res
            resultsStr[sc.name] = str(res.value)
            print(sc.name, res.value)
        except Exception as e:
            print(e)
    return resultsStr


def end(connection):
    connection.close()
    pass


run = True
while run:
    cmd = raw_input()
    if cmd == "connect":
        connection = connect()
    elif cmd == "collect":
        data = collect(connection)
    if cmd == "store":
        store(data, deviceId, auth)
    if cmd == "end":
        end(connection)
        break
