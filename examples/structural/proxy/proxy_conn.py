class DBConnection:
    def __init__(self, conn_id):
        self.conn_id = conn_id
        print(f"Create new connection {conn_id}")

    def query(self, sql):
        print(f"[{self.conn_id}] Executing: {sql}")


class ConnectionPoolProxy:
    def __init__(self, size=2):
        self.size = size
        self._pool = []
        self._used = []

    def get_connection(self):
        if self._pool:
            conn = self._pool.pop()
            self._used.append(conn)
            return conn
        elif len(self._used) < self.size:
            conn = DBConnection(len(self._used) + 1)
            self._used.append(conn)
            return conn
        else:
            raise Exception("No available connections.")

    def release(self, conn):
        self._used.remove(conn)
        self._pool.append(conn)
