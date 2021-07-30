import time 
import os
import pickle
import explore
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# DEFINED COLORS

GREEN = "\033[1;92m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RED = "\033[1;91m"

# END 

def clear():
	os.system('clear')




def select_Profile(driver):
	
	clear()
	print(f'{YELLOW}[+] Selecione o Perfil do instagram : \n')
	profiles = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/div[1]/div/select').text
	lista = []
	b = profiles.split()

	for profiles in b : 

		lista.append(str(profiles))

	opcao = 0
	listagem = lista

	for listagem in listagem:

		if opcao != 0 :

			print(f'[{opcao}] {listagem}\n')
		opcao = opcao + 1

	selected_is = int(input())
	clear()
	usuario = lista[selected_is]
	explore.login_in_insta(usuario, driver , selected_is)
		


clear()

hidden_browser = input(f'{CYAN}[+] Ocultar Navegador [S/N] : ')
user = input('\n[+] Digite Seu Email dizu : ')


def login_in_dizu(user):

	password = input('\n[+] Digite sua senha : ')
	clear()
	print('\n[INFO] Fazendo Login na dizu...')

	if hidden_browser == 's' or hidden_browser == 'S' or hidden_browser == 'sim':

		options = webdriver.ChromeOptions()
		options.add_argument("--headless")
		driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

	else :

		driver = webdriver.Chrome(ChromeDriverManager().install())

	driver.get('https:dizu.com.br/login')
	driver.find_element_by_xpath('//*[@id="login"]').send_keys(user)
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="senha"]').send_keys(password)
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="FormLogin"]/div[5]/button').click() # SUBMIT BUTTON.
	time.sleep(5)

	if driver.current_url == 'https://dizu.com.br/painel':

		clear()
		print('[+] Login Realizado com Sucesso')
		driver.maximize_window()
		explore.save_cookie_dizu(driver,user)
		driver.execute_script('window.location.href = "https://dizu.com.br/painel/conectar" ')
		time.sleep(1)
		driver.execute_script('scroll(0,780); document.body.style.zoom = 0.75')
		select_Profile(driver)

	else:

		print('[ERROR] Login OU senha invalidos;.\n')
		driver.quit()
		clear()
		user = input('\n[+] Digite Seu Email da dizu : ')
		login_in_dizu(user)






if explore.explore(user) == True:

	clear()
	print('\n[INFO] Cookie de Sessão Encontrado\n')

	print('[INFO] Fazendo Login...')
	driver = explore.login(user, hidden_browser)
	select_Profile(driver)

else :

	login_in_dizu(user) 