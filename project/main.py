from project.fsw import Fsw


print('in module project.main')
print(f'Fsw="{Fsw}"')
print('creating function main()')
def main():
    print('main() was called')
    print(f'Fsw={Fsw}')
    # connect to fsw
    fsw = Fsw()
    fsw.open_tcp('localhost')
    assert fsw.connected()

    # preset
    fsw.clear_status()
    fsw.preset()
    assert not fsw.errors

    # get default channel
    assert len(fsw.channels) == 1
    default_channel = fsw.channels[0]

    # create channel
    fsw.create_channel(name='My Channel', type='SAN')
    assert not fsw.errors
    assert 'My Channel' in fsw.channels

    # delete default channel
    fsw.delete_channel(default_channel)
    assert not fsw.errors
    assert fsw.channels == ['My Channel']




if __name__ == '__main__':
    main()
