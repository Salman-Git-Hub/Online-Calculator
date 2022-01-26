import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class WebCalculator(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # Loading icon from the web
        self.net = QNetworkAccessManager()
        self.net.finished.connect(self.load_icon)
        self.net.get(QNetworkRequest(QUrl('https://cdn2.iconfinder.com/data/icons/business-finance-solid/24/Calculator-512.png')))
        
        #Set window title
        self.setWindowTitle("Python Calculator")
        #Set window geometry
        self.setGeometry(200, 200, 900, 600)
        
        # Using web engine view
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        url = 'https://www.desmos.com/scientific'
        # Load the url
        self.webEngineView.load(QUrl(url))
        
    def load_icon(self, response):
        pixmap = QPixmap()
        pixmap.loadFromData(response.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
        

app = QApplication(sys.argv)
wc = WebCalculator()
wc.show()
sys.exit(app.exec_())
