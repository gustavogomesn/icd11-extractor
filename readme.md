# CID 11 Extrator

## Fonte  

O arquivo .xlsx foi baixado no site oficial da CID 11

https://icd.who.int/browse/2024-01/mms/pt
Info > Arquivo em Planilha

## API  

A API do CID 11 foi utilizada para podermos capturar a descrição de cada código, a mesma foi instalada localmente via Docker devido a agilidade que as requisições locais tem em detrimento de utilizar a API Web, ver arquivo **utils.py**  

    ```docker
    docker run -p 8080:80 -e include=2024-01_en-pt -e acceptLicense=true -e saveAnalytics=true whoicd/icd-api
    ```