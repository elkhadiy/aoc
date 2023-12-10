from importlib.metadata import metadata
from platformdirs import user_config_dir

__app_metadata = metadata(__package__)
__app__ = __app_metadata['Name']
__version__ = __app_metadata['Version']
__author__ = __app_metadata['Author']

configd = user_config_dir(__app__,
                          __author__,
                          version=__version__,
                          roaming=True,
                          ensure_exists=True)

from .api import input, submit, login
