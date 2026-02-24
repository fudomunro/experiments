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
