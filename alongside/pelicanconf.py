AUTHOR = "Alongside Ltd."
SITENAME = "Alongside Live-In Home Support"
SITEURL = ""

PATH = "content"
TIMEZONE = "America/Halifax"
DEFAULT_LANG = "en"

# Feed generation is usually not needed for a business site
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme settings
THEME = "theme"
DIRECT_TEMPLATES = []

# URL settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Static paths
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Custom variables for Alongside updates
HIRING_NEEDS_TEXT = "We are currently looking for compassionate caregivers."
SHOW_HIRING_BANNER = True

# Contact Info (Somerset as main office per STEP5.md)
CONTACT_ADDRESS = {
    "street": "462 Hwy 360",
    "city": "Somerset",
    "province": "NS",
    "postal_code": "B0P 1E0",
}
CONTACT_PHONE = "(902) 578-9077"
CONTACT_EMAIL = "alongsidehomecare@gmail.com"

# Social links
SOCIAL = (("Facebook", "https://www.facebook.com/Alongside-Live-In-Home-Support-Ltd"),)

DEFAULT_PAGINATION = False

# Markdown settings
MARKDOWN = {
    "extension_configs": {
        "md_in_html": {},
    },
    "extensions": ["md_in_html"],
}

# Use document-relative URLs for easier staging in a subdirectory
RELATIVE_URLS = True
