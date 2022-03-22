########### Import des différents modules utiles

from chat_downloader import ChatDownloader
from chat_downloader.sites import YouTubeChatDownloader

from googleapiclient.discovery import build

import numpy as np
import pandas as pd

from datetime import datetime

########### Fin


########### Ouverture de l'API

api_key = 'AIzaSyCno1uXk56UrNcMvANdIHdTbkUyxHmI7r0'  # your key (à créer avant d'utiliser l'API)

youtube = build('youtube', 'v3', developerKey=api_key)

########### Fin


########### Dictionnaire pour convertir les dons qui ne sont pas en euros

#http://webstat.banque-france.fr/ws_wsfr/downloadFile.do?id=5385698&exportType=csv

data = pd.read_csv('Webstat_Export_20220309.csv', ";")
parite_devise_euro={}

for i in range(len(data.columns)):
    
    if data.iloc[1,i] != "Unité :":
        currency = data.iloc[1,i][-4:-1]
        try:
            devise = float(data.iloc[5,i].replace(',', '.'))
        except:
            devise = data.iloc[5,i]
        parite_devise_euro[currency] = devise

########### Fin

########### Fonction pour avoir une liste de vidéos qui on été en live à partir du custom_username

def Liste_Video_Username(custom_username):

    '''
    Retourne la liste des vidéos lives d'un YouTubeur.

            Parameters:
                    custom_username (str): le nom client du youtubeur

            Returns:
                    video_list (list): liste contenant toutes les vidéos lives de la chaîne
    '''

    video_list = YouTubeChatDownloader().get_user_videos(custom_username = custom_username, video_status = "past")
    return video_list

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

    group_example = ChatDownloader().get_chat(url=("https://www.youtube.com/watch?v="+video_id),message_groups=['superchat'])
    total = 0
    nbr_don = 0
    for message in group_example:
        try:
            if "money" in message.keys():
                montant = message['money']['amount']
                devise = message['money']['currency']
                
                if  devise != 'EUR':
                    montant = round(montant/parite_devise_euro[devise], 2)
                
                total = round(total + montant, 2)
                nbr_don = nbr_don + 1
            else:
                pass

        except:
            pass
    return total, nbr_don
        #group_example.print_formatted(message)

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
                        'duree_live': la durée du live,
                        'total_don': le montant total des dons sur le live (en euros),
                        'nbr_don' : le nombre de total de dons effectués durant le live,
                        'mean_don': la moyenne du montant du don (en euros),
                        'mean_don_heure': le moyenne par heure du montant total des dons effectués,
                        'nbr_view': le nombre de vue entre la date de publication et le jour où l'information a été récupérée,
                        'nbr_like': le nombre de like entre la date de publication et le jour où l'information a été récupérée,
                        'nbr_com_live': le nombre de commentaire durant le live
                    }
    '''

    request = youtube.videos().list(
            part = ['snippet','statistics', "liveStreamingDetails"],
            id = video_id
        )

    response = request.execute()

    for item in response['items']:
        snip = item['snippet']
        stat = item['statistics']
        live_details = item['liveStreamingDetails']
        
        date = datetime.strptime(snip['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        #cId = snip['channelId']
        titre = snip['title']
        cTitle = snip['channelTitle']

        nbr_view = int(stat['viewCount'])
        nbr_like = int(stat['likeCount'])
        nbr_com_live = int(stat['commentCount'])

        start = datetime.strptime(live_details['actualStartTime'], '%Y-%m-%dT%H:%M:%SZ')
        end = datetime.strptime(live_details['actualEndTime'], '%Y-%m-%dT%H:%M:%SZ')
        duree = end - start
    
    
    total, nbr_don = Get_Montant_Don(video_id)

    mean_don_heure = round((total / duree.total_seconds()) * 3600, 2)

    new_row = {'nom_chaine': cTitle,
                'video_ID': video_id,
                'video_titre': titre,
                'date_publi': date.date(),
                'duree_live': duree,
                'total_don': total,
                'nbr_don' : nbr_don,
                'mean_don': round(total/nbr_don,2),
                'mean_don_heure': mean_don_heure,
                'nbr_view': nbr_view,
                'nbr_like': nbr_like,
                'nbr_com_live':nbr_com_live
    }

    return new_row

########### Fin