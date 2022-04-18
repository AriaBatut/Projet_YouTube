# Projet E4: Profils de Youtubeurs

## Introduction:
 Youtube est l’une des sources « d’informations » les plus complètes où les vidéos sont mises à disposition en temps réel.
 Les utilisateurs peuvent interagir en notant et en commentant les vidéos. Même si chacun peut partager son contenu, depuis l'apparition des chaînes, 
 YouTube promeut les créateurs de contenus individuels, dits youtubeurs. Grâce à ce média, plusieurs vidéastes ont acquis une notoriété sur la plateforme,
 et certains au-delà.

C’est aujourd’hui grâce à des vidéos postées sur cette plateforme, ou bien encore certains choisissent de se diversifier en partageant des vidéos en temps réel,
que l’on appelle live, et où les gens peuvent commenter en direct pour interagir avec leur youtubeur préféré, que beaucoup d’entre eux arrivent à gagner leur vie. 
C’est de là qu'est né le marketing influence c’est à dire le métier d’influenceur qui monétise son image.

En effet, Youtube permet une rémunération, que ce soit via le nombre de vues, ou bien maintenant grâce aux pubs sur la plateforme ou bien les placements de produits, 
partenariat entre une marque et un influenceur, que font les vidéastes au sein de leurs vidéos partagées.

*Mais est-ce réellement le seul revenu qu’ils puissent avoir ?*

C’est le sujet de notre étude. Nous allons nous intéresser aux différentes manière que les youtubers peuvent gagner de l’argent et si tous ont les mêmes revenus.
Nous savons déjà qu’ils n’ont pas tous la même visibilité, ainsi que pas la même quantité de placement de produit ce qui va déjà créer des large écart entre les
youtubeurs à succès et ceux qui viennent de se lancer ou qui ont peu de visibilité.

Notre étude a été faite en partenariat avec Wizdeo, une agence de talents YouTube développant des outils data pour apporter aux créateurs les revenus nécessaires 
au développement de leurs communautés et de leurs projets.

Après discussion, nous sommes parvenus a trois revenus qu’ils peuvent avoir en plus et sur lesquels nous avons basé nos recherches:
- **Crowdfunding :** des sites tiers sur lesquels généralement les “petits” youtubeurs peuvent recevoir des dons par les personnes qui les suivent.
- **Merchandising :** ce sont les activités économiques que les youtubeurs peuvent développer à côté de leur activité sur Youtube comme par exemple des boutiques 
de vêtement en ligne.
- **Membership et dons en live :** certain youtubeurs ont commencé à partager des lives sur lesquels les spectateurs de celui-ci peuvent faire un dons
(une somme d’argent au choix du spectateur qui veut donner) directement aux youtubeurs, ou bien même devenir membre de leur chaîne et avoir accès à certains 
avantages mais en échange d’une somme d’argent fixe, ce qu’on appelle les subs. La plateforme la plus populaire pour cela est Twitch, mais Youtube le fait aussi.

## User Guide
1) Cloner tout le projet à partir du GIT
`git clone https://github.com/AriaBatut/Projet_YouTube`

2) Télécharger les librairies sur la machine. Il est important d'importer tous les modules qui seront nécessaires au bon fonctionnement des programmes. Pour cela utiliser la commande suivante dans un terminal, en vous aillant placé au préalable dans le dossier dans lequel vous avez téléchargé le projet:
`python -m pip install -r requirements.txt`

3) Ensuite vous pouvez parcourir tous les dossiers et trouvez différents fichiers *Jupyter Notebook* que vous pouvez ouvrir. Ils sont tous expliqués avec le code commenté. Chaque case de code est exécutable.

## Developper Guide
Voici ici une liste des fichiers que vous pouvez trouver, qui ont été créés pour notre projet.

**Fichiers fournis**
- *2021_10_08_FR_fr_Channels_LISIS_STUDENTS.xlsx*
Ce fichier est un tableau excel regroupant les 6000 premiers Youtubeurs français avec des informations sur leur chaîne respective. Il y a au total 6008 lignes et 139 colonnes. Les colonnes que nous avons le plus utilisées sont les suivantes:
  - wa_id : est leur ID au sein de l’entreprise WIZDEO qui nous a fournis ce fichier
  - display_name : qui est leur nom de youtubeur
  - yt_user_id : est l’identifiant de leur chaîne sur Youtube, c’est a dire que pour trouver leur chaîne correspondante il suffit de taper l’URL suivant : https://www.youtube.com/channel/UC+yt_user_id

