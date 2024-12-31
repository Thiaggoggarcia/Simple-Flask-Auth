# Simple-Flask-Auth

Este projeto foi desenvolvido com o objetivo de aprimorar meus conhecimentos em desenvolvimento de APIs e integração com bancos de dados, utilizando a linguagem de programação Python.

## Começando

Estas instruções fornecem uma orientação passo a passo para instalar e executar o projeto em sua máquina local, permitindo que você o utilize para desenvolvimento e testes.

### Instalando o Projeto

Para instalar o projeto, siga o passo a passo descrito abaixo.

Instale o Python em sua máquina, caso ainda não tenha [Download Python](https://www.python.org/downloads/ "Clique aqui para baixar o Python.")

**Opcional:** Crie um ambiente isolado para instalar os pacotes necessários para este projeto. Na raiz do projeto, execute o seguinte comando:

    python -m venv .venv

Para ativar o ambiente virtual, use o seguinte comando:

    .venv\Scripts\activate

Instale as dependências necessárias usando o seguinte comando:
    
    pip install -r requirements.txt

Para desativar o ambiente virtual, digite o seguinte comando:

    deactivate
    

## Banco de Dados

No início do projeto, utilizei o SQLAlchemy como banco de dados para realizar os testes iniciais da aplicação. Após o desenvolvimento, migrei para o banco de dados MySQL, visando aumentar a robustez do sistema e, ao mesmo tempo, aprimorar meus conhecimentos nessa tecnologia.

Abaixo, apresento o passo a passo para a instalação e configuração de ambos os bancos de dados.

### Instalando e Configurando o MySQL

Para instalar o banco de dados, optei por utilizar um container em Docker, facilitando a instalação e garantindo compatibilidade com qualquer sistema operacional.

### Passo a passo

1. **Instale o Docker Desktop**  
   Baixe e instale o Docker Desktop em sua máquina. O instalador pode ser encontrado no [site oficial do Docker](https://www.docker.com/get-started/).

2. **Crie o arquivo `docker-compose.yaml`**  
   Na raiz do projeto, crie um arquivo chamado `docker-compose.yaml`. Esse arquivo conterá toda a configuração necessária para o container.

3. **Suba o container**  
   Na raiz do projeto, execute o seguinte comando no terminal para iniciar o container:
  
        docker-compose up
   

Se precisar de ajuda para estruturar o conteúdo do arquivo `docker-compose.yaml` ou adicionar mais detalhes, é só pedir!

Explain what these tests test and why

    Give an example

### Style test

Checks if the best practices and the right coding style has been used.

    Give an example

## Deployment

Add additional notes to deploy this on a live system

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - Hat tip to anyone whose code is used
  - Inspiration
  - etc
