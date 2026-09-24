# Pulse Dashboard

A tiny sales dashboard built for a Claude Code workshop. It runs on the
Python standard library, so there is nothing to install.

## Quick start

```bash
python3 server.py
```

Open http://localhost:8000

## Run the tests

```bash
python3 -m pytest tests/ -q
```

## Layout

```
pulse-dashboard/
├── CLAUDE.md            project context for Claude Code
├── server.py            HTTP server and routing
├── app/
│   └── data_loader.py   CSV loading and aggregation
├── static/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── data/sales.csv       901 sample orders
└── tests/test_data_loader.py
```

## Workshop exercises

Each prompt below is a self-contained task for Claude Code. They build on
each other but can be run in any order.

### 1. Explore (5 min)
```
Explain what this codebase does and how the pieces fit together.
```

### 2. Clean the data (10 min)
```
data/sales.csv has messy rows: blank amounts, a lowercase region, a
non-ISO date and an amount with a comma. Make the loader handle all of
these and add tests that prove it.
```

### 3. Add a feature (15 min)
```
Add a date range filter to the dashboard. The API should accept
start and end query parameters and the frontend should have two date
inputs that refresh the charts.
```

### 4. Refactor (10 min)
```
The aggregation functions in app/data_loader.py repeat the same
group-and-sum pattern. Refactor them into one reusable helper without
changing the API response shape.
```

### 5. Add a test suite (10 min)
```
The HTTP layer has no tests. Add tests for /api/summary that check the
status code, content type and response keys.
```

### 6. Fix a planted bug (10 min)
```
Revenue by month is sorted as strings. Confirm whether this breaks and
fix it properly.
```

### 7. Performance (10 min)
```
Every request re-reads and re-aggregates the CSV. Add caching that
invalidates when the file changes, and show me the before and after.
```

### 8. Documentation (5 min)
```
Update CLAUDE.md to reflect everything we changed today.
```
