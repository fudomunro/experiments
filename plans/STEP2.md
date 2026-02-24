# Define the blog

We want to give the blog portion of unified-designs.com it's own place to live. Let's use writing.unified-designs.com for now.

Let's put an "under construction" placeholder at unified-designs.com .

I have an older blog at alecmunro.blogspot.com , and I want to mirror all of the content there to the new blog (and at some point shut the old one down.)

## Implementation Plan

### Phase 1: Subdomain Setup & Nginx Configuration
* [x] **DNS Update**: Add an `A` record in Squarespace for the `writing` subdomain (i.e., `writing.unified-designs.com`) pointing to the Target Server IP (`138.197.8.215`).
* [x] **Nginx Virtual Hosts**:
  * Create a new Nginx configuration file for `writing.unified-designs.com` on the Target Server and set the document root to `/var/www/writing.unified-designs.com/html`.
  * Ensure the existing `unified-designs.com` server block remains pointed to `/var/www/unified-designs.com/html`.
* [x] **SSL Provisioning**: Run Certbot to generate an SSL certificate for `writing.unified-designs.com`.

### Phase 2: Pelican Reconfiguration
* [x] **Update Pelican Settings**: Modify `pelicanconf.py` in the local `experiments` directory:
  * Change `SITEURL` to `https://writing.unified-designs.com`.
  * Remove the `INDEX_SAVE_AS` override that previously pushed the blog index to `/writing/index.html`.
  * Remove the `ARTICLE_URL` and `ARTICLE_SAVE_AS` overrides so articles are generated at the root level rather than nested under `/writing/`.
* [x] **Update Deployment Script**: Change `deploy.sh` to sync the generated Pelican output to the new path (`root@138.197.8.215:/var/www/writing.unified-designs.com/html/`).
* [x] **Deploy**: Run the build and sync to push the blog to the new subdomain.

### Phase 3: Root Domain Under Construction Placeholder
* [x] **Create Placeholder**: Create a simple HTML file (`index.html`) with an "Under Construction" message and minimal styling.
* [x] **Deploy Placeholder**: Replace the contents of `/var/www/unified-designs.com/html/` on the Target Server with this new placeholder file.

### Phase 4: Blogger Content Migration
* [x] **Export Blogger Data**: Log into Blogger (`alecmunro.blogspot.com`), navigate to Settings -> Manage Blog, and click "Back up content" to download the blog's XML export.
* [x] **Install Importer**: Ensure `pelican[markdown]` and `beautifulsoup4` are installed, which are needed for the `pelican-import` command.
* [x] **Convert Content**: Use the Pelican importer tool to convert the Blogger XML format into individual Markdown files.
  * *Command:* `uv run pelican-import --blogger path/to/blogger-export.xml -o public/writing/ -m markdown`
* [ ] **Migrate Assets**: Download any externally hosted images from the old blog (Google Photos/Blogger CDNs), save them into the `public/images/` directory in the Pelican project, and update the Markdown files to reference them locally.
* [ ] **Review and Formatting**: Review the newly generated Markdown files to fix any layout issues, broken links, or missing metadata (tags/categories).
* [ ] **Final Deployment**: Rebuild and deploy the site to push the old Blogger content to `writing.unified-designs.com`.
* [ ] **Decommission Blogger**: Update the old Blogger site with a final post redirecting readers to the new domain, or edit the Blogger template to use a JavaScript meta-refresh redirect to `writing.unified-designs.com`, before eventually shutting it down.
