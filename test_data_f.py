import pandas as pd
import test
import temp

df = pd.DataFrame(columns=['nom_chaine','video_ID','video_titre','date_publi',
                            'duree_live', 'total_don', 'nbr_don', 'mean_don',
                            'mean_don_heure', 'nbr_view', 'nbr_like', 'nbr_com_live'])

#video_list = temp.Liste_Video_Username('MichouFr')
video_list = ['NBcUl3oCUug', "qenUHy8e4XQ", 'I7oTq8i9yoE', 'bNaNLCUPH64', 'Pei5CPhYzsU',
                'pqGerv_SZi0', '9u1zTePZTbQ', '8WGgcmFrAh4', 'hqvf_Pvyjwo', 'wZUKnm0zo-g', 'kgt2XBsgbtI','jcshh0ICCzI',
                'GFK-iC_uuHs', '8lhs9IY8044', 'ZH1LyZtnRDQ', 'Xw4XIGSvuWU', 'YkoqTG08hzk', 'tRBOGTdW-FE','qtpoK_uKe5g', 'HBZslQ7TVH8', 'FyD3SAIUKns', 'cn2-pOxZ--o',  ]
vid = 0
vid_1 = 1

#for video in video_list:
#    if video["video_id"] != 'yZBBqXG129Q':
        #new = test.create_row_data_frame(video["video_id"])
for id_video in video_list:
    new = test.create_row_data_frame(id_video)
    df = df.append(new, ignore_index=True)
    vid = vid + 1
    print(vid)
    if vid == 10:
        name = "michou_dons_live"+str(vid*vid_1)+".csv"
        vid_1 = vid_1+1
        vid = 0
        df.to_csv(name)

df.to_csv("dons_live.csv")
#df.to_csv("michou_dons_live.csv")

