from core.requesthttp import RequestHTTP
from core.socket_gen import req_socket_gen

import argparse
import threading
import socks

def main():

    parser = argparse.ArgumentParser(description='script 1 - guide whitelacker')
    parser.add_argument('-t', '--threads', type=int)
    parser.add_argument('-m', '--numsock',type=int)
    parser.add_argument('-u', '--addr', type=str)
    parser.add_argument('-d', '--timeout',type=int, default=0)
    parser.add_argument('-a', '--useragent', type=str,default="Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0")
    parser.add_argument('-p', '--accept', type=str, default="text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5")
    parser.add_argument('-c', '--conn',type=str, default="Keep-Alive")
    args = parser.parse_args()


    for x in range(args.threads):
        print("yes")
        RequestHTTP(x+1,req_socket_gen(args.addr,args.useragent,args.accept, args.conn), args.numsock, args.timeout).start()


    requesthttp.go.set()

main()
