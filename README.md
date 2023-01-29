# Flask-Anime-Hub-App

This is a Flask web app that lets you watch and keep track of your favorite anime. The app uses a scraper called gogoscraper to fetch anime information and streaming links, and SQLite for data storage.

## Features

* Search for anime by title
* View detailed information about an anime, including a brief summary and a list of episodes
* Follow and keep track of anime in a "following" list
* Watch anime with a built-in video player
* Update the last watched episode of a followed anime

## Prerequisites

* [Python 3.11](https://www.python.org/downloads/)
* Flask
* SQLite3
* BeautifulSoup4

## Installation

1. Clone the repository

```
 git clone
```

2. Change into the project directory

```
 cd my-anime-dev
```

3. Create and activate a virtual environment

```
 source venv/bin/activate
```

4. Install the required packages

```
 pip install -r requirements.txt
```

5. Start the app

```
 export FLASK_APP=app.py
 flask run
```

**The app should now be running on **[http://localhost:5000](http://localhost:5000/).

## Preview

![1675007496832](image/README/1675007496832.png)

## Contributing

This is an open-source project, and contributions are welcome. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

**This project is licensed under the MIT License - see the **[LICENSE](https://chat.openai.com/LICENSE) file for details.

## Contributors

* [Shalin Devkota](https://www.github.com/GenVenom) - Backend and Idea For this Project
* [Sulav Baral](https://github.com/tyzrex) - Frontend and Design
