# The Seeker of Judas
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QIcon, QFont, QPixmap
from random import shuffle

class Seekers:
    def __init__(self):
        # Create frame
        frame = QFrame()
        vb.addWidget(frame)

        # Add label
        form = QFormLayout(frame)
        Title = QLabel('The Seeker of Judas')
        Title.setFont(QFont('Elephant', 26))
        Title.setStyleSheet('color:blue;')
        Title.setAlignment(Qt.AlignCenter)
        form.addRow(Title)

        frame = QFrame()
        form.addRow(frame)
        grid = QGridLayout(frame)
        target0 = QRadioButton('Disciple1')
        target0.setChecked(True)
        grid.addWidget(target0, 0,0)
        target1 = QRadioButton('Disciple2')
        grid.addWidget(target1, 0,1)
        target2 = QRadioButton('Disciple3')
        grid.addWidget(target2, 0,2)
        target3 = QRadioButton('Disciple4')
        grid.addWidget(target3, 1,0)
        target4 = QRadioButton('Disciple5')
        grid.addWidget(target4, 1,1)
        target5 = QRadioButton('Disciple6')
        grid.addWidget(target5, 1,2)
        target6 = QRadioButton('Disciple7')
        grid.addWidget(target6, 2,0)
        target7 = QRadioButton('Disciple8')
        grid.addWidget(target7, 2,1)
        target8 = QRadioButton('Disciple9')
        grid.addWidget(target8, 2,2)
        target9 = QRadioButton('Disciple10')
        grid.addWidget(target9, 3,0)
        target10 = QRadioButton('Disciple11')
        grid.addWidget(target10, 3,1)
        target11 = QRadioButton('Disciple12')
        grid.addWidget(target11, 3,2)

        self.targets = [target0, target1, target2, target3, target4, target5, target6, target7, target8, target9, target10, target11]

        # Add button
        btn = QPushButton('Select', clicked=self.seek)
        btn.setToolTip('click to blast')
        form.addRow(btn)

    def seek(self):
        real = ['Disciple1', 'Disciple2', 'Disciple3', 'Disciple4', 'Disciple5', 'Disciple6',
        'Disciple7', 'Disciple8', 'Disciple9', 'Disciple10', 'Disciple11', 'Disciple12']
        shuffle(real)
        Real = real[0]
        for target in self.targets:
            if target.isChecked():
                if target.text() == Real:
                    QMessageBox.information(win, 'Status', 'Congratulations!: Mission successful')
                else:
                    QMessageBox.critical(win, 'Status', 'Retry: Mission failed!')


app = QApplication([])
app.setStyle('Fusion')

# Set window and widget color
qp = QPalette()
qp.setColor(QPalette.Window, Qt.yellow)
qp.setColor(QPalette.Button, Qt.gray)
app.setPalette(qp)

# Create window
win = QWidget()
win.setFixedSize(490,300)
win.setWindowTitle('The Seeker of Judas')
win.setFont(QFont('Arial Bold', 20))

# Create menu bar
vb = QVBoxLayout(win)
bar = QMenuBar()
bar.setNativeMenuBar(False)
Menu = bar.addMenu("≡ Menu")
vb.addWidget(bar)

def about(self):
    dialog = QDialog()
    dialog.setWindowTitle('About')
    dialog.setFont(QFont('Arial Bold', 10))
    dialog.setFixedSize(250,280)
    vb = QVBoxLayout(dialog)
    fme = QFrame()
    vb.addWidget(fme)
    grid = QGridLayout(fme)
    product = QLabel('The Seeker\nof Judas')
    product.setFont(QFont('Elephant', 16))
    product.setStyleSheet('color:blue;')
    grid.addWidget(product, 0,0)

    frame = QGroupBox('Developed by:')
    vb.addWidget(frame)
    form = QFormLayout(frame)
    details = QLabel('Name: Peter Oyelegbin \n\nWhatsApp: 08078828296 \n\nGmail: peteroyelegbin@gmail.com \n\n© 2020')
    form.addRow(details)

    close = QPushButton('Close', clicked=dialog.close)
    vb.addWidget(close)
    dialog.exec_()

# Add menu item
About = QAction("About", triggered=about)
Menu.addAction(About)
Quit = QAction("Quit", triggered=win.close)
Quit.setShortcut('Ctrl+Q')
Quit.setStatusTip('Exit application')
Menu.addAction(Quit)

Seekers = Seekers()

win.show()
app.exec_()
