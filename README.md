# 📈 Stock Data API

## Overview

The **Stock Data API** is a Django-based web service that retrieves real-time
stock price data for multiple companies using the Alpha Vantage API. Users can
request stock prices by providing stock symbols as query parameters, and the API
returns structured JSON responses.

## Features

- Fetch real-time stock prices for multiple symbols.
- Return JSON-formatted responses for easy integration.
- Built using Django REST Framework for scalability.

## Tech Stack


- **API Integration:** Alpha Vantage API
 - **Environment Management:** Python virtual environments

## Installation

### Prerequisites

- Python 3.8+
- Django
- Requests library

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-data-api.git
   cd stock-data-api
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:** Create a `.env` file and add your Alpha
Vantage API key:
   ```
   ALPHA_VANTAGE_API_KEY=your_api_key_here
   ```
5. **Run database migrations:** (If using PostgreSQL for persistent storage)
   ```bash
   python manage.py migrate
   ```
6. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoint

```
GET /api/stocks/?symbols=AAPL&symbols=GOOGL&symbols=MSFT
```

### Example Response

```json
{
 i {"time": "2024-03-01 16:00:00", "price": "330.10"}
}
```

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue
if you have suggestions or improvements.

## License

This project is licensed under the **MIT License**. See the LICENSE file for
details.

