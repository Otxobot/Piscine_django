import requests
import json
import dewiki
import sys
import os


def format_filename(search_term):
    """Format the search term to create a valid filename."""
    return search_term.replace(" ", "_") + ".wiki"


def search_wikipedia(term, language="en"):
    try:
        # Wikipedia API endpoint
        api_url = f"https://{language}.wikipedia.org/w/api.php"

        # API parameters
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "explaintext": True,
            "titles": term,
        }

        # Make the request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse the response JSON
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        if not pages:
            raise ValueError("No results found.")

        # Extract the content
        for page_id, page_data in pages.items():
            if page_id == "-1":
                raise ValueError("No results found for the search term.")
            return dewiki.from_string(page_data.get("extract", ""))

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error during API request: {e}")
    except ValueError as ve:
        raise RuntimeError(str(ve))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py <search_term>")
        return

    search_term = sys.argv[1]

    if not search_term.strip():
        print("Error: Search term cannot be empty.")
        return

    try:
        result = search_wikipedia(search_term)

        # Format the filename
        filename = format_filename(search_term)

        # Write the result to the file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(result)

        print(f"Search result saved to: {filename}")

    except RuntimeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
