import yaml
from yaml.loader import Loader

class YamlHandler:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.file = yaml.load(f,Loader=yaml.FullLoader)
    def get_netbackup_baseurl(self):
        return (self.file["netbackup"]).get('domainname')

    def get_netbackup_domainname(self):
        return (self.file["netbackup"]).get('domainname')

    def get_netbackup_domaintype(self):
        return (self.file['netbackup']).get('domaintype')

    def get_netbackup_username(self):
        return (self.file['netbackup']).get('username')

    def get_netbackup_password(self):
        return (self.file['netbackup']).get('password')

    def get_netbackup_content_type(self):
        return (self.file['netbackup']).get('content_type')

    def get_windows_toolserver(self):
        return (self.file['windows']).get('toolserver')

    def get_windows_useradmin(self):
        return (self.file['windows']).get('useradmin')

    def get_windows_password(self):
        return (self.file['windows']).get('password')

    def get_windows_dc(self):
        return (self.file['windows']).get('dc')

    def get_windows_zone(self):
        return (self.file['windows']).get('zone')

    def get_vcenter_servername(self):
        return (self.file['vcenter']).get('servername')

    def get_vcenter_username(self):
        return (self.file['vcenter']).get('username')

    def get_vcenter_password(self):
        return (self.file['vcenter']).get('password')

    def get_vcenter_port(self):
        return (self.file['vcenter']).get('port')

    def get_vra_vrafqdn(self):
        return (self.file['vra']).get('servername')

    def get_vra_username(self):
        return (self.file['vra']).get('username')

    def get_vra_password(self):
        return (self.file['vra']).get('password')
        
    def get_vrops_vropsfqdn(self):
        return (self.file['vra']).get('servername')

    def get_vrops_username(self):
        return (self.file['vra']).get('username')

    def get_vrops_password(self):
        return (self.file['vra']).get('password')


