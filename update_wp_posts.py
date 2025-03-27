import requests
import random
import datetime
from requests.auth import HTTPBasicAuth

# WordPress credentials and API URL
WP_SITE_URL = "https://ugtechmag.com"
WP_USERNAME = "your_admin_username"
WP_APP_PASSWORD = "your_generated_password"

API_URL = f"{WP_SITE_URL}/wp-json/wp/v2/posts"

# Generate a random publish date between Jan and Feb 2025
def random_publish_date():
    start_date = datetime.datetime(2025, 1, 1)
    end_date = datetime.datetime(2025, 2, 28)
    random_days = random.randint(0, (end_date - start_date).days)
    new_date = start_date + datetime.timedelta(days=random_days)
    return new_date.strftime("%Y-%m-%dT%H:%M:%S")

# Fetch all posts using pagination
def get_wp_posts():
    posts = []
    page = 1  # Start from page 1
    while True:
        response = requests.get(
            API_URL,
            params={"per_page": 50, "page": page},  # Fetch 50 posts per request
            auth=HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)
        )

        print(f"DEBUG: Fetching Page {page}, Status Code: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()
            except ValueError:  # If response is not JSON
                print(f"❌ Error: Non-JSON response (Page {page})")
                print(f"DEBUG: Response content: {response.text}")
                break

            if not data:  # If no more posts, break the loop
                break
            posts.extend(data)
            page += 1  # Move to the next page
        else:
            print(f"❌ Error fetching posts (Page {page}): {response.text}")
            break
    return posts

# Update posts that contain '2024' in title or content
def update_wp_posts():
    posts = get_wp_posts()
    for post in posts:
        post_id = post["id"]
        title = post["title"]["rendered"]
        content = post["content"]["rendered"]

        # Only proceed if '2024' is found in title or content
        if "2024" in title or "2024" in content:
            print(f"DEBUG: Updating post ID {post_id} with title: {title}")

            # Replace 2024 with 2025
            new_title = title.replace("2024", "2025")
            new_content = content.replace("2024", "2025")
            new_date = random_publish_date()

            # Update post
            update_response = requests.post(
                f"{API_URL}/{post_id}",
                json={
                    "title": new_title,
                    "content": new_content,
                    "date": new_date
                },
                auth=HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)
            )

            if update_response.status_code == 200:
                print(f"✅ Updated post ID {title} with new date: {new_date}")
            else:
                print(f"❌ Failed to update post ID {title}: {update_response.text}")
        else:
            print(f"DEBUG: Skipping post ID {post_id} as it does not contain '2024' in the title or content.")

# Run the script
update_wp_posts()
