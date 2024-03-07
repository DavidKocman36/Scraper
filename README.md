# Real estate scraper

This project contains a scraper which scrapes the srealty.cz real estate website for the first 500 ads and saves them in a local postgre db. The custom HTML server then views these 500 ads on a website.

## Installation

1. Clone this git repo
2. Run `docker compose up`
3. The page should be available at 127.0.0.1:8080

The first request to the page is slower because scraper is active. The images also take some time to load.