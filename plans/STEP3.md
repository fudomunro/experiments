# Add a place to show off projects

I'm working on a couple of projects, including the event coordinator app at /Users/alec/Pictures/Work/lindsay/event-coordinator .

I want a place to show off these projects and write a little bit about each of them. Probably another subdomain at projects.unified-designs.com . 

In general, these projects will be collaborations with others, and will have Github repositories where the code is stored. Most will also have some kind of public facing site to direct people to.

## Implementation Plan

### Phase 1: Subdomain Setup & Nginx Configuration
* [x] **DNS Update**: Add an  record in Squarespace for the  subdomain () pointing to the Target Server IP ().
* [x] **Nginx Virtual Hosts**: Create a new Nginx configuration file for  on the Target Server and set the document root to .
* [x] **SSL Provisioning**: Run Certbot to generate an SSL certificate for  once DNS propagates.

### Phase 2: Static Site Generation Setup
* [x] **Initialize Projects Site**: Set up a lightweight static site generator specifically for the portfolio of projects in a local directory like  (can use Pelican again, or a simple custom HTML/Markdown script since it will be a minimalist showcase).
* [x] **Theme/Template Creation**: Develop a clean layout suited for showcasing software projects, including fields for title, description, GitHub repository link, and live demo link.
* [x] **Deployment Automation**: Create a  script to build the static site and  it to .

### Phase 3: Add Initial Projects
* [x] **Event Coordinator**: Create the first project entry for the "Group Event Coordinator" MVP prototype, summarizing its features (React, Supabase, AI-powered scheduling), and linking to its repository and its live staging environment.
* [x] **Future Projects**: Document a standardized Markdown format or JSON structure for easily adding future collaborative projects to the gallery.

### Phase 4: Cross-linking
* [x] **Update Main Landing Page**: Edit the "Under Construction" placeholder at  to include a prominent link to .
* [x] **Update Blog Navigation**: Update the Pelican blog at  to include a navigation link pointing to the new Projects gallery.

## Implementation Plan

### Phase 1: Subdomain Setup & Nginx Configuration
* [x] **DNS Update**: Add an  record in Squarespace for the  subdomain () pointing to the Target Server IP ().
* [x] **Nginx Virtual Hosts**: Create a new Nginx configuration file for  on the Target Server and set the document root to .
* [x] **SSL Provisioning**: Run Certbot to generate an SSL certificate for  once DNS propagates.

### Phase 2: Static Site Generation Setup
* [x] **Initialize Projects Site**: Set up a lightweight static site generator specifically for the portfolio of projects in a local directory like  (can use Pelican again, or a simple custom HTML/Markdown script since it will be a minimalist showcase).
* [x] **Theme/Template Creation**: Develop a clean layout suited for showcasing software projects, including fields for title, description, GitHub repository link, and live demo link.
* [x] **Deployment Automation**: Create a  script to build the static site and sync it to the Target Server.

### Phase 3: Add Initial Projects
* [x] **Event Coordinator**: Create the first project entry for the "Group Event Coordinator" MVP prototype, summarizing its features (React, Supabase, AI-powered scheduling), and linking to its repository and its live staging environment.
* [x] **Future Projects**: Document a standardized Markdown format or JSON structure for easily adding future collaborative projects to the gallery.

### Phase 4: Cross-linking
* [x] **Update Main Landing Page**: Edit the "Under Construction" placeholder at  to include a prominent link to .
* [x] **Update Blog Navigation**: Update the Pelican blog at  to include a navigation link pointing to the new Projects gallery.

## Implementation Plan

### Phase 1: Subdomain Setup & Nginx Configuration
* [x] **DNS Update**: Add an  record in Squarespace for the  subdomain () pointing to the Target Server IP ().
* [x] **Nginx Virtual Hosts**: Create a new Nginx configuration file for  on the Target Server and set the document root to .
* [x] **SSL Provisioning**: Run Certbot to generate an SSL certificate for  once DNS propagates.

### Phase 2: Static Site Generation Setup
* [x] **Initialize Projects Site**: Set up a lightweight static site generator specifically for the portfolio of projects in a local directory like  (can use Pelican again, or a simple custom HTML/Markdown script since it will be a minimalist showcase).
* [x] **Theme/Template Creation**: Develop a clean layout suited for showcasing software projects, including fields for title, description, GitHub repository link, and live demo link.
* [x] **Deployment Automation**: Create a  script to build the static site and sync it to the Target Server ().

### Phase 3: Add Initial Projects
* [x] **Event Coordinator**: Create the first project entry for the "Group Event Coordinator" MVP prototype, summarizing its features (React, Supabase, AI-powered scheduling), and linking to its repository and its live staging environment.
* [x] **Future Projects**: Document a standardized Markdown format or JSON structure for easily adding future collaborative projects to the gallery.

### Phase 4: Cross-linking
* [x] **Update Main Landing Page**: Edit the "Under Construction" placeholder at  to include a prominent link to .
* [x] **Update Blog Navigation**: Update the Pelican blog at  to include a navigation link pointing to the new Projects gallery.

## Implementation Plan

### Phase 1: Subdomain Setup & Nginx Configuration
* [x] **DNS Update**: Add an `A` record in Squarespace for the `projects` subdomain (`projects.unified-designs.com`) pointing to the Target Server IP (`138.197.8.215`).
* [x] **Nginx Virtual Hosts**: Create a new Nginx configuration file for `projects.unified-designs.com` on the Target Server and set the document root to `/var/www/projects.unified-designs.com/html`.
* [x] **SSL Provisioning**: Run Certbot to generate an SSL certificate for `projects.unified-designs.com` once DNS propagates.

### Phase 2: Static Site Generation Setup
* [x] **Initialize Projects Site**: Set up a lightweight static site generator specifically for the portfolio of projects in a local directory like `/Users/alec/Pictures/Work/projects_site` (can use Pelican again, or a simple custom HTML/Markdown script since it will be a minimalist showcase).
* [x] **Theme/Template Creation**: Develop a clean layout suited for showcasing software projects, including fields for title, description, GitHub repository link, and live demo link.
* [x] **Deployment Automation**: Create a `deploy.sh` script to build the static site and sync it to the Target Server (`/var/www/projects.unified-designs.com/html/`).

### Phase 3: Add Initial Projects
* [x] **Event Coordinator**: Create the first project entry for the "Group Event Coordinator" MVP prototype, summarizing its features (React, Supabase, AI-powered scheduling), and linking to its repository and its live staging environment.
* [x] **Future Projects**: Document a standardized Markdown format or JSON structure for easily adding future collaborative projects to the gallery.

### Phase 4: Cross-linking
* [x] **Update Main Landing Page**: Edit the "Under Construction" placeholder at `unified-designs.com` to include a prominent link to `projects.unified-designs.com`.
* [x] **Update Blog Navigation**: Update the Pelican blog at `writing.unified-designs.com` to include a navigation link pointing to the new Projects gallery.
