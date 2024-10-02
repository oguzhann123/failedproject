import time
import xpaths
import password
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Unicode karakterler için stdout ayarları
sys.stdout.reconfigure(encoding='utf-8')




# Chrome tarayıcı seçeneklerini oluşturun
driver_path = "C:\\Users\\Oguzhan\\Desktop\\dd\\Booking-Visa-Appointments-with-VFS-Global-main\\chromedriver.exe"

# Service ve Options ayarları
service = Service(driver_path)
options = Options()

# Mevcut Chrome profilini kullanmak için argumentler
options.add_argument("user-data-dir=C:\\Users\\Oguzhan\\AppData\\Local\\Google\\Chrome\\User Data")  # Kullanıcı verisi dizini
options.add_argument("profile-directory=Profile 8")  # Kullanmak istediğiniz profil dizini

# Diğer seçenekler
options.add_argument("--no-sandbox")  # Sandbox'ı devre dışı bırak
options.add_argument("--disable-dev-shm-usage")  # Paylaşımlı belleği devre dışı bırak
# options.add_argument("--headless")  # Tarayıcıyı başlatmadan arka planda çalıştırmak için bu satırı kaldırın
options.add_argument("--disable-gpu")  # GPU'yu devre dışı bırak
options.add_argument("--remote-debugging-port=9222")  # Uzaktan hata ayıklamayı etkinleştir

# WebDriver'ı başlatın
browser = webdriver.Chrome(service=service, options=options)

# Biraz bekle sayfanın tam yüklenmesi için
time.sleep(5)  # Sayfanın tamamen açılmasını beklemek için 5 saniye

# VFS Global linkine git
browser.get('https://visa.vfsglobal.com/tur/tr/pol/login')

# Yönlendirme olup olmadığını kontrol edin
time.sleep(5)  # Sayfanın yüklenmesini beklemek için
if "vfsglobal" in browser.current_url:
    print("Doğru sayfadasınız!")
else:
    print("Yanlış sayfa, tekrar yönlendiriliyor...")
    browser.get('https://visa.vfsglobal.com/tur/tr/pol/login')


# Sayfanın tamamen yüklenmesini bekleyin
WebDriverWait(browser, 30).until(
    lambda d: d.execute_script('return document.readyState') == 'complete'
)



# Eğer bir pop-up ya da çerez onayı penceresi varsa, onu kapatın
try:
    cookie_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))  # XPath'inizi buraya ekleyin
    )
    cookie_button.click()
except:
    print("Çerez onayı yok veya kapanamadı, devam ediliyor...")



  # CAPTCHA'nın manuel çözülmesini bekle
input("Lütfen CAPTCHA'yı çözün ve Enter'a basarak devam edin...")

# CAPTCHA çözüldükten sonra sayfanın yüklenmesini bekle
WebDriverWait(browser, 30).until(
    lambda d: d.execute_script('return document.readyState') == 'complete'
)


# Wait for the checkboxes to be present
wait = WebDriverWait(browser, 10)

# Select the first checkbox
first_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="checkbox"])[1]')))
first_checkbox.click()

# Select the second checkbox
second_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="checkbox"])[2]')))
second_checkbox.click()

# Wait for the 'Yeni Rezervasyon Başlat' button to become clickable and then click it
start_reservation_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Yeni Rezervasyon Başlat")]')))
start_reservation_button.click()




# Click the "Şartlar ve Koşullar" checkbox and continue
def accept_terms():
    # Check the terms and conditions box
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//mat-checkbox'))).click()  # Update the XPath with the correct one for the checkbox
    
    # Click the "Devam et" button
    continue_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Devam et")]')))
    continue_button.click()

    # Accept the terms and conditions
accept_terms()

def fill_form():
    # Fill "İsim" field
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-6"]'))).send_keys('YourFirstName')

    # Fill "Soyisim" field
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-7"]'))).send_keys('YourLastName')

    # Select "Cinsiyet"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-1"]'))).click()
    gender_option = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Male")]')))  # Update with the correct gender text
    gender_option.click()

    # Select "Uyruk"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-3"]'))).click()
    nationality_option = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Turkey")]')))  # Update with the correct nationality text
    nationality_option.click()

    # Fill "Pasaport Numarası" field
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-8"]'))).send_keys('U18238184')

    # Fill "İletişim Numarası" fields
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-9"]'))).send_keys('44')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-10"]'))).send_keys('0123456789')

    # Fill "E Posta" field
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-11"]'))).send_keys('HasanSelamentlekal@gmail.com')
    
def submit_form():
    save_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div/app-applicant-details/section/mat-card[2]/app-dynamic-form/div/div/app-dynamic-control/div/div/div[1]/button')))
    save_button.click()

# Fill out the form
fill_form()

# Submit the form
submit_form()

# E-posta gönderme fonksiyonu
def send_email(subject, body, to_email):
    sender_email = "papa.cafercan@gmail.com"
    sender_password = ""  # 16 karakterlik şifren

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {e}")
    finally:
        server.quit()

# Randevu kontrolü ve email gönderme
randevu_bulundu = False  # Bu değişkeni randevu bulma işlemi sonunda güncelle

if randevu_bulundu:
    send_email("Randevu Bulundu!", "Randevunuz bulundu, hemen giriş yapın.", "nebaktn.degsk@gmail.com")
else:
    send_email("Randevu Bulunamadı", "Henüz randevu bulunamadı, tekrar deneyin.", "nebaktn.degsk@gmail.com")


# Tarayıcının kapanmasını önlemek için
input("İşlemler tamamlandı. Tarayıcıyı kapatmak için Enter'a basın...")


