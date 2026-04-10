#!/bin/bash
# Local development helper — generates map.local.html with a real Mapbox token
# and starts a local server. Never commit map.local.html or .env.local.

# Load token from .env.local if it exists
if [ -f .env.local ]; then
  source .env.local
fi

if [ -z "$MAPBOX_TOKEN" ]; then
  echo "Error: MAPBOX_TOKEN is not set."
  echo ""
  echo "Either:"
  echo "  1. Run:  MAPBOX_TOKEN='pk.your_token_here' ./dev.sh"
  echo "  2. Or create .env.local with:  MAPBOX_TOKEN=pk.your_token_here"
  exit 1
fi

sed "s|YOUR_MAPBOX_ACCESS_TOKEN|${MAPBOX_TOKEN}|g" map.html > map.local.html
echo "Generated map.local.html"
echo "Opening http://localhost:8080/map.local.html"
open "http://localhost:8080/map.local.html" &
python3 -m http.server 8080
