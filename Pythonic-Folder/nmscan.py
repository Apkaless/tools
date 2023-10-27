import nmap


def Scanner(ip: str, argu: str):

    print(f'\nScanning: {ip}\n')

    nm = nmap.PortScanner()

    scan = nm.scan(ip, arguments=argu)

    devices = [host for host in nm.all_hosts()]

    stats = nm.scanstats()

    for device in devices:

        try:
            for proto in nm[ip].all_protocols():

                for port in scan['scan'][device][proto].keys():

                    print(f'{port}:Open:Proto:{proto}:Name:{scan["scan"][devices[0]]["tcp"][port]["name"] if len(scan["scan"][devices[0]]["tcp"][port]["name"]) >= 1 else "Unknown"}')
        except:
            print('No Open Ports Were Found')
        finally:
            print(f'\n{"*"*20}\nUPHOSTS: {stats["uphosts"]}\nDOWNHOSTS: {stats["downhosts"]}\nTime Elapsed: {stats["elapsed"]}')


Scanner(ip=input('Ip: '), argu='-F')