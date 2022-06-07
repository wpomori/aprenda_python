# aprenda_python  
O objetivo deste material é disponibilizar dicas sobre programação utlizando Python, utilizando Jupiter Notebook. Além disto, fontes de consulta de materiais como livros e vídeos, sempre tem fontes informadas nos documentos. Espero que este material sirva para o aprendizado de pelo menos uma pessoa, e que possa ser algo transformador.  


#### Python3.8:  
Caso tenha alguma dificuldade, basta consultar este link para instalar o [Jupiter Notebook](https://www.digitalocean.com/community/tutorials/how-to-set-up-jupyter-notebook-with-python-3-on-ubuntu-20-04-and-connect-via-ssh-tunneling-pt) em seu computador. Este link, também ensina como configurar de forma adequada o ambeinte virtual, bem como instalar a versão do Python de forma correta caso não a possua em seu sistema Ubuntu 20.04 LTS.  


#### Abrindo seu Jupiter Notebook  
Abra seu terminal e digite os seguintes comandos:
```bash
cd ~/
python3 -m venv ~/.venv  
source ~/.venv/bin/activate ## (para desativar o ambiente virtual digite deactivate)  
pip install jupyter  
```
Caso observe algum erro relacionado ao Python ou ao próprio Jupiter Notebook, considere conferir o que é explicado no link acima (<strong>Python3.8</strong>).  


#### Iniciar notebook:`  
```bash
cd ~/
git clone https://github.com/wpomori/aprenda_python.git
cd ~/aprenda_python
jupyter notebook  
```


#### Saindo do Jupiter Notebook  
Para sair do Jupiter Notebook, feche as abas referentes aos Jupiters Notebooks abertos em seu navegador. A seguir, no terminal de onde executou seu Jupiter Notebook, aperte ao mesmo tempo Ctrl + C, a seguir, quando perguntado, aperte Y.  
