# ✈️ Flight Price Prediction

A machine learning web application built with **Python and Streamlit** that predicts flight prices based on selected flight details.

The application provides an interactive interface where users can enter flight information such as airline, source and destination cities, departure and arrival times, number of stops, class, duration, and days remaining before departure.

## 📌 Features

* ✈️ Interactive flight price prediction interface
* 🏙️ Source and destination city selection
* 🛫 Airline and flight number selection
* 🕐 Departure and arrival time selection
* 🛑 Number of stops selection
* 💺 Flight class selection
* ⏱️ Flight duration input
* 📅 Days left before departure
* ✅ Source and destination validation
* 🔎 Route-based flight availability checking
* 🤖 Pre-trained machine learning model
* 💰 Flight price displayed in Indian Rupees (₹)
* 📋 Displays selected flight details after prediction

## 🛠️ Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Application development          |
| Streamlit    | Web application interface        |
| Pandas       | Data loading and data processing |
| Scikit-learn | Machine learning                 |
| Pickle       | Loading the trained model        |

## 📂 Project Structure

```
Flight-Price-Prediction/
│
├── app.py
├── flight_price_Dataset.csv
├── model_flight.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                       | Description                            |
| -------------------------- | -------------------------------------- |
| `app.py`                   | Main Streamlit application             |
| `flight_price_Dataset.csv` | Flight dataset used by the application |
| `model_flight.pkl`         | Pre-trained machine learning model     |
| `requirements.txt`         | Required Python dependencies           |
| `README.md`                | Project documentation                  |

## ⚙️ How the Application Works

The application follows these steps:

```
User
  ↓
Enter Flight Details
  ↓
Validate Input
  ↓
Check Flight Availability
  ↓
Create Prediction Data
  ↓
Load Pre-trained Model
  ↓
Predict Flight Price
  ↓
Display Result
```

The selected flight information is converted into a Pandas DataFrame and passed to the trained model to generate the prediction.

## 🔍 Input Features

| Feature          | Description                               |
| ---------------- | ----------------------------------------- |
| Airline          | Selected airline                          |
| Flight           | Flight number                             |
| Source City      | Departure city                            |
| Departure Time   | Scheduled departure time                  |
| Stops            | Number of stops                           |
| Arrival Time     | Scheduled arrival time                    |
| Destination City | Arrival city                              |
| Class            | Flight class                              |
| Duration         | Flight duration in hours                  |
| Days Left        | Number of days remaining before departure |

## 🚀 Installation

### 1. Clone the Repository

```
git clone <[https://github.com/sanjaykumar-21/Flight-Price-Prediction-System]>
```

Navigate to the project directory:

```
cd Flight-Price-Prediction
```

### 2. Create a Virtual Environment

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

After running the command, Streamlit will provide a local URL. Open that URL in your browser to use the application.

## 🖥️ How to Use

1. Open the Streamlit application.
2. Select the **Source City**.
3. Select the **Destination City**.
4. Select the **Airline**.
5. Select an available **Flight Number**.
6. Select the **Departure Time**.
7. Select the **Arrival Time**.
8. Select the number of **Stops**.
9. Select the flight **Class**.
10. Enter the flight **Duration**.
11. Enter the number of **Days Left** before departure.
12. Click **🔮 Predict Flight Price**.
13. View the predicted flight price and selected flight details.

## ⚠️ Validation and Error Handling

### Same Source and Destination

The application prevents predictions when the source and destination cities are the same.

### Flight Availability

The application checks the selected route and retrieves available flight numbers. If no flight is available for the selected route, a warning is displayed.

### Model Loading

The application loads the trained model from:

```
model_flight.pkl
```

If the model cannot be loaded, an error message is displayed.

### Prediction Error

If an error occurs while generating the prediction, the application displays an error message.

## 🤖 Machine Learning Model

The project uses a pre-trained machine learning model stored in:

```
model_flight.pkl
```

The model is loaded when the application starts. When the user clicks the prediction button, the application creates the required input data and passes it to the model to generate the predicted flight price.

## 📊 Dataset

The application uses the following dataset:

```
flight_price_Dataset.csv
```

The dataset provides flight information used by the application for selecting cities, airlines, flights, departure times, arrival times, stops, classes, duration, and days left.

## 📦 Requirements

Install the required packages using:

```
pip install -r requirements.txt
```

Main dependencies include:

```
streamlit==1.63.0
pandas==3.0.5
numpy==2.5.2
scikit-learn==1.9.0
scipy==1.18.1
joblib==1.6.0
cloudpickle==3.1.2
```

For the complete list of dependencies, refer to `requirements.txt`.

## 🚧 Future Improvements

* 📈 Add model performance metrics
* 📊 Add flight-price visualizations
* 🔍 Add exploratory data analysis
* 🎯 Improve input filtering based on selected routes
* 💡 Display estimated price ranges
* 🔄 Add automated model retraining
* ☁️ Deploy the application online
* 📱 Improve the interface for mobile devices

## 📸 Application Preview

You can add a screenshot of your application to the README.

Create a folder named `screenshots` and add your screenshot:

```
screenshots/
└── app.png
```

Then add the following to your README:

```
![Flight Price Prediction App](screenshots/app.png)
```

## ⭐ Acknowledgements

This project was developed using:

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* SciPy
