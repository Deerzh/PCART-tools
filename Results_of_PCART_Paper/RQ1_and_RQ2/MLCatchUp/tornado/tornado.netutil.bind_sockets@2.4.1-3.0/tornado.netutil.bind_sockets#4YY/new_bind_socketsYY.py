import tornado.netutil
import socket
sockets = tornado.netutil.bind_sockets(8888, address='0.0.0.0', flags=None)
