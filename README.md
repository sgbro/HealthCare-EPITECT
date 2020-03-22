# EPITECT - DISEASE SURVEILLANCE AND PREDICTION SYSTEM

**EPITECT** is an initiative taken by us to forecast/predict the number of patients infected with **Novel Corona Virus COVID-19**.
Our Model is a **Machine learning** based model that predicts the number of patients infected with corona, the recovery rate and the number of deaths that will be caused due to corona in the upcoming days in the future.

The new strain of Coronavirus has had a worldwide effect. It has affected people from different countries. The dataset provides, a time series data tracking the number of people effected by the virus, how many deaths has the virus caused and the number of reported people who have recovered.
Data is coming from https://github.com/CSSEGISandData/COVID-19 updated daily. We have normalized data a bit - unpivoted and transferred dates to be more machine readable. Alongwith that we’ve used dataflows to process and normalize the data.

The training is done through **Artificial Neural Networks**. The dates, longitude and latitude are label encoded and one hot encoded and are fed into a artificial neural network having two hidden layers and an output layer having the linear activation function.
The network is then used to predict the number of cases in the future by changing the date data field.
With the help of Drop-down menu you select the locations whose prediction you want and accordingly the results are displayed (presently due to lack of data there’s a limitation to this attribute, but in future with sufficient available data it can be proceed easily).

Basically the UI displays two types of result :-
•	The World-wide prediction of the disease, with the help of global map.
•	Second is the region-specific prediction based on the region selected from the drop-down
It shows various comparisons among different predicted rates in form of Line-Charts as well as Bar-Charts.
These comparisons can be studied for further analysis by the concerned authorities.

##### **Setup development environment:**
We assume you have python 3.0+ installed.
•	Create a directory where you can keep your cloned repository then cd to that directory.
•	git clone https://github.com/sgbro/HealthCare-EPITECT.git
•	cd to the cloned repository
•	install the required libraries.
NOTE: **activate** your virtual environment before this so that it gets installed in that environment.
•	run the **app.py** file so that the project will run in your browser locally.