- *2021_10_08_LIVE_VIDEOS.xlsx*
Ce fichier est un corpus de 39 000 vidéos, parmi le corpus de 400 000 vidéos, qui ont été faites en live sur Youtube. Attention, il est possible que certaines soient des avant première d’une vidéo enregistrée. Il faut donc prendre seulement les vidéos dont la durée est supérieur à 30 ou 45 minutes pour être certain que c’était bien un live qui a été diffusé. Il y a 6 colonnes:
  - wa_id, est leur ID au sein de l’entreprise WIZDEO qui nous a fournis ce fichier
  - yt_channel_id est l’identifiant de leur chaîne sur Youtube, c’est a dire que pour trouver leur chaîne correspondante il suffit de taper l’URL suivant : https://www.youtube.com/channel/yt_channel_id
  - video_id : c’est l’identifiant dans l’url Youtube pour retrouver une vidéo en particulier. On utilise l’url sous la forme suivante: https://www.youtube.com/watch?v=video_id
  - title : c’est le titre de la vidéo
  - uploaded : c’est la date et l’heure de la publication
  - duration : c’est la durée de la vidéo

**Fichiers créés**
- *requirement.txt*

Ce fichier contient le nom de tous les modules qui sont nécessaires d’être installés pour le bon fonctionnement des programmes

  **Dans le dossier Fichiers_Crowd**
- *Function Scraping Crowd.ipynb*

Ce fichier contient les fonctions suivantes :

  1) function_get_link_donation : dans cette fonction on met en paramètre un lien URL d’une vidéo youtube et on récupère à la fin les liens de crowdfunding présent dans la description de la vidéo youtube.
  2) function_get_sum_donation : cette fonction prend en paramètre un lien de crowdfunding et elle retourne l’URL, le don sur le site, le nombre d’abonnés qui ont participé au crowdfunding et le temps. Cette fonction retourne les dons et abonnées de deux sites de crowdfunding ‘tipeee’ et ‘utip’.
Ensuite dans ce même fichier on utilise la deuxième fonction sur les données de WIZDEO.

- *Chaine_Lien_crownfunding_f.csv*

Ce fichier, format csv, contient les liens Tipeee avec le nom des chaînes, les données venant d'excel WIZDEO.

- *Chaine_Lien_Dons_crownfunding_tipers_time_summary_f.csv*

Ce fichier, format csv, contient le nom du youtubeur, les liens Tipeee, les dons, le nombre de tipers données venant d'excel WIZDEO.

- *Lien_Dons_crownfunding_tipers_time_JSON_utip.xlsx/.csv*

Résultat sous format excel et csv avec wa_id, le nom du site, le lien, le don, le nombre d’abonnées et le temps où on a collecté l’information du site pour uTip.

- *Lien_Dons_crownfunding_tipers_time_JSON_tipeee.xlsx/.csv*

Résultat sous format excel et csv avec wa_id, le nom du site, le lien, le don, le nombre d’abonnées et le temps où on a collecté l’information du site pour Tipeee.

- *Lien_Dons_crownfunding_tipers_time_JSON_utip_tipeee.xlsx/.csv*

Résultat sous format excel et csv avec wa_id, le nom du site, le lien, le don, le nombre d’abonnées et le temps où on a collecté l’information du site pour tous les sites de crowdfunding des fichiers JSON (1352/1456).

- *Results_utip.xlsx*

Résultat sous format excel et csv avec wa_id, le nom du site, le lien, le don, le nombre d’abonnées, le temps où on a collecté l’information du site avec en plus toutes les autres colonnes du fichier excel WIZDEO pour utip.

- *Results_tipeee.xlsx*

Résultat sous format excel et csv avec wa_id, le nom du site, le lien, le don, le nombre d’abonnées, le temps où on a collecté l’information du site avec en plus toutes les autres colonnes du fichier excel WIZDEO pour tipeee.


  **Dans le dossier Fichiers_Merch**
  
  **Dans le dossier Fichiers_Dons**
