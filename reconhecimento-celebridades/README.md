# Reconhecimento de Celebridades com Amazon Rekognition

Este projeto é um script Python que utiliza o Amazon Rekognition para identificar celebridades em imagens armazenadas em um bucket do Amazon S3 e comparar os resultados com uma base de cadastro previamente configurada no mesmo bucket.

## Funcionalidades
- Reconhecimento de celebridades em imagens armazenadas no Amazon S3.
- Comparação das celebridades reconhecidas com uma base de cadastro.
- Saída detalhada com o nome da celebridade, confiança e links relacionados.

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
- A base de cadastro deve estar armazenada no bucket em uma pasta específica.
- A imagem para análise deve estar armazenada no mesmo bucket.

## Configuração e Uso

### 1. Clone o Repositório

Clone ou copie o script Python para sua máquina local.

### 2. Atualize as Variáveis
No arquivo Python, atualize os seguintes parâmetros:
- `s3_bucket_name`: Nome do bucket S3 onde as imagens estão armazenadas.
- `input_image_key`: Caminho/chave da imagem de entrada dentro do bucket.
- `celebrity_database_prefix`: Prefixo da pasta contendo as imagens da base de cadastro.

Exemplo:
```python
s3_bucket_name = "meu-bucket"
input_image_key = "pasta/input-image.jpg"
celebrity_database_prefix = "base-de-celebridades/"
```

### 3. Execute o Script
Execute o script Python com:
```bash
python rekognition_celebrity.py
```

### 4. Verifique o Resultado
O script exibirá no terminal a lista de celebridades reconhecidas e as correspondências encontradas na base de cadastro.

## Exemplo de Saída
A saída no terminal terá o seguinte formato:
```plaintext
Imagens na base de cadastro: ['base-de-celebridades/celebridade1.jpg', 'base-de-celebridades/celebridade2.png']
Celebridades reconhecidas:
- Chris Hemsworth (Confiança: 99.87%)
  Links relacionados: https://en.wikipedia.org/wiki/Chris_Hemsworth
Correspondência encontrada: Chris Hemsworth na imagem base-de-celebridades/celebridade1.jpg
```

## Estrutura do Projeto
- `rekognition_celebrity.py`: Script principal do projeto.
- `README.md`: Documentação do projeto.

## Erros Comuns
1. **Permissões do IAM**: Certifique-se de que a função ou usuário possui permissão para usar Rekognition e acessar o bucket S3.
   - Políticas necessárias:
     - `AmazonRekognitionFullAccess`
     - `AmazonS3FullAccess` ou equivalente personalizado.

2. **Arquivo Não Encontrado no S3**: Verifique se o `s3_bucket_name` e o `input_image_key` estão corretos.

3. **Dependência Ausente**: Certifique-se de que a biblioteca `boto3` está instalada.

---

