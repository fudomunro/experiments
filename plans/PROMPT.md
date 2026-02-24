# Project Consolidation Plan

**Goal**: Gather all side projects and writing, manage them mostly in one place, with shareable details published to `unified-designs.com`.

## Infrastructure Details

*   **Older Server (To be decommissioned)**
    *   IP: `104.236.110.199`
    *   SSH: Port `8321`, `root` user
*   **Target Server (Consolidated host)**
    *   IP: `138.197.8.215`
    *   SSH: Port `22`, `root` user
*   **SSH Key**: `/Users/alec/Pictures/Work/lindsay/event-coordinator/deploy/keys/id_rsa`
*   **DNS**: `unified-designs.com` is managed via Squarespace Domains.

## Phase 1: Discovery & Inspection
*   [x] SSH into both servers using the provided key.
*   [x] Inspect web server configurations (Nginx/Apache), Docker containers, and active processes (systemd, PM2) on both servers.
*   [x] Compile a comprehensive list of all currently served sites, their domains, and their underlying technologies.
    *   *Older Server found 12+ older sites (PHP 5.6/7.0, MySQL, MongoDB).*
    *   *Target Server currently hosting alongside.ca, event-coordinator, and loopinevents.com.*

## Phase 2: Monitoring Setup
*   [x] Select a monitoring solution (either a self-hosted tool like Uptime Kuma on the Target Server, or a low-cost service like UptimeRobot for <$10/mo).
    *   *Installed Docker on the Target Server and deployed Uptime Kuma (accessible at `http://138.197.8.215:3001`).*
*   [x] Configure monitoring for all discovered sites to establish a baseline of health before migration begins.

## Phase 3: Migration to Target Server
*   [x] Replicate the required technology stacks on the Target Server using Docker containers (e.g., `php:5.6-fpm` and `php:7.0-fpm`) to ensure isolation from native software (PHP 8.1).
*   [x] Set up Dockerized database containers (MySQL and MongoDB) on the Target Server.
*   [x] Backup the older server databases (`mysqldump` and `mongodump`) and copy them to the Target Server to be restored into the new containers.
*   [x] Copy application files and Nginx configurations for the 12+ sites directly from the Older Server using `rsync` or `scp`.
*   [x] Update the native Nginx configuration on the Target Server to reverse-proxy PHP requests to the Dockerized FPM containers.
*   [x] Update DNS settings for the migrated domains to point to the Target Server IP (`138.197.8.215`).
*   [x] Re-provision SSL certificates (via Let's Encrypt/Certbot) on the Target Server.
*   [x] Verify the health of the migrated sites via the Uptime Kuma dashboard.

## Phase 4: Unified-Designs.com Integration
*   [x] Inspect the Python Pelican blog codebase currently located at `/Users/alec/Pictures/Work/experiments`.
*   [x] Update the Pelican setup to serve as both the main portfolio landing page (`unified-designs.com`) and the blog (e.g., under `/writing/` or a dedicated section).
*   [x] Set up a build and deployment process (scripted or CI/CD) to build the static Pelican site and deploy the `output` directory to the Target Server.
*   [x] Update Squarespace DNS records for `unified-designs.com` to point to the Target Server.

## Phase 5: Decommissioning
*   [ ] Confirm 100% uptime and correct functionality of all sites on the Target Server over a period of 1-2 weeks.
*   [ ] Power down and decommission the Older Server (`104.236.110.199`).
