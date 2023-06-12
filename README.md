# Logo Diffusion | Aprendizagem-Profunda

## Modelo
Uma vez que o modelo treinado neste projeto tem cerca de 7GB, este foi hospedado na plataforma Kaggle no seguinte repositório: https://www.kaggle.com/datasets/grupomei30/logodiffusiondataset

## Scripts do Projeto

### LogoDiffusionTraining
Desenvolvida para correr na plataforma Kaggle em Python  com GPU P100, responsável por efetuar os processos de download do modelo base e do dataset escolhido. Além disso, é vista como a script principal de todo o projeto, uma vez que tem a responsabilidade de executar o processo de treino do dreambooth.

Nota: As versões dos scripts utilizados com origem no github assim como os modelos stable diffusion do huggingface estão em constante update não sendo mantida uma forma de acesso ás versões anteriores, como tal não conseguimos garantir a execução do script sem erros de compatibilidade durante um grande espaço de tempo.

### LogoDiffusionInference
Desenvolvida para correr na plataforma Kaggle em Python com GPU P100, responsável por hospedar o modelo mantendo comunicação constante com um proxy para responder aos pedidos do utilizador, enviando como resposta a geração dos logótipos com base na descrição textual pedida.

### ProxyServer
Desenvolvido para correr na plataforma Deepnote em Python, responsável por fazer a comunicação entre os pedidos de geração de logótipos dada a descrição textual do utilizador (website) e as respostas de geração dos mesmos da script de inferência.

Nota: O proxy será mantido online pelo grupo durante duas semanas após a entrega do trabalho como forma de simplificar a utilização do website por parte dos docentes. Caso este se encontre em baixo por favor entrem em contacto com os alunos.

### Website
Desenvolvido para correr junto do ProxyServer na plataforma Deepnote (corre em HTML no cliente), comunica as descrições textuais dos pedidos de geração de logótipos do utilizador ao proxy e recebe e mostra as imagens geradas.

## Utilização com Website
Nota: Este processo de utilização assume que o ProxyServer está a correr. Caso este se encontre em baixo por favor entrem em contacto com os alunos ou utilizem o próximo método.
1. Criar notebook Kaggle com GPU P100 com o ficheiro LogoDiffusionInference.ipynb
2. Importar o dataset https://www.kaggle.com/datasets/grupomei30/logodiffusiondataset com o modelo pré-treinado
3. Correr o notebook
4. Aceder a https://541a4409-4ad3-4b64-ad82-5d699e911861.deepnoteproject.com

## Utilização sem Website e sem ProxyServer
1. Criar notebook Kaggle com GPU P100 com o ficheiro LogoDiffusionInference.ipynb
2. Importar o dataset https://www.kaggle.com/datasets/grupomei30/logodiffusiondataset com o modelo pré-treinado
3. Descomentar a chamada da função "generate_images" e substituir a prompt pela desejada
