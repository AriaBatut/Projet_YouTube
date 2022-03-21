from chat_downloader import ChatDownloader
from chat_downloader.sites import YouTubeChatDownloader

########### Dictionnaire pour convertir les dons qui ne sont pas en euros

#http://webstat.banque-france.fr/ws_wsfr/downloadFile.do?id=5385698&exportType=csv

import numpy as np
import pandas as pd
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

def Liste_Video_Username(custom_username):
    video_list = YouTubeChatDownloader().get_user_videos(custom_username = custom_username, video_status = "past")
    return video_list



def Get_Montant_Don(video_id):
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


# Créer un DF avec le nom de la chaine, le titre de la vidéo, la date de publication, la durée du live
# le montant total, une moyenne sur le montant du don (total/nbr_don), nombre de membre sur le live, nombre de nouveau membre
# nbr de vue, nbr de j'aime, moyenne pare heure (total/durée)