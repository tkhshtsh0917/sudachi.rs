from .sudachipy import (
    Dictionary,
    Tokenizer,
    SplitMode,
    MorphemeList,
    Morpheme,
    WordInfo,
)
from .config import Config
from . import errors

from importlib import import_module as _import_module
from importlib.util import find_spec as _find_spec
from pathlib import Path as _Path

__version__ = "0.6.9-a1"

_DEFAULT_RESOURCEDIR = _Path(__file__).resolve().parent / 'resources'
_DEFAULT_SETTINGFILE = _DEFAULT_RESOURCEDIR / 'sudachi.json'
_DEFAULT_RESOURCEDIR = str(_DEFAULT_RESOURCEDIR.resolve())
_DEFAULT_SETTINGFILE = str(_DEFAULT_SETTINGFILE.resolve())


def _get_absolute_dict_path(dict_type: str) -> str:
    pkg_path = _Path(_import_module(
        f'sudachidict_{dict_type}').__file__).parent
    dic_path = pkg_path / 'resources' / 'system.dic'
    return str(dic_path.resolve())


def _find_dict_path(dict_type='core'):
    if dict_type not in ['small', 'core', 'full']:
        raise ValueError('"dict_type" must be "small", "core", or "full".')

    is_installed = _find_spec(f'sudachidict_{dict_type}')
    if is_installed:
        return _get_absolute_dict_path(dict_type)
    else:
        raise ModuleNotFoundError(
            f'Package `sudachidict_{dict_type}` does not exist. '
            f'You may install it with a command `$ pip install sudachidict_{dict_type}`'
        )
