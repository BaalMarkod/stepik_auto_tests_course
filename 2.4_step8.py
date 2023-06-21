#правильная последовательность такая:
#1. Находим кнопку, которую надо нажать
#2. Пишем ожидание. Оно ничего возвращать не должно. Просто строка кода:
#WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "<От кого ждем>"), "<Что ждем>"))
#3. Кликаем по кнопке из п.1
#4. Прокручиваем страницу вниз. (Пока не прочел камменты 3 годичной давности удивлялся, почему после клика ничего не происходит)
#5. Ну и далее уже как обычно, берем Х, считаем по формуле, находим input, вставляем туда ответ, находим кнопку, нажимаем. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
#Находим кнопку, которую надо нажать
#<button id="book" class="btn btn-primary" onclick="checkPrice();" style="margin-top: 20px;">Book</button>
button = browser.find_element(By.ID, "book")
#Пишем ожидание. Оно ничего возвращать не должно. Просто строка кода #элемент с ценой <h5 id="price" style="display:inline;float:right">$95</h5>
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
#Кликаем по кнопке из п.1
button.click()
#скрол до элемента #<span class="nowrap" id="input_value">879</span>
x_element = browser.find_element(By.ID, "input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
print(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))#ln(abs(12*sin(x)))
y = calc(x)
print(y)
#находим поле для ввода и вводим текст <input class="form-control" name="text" id="answer" type="text" required="">
input1 = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)
#находим 2-ю кнопку и нажимаем <button id="solve" type="submit" class="btn btn-primary" disabled="disabled">Submit</button>
button2=browser.find_element(By.ID, "solve")
button2.click()
time.sleep(50)
