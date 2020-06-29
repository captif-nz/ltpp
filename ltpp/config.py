
from pathlib import Path
from configparser import ConfigParser


CONFIG_FILE = Path.home().joinpath(".ltpp.ini")


def config():
    """
    The config file must contain the following database connection details. Place this in
    the home directory with filename `.ltpp.ini`.

    [GENERAL]
    database_path = ****  (e.g. ~/local-databases/ltpp.mdb)

    """

    config_ = ConfigParser()
    config_.read(CONFIG_FILE)
    return config_


def get_config_param(parameter, raise_exception=True):
    value = config().get("GENERAL", parameter, fallback="")

    if value:
        return value

    if raise_exception:
        raise ConfigError(f"'{parameter}' not defined in the config file")

    return None


class ConfigError(Exception):
    pass
