
import re
import warnings
import pandas_access as mdb
from functools import lru_cache

from ltpp.config import get_config_param


TABLE_RE = re.compile("(\d+m)?(.+)")
database_path = get_config_param("database_path")


class Tables():
    def __init__(self, *args, **kwargs):
        """Loads LTPP data at initialisation"""
        for table in self._get_tables():
            try:
                self.__setattr__(
                    self._safe_table_name(table),
                    self._read_table(table)
                )
            except KeyError:
                warnings.warn(f"Could not load {table}", TableWarning)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        table_str = ", ".join(self.names())
        return f"Tables({table_str})"

    @lru_cache(maxsize=1)
    def _get_tables(self):
        """Get a list of tables in the MS Access database"""
        return mdb.list_tables(database_path)

    def _read_table(self, table_name):
        """Read data from tables in the MS Access database"""
        if table_name in self._get_tables():
            return mdb.read_table(database_path, table_name)

    @staticmethod
    def _safe_table_name(table_name):
        """Convert tables names to Python-attribute-safe versions"""
        parts = TABLE_RE.findall(table_name.lower())[0]
        safe_name = "_".join(parts[1].split(" "))
        if parts[0]:
            return safe_name + "_" + parts[0]
        return safe_name

    def names(self):
        """List the names of all tables"""
        return list(self.__dict__.keys())


class TableWarning(Warning):
    pass


tables = Tables()  # Load LTPP data at import.