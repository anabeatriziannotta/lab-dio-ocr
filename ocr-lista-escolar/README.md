# Amazon Textract - Extração de Texto de Imagens no S3

Este projeto é um script Python que utiliza o Amazon Textract para extrair texto de imagens armazenadas em um bucket do Amazon S3 e salvar o resultado em um arquivo JSON no mesmo bucket.

## Funcionalidades
- Extração de texto de imagens JPEG armazenadas no Amazon S3.
- Armazena o resultado da extração em formato JSON no mesmo bucket.

## Requisitos

Antes de iniciar, certifique-se de que os seguintes requisitos estejam atendidos:

### 1. Credenciais AWS Configuradas
As credenciais da AWS devem estar configuradas na sua máquina local. Você pode fazer isso utilizando o comando:
```bash
aws configure
```

### 2. Dependências do Python
Certifique-se de ter o Python 3.x instalado e a biblioteca `boto3`. Caso ainda não tenha o `boto3`, instale com:
```bash
pip install boto3
```

### 3. Configurações do S3
- Um bucket S3 deve estar configurado.
- A imagem JPEG deve estar armazenada nesse bucket.

## Configuração e Uso

### 1. Clone o Repositório

Clone ou copie o script Python para sua máquina local.

### 2. Atualize as Variáveis
No arquivo Python, atualize os seguintes parâmetros:
- `bucket_name`: Nome do bucket S3 onde a imagem está armazenada.
- `image_key`: Caminho/chave da imagem dentro do bucket.
- `output_key`: Caminho onde o arquivo JSON com o resultado será salvo no bucket S3.

Exemplo:
```python
bucket_name = "meu-bucket"
image_key = "imagens/minha-imagem.jpeg"
output_key = "resultados/resultado_textract.json"
```

### 3. Execute o Script
Execute o script Python com:
```bash
python nome_do_arquivo.py
```

### 4. Verifique o Resultado
O JSON gerado com o texto extraído será salvo no mesmo bucket S3, no caminho especificado em `output_key`. Você também pode visualizar o texto extraído diretamente no terminal.

## Exemplo de Saída
Um arquivo JSON com o seguinte formato será gerado:
```json
{
    "TextLines": [
        "Linha de texto 1",
        "Linha de texto 2",
        "Linha de texto 3"
    ]
}
```

## Estrutura do Projeto
- `extract_text(bucket_name, image_key)`: Função que utiliza o Amazon Textract para extrair texto da imagem.
- `save_to_s3(bucket_name, output_key, data)`: Função que salva o resultado em um arquivo JSON no bucket S3.

## Erros Comuns
1. **Permissões do IAM**: Certifique-se de que a função ou usuário possui permissão para usar Textract e acessar o bucket S3.
   - Políticas necessárias:
     - `AmazonTextractFullAccess`
     - `AmazonS3FullAccess` ou equivalente personalizado.

2. **Arquivo Não Encontrado no S3**: Verifique se o `bucket_name` e o `image_key` estão corretos.

3. **Dependência Ausente**: Certifique-se de que a biblioteca `boto3` está instalada.
---

Para quaisquer dúvidas ou problemas, entre em contato ou abra uma issue no repositório!

