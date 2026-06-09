from flask import Flask, render_template, request, url_for

app = Flask(__name__)

CATEGORIES = [
    "All Categories",
    "Mammals",
    "Birds",
    "Reptiles",
    "Amphibians",
    "Fish",
    "Plants",
    "Insects",
]

STATS = [
    {"value": "79,811", "label": "Species", "icon": "leaf"},
    {"value": "56", "label": "National Parks", "icon": "mountain"},
    {"value": "Thousands", "label": "of Images", "icon": "image"},
    {"value": "Enabled", "label": "Geospatial Search", "icon": "map"},
]

SPECIES = [
    {
        "slug": "mountain-goat",
        "common_name": "Mountain Goat",
        "scientific_name": "Oreamnos americanus",
        "park_name": "Glacier National Park",
        "category": "Mammals",
        "short_description": "A sure-footed alpine mammal adapted to cliffs, snowfields, and high-elevation meadows.",
        "description": "Mountain goats are iconic alpine specialists found in rugged western mountain ranges. Their split hooves, muscular shoulders, and dense white coats help them navigate steep terrain and survive cold, exposed environments. In national parks they are often observed near rocky ledges, subalpine meadows, and mineral licks.",
        "image_url": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=1200&q=80",
        "conservation_status": "Stable",
        "occurrence": "Present",
        "nativeness": "Native",
        "latitude": "48.7596",
        "longitude": "-113.7870",
        "park_location": "Northern Rocky Mountains, Montana",
        "ai_summary": "Mountain goats are alpine mammals adapted to steep mountain environments and rocky terrain. They are commonly found in high-elevation habitats throughout western North America.",
        "comments": [
            {
                "username": "Avery L.",
                "timestamp": "Jun 8, 2026 at 2:14 PM",
                "text": "Saw one above Hidden Lake overlook. The way it moved across the rocks was incredible.",
            },
            {
                "username": "Dr. Chen",
                "timestamp": "Jun 6, 2026 at 9:42 AM",
                "text": "Great example of alpine adaptation and cold-weather morphology.",
            },
        ],
    },
    {
        "slug": "california-condor",
        "common_name": "California Condor",
        "scientific_name": "Gymnogyps californianus",
        "park_name": "Grand Canyon National Park",
        "category": "Birds",
        "short_description": "A critically important scavenger with a massive wingspan and a remarkable recovery story.",
        "description": "California condors are among North America's largest flying birds. Intensive conservation programs have helped reintroduce them to portions of their historical range, including canyon landscapes where rising thermals support long-distance soaring.",
        "image_url": "https://images.unsplash.com/photo-1551085254-e96b210db58a?auto=format&fit=crop&w=1200&q=80",
        "conservation_status": "Endangered",
        "occurrence": "Rare",
        "nativeness": "Native",
        "latitude": "36.1069",
        "longitude": "-112.1129",
        "park_location": "Colorado Plateau, Arizona",
        "ai_summary": "California condors are large soaring scavengers that rely on open landscapes and canyon thermals. Their presence highlights major conservation recovery efforts in the American West.",
        "comments": [
            {
                "username": "Mika R.",
                "timestamp": "May 28, 2026 at 4:31 PM",
                "text": "The wing tag made it easy to identify during our ranger program.",
            }
        ],
    },
    {
        "slug": "giant-sequoia",
        "common_name": "Giant Sequoia",
        "scientific_name": "Sequoiadendron giganteum",
        "park_name": "Sequoia National Park",
        "category": "Plants",
        "short_description": "One of the largest tree species on Earth, known for massive trunks and long lifespans.",
        "description": "Giant sequoias are fire-adapted conifers that grow in scattered groves along the western Sierra Nevada. Their cinnamon-colored bark, enormous volume, and ecological dependence on disturbance make them a signature species of conservation landscapes.",
        "image_url": "https://images.unsplash.com/photo-1515965567292-91b98a2c0b1d?auto=format&fit=crop&w=1200&q=80",
        "conservation_status": "Vulnerable",
        "occurrence": "Present",
        "nativeness": "Native",
        "latitude": "36.4864",
        "longitude": "-118.5658",
        "park_location": "Sierra Nevada, California",
        "ai_summary": "Giant sequoias are immense, long-lived trees adapted to Sierra Nevada mixed-conifer forests. Their life cycle is closely connected to fire, which opens cones and creates space for seedlings.",
        "comments": [
            {
                "username": "NPS Volunteer",
                "timestamp": "Jun 1, 2026 at 11:05 AM",
                "text": "Visitors are always surprised by how thick and soft-looking the bark is.",
            }
        ],
    },
    {
        "slug": "american-alligator",
        "common_name": "American Alligator",
        "scientific_name": "Alligator mississippiensis",
        "park_name": "Everglades National Park",
        "category": "Reptiles",
        "short_description": "A keystone wetland reptile that shapes freshwater habitats throughout the Everglades.",
        "description": "American alligators create and maintain alligator holes that provide critical dry-season refuges for fish, birds, amphibians, and invertebrates. Their role as apex predators and ecosystem engineers makes them central to wetland health.",
        "image_url": "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=1200&q=80",
        "conservation_status": "Least Concern",
        "occurrence": "Common",
        "nativeness": "Native",
        "latitude": "25.2866",
        "longitude": "-80.8987",
        "park_location": "South Florida wetlands",
        "ai_summary": "American alligators are freshwater predators and ecosystem engineers. Their nesting, feeding, and digging behaviors influence wetland structure and support many other species.",
        "comments": [],
    },
    {
        "slug": "brook-trout",
        "common_name": "Brook Trout",
        "scientific_name": "Salvelinus fontinalis",
        "park_name": "Great Smoky Mountains National Park",
        "category": "Fish",
        "short_description": "A cold-water fish associated with clear mountain streams and shaded headwaters.",
        "description": "Brook trout require clean, cold, oxygen-rich water and are often used as indicators of stream health. In mountain parks, habitat restoration and monitoring programs track their response to warming temperatures and stream connectivity.",
        "image_url": "https://images.unsplash.com/photo-1510130387422-82bed34b37e9?auto=format&fit=crop&w=1200&q=80",
        "conservation_status": "Sensitive",
        "occurrence": "Localized",
        "nativeness": "Native",
        "latitude": "35.6532",
        "longitude": "-83.5070",
        "park_location": "Southern Appalachian Mountains",
        "ai_summary": "Brook trout are cold-water stream fish that depend on shaded, oxygen-rich habitats. Their distribution can reveal changes in watershed condition and climate stress.",
        "comments": [
            {
                "username": "Stream Team",
                "timestamp": "May 19, 2026 at 8:20 AM",
                "text": "Found during a citizen science survey in a shaded tributary.",
            }
        ],
    },
    {
        "slug": "monarch-butterfly",
        "common_name": "Monarch Butterfly",
        "scientific_name": "Danaus plexippus",
        "park_name": "Shenandoah National Park",
        "category": "Insects",
        "short_description": "A migratory pollinator known for orange-and-black wings and milkweed dependence.",
        "description": "Monarch butterflies rely on milkweed as host plants for caterpillars and nectar-rich flowers as adults. Protected park corridors can support migration, breeding, and public awareness of pollinator conservation.",
        "image_url": "https://images.unsplash.com/photo-1546975490-e8b92a360b24?auto=format&fit=crop&w=1200&q=80",
        "conservation_status": "At Risk",
        "occurrence": "Seasonal",
        "nativeness": "Native",
        "latitude": "38.4755",
        "longitude": "-78.4535",
        "park_location": "Blue Ridge Mountains, Virginia",
        "ai_summary": "Monarch butterflies are migratory pollinators whose life cycle depends on milkweed and flowering plants. Park meadows and corridors can contribute to seasonal habitat networks.",
        "comments": [],
    },
]


