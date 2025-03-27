# wp-auto-post-tool

# WordPress Post Updater

This script is designed to update WordPress posts that contain the year "2024" in the title or content. It fetches posts via the WordPress REST API, updates the year "2024" to "2025", and sets a random publish date between January and February 2025. This is useful for updating posts for the new year, especially when posts need to be refreshed with new information or timeframes.

## Features

- Fetches all posts from a WordPress site using pagination.
- Filters posts that contain the year "2024" in the title or content.
- Replaces "2024" with "2025" in the title and content.
- Assigns a random publish date between January and February 2025 for each updated post.
- Uses basic authentication with the WordPress API to perform updates.

## Requirements

- Python 3.x
- `requests` library

To install the required library, run:

```bash
pip install requests
Configuration
Before running the script, ensure that you configure the following variables:

WP_SITE_URL: The URL of your WordPress site (e.g., https://your-site.com).

WP_USERNAME: Your WordPress admin username.

WP_APP_PASSWORD: Your WordPress application password (generate this from your WordPress admin panel).

python
Copy
Edit
WP_SITE_URL = "https://your-site.com"
WP_USERNAME = "your_admin_username"
WP_APP_PASSWORD = "your_generated_password"
Functions
random_publish_date()
Generates a random publish date between January and February 2025.

get_wp_posts()
Fetches all posts from the WordPress site using pagination, returning a list of posts.

update_wp_posts()
Updates posts containing "2024" in the title or content by:

Replacing "2024" with "2025" in the title and content.

Assigning a random publish date between January and February 2025.

Usage
Once the configuration is set, run the script:

bash
Copy
Edit
python wp_post_updater.py
This will start the process of fetching posts, filtering them by the year "2024", and updating them with the new year and a random publish date.

License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet
Copy
Edit

This README explains what the script does, how to configure it, and provides the necessary instructions for setting up and running the script. Let me know if you'd like any adjustments!
