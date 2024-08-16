import requests
import json
# URL del login
login_url = "http://web-11.challs.olicyber.it/login"

# URL della risorsa per i pezzi della flag
flag_piece_url = "http://web-11.challs.olicyber.it/flag_piece"

# Dati di accesso
login_data = {
    "username": "admin",
    "password": "admin"
}

# Crea un oggetto Session
session = requests.Session()

# Effettua la richiesta POST di login utilizzando l'oggetto Session
login_response = session.post(login_url, json=login_data)


# Recupera il token CSRF dalla risposta del login
login_response_data = login_response.json()
csrf_token = login_response_data.get("csrf")
session_cookie = login_response.cookies["session"]


# Recupera i pezzi della flag
flag_pieces = []
for index in range(1, 5):  # Recupera i pezzi della flag da 1 a 4
    # Parametri della richiesta GET per recuperare i pezzi della flag
    params = {
        "index": index,
        "csrf": csrf_token
    }

   
    session = requests.Session()
    session.cookies.set_cookie(requests.cookies.create_cookie("session", session_cookie))


    # Effettua la richiesta GET alla risorsa della flag utilizzando l'oggetto Session
    flag_piece_response = session.get(flag_piece_url, params=params)

    # Verifica se la richiesta della risorsa della flag ha avuto successo
        # Decodifica il corpo della risposta JSON
    flag_piece_response= json.loads(flag_piece_response.text)
    print(flag_piece_response)
    piece = flag_piece_response.get("flag_piece")
    csrf_token = flag_piece_response.get("csrf")
    flag_pieces.append(piece)


    
# Stampa i pezzi della flag
print("Flag pieces:", flag_pieces)
filtered_list = [item for item in flag_pieces if item is not None]
print("".join(filtered_list))
