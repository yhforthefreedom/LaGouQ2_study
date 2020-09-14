import configparser


class ReadConfig:
    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]
