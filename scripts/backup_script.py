def eszkozfelvetel():
    ip = input('Adja meg az eszköz IP címét: ')
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'user',
        'password': 'cisco',
        'secret': 'cisco',
    }
    return device

from netmiko import ConnectHandler

def futtatas(device):
    try:
        conn = ConnectHandler(**device)
        ipconf = conn.send_command('show ip int brief')
        print(ipconf)

        conn.enable()
        shrun = conn.send_command('show running-config')
        device_name = conn.send_command('show running-config | include hostname').split()[1]
        file_name = device_name + '_backup.txt'
        conn.disconnect()
        try:
            with open(file_name, 'w') as f:
                f.write(shrun)
            print('Sikeres mentés')
        except:
            print('A mentés sikertelen')
    except:
        print('Nem sikerült kapcsolódni')

device = eszkozfelvetel()
futtatas(device)
