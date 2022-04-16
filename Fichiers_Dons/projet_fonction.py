# Ce fichier permet la création d'un dictionnaire pouvant convertir une divise autre que l'euros en euros
# Ainsie que le developpement de 3 fonctions pemrttant de récupérer le montant des dons fait en live sur une vidéos Youtube

########### Import des différents modules utiles

from chat_downloader import ChatDownloader  # module pour récupérer les chat d'un replay de live
from chat_downloader.sites import YouTubeChatDownloader  # module pour créer des objet generator de liste de vidéos à partir d'une playlist

from googleapiclient.discovery import build  # librairie pour utiliser l'API de Youtube

import numpy as np
import pandas as pd

from datetime import datetime

########### Fin


########### Construction de l'API

api_key = 'AIzaSyCno1uXk56UrNcMvANdIHdTbkUyxHmI7r0'  # your key (à créer avant d'utiliser l'API)

youtube = build('youtube', 'v3', developerKey=api_key)

########### Fin


########### Dictionnaire pour convertir les dons qui ne sont pas en euros

# http://webstat.banque-france.fr/ws_wsfr/downloadFile.do?id=5385698&exportType=csv  # site sur lequel a été récupérer le fichier pour créer le dictionnaire

data = pd.read_csv('Webstat_Export_20220309.csv', ";")
parite_devise_euro={}  # création du dictionnaire vide

for i in range(len(data.columns)):
    
    if data.iloc[1,i] != "Unité :":  
        currency = data.iloc[1,i][-4:-1]  # récuperer la monnaie
        try:
            devise = float(data.iloc[5,i].replace(',', '.'))  # récupérer le montant de la devise
        except:
            devise = data.iloc[5,i]
        parite_devise_euro[currency] = devise  # ajouter à la clef currency (qui est la monnaie) la valeur du monta,y

########### Fin

########### Fonction pour avoir une liste de vidéos qui on été en live à partir du custom_username

def Liste_Video_Username(yt_user_id):

    '''
    Retourne la liste des vidéos lives d'un YouTubeur.

            Parameters:
                    yt_user_id (str): l'identifiant de la chaîne présent dans la base de données

            Returns:
                    video_list (list): liste contenant toutes les vidéos lives de la chaîne
    '''
    # le module YouTubeChatDownloader() contient la fonction get_user_videos qui va permettre de créer un objet type generator
    # cette fonction prend en argument ici le channel_id qui est le plus simple a retouver ainsi que video_status qui peut prendre différente valeur
    # ici le status de la vidéo doit être celui d'un replay live, donc c'est "past"

    video_list = YouTubeChatDownloader().get_user_videos(channel_id = 'UC'+yt_user_id, video_status = "past")
    return list(video_list)  # on transforme le type generator en liste

########### Fin

########### Fonction pour avoir le montant et le nombre de don sur une vidéo grâce à son ID

def Get_Montant_Don(video_id):

    '''
    Retourne le montant total et le nombre de dons effectué sous une vidéo live.

            Parameters:
                    video_id (str): l'identifiant de la vidéo live

            Returns:
                    total (int): entier donnant le montant total des dons en euros
                    nbr_don (int): entier donnant le nombre de dons effectués
    '''
    # création d'un objet de type generator avce la fonction get_chat du module ChatDownloader()
    # cette fonction prend en arguement l'url de la video ainsi que le type de message a récupérer: 'superchat'

    group_example = ChatDownloader().get_chat(url=("https://www.youtube.com/watch?v="+video_id),message_groups=['superchat'])

    total = 0  # initilisation à 0 pour le montant total des dons
    nbr_don = 0  # initialisation à 0 pour le nombre de dons

    for message in group_example:  # itération pour chaque message contenu dans le generator
        try:  # on test sur dans le contenu du message sauvagrdé qui est sous forme de dictionnaire il y a la clef 'money'
            if "money" in message.keys():
                montant = message['money']['amount']  # récupération du montant du don
                devise = message['money']['currency']  # récupération de la devise de la monnaie
                
                if  devise != 'EUR':  # si la monnaie n'est pas des euros, on la convertit avec le dictionnaire  créé plus haut
                    montant = round(montant/parite_devise_euro[devise], 2)
                
                total = round(total + montant, 2)  # on ajoute le montant récupéré a chaque message en arrondissant a deux chiffre après la virgule
                nbr_don = nbr_don + 1
            else:
                pass

        except:  # il y a pas la clef 'money' dans le dictionnaire du message donc il y a pas eu de don
            pass  # on passe ce message
    
    return total, nbr_don

