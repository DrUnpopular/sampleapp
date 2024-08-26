import subprocess

def activate_proxy(settings):
    print("Activating Proxy: Shields Up!")
    
    # Example settings dictionary:
    # settings = {'protocol': 'Trojan', 'server': '123.456.789.10', 'port': 443, 'encryption': 'TLS'}
    
    # Configure the selected proxy settings
    if settings['protocol'] == 'Trojan':
        subprocess.run(['trojan', '-server', settings['server'], '-port', str(settings['port']), '-tls', settings['encryption']])
    elif settings['protocol'] == 'V2Ray':
        subprocess.run(['v2ray', '-server', settings['server'], '-port', str(settings['port']), '-security', 'auto'])
    elif settings['protocol'] == 'Hysteria':
        subprocess.run(['hysteria', '-server', settings['server'], '-port', str(settings['port']), '-protocol', 'quic'])
    
    print("Proxy Activated Successfully")

# Example Usage
proxy_settings = {
    'protocol': results['recommended_protocol'],
    'server': '123.456.789.10',
    'port': 443,
    'encryption': 'TLS'
}
activate_proxy(proxy_settings)