import PyQt5
import sys
import version1

#Implemented with help from https://pythonbasics.org/qt-designer-python/
class MLIDE(PyQt5.QtWidgets.QMainWindow, version1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MLIDE, self).__init__(parent)
        self.setupUi(self)

def main():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    form = MLIDE()
    form.show()
    app.exec_()
main()
