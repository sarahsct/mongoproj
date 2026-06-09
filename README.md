# EcoExplorer

EcoExplorer is a modern, responsive Flask-ready web interface for exploring biodiversity records from U.S. National Parks.

The generated UI includes:

- Home/search page with hero banner, keyword search, area search, category filtering, and database statistics
- Search results page with reusable species cards, top search, sidebar filters, and pagination styling
- Species detail page with image hero, profile data, AI species summary, geospatial section, comments, add-comment form, and related species
- Shared design system using Forest Green, Sage Green, Earth Beige, Dark Slate, and clean dashboard-style cards

## Preview locally

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

## Flask integration

Templates live in `templates/` and static assets live in `static/`.
The demo `app.py` passes sample dictionaries that match likely MongoDB-backed fields such as common name, scientific name, park name, category, GridFS image URL, comments, geospatial coordinates, and AI summaries.
