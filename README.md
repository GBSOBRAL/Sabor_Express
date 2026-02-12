# 🍴 Restaurant Management System 🍴
The Restaurant Management System is a comprehensive application designed to simplify the process of managing restaurants. It provides a command-line interface for users to interact with the system, allowing them to perform tasks such as listing restaurants, adding new restaurants, and toggling the active status of restaurants. The system also includes a FastAPI application that provides API endpoints for interacting with restaurant data.

## 🚀 Features
- **Restaurant Listing**: Displays a list of all restaurants, including their names, categories, and active status.
- **Add New Restaurant**: Prompts the user to input details for a new restaurant and adds it to the list.
- **Toggle Active Status**: Allows the user to toggle the active status of a restaurant.
- **API Endpoints**: Provides API endpoints for retrieving restaurant data, including a simple "Hello World" endpoint and an endpoint for retrieving restaurant data from a remote API.
- **Command-Line Interface**: Provides a simple text-based interface for managing the list of restaurants.

## 🛠️ Tech Stack
* **FastAPI**: The FastAPI framework for building the API.
* **Requests**: The requests library for making HTTP requests to the remote API.
* **Pydantic**: The Pydantic library for working with data models.
* **Uvicorn**: The Uvicorn library for running the FastAPI application.
* **OS**: The os module for clearing the console.

## 📦 Installation
### Prerequisites
* Python 3.8 or higher
* pip 20.0 or higher

### Installation
1. Clone the repository using `git clone https://github.com/your-repo/restaurant-management-system.git`
2. Navigate to the project directory using `cd restaurant-management-system`
3. Install the dependencies using `pip install -r requirements.txt`
4. Run the application using `uvicorn main:app --host 0.0.0.0 --port 8000`

## 💻 Usage
1. Run the application using `uvicorn main:app --host 0.0.0.0 --port 8000`
2. Open a web browser and navigate to `http://localhost:8000/docs` to access the API documentation
3. Use the command-line interface by running `python app.py`

## 📂 Project Structure
```markdown
.
├── app.py
├── main.py
├── requirements.txt
├── README.md
```

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and submit a pull request.

## 📝 License
The Restaurant Management System is licensed under the MIT License.
