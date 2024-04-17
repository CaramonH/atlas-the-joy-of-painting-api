# Atlas: The Joy of Painting API

Atlas is a RESTful API designed to provide resources and data related to the popular TV show "The Joy of Painting" by Bob Ross. This API offers information about episodes, paintings, techniques, and more, allowing users to explore and learn about the show and its content.

## Features

- **Episode Information**: Get details about each episode, including the season, episode number, title, and air date.
- **Painting Details**: Retrieve information about the paintings created in each episode, such as the title, description, and image.
- **Technique Insights**: Learn about Bob Ross's painting techniques and methods used in different episodes.
- **Search Functionality**: Search for episodes or paintings based on keywords or phrases.

## Technologies Used

- **Python**: Flask is used as the web framework for the API.
- **SQLite**: Database management is handled using SQLite for storing and retrieving data.
- **RESTful Design**: The API follows REST principles for a clear and intuitive interface.
- **JSON Format**: Data is exchanged in JSON format for easy consumption by clients.

## API Diagram
![image](https://github.com/CaramonH/atlas-the-joy-of-painting-api/assets/115739693/c42c36ef-9f4e-4a0f-9e39-d3816e0bc33d)

## Installation

To run the API locally, follow these steps:

1. Clone the repository: `git clone https://github.com/CaramonH/atlas-the-joy-of-painting-api.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `python create_db.py`
4. Run the API: `python app.py`

## Usage

Once the API is running, you can use tools like Postman or curl to interact with it. Here are some example endpoints:

- Get all episodes: `GET /episodes`
- Get a specific episode: `GET /episodes/<episode_id>`
- Search for episodes: `GET /episodes/search?q=<search_query>`
- Get all paintings: `GET /paintings`
- Get a specific painting: `GET /paintings/<painting_id>`

For detailed API documentation, refer to the API documentation at `/docs`.

## Contributing

Contributions to the Atlas API are welcome! If you have any ideas for improvements or new features, feel free to submit a pull request.
