# Fruits API

Hi! This is my submission for the Fruits API technical assignment.  
It’s a simple, containerized REST API built using **FastAPI**, which supports a fixed list of fruits with features like:

- Persistent data using a local JSON file  
- Counting repeated entries  
- Case-insensitive fruit input  
- Swagger UI for easy testing  
- Docker support  
- Automated testing with Pytest

---

## Features

- `GET /fruits` – List all fruits
- `POST /fruits` – Add a fruit (increments count if it already exists)
- `GET /fruits/by-name/{fruit_name}` – Look up a fruit by name (case-insensitive)
- `GET /fruits/{fruit_id}` – Look up a fruit by ID

---

## Tech Stack

||Tool        | Use                   ||
||------------|---------------------- ||
|| Python     | Main language         ||
|| FastAPI    | Web framework         ||
||Uvicorn     | ASGI server           ||
||Docker      | Containerization      ||
|| JSON       | Data persistence      ||
|| Pytest     | Automated testing     ||

---

##  How to Run the App

### Locally:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn app.main:app --reload


#Once running, 
open http://localhost:8000/docs
#This opens FastAPI's auto-generated Swagger UI , it's easy to test from there.

### With Docker

# Build image
docker build -t fruits-api .

# Run container
docker run -p 8000:8000 fruits-api

#Once running 
open Swagger UI: http://localhost:8000/docs

## Run Tests

pytest

->Ensure you're in the virtual environment and dependencies are installed first.

## Supported Fruits

# Only the following fruits are supported. Each has a predefined color.
-------------------------
|Fruit	    ||   Color  |
|-----------||----------|
|apple	    ||  red     |
|banana	    ||  yellow  | 
|orange	    ||  orange  |
|grape	    ||  purple  |
|kiwi	    ||  green   |
|lemon	    ||  yellow  |
|mango	    ||  orange  |
|pear	    ||  green   |
|pineapple  ||  brown   |
|strawberry ||  red     |

->If you try to add a fruit not in this list, the API will return an error.

### Additional Features Added
 The original assignment asked for a basic CRUD API. To make the app more realistic and user-friendly, I added a 
 
~ few improvements:

--> Case-insensitive fruit names
    Users can input "Apple", "apple", or "APPLE" and it’ll be handled the same.

--> Counting logic
    If a fruit is added again, the count field increments instead of creating a duplicate entry.

--> Name-based lookup
    Instead of using fruit IDs (which users won’t know), the API includes a GET /fruits/by-name/{fruit_name} endpoint to easily search by name.

--> Error validation
    Invalid fruits return helpful messages

--> Duplicate fruits increment count automatically

--> Only the fruit name is required when posting — color is auto-mapped

## Example API Test Scenarios (Swagger UI)

|===============================================================================================|
|Method	||  Endpoint	          ||Example Body / Path	    || Expected Result                  |
|=======||========================||========================||==================================|
|POST   || /fruits                ||   {"fruit": "Mango"}	||   Adds mango with count = 1      |
|POST	|| /fruits	              ||   {"fruit": "mango"}	||   Increments mango to count = 2  |
|POST	|| /fruits	              ||   {"fruit": "Papaya"}  ||	 Error – unsupported fruit      |
|GET	|| /fruits/by-name/mango  ||	                    ||   Returns mango details          |
|GET	|| /fruits/by-name/papaya ||	                    ||   Error – not found              |
|GET	|| /fruits		          ||                        ||   List of all added fruits       |
|GET	|| /fruits/1	          ||                        ||   Returns fruit with ID 1        |


## CI/CD Pipeline

-> As part of the assignment, I also set up a GitHub Actions-based CI/CD pipeline.
   Every time I push code or open a pull request to the main branch, the pipeline automatically does the following:

* Checks out the latest code

* Sets up a clean Python 3.11 environment

* Installs dependencies from requirements.txt

* Runs all API tests using pytest

* Builds the Docker image to ensure containerization works as expected

This helps ensure the project is always testable, stable, and deployment-ready.

-> You can find the pipeline config in:
   .github/workflows/ci.yml

-> And see workflow results in the Actions tab.


~~Thanks for the opportunity — it was a fun build!


