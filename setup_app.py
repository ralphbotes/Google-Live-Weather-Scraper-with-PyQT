import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
from icons.resources import *

# Custom packages
from get_weather import weather

class AppMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui",self)
        self.setWindowIcon(QIcon(':/icons/icons/thunderstorms.png'))

        self.button.clicked.connect(self.printValue)
        self.clearButton.clicked.connect(self.clear_text)

    def printValue(self):

        try:
            city = self.lineEdit.text()
            city = city+" weather"
            location_values = weather(city)                 # Display the plot

            self.location.setText(location_values[0])
            self.day_time.setText(location_values[1])
            self.forecast.setText(location_values[2])
            self.temperature.setText(location_values[3])
            self.humidity.setText(location_values[4])
            self.wind.setText(location_values[5])

            self.imageSet(location_values[2])

            self.set_error.setText("")

        except:
            self.clear_text()
            self.set_error.setText("Location error, please try again!")

    def clear_text(self):
        self.lineEdit.clear()
        self.location.clear()
        self.day_time.clear()
        self.forecast.clear()
        self.temperature.clear()
        self.humidity.clear()
        self.wind.clear()

        self.set_error.clear()

    def imageSet(self,forecast):

        iconCl = ":/icons/icons/cloudy.png"             
        iconFo = ":/icons/icons/fog.png"
        iconMi = ":/icons/icons/mist.png"
        iconPC = ":/icons/icons/partly_cloudy.png"      
        iconRL = ":/icons/icons/rain_light.png"
        iconRsC = ":/icons/icons/rain_s_cloudy.png"
        iconRa = ":/icons/icons/rain.png"
        iconSn = ":/icons/icons/snow.png"
        iconSsC = ":/icons/icons/sunny_s_cloudy.png"    
        iconSu = ":/icons/icons/sunny.png"             
        iconTS = ":/icons/icons/thunderstorms.png"
        iconSnL = ":/icons/icons/snow_light.png"
        
        # Check value of passed variable and assign after Creating widget
        self.pixmap = QPixmap()
        clean_forecast = forecast.lower().replace(" ", "")      # Set to lower and remove spaces

        if (clean_forecast == "clearwithperiodicclouds"):
            self.pixmap = QPixmap(iconSsC)

        elif (clean_forecast == "scatteredshowers" or clean_forecast == "isolatedthunderstorms"):
            self.pixmap = QPixmap(iconRsC)
        
        elif (clean_forecast == "clear" or clean_forecast == "sunny"):
            self.pixmap = QPixmap(iconSu)
        
        elif (clean_forecast == "cloudy"):
            self.pixmap = QPixmap(iconCl)

        elif (clean_forecast == "thunderstorm"):
            self.pixmap = QPixmap(iconTS)
        
        elif (clean_forecast == "snowshowers"):
            self.pixmap = QPixmap(iconSnL)

        elif (clean_forecast == "partlycloudy" or clean_forecast == "mostlycloudy" or
                clean_forecast == "mostlysunny"):
            self.pixmap = QPixmap(iconPC)
        
        elif (clean_forecast == "smoke" or clean_forecast == "haze"):
            self.pixmap = QPixmap(iconFo)

        elif (clean_forecast == "lightdrizzle" or clean_forecast == "showers"):
            self.pixmap = QPixmap(iconRL)

        elif (clean_forecast == "rain"):
            self.pixmap = QPixmap(iconRa)

        elif (clean_forecast == "snow"):
            self.pixmap = QPixmap(iconSn)

        else:
            self.pixmap = QPixmap(iconMi)
        
        self.img_label.setPixmap(self.pixmap)
        self.show()