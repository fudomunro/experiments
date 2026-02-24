# Translating

As part of my blogging, I'm learning Portuguese. To exercise my Portuguese capabilities, I'm going to translate my newer blog articles manually into Portuguese and get feedback from my friend Thiago, who is helping me learn Portuguese.

We will need the ability to add manual translation to articles, and a mechanism for Thiago to review the published articules and provide feedback on my use of language.

## Implementation Plan

### Phase 1: Plugin & Configuration
* [x] **Install Plugin**: Install `pelican-i18n-subsites` to handle multi-language support.
* [x] **Configure Pelican**: Update `pelicanconf.py` to enable the plugin, define `I18N_SUBSITES` for Portuguese (`pt`), and set URL patterns for translated articles.

### Phase 2: Theme Customization
* [x] **Create Local Theme**: Copy the `notmyidea` theme to a local `my-theme` directory to allow customization.
* [x] **Add Translation Links**: Modify `article.html` to display a "Read this article in: [Lang]" block if translations are available.

### Phase 3: Content Translation
* [x] **Translate Article**: Create a `.pt.md` version of "The twist on the experiment" with `Lang: pt` and matching `Slug`.
* [x] **Update English Article**: Ensure the original English article has `Lang: en`.

### Phase 4: Deployment
* [x] **Deploy**: Build and deploy the updated site to `writing.unified-designs.com`.
