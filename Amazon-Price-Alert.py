
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import smtplib

window = tk.Tk()
window.title("Amazon Price Notifier")

def check_price():
    url = url_entry.get()
    threshold = float(threshold_entry.get())
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    # The User-Agent header is a part of the HTTP request that identifies the client software
    # re = requests.get(
    #     'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')

   

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    price = float(soup.find('p', class_='price_color').text[1:])
    # print(type(price))
    if price < threshold:
        send_email(url)



def send_email(url):
    smt = smtplib.SMTP('smtp.gmail.com', 587)
    smt.ehlo()  # this line means we are saying "hello " to server
    smt.starttls()  # It starts security measures
    smt.login('jadhavomkar8087@gmail.com', 'dxyndqufzykvqsfm')
    smt.sendmail('jadhavomkar8087@gmail.com',
                 'amazonkatta2002@gmail.com', 
                 f"Subject: Amzon Price Notifier\n\n hi, price has dropped to your Desired price.\nbuy it ")
    smt.quit()  

# GUI elements
url_label = tk.Label(window, text="Amazon URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

threshold_label = tk.Label(window, text="Desired Price Threshold:")
threshold_label.pack()
threshold_entry = tk.Entry(window, width=10)
threshold_entry.pack()

submit_button = tk.Button(window, text="Submit", command=check_price)
submit_button.pack()

# Run the GUI
window.mainloop()
          
