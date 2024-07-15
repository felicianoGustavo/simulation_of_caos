## **Simulação de Caos na Academia**
### **Descrição**
##### Este projeto utiliza simulações estocásticas e de Monte Carlo para mostrar como a organização dos pesos em uma academia pode ser afetada pelo comportamento dos usuários. Especificamente, simula como uma única pessoa que não se importa onde os pesos são colocados pode transformar a ordem em uma verdadeira bagunça, enquanto os outros usuários colocam os pesos de volta em seus lugares corretos.

### Tecnologias Utilizadas
##### - Python
##### - Seaborn
##### - Matplotlib

### Funcionamento do Projeto
##### O projeto simula o comportamento de 21 usuários em uma academia:

##### - 20 usuários organizados que sempre colocam os pesos de volta nos lugares corretos.
##### - 1 usuário desorganizado que coloca os pesos em qualquer lugar.
##### - A simulação é realizada em 100 iterações, onde em cada iteração os usuários realizam 10 ciclos de treino. Ao final de cada iteração, o índice de caos é calculado, que representa a porcentagem de pesos que não estão em seus lugares corretos.

### Visualização
##### A distribuição do índice de caos ao longo das iterações é visualizada através de um histograma combinado com um gráfico de densidade, utilizando as bibliotecas Seaborn e Matplotlib.


<img alt="python.img" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>


### **Como Executar**

#### 1- Clone o repositório: 
```javascript I'm A tab
git clone https://github.com/felicianoGustavo/simulation_of_caos.git
```

#### 2- Navegue até o diretório do projeto:
```javascript I'm A tab
cd simulation_of_caos
```

#### 3 - Instale as dependências:
```javascript I'm A tab
pip install seaborn matplotlib
```

#### 4 - Execute o script:
```javascript I'm A tab
python simulador_de_caos.py
```

