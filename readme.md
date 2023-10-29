# Movie Data Scraping

This repository contains two Python scripts for scraping movie data from two popular websites: Rotten Tomatoes and IMDb.

## Rotten Tomatoes Script

### Description

The Rotten Tomatoes script extracts movie data, including audience scores, Tomatometer scores, and more, from Rotten Tomatoes' "Best Movies of All Time" list.

### Prerequisites

Before using the Rotten Tomatoes script, ensure you have the following libraries installed:

- `requests`
- `BeautifulSoup`
- `pandas`

### Usage

1. Run the Rotten Tomatoes script to scrape data from Rotten Tomatoes.

2. The script will collect movie details, and the results will be stored in a Pandas DataFrame.

3. You can customize the script to scrape other lists or pages on Rotten Tomatoes.

### Example

```python
# To run the Rotten Tomatoes script
python rotten_tomatoes_scraper.py
```

## IMDb Script

### Description

The IMDb script scrapes data from IMDb's "Top 250" movies list. It extracts details such as movie titles, release years, ratings, and more.

### Prerequisites

Before using the IMDb script, ensure you have the following libraries installed:

- `requests`
- `BeautifulSoup`

### Usage

1. Run the IMDb script to scrape data from IMDb's "Top 250" list.

2. The script will collect movie details, and the results will be displayed in the terminal.

3. You can customize the script to scrape other IMDb movie lists or pages.

### Example

```python
# To run the IMDb script
python imdb_scraper.py
```

## Legal Considerations

Please ensure that you comply with the terms of use and legal regulations when scraping data from websites. Respect the website's `robots.txt` file and review their terms of service before scraping.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Serag el-dein Amged Abd-Alfattah Ahmed
- Student ID: 20201498528

Feel free to use and modify these scripts as needed for your own projects. If you have any questions or encounter issues, please don't hesitate to reach out.
```

You can copy and paste this into your `README.md` file in your GitHub repository. Make sure to customize it with any additional information you want to provide.