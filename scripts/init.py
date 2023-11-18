from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.56.2:2181')
zk.start()

zk.ensure_path("/kafka-manager/mutex/locks")
zk.ensure_path("/kafka-manager/mutex/leases")
zk.set("/kafka-manager/mutex/locks", b"")
zk.set("/kafka-manager/mutex/leases", b"")

zk.stop()