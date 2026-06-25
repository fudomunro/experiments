#!/bin/bash
set -euo pipefail

SITES=("blog" "projects" "landing")

SSH_CMD="ssh -i /Users/alec/Pictures/Work/lindsay/event-coordinator/deploy/keys/id_rsa -o StrictHostKeyChecking=no"

deploy_site() {
    local site="$1"
    case "$site" in
        blog)
            echo "▸ Building blog..."
            uv run pelican -s pelicanconf.py
            echo "▸ Deploying blog → writing.unified-designs.com"
            rsync -avz -e "$SSH_CMD" --delete output/ root@138.197.8.215:/var/www/writing.unified-designs.com/html/
            ;;
        projects)
            echo "▸ Building projects portfolio..."
            (cd projects_portfolio && uv run build.py)
            echo "▸ Deploying projects → projects.unified-designs.com"
            rsync -avz -e "$SSH_CMD" --delete projects_portfolio/public/ root@138.197.8.215:/var/www/projects.unified-designs.com/html/
            ;;
        landing)
            echo "▸ Deploying landing page → unified-designs.com"
            rsync -avz -e "$SSH_CMD" --delete root_landing/public/ root@138.197.8.215:/var/www/unified-designs.com/html/
            ;;
        *)
            echo "Unknown site: $site" >&2
            echo "Available: ${SITES[*]}" >&2
            exit 1
            ;;
    esac
}

if [[ $# -eq 0 ]]; then
    echo "Deploying all sites..."
    for site in "${SITES[@]}"; do
        deploy_site "$site"
        echo ""
    done
    echo "✓ All sites deployed."
else
    for site in "$@"; do
        deploy_site "$site"
    done
    echo "✓ Done."
fi