def get_species(slug):
    return next((species for species in SPECIES if species["slug"] == slug), SPECIES[0])


@app.route("/")
def home():
    featured_species = SPECIES[:3]
    return render_template(
        "index.html",
        title="EcoExplorer",
        categories=CATEGORIES,
        stats=STATS,
        featured_species=featured_species,
    )


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    area = request.args.get("area", "").strip().lower()
    category = request.args.get("category", "All Categories")
    selected_park = request.args.get("park", "")
    has_image = request.args.get("has_image") == "on"
    has_comments = request.args.get("has_comments") == "on"

    filtered_species = []
    for species in SPECIES:
        text_matches = not query or query in " ".join(
            [
                species["common_name"],
                species["scientific_name"],
                species["short_description"],
                species["description"],
            ]
        ).lower()
        area_matches = not area or area in " ".join(
            [species["park_name"], species["park_location"]]
        ).lower()
        category_matches = category == "All Categories" or species["category"] == category
        park_matches = not selected_park or species["park_name"] == selected_park
        image_matches = not has_image or bool(species.get("image_url"))
        comments_matches = not has_comments or bool(species.get("comments"))

        if (
            text_matches
            and area_matches
            and category_matches
            and park_matches
            and image_matches
            and comments_matches
        ):
            filtered_species.append(species)

    parks = sorted({species["park_name"] for species in SPECIES})
    return render_template(
        "results.html",
        title="Search Results",
        categories=CATEGORIES,
        parks=parks,
        species_results=filtered_species,
        query=request.args.get("q", ""),
        area=request.args.get("area", ""),
        selected_category=category,
        selected_park=selected_park,
        has_image=has_image,
        has_comments=has_comments,
        total_results=len(filtered_species),
    )


@app.route("/species/<slug>")
def species_detail(slug):
    species = get_species(slug)
    related_species = [item for item in SPECIES if item["slug"] != species["slug"]][:3]
    return render_template(
        "species_detail.html",
        title=species["common_name"],
        species=species,
        related_species=related_species,
    )


@app.context_processor
def inject_helpers():
    return {"species_detail_url": lambda slug: url_for("species_detail", slug=slug)}


if __name__ == "__main__":
    app.run(debug=True)
