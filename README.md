# PROJETO EMI ( ESTAÇÃO METEOROLOGICA INTELIGENTE )

### FLUXOGRAMA DO PROJETO

![Captura de tela 2025-02-18 143643](https://github.com/user-attachments/assets/2cbb9c78-8514-4324-96ac-709fb49674f9)


O projeto foi idealizado para coletar temperatura e umidade do ambiente em que o raspiberry esta, utilizando o sensor ==DHT22==.

Após a realização da coleta, ele ira mandar para a cloud, foi escolhido o SUPABASE, por ser de graça, até uma certa quantidade de dados, e principalmente pelo seu istant API, que é uma api que realiza o CRUD (CREATE, READ,DELETE E UPDATE), principal operação em aplicações.

Com os dados recebidos através de uma requisição post, feita pelo raspiberry, populando nossa base de dados do supabase.

A visualização desses dados será através do aplicativo mobile, criado em react native. Mostrando as últimas requisições feitas, ou seja um real time da temperatura e umidade do ambiente. 

---
# Configuração do Raspberry

Para a configuração do raspberry foi utilizado o sistema operacional UBUNTU SERVER 22.04 LTS, abaixo esta todos os passos para a realização dessa configuração com o ubuntu server ja salvo no cartão sd do raspberry.

Depencias linux para rodar o python 3:

```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```

### Comandos uteis para a utilização do ubuntu.

Para vê os processos da maquina ocorrendo em tempo real

```bash
sudo apt install btop para ver os status da maquina
```

para dividir a tela:
```bash
tmux
```

# Configuração do Git e Git hub

Para instalar e configurar o Git no Ubuntu, siga os passos abaixo:

---

### **1. Instalar o Git**

1. Abra o terminal no Ubuntu.
2. Atualize os repositórios locais:
    
    ```bash
    sudo apt update
    ```
    
3. Instale o Git:
    
    ```bash
    sudo apt install git
    ```
    
4. Verifique se o Git foi instalado corretamente:
    
    ```bash
    git --version
    ```
    

---

### **2. Configurar usuário do Git**

1. Configure o nome de usuário global:
    
    ```bash
    git config --global user.name "Seu Nome"
    ```
    
2. Configure o e-mail global:
    
    ```bash
    git config --global user.email "seu-email@example.com"
    ```
    
3. Verifique as configurações:
    
    ```bash
    git config --list
    ```
    

---

### **3. Logar no Git (com GitHub, GitLab ou outro)**

O Git em si não possui login, mas é possível se autenticar em serviços de controle de versão como GitHub ou GitLab. Use uma chave SSH ou um token de acesso.

#### **Método Autenticação com Chave SSH**

1. Gere uma chave SSH:
    
    ```bash
    ssh-keygen -t ed25519 -C "seu-email@example.com"
    ```
    
    - Pressione `Enter` para salvar no local padrão.
    - Opcional: Defina uma senha para proteger a chave.
2. Adicione a chave SSH ao agente:
    
    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```
    
3. Copie a chave pública:
    
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    
4. Adicione a chave ao GitHub/GitLab:
    
    - GitHub: [Adicionar chave SSH](https://github.com/settings/keys)
    - GitLab: [Adicionar chave SSH](https://gitlab.com/-/profile/keys)
5. Teste a conexão:
    
    ```bash
    ssh -T git@github.com
    ```
    
    Ou para GitLab:
    
    ```bash
    ssh -T git@gitlab.com
    ```

	 Após isso crie uma pasta em seu diretório e clone seu projeto para dentro desta pasta. Faça as modificações que precisa e pode dar um:
	 ```bash
	 git push origin main
```

Com isso, você pode começar a usar o Git para gerenciar seus repositórios. Caso tenha dúvidas, posso ajudar com mais detalhes! 😊

---

# Ativando ambiente virtual dentro da pasta do projeto.

Navegue até a pasta do projeto, ou o código e ative o ambiente virtual da maquina ubuntu.

  1. Para criar o ambiente virtual
  ```
  python3 -m venv .venv
 ```   

   2.  Para ativar o ambiente virtual 
   ```
   source .venv/bin/activate
```

   3. para sair do ambiente virtual 
   ```bash
   deactivate 
```

---

###  **UTILIZANDO DHT22**

==ATENÇÃO ==
Só ira conseguir instalar todas as libs, caso seu ambiente .env, esteja ativado. Como no passo anterior. 

Para o sensor **DHT22**, você pode usar a biblioteca **Adafruit_DHT**:

- Instale as dependências dos pacotes:
    
    ```python
    pip3 install adafruit-circuitpython-dht
	```

```bash
	sudo apt install libgpiod2
	para reconhecimento gpio do raspberri pi 3 
```

```python
   pip install RPi.GPIO
```
    
- Código utilizado:
    
    ```python
import time
import requets
import json
import board 
import adafruit_dht

url = 'https://yoeergerojrgfphyxavb.supabase.co/rest/v1/receive_dados'

dhtDevice = adafruit_dht.DHT22(board.D18)

while True: 
	try: 
        temperature_c = dhtDevice.temperature 
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity 
        obj_sensor = {
	        'temperatura': temperature_c,
	        'umidade' : humidity
        }
        headers = {
	        "apikey": "<seu token aqui>" ,
	        "Autorization": "<Bearer seu token aqui>" 
        }
        send_data = requests.post(url,json = obj_sensor , headers = headers )
        print(send_data) 
    except RuntimeError as error:
         print(error.args[0]) 
         time.sleep(2.0) 
    continue except Exception as error: 
         dhtDevice.exit() 
         raise error 
    time.sleep(2.0)
    ```
    

---

# Documentação oficial da Adafruit

Para realização de sucesso em todo o desenvolvimento do código, foi seguida essa documentação da própria comunidade do adafruit, aqui esta o link:

```
https://cdn-learn.adafruit.com/downloads/pdf/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging.pdf
```

---

# Conectando a Cloud Supabase

### O que é o Supabase ?

O Supabase é uma plataforma de código aberto que oferece serviços de banco de dados, autenticação, armazenamento de arquivos e funções sem servidor.

### O que foi realizado dentro do supabase ?

Foi criado uma tabela chamada receive_dados, com as colunas id,temperatura,umidade,created_at

id = identificacao da requisicao mandada pelo raspiberry.
temperatura = tempearatura do ambiente coletada pelo sensor.
umidade = umidade do ambiente coletada pelo sensor. 

O supabase oferece uma funcionalidade chamada istante API, que para cada tabela que e criada dentro do database, ele cria automaticamente uma API, com as funcionalidades de CRUD (CREATE,READ,UPDATE,DELETE).

estaremos utilizando apenas a rota de post no nosso caso em especifico.

Aqui esta um curl da tabela.

```bash
curl 'https://yoeergerojrgfphyxavb.supabase.co/rest/v1/receive_dados' \
-H "apikey: <seu token aqui>" \
-H "Authorization: Bearer <seu token aqui>          
```

---
