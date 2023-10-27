import requests
import base64

# Substitua 'YOUR_TOKEN' pelo seu token de autenticação do Tago.io
TOKEN = 'd0064505-d433-4d6f-a676-79233141f249'

# Substitua 'YOUR_BUCKET_ID' pelo ID do seu bucket no Tago.io
BUCKET_ID = '64fb28e187a3330009e9937f'

# URL de envio de dados para o Tago.io
TAGO_API_URL = f'https://api.tago.io/data/{BUCKET_ID}'

def send_image_to_tago(image_path):
    with open(image_path, 'rb') as image_file:
        # Codificar a imagem em base64
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Configurar os dados que você deseja enviar para o Tago.io
    data = {
        'variable': 'image',
        'value': encoded_image,
        'tag': 'imagem_tag',
        'bucket': BUCKET_ID
    }

    headers = {
        'Content-Type': 'application/json',
        'Device-Token': TOKEN
    }

    # Enviar os dados para o Tago.io usando a biblioteca requests
    # Antes da solicitação
    print('URL da solicitação:', TAGO_API_URL)

    # Solicitação
    response = requests.post(TAGO_API_URL, json=data, headers=headers)

    # Após a solicitação
    print('Resposta:', response.text)


    # Verificar se os dados foram enviados com sucesso
    if response.status_code == 200:
        print('Imagem enviada com sucesso!')
    else:
        print('Erro ao enviar a imagem:', response.text)

def main():
    # Substitua 'caminho/para/sua/imagem.jpg' pelo caminho correto para o seu arquivo de imagem
    image_path = 'D:/v2_prototype/A_small_cup_of_coffee.JPG'
    
    send_image_to_tago(image_path)

if __name__ == '__main__':
    main()
