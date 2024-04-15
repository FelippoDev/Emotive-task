# Take Home - Mars Photo List API
Retrieve all mars photos from a specific day and camera.

## Requirements
Ensure a seamless setup with the following prerequisites:
* Docker - See [Get Docker](https://docs.docker.com/get-docker/)
* Docker Compose - Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)
* API Key - To generate the API Key access the NASA website, See [Generate NASA API Key](https://api.nasa.gov/index.html)


## Setup
1. Clone github repository in your local system `git clone https://github.com/FelippoDev/Emotive-task`
2. Navigate to the project directory in your terminal
3. Create the necessary environment variables: within the repository, create a file called `.env` inside ```app``` folder then inside this file set the environment variables following the examples in the `.env.example`
4. set the environment variable `NASA_BASE_URL` to `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos` and the variable ```NASA_API_KEY``` set the generated [API Key](#requirements)
5. At last, run the command:
```python
    docker-compose up --build
```

## Starting
You can access the API docs by visiting this URL in your preferred browser.
API Docs: `http://127.0.0.1:8000/`

## API
In the API we have a endpoint called `GET /api/v1/mars_photos` that awaits two query parameters:

- **camera(Enum):** Select camera by name, Only accepts the following cameras names:
    1. `Chemistry and Camera Complex`
    2. `Navigation Camera`
    3. `Rear Hazard Avoidance Camera`
    4. `Front Hazard Avoidance Camera`
    5. `Mast Camera`
    6. `Mars Hand Lens Imager`
    7. `Mars Descent Imager`

- **earth_date(Date):** Retrieve mars photo by earth date, example: `2024-01-01`

