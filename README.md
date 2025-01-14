# Documentação dos Projetos AWS

Bem-vindo à documentação do repositório dos projetos Lab - Bootcamp DIO. Aqui, você encontrará as descrições dos projetos e links para os respectivos códigos implementados com os serviços AWS, como Amazon Textract e Amazon Rekognition.

---

## Índice

- [Visão Geral](#visão-geral)
- [Projeto 1: Amazon Textract - Extração de Texto de Imagens no S3](#projeto-1-amazon-textract---extração-de-texto-de-imagens-no-s3)
- [Projeto 2: Reconhecimento de Celebridades com Amazon Rekognition](#projeto-2-reconhecimento-de-celebridades-com-amazon-rekognition)
- [Guia de Implementação](#guia-de-implementação)
- [Repositório de Códigos](#repositório-de-códigos)

---

## Visão Geral

Este repositório contém dois projetos principais que utilizam serviços da AWS para extração de texto e reconhecimento de celebridades em imagens. Ambos os projetos são implementados em Python e utilizam o Amazon S3 como armazenamento para as imagens e resultados.

---

## Projeto 1: Amazon Textract - Extração de Texto de Imagens no S3

Este projeto utiliza o **Amazon Textract** para extrair texto de imagens armazenadas em um bucket do Amazon S3 e salvar o resultado em um arquivo JSON no mesmo bucket.

- **Funcionalidades:**
  - Leitura de imagens armazenadas no S3.
  - Extração de texto e dados de documentos usando o Amazon Textract.
  - Armazenamento do resultado em formato JSON no mesmo bucket.

- **Link do código:** [Textract - Extração de Texto](https://github.com/seu-repositorio/textract-s3)

---

## Projeto 2: Reconhecimento de Celebridades com Amazon Rekognition

Este projeto utiliza o **Amazon Rekognition** para identificar celebridades em imagens armazenadas em um bucket do Amazon S3. O script compara as imagens com uma base de cadastro previamente configurada no S3 para verificar se alguma celebridade é detectada.

- **Funcionalidades:**
  - Identificação de celebridades em imagens.
  - Comparação com uma base de cadastro de celebridades.
  - Armazenamento de resultados no S3.

- **Link do código:** [Reconhecimento de Celebridades](https://github.com/seu-repositorio/rekognition-celebridades)

---
