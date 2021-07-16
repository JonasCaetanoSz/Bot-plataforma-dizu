from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
import os
from getpass import getpass
from selenium.common.exceptions import WebDriverException

passar = None

# DEFINED COLORS 

GREEN = "\033[1;92m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RED = "\033[1;91m"

# END
def clear():

	os.system('clear')

def do_tasks(driver):
	number_tarefa = 0
	time.sleep(1)

	while True:

		time.sleep(35)

		try:

			driver.execute_script('document.querySelector("#conectar_step_4 > p").click()')
			number_tarefa = number_tarefa + 1
			print(f'\n{GREEN}[INFO] Realizando Tarefa Nº {number_tarefa} Agora.')
			driver.execute_script('document.querySelector("#conectar_step_5 > button").click()')
			passar = True

		except WebDriverException as erro:

			print(f'\n{YELLOW}[INFO] Sem tarefas Agora,Buscando novamente...{GREEN}')
			driver.execute_script("document.querySelector('#iniciarTarefas').click()")
			passar = False

		time.sleep(8)

		if passar == True:

			driver.switch_to.window(driver.window_handles[1])
			driver.execute_script('var button = document.querySelector("button"); if (button.textContent == "Seguir" ) {button.click()} else {document.querySelector("article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()}')
			time.sleep(15)
			driver.close()
			driver.switch_to.window(driver.window_handles[0])

		else : 

			pass

def login_insta(driver , insta_list , user_select):
	
	usuario = insta_list[user_select]
	passw_insta = input(f'[+] digite a senha do perfil {usuario} : ')
	clear()
	print(f'\n{CYAN}[INFO] Fazendo login no instagram...')
	driver.execute_script('window.open("https://instagram.com/")')
	time.sleep(5)
	driver.switch_to.window(driver.window_handles[1])
	clear()
	print(f'\n{CYAN}[INFO] Fazendo login no instagram...')
	time.sleep(5)
	input_insta_user = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
	input_insta_passw = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
	input_insta_user.send_keys(usuario)
	time.sleep(2)
	input_insta_passw.send_keys(passw_insta)
	driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
	time.sleep(5)

	if driver.current_url == 'https://www.instagram.com/accounts/onetap/?next=%2F':

		driver.execute_script('window.close()')
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(2)
		clear()
		print(f'{GREEN}\n[INFO] Login realizado,iniciando Tarefas...')
		
	else:

		print('\n\nSenha incoreta tente novamente.')
		driver.execute_script('window.close()')
		time.sleep(5)
		clear()
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(1)
		login_insta(driver,insta_list , user_select)

def select(driver):


	time.sleep(3)
	insta_str = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/form/div[1]/div/select').text
	insta_list = []
	b = insta_str.split()

	for insta_str in b :

		insta_list.append(str(insta_str))

	clear()
	print(f'{YELLOW}[+] selecione o perfil : \n\n')

	e = 0

	listagem = insta_list

	for listagem in listagem:

		print(f'[{e}] {listagem}\n')

		e = e + 1

	user_select = int(input())

	while user_select > len(insta_list) or user_select == 0:

		print(f'{RED}resposta invalida{RESET}\n')
		
		user_select = int (input('digite uma das opção: '))
	login_insta(driver , insta_list , user_select)

	driver.execute_script("document.body.style.zoom = 0.75")
	driver.execute_script(f'document.querySelector("#instagram_id").selectedIndex = {user_select }')
	time.sleep(1)
	driver.execute_script("document.querySelector('#iniciarTarefas').click()")
	driver.execute_script("scroll(0,1390)")

	clear()

	print(f'\n{GREEN}[INFO] o perfil foi selecionado com sucesso!')
	do_tasks(driver)



def login():


	clear()
	options = None
	user_dizu = input(f'{CYAN}[+] digite seu email do dizu : ')
	passw_dizu = getpass(f'{CYAN}\n[+] digite sua senha do dizu : ')
	browser_view = input(f'{CYAN}\n[+] ocultar o navegador [S/N]: ')
	if browser_view == 'S' or browser_view == 's' or browser_view == 'sim':

		options = webdriver.ChromeOptions()
		options.add_argument("--headless")
		driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

	else:

		driver = webdriver.Chrome(ChromeDriverManager().install())
	clear()
	driver.maximize_window()
	print(f'\n{GREEN}[INFO] Fazendo login no Dizu aguarde...')
	driver.get('https://dizu.com.br/login')
	user = driver.find_element_by_xpath('/html/body/div[1]/section/form/div[1]/div/input')
	time.sleep(2)
	senha = driver.find_element_by_xpath('/html/body/div[1]/section/form/div[2]/div/input')
	user.send_keys(user_dizu)
	senha.send_keys(passw_dizu)
	time.sleep(2)
# CLICK IN BUTTON SUBMIT
	driver.find_element_by_xpath('/html/body/div[1]/section/form/div[5]/button/p').click()
	time.sleep(3)

	if driver.current_url == 'https://dizu.com.br/painel':

		clear()
		print(f'\n{GREEN}[INFO] login realizado com sucesso!')
		driver.execute_script("window.location.href = 'https://dizu.com.br/painel/conectar' ")
		time.sleep(1)
		driver.execute_script("scroll(0,780); document.body.style.zoom = 0.75")
		select(driver)

	else:

		clear()
		print(f'{YELLOW}[INFO] ocoreu um erro ao logar')
		driver.quit()
		login()


	while True:
		pass

login()