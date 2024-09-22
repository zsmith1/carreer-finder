# carreer-finder
Tool to search careers pages for specific companies. This tool works by comparing the HTML of the careers page with the last HTML scraped and outputs if there are any changes.

## Dependencies
- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Supabase](https://supabase.com/)

## Setting up Supabase
Supabase requires 2 tables to be created `Company` and `Scrapes`.

- `Company`: has 3 columns. `id(int8)`, `name(text)` and `careers_url(text)`
- `Scrapes`: has 4 columns. `id(int8)`, `created_at(timestamptz)`, `value(json)`, `company_id(int8, foreign key)`

## Running the tool
- You will need to manually insert the company careers pages you want to get in the `Company` table
- Add the `SUPABASE_URL` and `SUPABASE_KEY` environment variables
- `poetry run python3 main.py`