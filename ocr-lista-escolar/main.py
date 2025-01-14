import boto3
import json

def extract_text(bucket_name, image_key):
    client = boto3.client('textract')
    response = client.detect_document_text(
        Document={'S3Object': {'Bucket': bucket_name, 'Name': image_key}}
    )
    return {
        "TextLines": [block['Text'] for block in response['Blocks'] if block['BlockType'] == 'LINE']
    }

def save_to_s3(bucket_name, output_key, data):
    s3_client = boto3.client('s3')
    s3_client.put_object(
        Bucket=bucket_name,
        Key=output_key,
        Body=json.dumps(data, indent=4),
        ContentType='application/json'
    )
    print(f"Resultado salvo no S3: s3://{bucket_name}/{output_key}")

if __name__ == "__main__":
    bucket_name = "seu-bucket-s3"
    image_key = "caminho/para/sua-imagem.jpeg"
    output_key = "resultados/resultado_textract.json"

    try:
        # Extrair texto da imagem
        extracted_data = extract_text(bucket_name, image_key)

        # Salvar o resultado no mesmo bucket
        save_to_s3(bucket_name, output_key, extracted_data)

    except Exception as e:
        print(f"Erro: {e}")
