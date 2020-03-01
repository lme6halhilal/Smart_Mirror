import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
web = QWebEngineView()  # بكج خاص بعرض محركات الويب
web.load(QUrl("https://www.iau.edu.sa/ar"))  # لتحميل رابط الموقع
web.setWindowTitle('IAU Website')  # عنوان الصفحة فوق فحال كان فل سكرين ما يحتاج بس الان للتوضيح
web.showMaximized()  # web.showFullScreen() #ممكن نستبدلها فيه عشان تصير الشاشة كاملة بدون حدود
sys.exit(app.exec_())
