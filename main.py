import requests
import json

# Replace these values with your own
notion_api_key = "YOUR_NOTION_API_KEY"
notion_database_id = "YOU_NOTION_DATABASE_ID"
apple_calendar_api_key = "YOUR_APPLE_CALENDAR_API_KEY"
apple_calendar_user_id = "YOUR_APPLE_CALENDAR_USER_ID"

# Set up the Notion API client
notion_headers = {
    "Authorization": f"Bearer {notion_api_key}",
    "Content-Type": "application/json",
}

# Set up the Apple Calendar API client
apple_calendar_headers = {
    "Authorization": f"Bearer {apple_calendar_api_key}",
    "Content-Type": "application/json",
}

# Get the list of events from the Apple Calendar API
events_url = f"https://api.apple.com/calendar/v1/calendars/{apple_calendar_user_id}/events"
events_response = requests.get(events_url, headers=apple_calendar_headers)
events_data = events_response.json()

# Iterate over the events and add them to the Notion database
for event in events_data["events"]:
    # Extract the relevant event data
    start_time = event["start"]["dateTime"]
    end_time = event["end"]["dateTime"]
    summary = event["summary"]

    # Create a new page in the Notion database with the event data
    new_page = {
        "start_time": {
            "start": start_time
        },
        "end_time": {
            "start": end_time
        },
        "summary": summary,
    }
    create_page_url = f"https://api.notion.com/v3/databases/{notion_database_id}/pages"
    requests.post(create_page_url, headers=notion_headers, json=new_page)

print("Done!")
