# Alongside: Deferred Dynamic Features

This document outlines the deferred tasks for the Alongside website update, specifically focusing on the dynamic functionality requested by management. These tasks will be addressed after the initial static-site migration (STEP5.md) is complete.

## 1. Dynamic Management UI
- **Goal**: Create a dedicated page/interface that allows Alongside management to quickly enter, edit, and publish current hiring needs.
- **Context**: The initial version handles the "Hiring Needs" banner statically (requiring a code or config update). This new UI needs to be user-friendly for non-technical staff.

## 2. Backend Data Storage
- **Goal**: Establish a data store for the hiring needs text and its active/inactive status.
- **Options to evaluate**: 
  - Lightweight database (e.g., SQLite).
  - Flat file (JSON/YAML) managed by a simple server-side script.
  - A minimal Headless CMS (e.g., Decap CMS / Netlify CMS) that naturally integrates with Pelican.

## 3. Authentication & Security
- **Goal**: Secure the management page so only authorized personnel can make changes to the site.
- **Options to evaluate**:
  - Basic HTTP Authentication (`htpasswd`).
  - A lightweight session-based login script.
  - Delegating authentication to a third-party service (if using a headless CMS).

## 4. Site Regeneration vs. Dynamic Fetching
- **Goal**: Ensure changes made in the management UI are immediately reflected on the live site's banner.
- **Options to evaluate**:
  - **Static Rebuild**: Triggering a Pelican site rebuild automatically when data is saved (via CI/CD webhook or local server script).
  - **Dynamic Fetch**: Fetching the hiring needs dynamically via a client-side JavaScript request to an API endpoint, avoiding the need to rebuild the static site on every small update.