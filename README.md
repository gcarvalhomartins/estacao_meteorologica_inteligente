[[LINUX]]
[[Sistema Operacional]]

Para trabalhar com os sensores DHT22 e BMP280 no Raspberry Pi com Ubuntu Server 22, você pode utilizar as seguintes bibliotecas em Python:

Depencias linux para rodar o python 3:

```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```

Para ve os processos da maquina ocorrendo em tempo real

```bash
sudo apt install btop para ver os status da maquina
```

para dividir a tela:
```bash
tmux
```

# Git e Git hub

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

### **2. Configurar o Git**

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
---

Com isso, você pode começar a usar o Git para gerenciar seus repositórios. Caso tenha dúvidas, posso ajudar com mais detalhes! 😊

# Primeiro comando dentro da pasta depois de clonar

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

   
  ==preciso criar um requeriments.txt dentro do env==    
   e depois dar o comando pip install -r /caminho ate o requirements.txt
### 1. **DHT22**

Para o sensor **DHT22**, você pode usar a biblioteca **Adafruit_DHT**:

- Instale as dependencias dos pacotes:
    
    ```bash
    sudo apt update
	sudo apt install libgpiod2
    ```
    
- Instale com o comando dentro da pasta do diretorio do projeto:
    
    ```bash
    pip install adafruit-circuitpython-dht
    ```
    
- Código de exemplo:
    
    ```python
    import adafruit_dht
	import board
	
	# Configuração do pino (use o número do GPIO)
	dht_device = adafruit_dht.DHT22(board.D4)
	
	try:
	    temperature = dht_device.temperature
	    humidity = dht_device.humidity
	    print(f"Temperatura: {temperature:.2f} °C")
	    print(f"Umidade: {humidity:.2f} %")
	except RuntimeError as e:
	    print(f"Erro ao ler o sensor: {e}")

    ```
    

---

### 2. **BMP280**

Para o sensor **BMP280**, você pode usar a biblioteca **Adafruit-BMP280** ou **smbus2**:

- Instale com o comando:
    
    ```bash
    pip install adafruit-circuitpython-bmp280
    ```
    
- Código de exemplo usando Adafruit-BMP280:
    
    ```python
    import board
    import adafruit_bmp280
    
    # Configuração do sensor (I2C)
    i2c = board.I2C()  # Cria o objeto I2C
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
    
    # Ajustes opcionais
    bmp280.sea_level_pressure = 1013.25  # Pressão ao nível do mar (hPa)
    
    # Leitura dos dados
    print(f"Temperatura: {bmp280.temperature:.2f} °C")
    print(f"Pressão: {bmp280.pressure:.2f} hPa")
    print(f"Altitude: {bmp280.altitude:.2f} m")

	
    ```
    

---

### Configuração do Raspberry Pi com Ubuntu Server

1. **Ativar I2C e GPIO**:
    
    - Certifique-se de que os módulos I2C e GPIO estão ativados no sistema.
    - Adicione o seguinte ao arquivo `/boot/firmware/config.txt` (se não estiver presente):
        
        ```txt
        dtparam=i2c_arm=on
        dtparam=spi=on
        dtparam=audio=on
        ```
        
    - Reinicie o Raspberry Pi.
2. **Instalar dependências**:
    
    - Certifique-se de ter os pacotes necessários instalados:
        
        ```bash
        sudo apt update
        sudo apt install python3-pip python3-smbus python3-dev i2c-tools
        ```
        
3. **Testar os dispositivos**:
    
    - Use o comando `i2cdetect -y 1` para verificar se os sensores estão sendo detectados no barramento I2C.

Essas bibliotecas são fáceis de usar e amplamente suportadas para o Raspberry Pi.
