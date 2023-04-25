import threading
from time import sleep
import time
from selenium import webdriver
from PyQt5 import QtWidgets, uic
from selenium.webdriver.common.by import By

app = webdriver.Chrome(executable_path=r"C:\Users\R2021\Desktop\Projeto micro bot Blaze\driver\chromedriver")
app.get("https://www.horariodebrasilia.org/")


def vai():
    while True:
        try:
            tempo = app.find_element(By.XPATH, '//*[@id="relogio"]').text
            j1.label.setText(tempo)
        except NameError as erro:
            continue
        except Exception as erro:
            continue


clocking = QtWidgets.QApplication([])
j1 = uic.loadUi("relogio.ui")
j1.show()

threading.Thread(target=vai).start()


clocking.exec() 