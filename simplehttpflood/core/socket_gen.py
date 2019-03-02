
#function for generator sockets
def req_socket_gen(host,user_agent, accept, connection):
    url =  host.replace("http://", "").split("/")[0]
    
    return "GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent:  %s\r\nAccept: %s\r\nConnection: %s\r\n" % (host, url, accept, connection)
