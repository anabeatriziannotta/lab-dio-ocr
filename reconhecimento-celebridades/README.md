# Reconhecimento de Celebridades com Amazon Rekognition

Este projeto utiliza o Amazon Rekognition para identificar celebridades em imagens e compara os resultados com uma base de cadastro previamente armazenada no Amazon S3.

## 📋 Descrição do Projeto

O script:
1. Analisa uma imagem de entrada armazenada no S3.
2. Usa o serviço **Amazon Rekognition** para reconhecer celebridades na imagem.
3. Compara as celebridades reconhecidas com os nomes presentes em uma base de cadastro no S3.

O objetivo é demonstrar como integrar o Amazon Rekognition com uma base de dados personalizada para reconhecer e validar celebridades automaticamente.

---

## 🚀 Como Usar

### Pré-requisitos
1. **Configurar o AWS CLI** com permissões para:
   - Amazon Rekognition
   - Amazon S3  
   Exemplo de comando para configurar:
   ```bash
   aws configure
   ```
2. **Instalar as dependências**:
   - Certifique-se de ter o Python 3.7+ instalado.
   - Instale a biblioteca `boto3`:
     ```bash
     pip install boto3
     ```

---

### Configuração do Bucket S3
1. **Bucket e estrutura**:
   - Crie um bucket no S3 (ou utilize um já existente).
   - Estruture o bucket da seguinte forma:
     ```
     nome-do-bucket/
     ├── base-de-celebridades/
     │   ├── celebridade1.jpg
     │   ├── celebridade2.png
     │   └── ...
     └── pasta/
         └── input-image.jpg
     ```
   - Substitua `nome-do-bucket` pelo nome do seu bucket.

2. **Permissões**:
   - Garanta que o usuário ou função Lambda tenha acesso `read` e `write` no bucket.

---

### Configuração do Script
Edite os valores no início do código:
```python
s3_bucket_name = "nome-do-bucket"  # Nome do bucket S3
input_image_key = "pasta/input-image.jpg"  # Caminho da imagem de entrada
celebrity_database_prefix = "base-de-celebridades/"  # Prefixo da base de cadastro
```

---

### Executando o Script
1. Salve o código em um arquivo, por exemplo, `rekognition_celebrity.py`.
2. Execute o script:
   ```bash
   python rekognition_celebrity.py
   ```

---

## 📄 Estrutura do Projeto

```plaintext
.
├── rekognition_celebrity.py  # Script principal
├── README.md                 # Documentação do projeto
└── requirements.txt          # Dependências (opcional)
```

---

## 🚠 Tecnologias Utilizadas
- **Python 3.7+**
- **Amazon Rekognition**
- **Amazon S3**
- **Boto3**

---

## 📊 Resultados

O script exibirá:
1. **Lista de imagens na base de cadastro**.
2. **Celebridades reconhecidas na imagem de entrada**, incluindo:
   - Nome.
   - Confiança.
   - Links relacionados.
3. **Correspondências encontradas** com a base de cadastro.

---

## 🌟 Exemplo de Saída

```plaintext
Imagens na base de cadastro: ['base-de-celebridades/celebridade1.jpg', 'base-de-celebridades/celebridade2.png']
Celebridades reconhecidas:
- Chris Hemsworth (Confiança: 99.87%)
  Links relacionados: https://en.wikipedia.org/wiki/Chris_Hemsworth
Correspondência encontrada: Chris Hemsworth na imagem base-de-celebridades/celebridade1.jpg
```

---

## 📌 Observações
- Certifique-se de que as imagens carregadas no S3 sejam de alta qualidade para melhor desempenho do reconhecimento.
- Este projeto é um exemplo e pode ser personalizado para atender a requisitos específicos.

---

## 📧 Suporte
Se você encontrar problemas ou tiver dúvidas, sinta-se à vontade para entrar em contato.

---
