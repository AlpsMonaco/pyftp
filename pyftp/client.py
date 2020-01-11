from ftplib import FTP
from exception import ftp_exit


def start_ftp_client(ftp_tuple):
    host, port, user, password, _ = ftp_tuple

    ftp = FTPClient(host, port, user, password)
    ftp.start_interact_ftp()
    pass


class FTPClient:
    __ftp_session = None
    __quit = False

    def __init__(self, host='', port=21, user='', password=''):
        ftp_client = FTP()
        ftp_client.encoding = 'utf-8'

        try:
            ftp_client.connect(host, int(port))
            ftp_client.login(user, password)
            pass
        except Exception as e:
            ftp_exit(1, 'login failed.')
            pass
        else:
            self.__ftp_session = ftp_client
            pass

    def start_interact_ftp(self):
        while not self.__quit:
            try:
                input_cmd = input(">")
                pass
            except KeyboardInterrupt as e:
                self.__quit = True
                pass

            self.ftp_command_parser(input_cmd)
            pass

    def close(self):
        self.__ftp_session.close()
        pass

    def list_dir(self):
        self.__ftp_session.dir()
        pass

    def get_cwd(self):
        self.__ftp_session.pwd()
        pass

    def rm_file(self, file):
        try:
            self.__ftp_session.delete(file)
            pass
        except Exception as identifier:
            self.opt_failed('delete file failed')
            pass
        pass

    def rm_dir(self, dir):
        try:
            self.__ftp_session.rm_dir(dir)
            pass
        except Exception as identifier:
            self.opt_failed('delete file failed')
            pass
        pass
    
    def cd_dir(self,dir):
        self.__ftp_session.cmd(dir)
        pass

    def opt_failed(self, msg=''):
        print('Error: ' + msg)
        pass

    def __print_invalid(self):
        print("invalid argument")

    def print_help(self):
        print('''
Usage:
ls     = list folder
q/quit = quit
cwd    = show current ftp dir path
''')

    def ftp_command_parser(self, cmd):
        cmd = str(cmd).strip()
        cmd_list = cmd.split()

        ftp_cmd = cmd_list[0]

        if ftp_cmd == 'ls':
            self.list_dir()
            pass
        elif ftp_cmd == "pwd":
            print(self.get_cwd())
            pass
        elif ftp_cmd == "cd":
            print(self.cd_dir())
            pass
        elif ftp_cmd == 'q' or ftp_cmd == 'quit':
            self.__quit = True
        else:
            self.__print_invalid()
            pass
        pass
