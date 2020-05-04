"""LanguageTool through server mode.

    migration URL: https://languagetool.org/http-api/migration.php
"""

__version__ = '2.0.1'

from .language_tag import LanguageTag
from .match import Match
from .server import LanguageTool
from . import utils