import hashlib
from pathlib import Path

AUTHOR = 'Alec Munro'
SITENAME = 'Unified Designs Blog'
SITEURL = 'https://writing.unified-designs.com'
PATH = 'public'
TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
STATIC_PATHS = ['images', 'baking', 'language']

THEME = 'my-theme'

PLUGINS = ['pelican.plugins.i18n_subsites']
I18N_SUBSITES = {
    'pt': {
        'SITENAME': 'Blog da Unified Designs',
        'LOCALE': 'pt_BR.UTF-8',
    }
}

MENUITEMS = (
    ('Home', 'https://unified-designs.com'),
    ('Projects', 'https://projects.unified-designs.com'),
    ('Writing', 'https://writing.unified-designs.com'),
)

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}.html'

# Cache-busting: changes whenever any theme CSS file changes, so Cloudflare and
# browsers fetch the new stylesheet instead of serving a stale cached copy.
CSS_VERSION = hashlib.sha256(
    b''.join(p.read_bytes() for p in sorted(Path(__file__).parent.joinpath('my-theme/static/css').glob('*.css')))
).hexdigest()[:10]
