from googleapiclient.discovery import build

from datetime import datetime


import temp  # importer le module du fichier temp.py
# essaie 'NBcUl3oCUug'

api_key = 'AIzaSyCno1uXk56UrNcMvANdIHdTbkUyxHmI7r0'

youtube = build('youtube', 'v3', developerKey=api_key)

def create_row_data_frame(video_id):

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
    
    
    total, nbr_don = temp.Get_Montant_Don(video_id)

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