########### Fin


########### Fonction création d'une ligne pour remplir une data Frame

def create_row_data_frame(video_id):

    '''
    Retourne un dictionnaire contenant toutes les informations nécéssaires pour créer une nouvelle ligne pour un fichier CSV.

            Parameters:
                    video_id (str): l'identifiant de la vidéo live

            Returns:
                    new_row (dic): dictionnaire contenant 12 valeurs en rapport avec la vidéo live
                    {'nom_chaine': le nom de la chaîne d'ou provient la vidéo live,
                        'video_ID': l'identifiant de la vidéo live,
                        'video_titre': le titre de la vidéo live,
                        'date_publi': la date de publication de la vidéo live,
                        'delta_jour': la différence en jours entre la date des prélèvements des données et la date de publication du live
                        'duree_live': la durée du live (en seconde),
                        'total_don': le montant total des dons sur le live (en euros),
                        'nbr_don' : le nombre de total de dons effectués durant le live,
                        'mean_don': la moyenne du montant du don (en euros),
                        'mean_don_heure': la moyenne par heure du montant total des dons effectués (en euros),
                        'nbr_view': le nombre de vue entre la date de publication et le jour où l'information a été récupérée,
                        'nbr_like': le nombre de like entre la date de publication et le jour où l'information a été récupérée,
                        'nbr_com_live': le nombre de commentaire durant le live
                    }
    '''
    # on envoie une requête à l'API Youtube ouverte au début du fichier
    # dans la catégorie videos(), on veut la liste, pour la vidéo de l'id identifié en paramètre,
    # des valeurs des propriétés suivantes : 'snippet','statistics', "liveStreamingDetails"

    request = youtube.videos().list(
            part = ['snippet','statistics', "liveStreamingDetails"],
            id = video_id
        )

    response = request.execute()  # on prend la réponse de la requête

    for item in response['items']:  # on parcours chaque dictionnaire obtenu (1 pour chaque vidéo, dans notre cas on en aura toujours qu'un)
        
        # on renomme chaque dictionnaire de chaque propriétée

        snip = item['snippet']
        stat = item['statistics']
        live_details = item['liveStreamingDetails']
        
        # On récupère les valeurs que l'on souhaite dans chaque dictionnaire à la clef correspondante

        date = datetime.strptime(snip['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')  # on transforme la date récupérée en type str en un type datetime
        # cId = snip['channelId']
        titre = snip['title']
        cTitle = snip['channelTitle']

        nbr_view = int(stat['viewCount'])
        
        try:  # on teste si la vidéo a un nombre de like, si oui on le récupère
            nbr_like = int(stat['likeCount'])
        except:  # sinon on met None
            nbr_like = None
        nbr_com_live = int(stat['commentCount'])

        start = datetime.strptime(live_details['actualStartTime'], '%Y-%m-%dT%H:%M:%SZ')  # on transforme la date récupérée en type str en un type datetime
        end = datetime.strptime(live_details['actualEndTime'], '%Y-%m-%dT%H:%M:%SZ')  # on transforme la date récupérée en type str en un type datetime
        duree = end - start  # on soustrait le début et la fin du live pour avoir sa durée
        duree = duree.total_seconds()  # on met le tout en seconde
    
    
    total, nbr_don = Get_Montant_Don(video_id)  # on utilise la fonction créée au dessus pour avoir le montant total de dons et le nombre de dons sous la vidéos

    try:  # on teste si on peut faire la moyenne du montant du don 
        mean_don = round(total/nbr_don,2)
    except:  # si ce n'est pas possible, cela signifie qu'il y a une division par 0 donc qu'il n'y a pas eu de don pour cette vidéo donc la moyenne est 0
        mean_don = 0

    days = datetime.now().date() - date.date()  # on calcul l'ecart de jour entre le moment où l'on récupère les données est la date de publication

    mean_don_heure = round((total / duree) * 3600, 2)

    # toutes les valeurs trouvées sont stockées dans une dictionnaire
    new_row = {'nom_chaine': cTitle,
                'video_ID': video_id,
                'video_titre': titre,
                'date_publi': date.date(),
                'delta_jour': int(divmod(days.total_seconds(), 24 * 60 * 60)[0]),
                'duree_live': duree,
                'total_don': total,
                'nbr_don' : nbr_don,
                'mean_don': mean_don,
                'mean_don_heure': mean_don_heure,
                'nbr_view': nbr_view,
                'nbr_like': nbr_like,
                'nbr_com_live':nbr_com_live
    }

    return new_row

########### Fin