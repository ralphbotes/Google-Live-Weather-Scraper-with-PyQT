from setup_app import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = AppMainWindow()
    mainWindow.show()

    try:
        sys.exit(app.exec_())
    except:
        print('Closing window')