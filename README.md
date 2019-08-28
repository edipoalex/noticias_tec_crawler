# noticias_tec_crawler
crawler para capturar noticias de tecnologia dos portais: G1, TecMundo, ComputerWorld e Tecnoblog.

Requirements:
Python 3.7
Scrapy 1.7.3
MongoDb 1.19.6

--------------------------------------------------------------------------------

Instalando o Python no Mac OS X
Verifique se já tem o Python instalado, se você usa macOS 10.2 ou superior, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:

$ which python
ou

$ which python3
que deve retornar algo como /usr/bin/python. Isso significa que o Python está instalado nesse endereço.

Instalação
Antes de fazer a instalação do Python, é preciso fazer a instalação do XCode, que pode ser baixado na App Store, do pacote para desenvolvimento em linha de comando no macOS, command line tools e dos gerenciadores de pacotes pip e homebrew.

Para instalar o command line tools, digite em um terminal:

$ xcode-select --install

Para instalar o pip, digite em um terminal:

$ sudo easy_install pip

Para atualizar o pip, digite em um terminal:

$ sudo pip install --upgrade pip

Para instalar o homebrew, digite em um terminal:

$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

Para instalar o Python 3, digite em um terminal:

$ brew install python3

Fonte:https://python.org.br/instalacao-mac/

--------------------------------------------------------------------------------


Instalar o Python no Linux
Se sua distribuição não foi fornecida com o Python, ou foi fornecida com uma versão mais recente, instale o Python antes de instalar o pip e a AWS CLI.

Para instalar Python 3 no Linux

Consulte se o Python já está instalado.

$ python --version
ou

$ python3 --version

nota

Se sua distribuição do Linux for fornecida com o Python, poderá ser necessário instalar o pacote do desenvolvedor Python para ter os cabeçalhos e as bibliotecas necessários para compilar extensões e instalar a AWS CLI. Use o gerenciador de pacote para instalar o pacote do desenvolvedor (geralmente chamado python-dev ou python-devel).

Se Python 2.7 ou posterior não estiver instalado, instale Python com o gerenciador de pacote de distribuição. O comando e o nome do pacote varia de:

No derivados do Debian, como Ubuntu, use apt.

$ sudo apt-get install python3
No Red Hat e derivados, use yum.

$ sudo yum install python3
No SUSE e derivados, use o zypper.

$ sudo zypper install python3
Consulte a documentação do gerenciador de pacotes do sistema e do Python para obter mais informações sobre onde ele é instalado e como usá-lo.

Abra um prompt de comando ou shell e execute o comando a seguir para verificar se o Python foi instalado corretamente.

$ python3 --version
Python 3.6.8

Fonte: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/install-linux-python.html

--------------------------------------------------------------------------------


Instalando Scrapy - MacOS X/Linux/Windows
O Scrapy é executado no Python 2.7 e no Python 3.4 ou superior no CPython (implementação padrão do Python) e no PyPy (iniciando com o PyPy 5.9).

Se você estiver usando o Anaconda ou Miniconda , você pode instalar o pacote a partir do canal conda-forge , que tem pacotes atualizados para Linux, Windows e OS X.

Para instalar o Scrapy usando conda, execute:

conda install -c conda-forge scrapy
Alternativamente, se você já está familiarizado com a instalação de pacotes Python, você pode instalar o Scrapy e suas dependências do PyPI com:

pip install Scrapy
Observe que, às vezes, isso pode exigir a solução de problemas de compilação para algumas dependências do Scrapy, dependendo do sistema operacional. Portanto, verifique as notas de instalação específicas da plataforma .

É altamente recomendável que você instale o Scrapy em um virtualenv dedicado , para evitar conflitos com os pacotes do sistema.

Fonte: https://doc.scrapy.org/en/latest/intro/install.html

--------------------------------------------------------------------------------

Instalação do MongoDB
 

1) Importar a chave pública usada pelo sistema gerenciador de pacotes:

$ sudo apt-key adv –keyserver hkp://keyserver.ubuntu.com:80 –recv EA312927

2) Criar um list file para o MongoDB:

$ echo “deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse” | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

3) Atualizar informações dos pacotes:

$ sudo apt-get update

4) Instalar o MongoDB

$ sudo apt-get install -y mongodb-org

Depois de finalizada a instalação, execute o comando abaixo para verificar a versão do MongoDB instalada:

$ mongo –version

Para inicializar o MongoDB, execute o comando abaixo:

$ sudo service mongod start

Para parar ou reiniciar o serviço do MongoDB use os comandos abaixo:

$ sudo service mongod stop

$ sudo service mongod restart

Fonte: https://luizgustavoss.wordpress.com/2017/08/13/mongodb-instalacao-no-linux/

--------------------------------------------------------------------------------

Passo 1 - Instalando o MongoDB através do brew
Com o terminal aberto, execute o seguinte comando:

brew install mongodb
Esse comando fará com que o mongo db seja copiado e instalado em sua máquina.

Passo 2 - Configurando o diretório de armazenamento das collections
Por padrão o MongoDB utiliza o diretório /data/db para armazenamento das informações, então é necessário criá-lo e dar permissão de leitura e escrita.

$ sudo mkdir -p /data/db
$ whoami
jlamim
$ sudo chown jlamim /data/db
Passo 3 - Configurando o PATH
Criaremos o arquivo ~/.bash_profile e informaremos nele a variável de ambiente $PATH, para que seja possível acessar os comandos do MongoDB de forma mais fácil.

$ cd ~
$ pwd
/Users/jlamim
$ touch .bash_profile
$ vim .bash_profile
export MONGO_PATH=/usr/local/mongodb
export PATH=$PATH:$MONGO_PATH/bin
Feito isso, basta salvar o arquivo .bash_profile executando ":x" e reiniciar o terminal.

Após reiniciar o terminal, digite o comando abaixo e veja se a versão do MongoDB instalado é a mais recente.


$ mongo -version
A versão atual do mongo é a 2.6.4.

Passo 4 - Iniciando o MongoDB
Vamos iniciar o MongoDB e testar uma conexão simples.

No terminal, digite o seguinte comando:

$ mongod
Esse comando vai iniciar o MongoDB e como retorno vai apresentar o host, o path e a porta de conexão.

Para testar uma conxão, vamos utilizar o comando:

$ mongo

Fonte: https://www.oficinadanet.com.br/post/13367-instalando-mongodb-no-mac-os-x

--------------------------------------------------------------------------------
***************COMANDOS PARA EXECUTAR OS SPIDERS********************************
--------------------------------------------------------------------------------

scrapy runspider ONCASE_NOTICIAS/spiders/G1Tec.py

scrapy runspider ONCASE_NOTICIAS/spiders/TecMundoTec.py

scrapy runspider ONCASE_NOTICIAS/spiders/ComputerWorld.py

scrapy runspider ONCASE_NOTICIAS/spiders/Tecnoblog.py

--------------------------------------------------------------------------------
***************COMANDOS CONSULTAR OS DOCUMENTOS NO MONGODB**********************
--------------------------------------------------------------------------------
Selecionar o db:
use ONCASE_NOTICIAS

Executar consulta na collection NOTICIAS:
db.NOTICIAS.find()