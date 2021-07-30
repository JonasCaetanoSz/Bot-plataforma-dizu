import os
import pickle
import time
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def explore(login):

	if f'{login}.pkl' in os.listdir('Cache/Dizu'):

		return True




def make_tasks(driver):

	task_number = 0
	script_insta = open ('Scripts/insta.js' , 'r').read()
	advance = None

	while True:

		time.sleep(35) # IS THE INTERVAL.

		try:

			driver.execute_script('document.querySelector("#conectar_step_4 > p").click()')
			task_number = task_number + 1
			print(f'\n\033[1;92m[INFO] Realizando Tarefa Nº {task_number} Agora.')
			advance = True

		except WebDriverException as Sem_tarefas :

			print(f'\n\033[1;33m[INFO] Sem tarefas Agora,Buscando novamente...')
			driver.execute_script("document.querySelector('#iniciarTarefas').click()")
			advance = False

		if advance:

			driver.switch_to.window(driver.window_handles[1])
			time.sleep(8.2)
			driver.execute_script(script_insta)
			time.sleep(11)
			driver.close()
			driver.switch_to.window(driver.window_handles[0])
			time.sleep(1)
			driver.execute_script('document.querySelector("#conectar_step_5 > button").click()')





def login(user,hidden_browser):


	if hidden_browser == 's' or hidden_browser == 'S' or hidden_browser == 'sim':

		options = webdriver.ChromeOptions()
		options.add_argument("--headless")
		driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

	else :

		driver = webdriver.Chrome(ChromeDriverManager().install())

	os.system('clear')
	print('\n[INFO] Fazendo Login na dizu, aguarde...')
	cookie_dizu = pickle.load(open(f"Cache/Dizu/{user}.pkl", "rb"))
	driver.get('https://dizu.com.br/login')

	for cookie in cookie_dizu :

		driver.add_cookie(cookie)

	driver.execute_script('window.location.href = "https://dizu.com.br/painel/conectar" ')

	if driver.current_url == 'https://dizu.com.br/painel/conectar':
		
		os.system('clear')
		driver.execute_script('scroll(0,780); document.body.style.zoom = 0.75')
		print('\033[1;92m[INFO] Login Realizado com Sucesso\n')
		return driver

	else : 

		print('[ERROR] Este Cookie Não é mais valido. ')

	return driver



def save_cookie_dizu(driver,user):

	pickle.dump(driver.get_cookies() , open(f'Cache/Dizu/{user}.pkl' , 'wb'))




def save_cookie_instagram(driver,user):

	pickle.dump(driver.get_cookies() , open(f'Cache/Instagram/{user}.pkl' , 'wb'))
	



def login_in_insta(user,driver,selected):

	if f'{user}.pkl' in os.listdir('Cache/Instagram'):

		print(f'\n[INFO] Fazendo Login com o Perfil {user}')
		driver.execute_script('window.open("https://www.instagram.com/")')
		driver.switch_to.window(driver.window_handles[1])
		cookie_insta = pickle.load(open(f"Cache/Instagram/{user}.pkl", "rb"))
		time.sleep(2)

		for cookie in cookie_insta:

			driver.add_cookie(cookie)

		time.sleep(2)
		driver.execute_script('window.location.href = "https://www.instagram.com" ')
		time.sleep(1)
		os.system('clear')
		print(f'\n\033[1;92m[INFO] Login Realizado,iniciando tarefas!')
		driver.execute_script('window.close()')
		driver.switch_to.window(driver.window_handles[0])
		driver.execute_script(f'document.querySelector("#instagram_id").selectedIndex = {selected}')
		driver.maximize_window()
		driver.execute_script("document.querySelector('#iniciarTarefas').click()")
		make_tasks(driver)

	else:

		password = input(f'\nDigite a senha de {user} : ')
		os.system('clear')
		print('\n\033[1;92m[INFO] Fazendo Login no instagram..')
		driver.execute_script('window.open("https://www.instagram.com/")')
		driver.switch_to.window(driver.window_handles[1])
		driver.maximize_window()
		time.sleep(8)
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
		time.sleep(5)

		if driver.current_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':

			os.system('clear')
			print('\n[INFO] Login Realizado,iniciando tarefas..')
			save_cookie_instagram(driver,user)
			driver.execute_script('window.close()')
			driver.switch_to.window(driver.window_handles[0])
			driver.execute_script(f'document.querySelector("#instagram_id").selectedIndex = {selected}')
			driver.maximize_window()
			driver.execute_script("document.querySelector('#iniciarTarefas').click()")
			make_tasks(driver)

		else :

			os.system('clear')
			driver.close()
			driver.switch_to.window(driver.window_handles[0])
			print(f'\033[1;91m[ERROR] login ou senha invalidos tente novamente : \n\n\n')
			login_in_insta(user,driver,selected)