- *Webstat_Export_20220309.csv*

Ce fichier a été téléchargé [ici](http://webstat.banque-france.fr/ws_wsfr/downloadFile.do?id=5385698&exportType=csv). Il représente un tableau avec le cours de l’euros pour toutes les différentes monnaies. Ce fichier nous permet de construire un dictionnaire pour convertir en euros les dons d’argent faits dans une autre monnaie.

- *projet_fonction.py*

Ce fichier contient les imports des différents modules utiles ainsi que la création du dictionnaire pour convertir les dons en euros et la création des 3 fonctions utiles pour récupérer les dons sur les replay de live.

- *creation_fichier_IDvideo.ipynb*

Ce fichier permet de faire tourner des lignes de code créant un fichier CSV d’une seule colonne contenant des identifiants de vidéos récupérées dans la catégories “Diffusion en direct terminées” de chaque chaîne. C'est-à-dire que ces vidéos sont des replay de live qui ont été répertoriées. En effet, sur Youtube, il est possible de publier des vidéos en “non répertoriées". Par exemple, sur la chaîne de Michou, il y a une playlist de ses rediffusions de live où les dernières sont très récentes. Cependant, dans la catégorie “Diffusions en direct terminées” de sa chaîne, la dernière date d’il y a plus d’un an.

- *videos_ID.csv*

Ce fichier est le CSV qui a été créée lors de l’exécution du fichier au-dessus. Il n’a qu’une seule colonne, qui contient des identifiants vidéo de replay de live répertoriés.

- *creation_csv_dons.ipynb*

Ce fichier permet de faire tourner des lignes de code créant un fichier CSV qui permet de stocker des informations sur un replay de live, avec en particulier des valeurs sur les dons qui ont été effectués. Dans ces lignes, on peut retrouver des fonctions qui sont créées dans le fichier projet_fonction.py. Après plusieurs executions, avec différentes manières d’obtenir des ID de vidéos, nous avons obtenus 3 fichiers “finaux” qui sont expliqués ci dessous.

- *dons_live.csv*

Ce fichier CSV présente des données sur des live en particulier le montant de dons et le nombre de dons reçu lors d’un live.Les vidéos traitées ont été choisies à la main dans les playlists de replay live de Michou et Inoxtag et répertoriées dans une liste de 22 identifiants. Ce fichier comporte 23 lignes et 13 variables séparées par des virgules.

- *Graph_dons_lives.ipynb*

Ce fichier contient des lignes de code qui sont un petit exemple de comment traiter les fichiers CSV obtenus et un graphique a été réalisé à la fin. C’est le fichier dons_live.csv qui a été utilisé pour créer une data frame.

- *dons_live8810.csv*

Ce fichier CSV présente des données sur des live en particulier le montant de dons et le nombre de dons reçu lors d’un live. Les vidéos traitées ont été trouvées grâce aux identifiants générés et stockés dans le fichier videos_ID.csv. Ce fichier comporte 8810 lignes et 13 variables séparées par des virgules.

- *dons_live_total.csv*

Ce fichier CSV présente des données sur des live en particulier le montant de dons et le nombre de dons reçu lors d’un live. Les vidéos traitées ont été trouvées grâce aux identifiants contenus dans le corpus de 32904 vidéos (dans le fichier *2021_10_08_LIVE_VIDEOS.xlsx*). Ce fichier comporte 23761 lignes et 13 variables séparées par des virgules.

- *Traitement_BDD.ipynb*

Ce fichier contient les lignes de code permettant le traitement de la base de données dons_live_total.csv. Mais aussi quelques analyses statistiques faites sur les bases des données. En particulier une comparaison annuelle tirée de nos bases de données( dons_live8810.csv et dons_live_total_II.csv).

- *dons_live_total_II.csv*

Ce fichier CSV provient d’un traitement des données fait dans le fichier *Traitement_BDD.ipynb*, il correspond au fichier dons_live_total.csv avec les vidéos de moins de 30 minutes supprimées. Car elles sont considérées comme des “Avant-premières” et non des lives

- *Projet Analyse des données.pbix*

Ce fichier contient une analyse des différentes données récoltées sur les dons. Il est nécessaire d'avoir l'application Power BI pour ouvrir le fichier et pouvoir manipuler les différentes données.


