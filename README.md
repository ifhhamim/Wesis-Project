Project Title: WESIS Research Portal Scraper
Tools: Python, Selenium, BeautifulSoup, Requests, Pandas

Project Description
An automated scraper for WESIS.com (research database) that:

Logs in programmatically using POST requests/session handling.

Navigates dynamic elements (CSS selectors, dropdowns) with Selenium.

Extracts structured research data (titles, authors, abstracts) across multiple pages/links.

Handles anti-scraping measures via randomized delays and headless browsing.

Key Features
✅ Login Automation

Uses requests.Session() or Selenium to authenticate (POST method).

Stores cookies to maintain session.

✅ Dynamic Content Handling

Waits for elements (WebDriverWait) + explicit delays for JS-heavy pages.

CSS/XPath selectors to click buttons/expand sections.

✅ Multi-Link Crawling

Iterates through research item URLs in a loop.

Extracts metadata (PDF links, citations, keywords) with BeautifulSoup.

✅ Data Export

Saves cleaned data to CSV/Excel (Pandas) or JSON.
