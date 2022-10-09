#!/usr/bin/env bash
set -euo pipefail

docker build -t spotify-proxy:latest .

docker run --rm -it -p 8080:8080 --env-file .env --name spotify-proxy spotify-proxy:latest
