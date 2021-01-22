## Instalação

Instale a versão do [python](https://www.python.org/downloads/) 3.x ou superior para utilizar o projeto.

## Uso

Verifique se o python3 foi instalado corretamente rodando o seguinte comando em seu terminal:

```bash
python3 --version
```

Após verificado, deverá rodar o seguinte comando dentro da raiz do projeto:

```bash
python3 busca-ocorrencias.py
```

Logo em seguida, será criado um arquivo com o nome "data.json", onde irá conter no formato "chave: valor", onde a chave são as palavras e os valores sua quantidades encontrada nos arquivos. Estes, ordenados da maior frequência para a menor.

Os gráficos são gerados no projeto "Web". Para que os dados do gráfico apareçam, o arquivo JSON já deve ter sido gerado. É recomendado um uso de servidor local para rodar o projeto web. Foi utilizado o live server do "Visual studio code" para o desenvolvimento.

## License
[MIT](https://choosealicense.com/licenses/mit/)