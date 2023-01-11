from project.fsw import Fsw


def main():
    # connect to fsw
    fsw = Fsw()
    fsw.open_tcp('localhost')
    assert fsw.connected()

    # preset
    fsw.clear_status()
    fsw.preset()
    assert not fsw.errors
    assert not fsw.channels

    # create channel
    fsw.create_channel(name='My Channel', type='SAN')
    assert not fsw.errors
    assert len(fsw.channels) == 1


if __name__ == '__main__':
    main()
