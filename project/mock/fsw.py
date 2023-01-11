class Fsw:

    def __init__(self):
        self._open     = False
        self._channels = {}


    # connect

    def open_tcp(self, address):
        assert not self._open
        self._open = True

    def connected(self):
        return self._open

    def close(self):
        assert self._open
        self._open = False


    # instrument preset

    def preset(self):
        assert self.connected()
        self._channels = {}


    # errors

    @property
    def errors(self):
        assert self.connected()
        # no errors
        return []

    def clear_status(self):
        assert self.connected()


    # channels

    @property
    def channels(self):
        assert self.connected()
        return list(self._channels.keys())

    def create_channel(self, name, type='SAN'):
        assert self.connected()
        self._channels[name] = type

    def delete_channel(self, name):
        assert self.connected()
        del(self._channels[name])
