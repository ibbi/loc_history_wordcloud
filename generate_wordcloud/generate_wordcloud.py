import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


hardCoded = {'College Park': 713833, 'University Park': 1515, 'Hyattsville': 464, 'Mount Rainier': 569, 'Chillum': 314, 'Washington, D.C.': 8326, 'Glassmanor': 25, 'Woodburn': 1914, 'Oak Hill': 88739, 'Bethesda': 1274, 'Brookmont': 528, 'Berwyn Heights': 4820, 'East Riverdale': 283, 'New Carrollton': 289, 'Lanham': 369, 'Lanham-Seabrook': 12971, 'Goddard': 996, 'Greenbelt': 275, 'Beltsville': 1401, 'Hillandale': 393, 'Four Corners': 692, 'Forest Glen': 225, 'Cabin John': 1507, 'Potomac': 996, 'Poolesville': 714, 'Loudoun Valley Estates': 1263, 'North Bethesda': 372, 'Garrett Park': 69, 'Calverton': 787, 'West Laurel': 46, 'North Laurel': 40, 'Jessup': 54, 'West Elkridge': 43, 'Elkridge': 30, 'Lansdowne': 47, 'Baltimore': 1697, 'Dundalk': 64, 'Rosedale': 48, 'Rossville': 44, 'White Marsh': 68, 'Joppatowne': 60, 'Edgewood': 18, 'Riverside': 77, 'Perryman': 7, 'Aberdeen': 88, 'Havre de Grace': 70, 'Perryville': 76, 'Charlestown': 28, 'North East': 62, 'Newark': 23, 'Brookside': 103, 'Beckett': 9, 'Bellmawr': 7, 'Barrington': 6, 'Lawnside': 6, 'Ellisburg': 3, 'Kingston Estates': 3, 'Ramblewood': 14, 'Mount Laurel': 19, 'Mount Holly': 28, 'Tullytown': 20, 'Morrisville': 16, 'Mercerville-Hamilton Square': 70, 'Whittingham': 4330, 'East Franklin': 270, 'West Orange': 328, 'Financial District': 1070, 'Gramercy Park': 448, 'Yardley': 11, 'Woodside': 5, 'Woodbourne': 3, 'Langhorne Manor': 2, 'Penndel': 8, 'Trevose': 3, 'Cinnaminson': 2, 'Tacony': 9, 'Pennsauken': 40, 'Camden': 1, 'Center City': 15, 'Pennsport': 6, 'Whitman': 31, 'National Park': 15, 'Colwyn': 32, 'Folcroft': 13, 'Prospect Park': 4, 'Ridley Park': 28, 'Woodlyn': 9, 'Eddystone': 5, 'Chester': 11, 'Upland': 80, 'Trainer': 13, 'Linwood': 8, 'Boothwyn': 8, 'Claymont': 24, 'Bellefonte': 13, 'Wilmington': 47, 'Elsmere': 8, 'Newport': 47, 'Bear': 19, 'Elkton': 80, 'Kingsville': 17, 'Overlea': 15, 'Arbutus': 39, 'Savage': 53, 'Bowie': 26, 'Riva': 21, 'Arnold': 4, 'Cape Saint Claire': 218, 'Grasonville': 11, 'Centreville': 11, 'Easton': 24, 'Trappe': 17, 'Cambridge': 26, 'Hurlock': 11, 'Hebron': 20, 'Pittsville': 15, 'West Ocean City': 33, 'Ocean City': 111, 'Ocean Pines': 1, 'Berlin': 49, 'Salisbury': 9, 'Stevensville': 3, 'Fairwood': 48, 'Woodmore': 110, 'Springdale': 38, 'Glenarden': 87, 'Chevy Chase': 333, 'South Kensington': 160, 'Travilah': 270, 'Landover Hills': 15, 'Cheverly': 38, 'Bladensburg': 15, 'Fairmount Heights': 128, 'Capitol Heights': 20, 'Coral Hills': 27, 'Silver Hill': 74, 'Hillcrest Heights': 152, 'Edmonston': 90, 'Seabrook': 365, 'Glenn Dale': 32, 'Mount Vernon': 19, 'Woodlawn': 13, 'Colmar Manor': 132, 'Cottage City': 16, 'Riverdale Park': 58, 'Robinwood': 103, 'Hancock': 67, 'McConnellsburg': 48, 'Martinsburg': 22, 'Roaring Spring': 11, 'Windber': 10, 'Somerset': 132, 'Ligonier': 14, 'Montrose-Ghent': 7405, 'Clark-Fulton': 267, 'Detroit-Shoreway': 138, 'Amherstburg': 306, 'Windsor': 3752, 'Silver Spring': 364, 'Redland': 29, 'Green Valley': 24, 'Myersville': 72, 'Mount Pleasant': 51, 'Youngwood': 33, 'New Stanton': 37, 'West Newton': 20, 'Washington': 19, 'Wolfdale': 19, 'Bethlehem': 13, 'Wheeling': 25, 'Barnesville': 30, 'Byesville': 33, 'New Concord': 9, 'Pleasant Grove': 13, 'Zanesville': 18, 'Etna': 16, 'Columbus': 19691, 'Grandview Heights': 6, 'Upper Arlington': 2, 'Lincoln Village': 8, 'Lake Darby': 15, 'West Jefferson': 10, 'Choctaw Lake': 41, 'Lisbon': 5, 'Springfield': 54, 'Enon': 16, 'Holiday Valley': 3, 'Park Layne': 2, 'Huber Heights': 13, 'Northridge': 1, 'Vandalia': 5, 'Shiloh': 1, 'Englewood': 5, 'Clayton': 19, 'New Paris': 34, 'Centerville': 18, 'Cambridge City': 14, 'New Castle': 16, 'Knightstown': 19, 'Greenfield': 29, 'Cumberland': 26, 'Meridian Hills': 4, 'Zionsville': 10, 'Whitestown': 1, 'Dale': 4, 'Lebanon': 47, 'Mulberry': 3, 'West Lafayette': 1909, 'Lafayette': 8, 'Dayton': 15, 'Thorntown': 7, 'Indianapolis': 1, 'London': 1, 'Bexley': 3, 'Blacklick Estates': 3, 'Reynoldsburg': 5, 'Millersport': 4, 'Harbor Hills': 2, 'Thornport': 11, 'West Liberty': 26, 'McGovern': 5, 'McMurray': 31, 'Edgemoor': 12, 'Wyncote': 1, 'Philadelphia': 5407, 'Wharton': 86, 'Adelphi': 312452, 'Langley Park': 285, 'Rockville': 553, 'Derwood': 58, 'Gaithersburg': 324, 'North Kensington': 9, 'Milton': 5, 'Bellevue': 1, 'White Oak': 14, 'Colesville': 2, 'Ashton-Sandy Spring': 1, 'Olney': 9, 'Montgomery Village': 484, 'Kings Park West': 464, 'Brentwood': 16, 'Wheaton': 1, 'Riyadh': 15828, 'Oosteinde': 243, 'Baltimore Highlands': 6, 'Brooklyn Park': 11, 'Glasgow': 6, 'Wilmington Manor': 14, 'Norwood': 1, 'Atlantic City': 1, 'Near South Side': 1, 'Landover': 20, 'Davidsonville': 26, 'Crownsville': 7, 'Gambrills': 40, 'Glen Burnie': 4, 'Severn': 7, 'São Miguel do Araguaia': 1, 'Fairland': 174, 'Laurel Hill': 22, 'Bilma': 2, 'Khobar': 117, 'shokhaibٍ': 17, 'Ad Dawādimī': 20, '‘Afīf': 20, 'Al Muwayh': 14, 'Ta’if': 8, 'Unayzah': 1, 'Al Bahah': 2, 'Al Hadā': 3, 'Mecca': 46, 'Medina': 2, 'National Harbor': 59, 'South Gate': 5, 'Pumphrey': 2, 'Edgemere': 4, 'Essex': 8, 'Perry Hall': 19, 'Millbourne': 2, 'Narberth': 9, 'Plymouth Meeting': 9, 'West Conshohocken': 11, 'Norristown': 1, 'North Wales': 11, 'Souderton': 4, 'Telford': 9, 'Spinnerstown': 17, 'Wescosville': 6, 'Schnecksville': 8, 'Weissport East': 33, 'Towamensing Trails': 114, 'White Haven': 6, 'Mountain Top': 3, 'Plains': 3, 'Pittston': 5, 'Moosic': 3, 'Old Forge': 4, 'Taylor': 2, 'Scranton': 3, 'Throop': 11, 'Olyphant': 46, 'Mayfield': 8, 'Simpson': 9, 'Susquehanna': 23, 'Montrose': 9, 'Sayre': 41, 'South Waverly': 21, 'Horseheads North': 83, 'Westfield': 67, 'Gates-North Gates': 148, 'Fort Erie': 266, 'Niagara Falls': 6, 'St. Catharines': 3, 'Hamilton': 2, 'Oakville': 1, 'Etobicoke': 4, 'Toronto': 36, 'North York': 90, 'Willowdale': 4, 'Concord': 2054, 'Vaughan': 16, 'Mississauga': 614, 'East York': 3, 'Burlington': 1, 'Binbrook': 1, 'Thorold': 1, 'Slatington': 6, 'Macungie': 1, 'Woxall': 1, 'Skippack': 1, 'Lansdale': 5, 'Middletown': 4, 'Fort George G Mead Junction': 8, 'South Laurel': 12, 'Takoma Park': 45, 'Columbia': 25, 'Plum Creek': 14, 'Day Heights': 1, 'Darnestown': 210, 'Leisure World': 4, 'Friendly': 1, 'Damascus': 229, 'Mechanicsburg': 2, 'Parole': 13, 'Hanover': 8, 'Ferndale': 10, 'Linthicum': 8, 'Brunswick': 16, 'Twin Lakes': 294, 'Fort Hunt': 3, 'Lakewood': 354, 'Nashville': 5017, 'Sorrento Valley': 1, 'Tarrant': 117, 'Birmingham': 26, 'Fairfield': 5, 'Bessemer': 109, 'Tuscaloosa': 1842, 'Holt': 5, 'Coaling': 3, 'Vance': 2, 'North Bibb': 1, 'Woodstock': 2, 'Lake View': 3, 'Helena': 1, 'Hoover': 2, 'Vestavia Hills': 2, 'Cahaba Heights': 47, 'Meadowbrook': 227, 'Lake Purdy': 8, 'Highland Lakes': 24, 'Irondale': 8, 'Charlotte': 35, 'Belmont': 54, 'Pueblo': 1, 'Fairplay': 1, 'Paradise': 575, 'Millbrae': 376, 'San Bruno': 8, 'Burlingame': 9, 'San Mateo': 12, 'Redwood City': 6, 'Palo Alto': 64, 'Sunnyvale': 4, 'Santa Clara': 102, 'Milpitas': 1289, 'Fremont': 211, 'San Jose': 28, 'Alameda': 37, 'Emeryville': 40, 'Albany': 10, 'Richmond': 2, 'Berkeley': 224, 'Spencer': 2, 'Rosemont': 135, 'Schiller Park': 1, 'Doha': 122, 'Srinagar': 43568, 'Kolkata': 3, 'Soyībug': 61, 'Gurgaon': 959, 'Deoli': 16, 'Maryland City': 1, 'Summerfield': 25, 'Largo': 18, 'Kettering': 5, 'Mitchellville': 97, 'Lake Arbor': 44, 'Prairie du Sac': 1, 'Santa Ana': 18, 'Hallbergmoos': 19, 'Marzling': 45, 'Eynesil': 12, 'Karol Bāgh': 488, 'Vijayawada': 3274, 'Pulwama': 28, 'Kupwāra': 417, 'Pattan': 9, 'Southern Gateway': 913, 'Pennsville': 8, 'Carneys Point': 18, 'Swedesboro': 12, 'Mullica Hill': 7, 'Paulsboro': 4, 'Woodbury Heights': 12, 'Woodbury': 4, 'Westville': 2, 'Runnemede': 3, 'Magnolia': 1, 'Ashland': 4, 'Sunset Park': 616, 'Dover Beaches North': 455, 'Chinatown': 42713, 'Germantown': 22, 'Clarksburg': 27, 'Urbana': 22, 'Buckeystown': 5, 'Ballenger Creek': 26, 'Frederick': 626, 'Clover Hill': 61, 'Indian Springs Village': 1, 'Zgornje Gorje': 2, 'Braddock Heights': 15, 'Hagerstown': 15, 'Halfway': 106, 'Wilson-Conococheague': 21, 'Salix': 3, 'Manor': 7, 'Level Green': 5, 'Plum': 4, 'Oakmont': 6, 'Russellton': 6, 'Mars': 9, 'Seven Fields': 3, 'Cranberry Township': 24, 'Zelienople': 5, 'Rochester': 1, 'New Brighton': 7, 'West Mayfield': 11, 'New Beaver': 33, 'Oakwood': 11, 'Sharon': 57, 'Champion Heights': 90, 'Monroeville': 1, 'Williamsport': 1, 'Boonsboro': 8, 'Boston': 265, 'Fort Belvoir': 9, 'Quantico Station': 21, "Boswell's Corner": 38, 'Fort Lee': 31, 'Gaston': 14, 'Norlina': 6, 'South Rosemary': 1461, 'Havelock': 26, 'Warrenton': 11, 'Woodlake': 1, 'Friendship Village': 45, 'Crofton': 3, 'Annapolis': 115, 'Abu Dhabi': 169, 'New Delhi': 64, 'Tsrār Sharīf': 2, 'Gāndarbal': 68, 'Māgām': 36, 'Mānsa': 1, 'Nāngloi Jāt': 2, 'Beri Khās': 1, 'Yazman': 22, 'Forestville': 5, 'Morningside': 4, 'Temple Hills': 2, 'Oxon Hill-Glassmanor': 2, 'Forest Heights': 2, 'Lutherville': 4, 'Mays Chapel': 6, 'Parkville': 2, 'Bel Air South': 1, 'Carney': 4, 'Aalsmeer': 20, 'Hoofddorp': 5, 'Amstelveen': 11, 'Amsterdam': 3080, 'Duivendrecht': 48, 'Diemen': 1, 'Muiden': 2, 'Hilversumse Meent': 2, 'Bussum': 4, 'Hilversum': 8, 'Baarn': 2, 'Hoogland': 2, 'Amersfoort': 5, 'Randenbroek': 1, 'Nijkerkerveen': 1, 'Terschuur': 2, 'Voorthuizen': 3, 'Kootwijkerbroek': 1, 'Garderen': 2, 'Uddel': 1, 'Orden': 1, 'Binnenstad': 1, 'Apeldoorn': 2, 'Matenhorst': 1, 'Woudhuis': 1, 'De Hoven': 1, 'Deventer': 7, 'Schalkhaar': 1, 'Het Oostrik': 1, 'Laren': 2, 'Markelo': 2, 'Wierden': 3, 'Almelo': 3, 'Nijrees': 1, 'Borne': 1, 'Woolde': 1, 'Hengelo': 4, 'Klein Driene': 1, 'Rheine': 1, 'Ibbenbüren': 1, 'Bad Oeynhausen': 1, 'Großgoltern': 1, 'Seelze': 1, 'Hannover': 6, 'Laatzen': 1, 'Lehrte': 2, 'Dollbergen': 1, 'Westhagen': 2, 'Wolfsburg': 2, 'Danndorf': 1, 'Mieste': 5, 'Jävenitz': 1, 'Lüderitz': 2, 'Uenglingen': 1, 'Stendal': 7, 'Tangermünde': 1, 'Schönhausen': 4, 'Rathenow': 1, 'Nennhausen': 3, 'Nauen': 14, 'Siemensstadt': 2, 'Westend': 1, 'Halensee': 5, 'Wilmersdorf': 1, 'Tiergarten': 17, 'Mitte': 6, 'Berlin Treptow': 656, 'Friedrichshain': 728, 'Alt-Treptow': 5, 'Rummelsburg': 1, 'Karlshorst': 4, 'Köpenick': 4, 'Adlershof': 1, 'Altglienicke': 5, 'Schönefeld': 120, 'Zaandam': 2, 'Pantops': 658, 'Isla Vista': 2360, 'Kingman': 4, 'Twentynine Palms': 6, 'New Matamoras': 1, 'Barstow Heights': 5, 'Leona Valley': 3, 'Ojai': 7, 'Carpinteria': 5, 'Toro Canyon': 5, 'Silver Lakes': 6, 'Jemez Pueblo': 1, 'Castaic': 13, 'Mission Canyon': 7, 'Flagstaff': 3, 'Willow Valley': 2, 'Mohave Valley': 3, 'Piru': 6, 'Crownpoint': 3, 'Ganado': 2, 'Spearman': 2, 'Rockport': 1, 'Los Alamos': 1, 'LeChee': 1, 'Mosquero': 2, 'Houston': 1, 'Carbondale': 1, 'Lewisport': 1, 'Gallipolis': 2, 'Oakland': 90, 'Belmont Estates': 6, 'Santa Barbara': 10, 'Paulden': 1, 'Desert View Highlands': 1, 'Meiners Oaks': 2, 'Window Rock': 1, 'Parks': 2, 'Needles': 5, 'Sun Village': 2, 'Fillmore': 3, 'Montecito': 3, 'Goleta': 20, 'Palmdale': 2, 'Dilkon': 2, 'Goodwell': 1, 'Alva': 1, 'Caney': 1, 'Midway': 1, 'Carrier Mills': 1, 'Golden Valley': 1, 'Medford': 1, 'Jackson': 1, 'Elk Creek': 1, 'Oak View': 1, 'Fort Irwin': 4, 'Strafford': 1, 'Mira Monte': 2, 'Adelanto': 2, 'Summerland': 1, 'Salem': 1, 'Barstow': 1, 'Mooreland': 1, 'Fountainhead-Orchard Hills': 21, 'Paramount-Long Meadow': 8, 'Cavetown': 225, 'Smithsburg': 9, 'Wayne Heights': 18, 'Highfield-Cascade': 153, 'Waynesboro': 581, 'Chevy Chase Village': 8, 'Highland': 10, 'Ellicott City': 1, 'Milford Mill': 2, 'Pikesville': 5, 'Towson': 1, 'Hampton': 1, 'Rising Sun': 11, 'Oxford': 6, 'West Grove': 2, 'Toughkenamon': 3, 'Kennett Square': 32, 'Thorndale': 19, 'South Coatesville': 2, 'Caln': 3, 'Avondale': 1, 'Bowling Green': 2, 'Frostburg': 9, 'Meyersdale': 22, 'Fairchance': 5, 'Point Marion': 27, 'Waynesburg': 6, 'Muse': 2, 'Cecil-Bishop': 1, 'Upper Saint Clair': 3, 'Rennerdale': 3, 'McKees Rocks': 16, 'Pittsburgh': 1219, 'Mount Oliver': 62, 'Millvale': 10, 'West View': 15, 'Gulivoire Park': 3, 'Prescott': 40, 'Elko New Market': 874, 'Lamar': 1, 'El Dorado': 1, 'Western Lake': 1, 'Chino Valley': 1, 'Black Canyon City': 4, 'Boulder City': 1, 'Henderson': 1, 'Whitney': 1, 'Fairview': 8, 'Lents': 9, 'Orchards': 7, 'Walnut Grove': 85, 'Vancouver': 27, 'Portland': 7674, 'Wood Village': 1, 'Gresham': 14, 'Sandy': 275, 'Mount Hood Village': 159, 'Happy Valley': 16, 'Clackamas': 39, 'Oatfield': 7, 'Milwaukie': 223, 'Lake Oswego': 3, 'Metzger': 27, 'Garden Home-Whitford': 2, 'Kenton': 105, 'Hazel Dell': 13, 'Salmon Creek': 13, 'Mount Vista': 26, 'La Center': 47, 'Woodland': 53, 'Amboy': 86, 'Morton': 4, 'Yacolt': 20, 'North Portland': 6, 'Daly City': 10, 'South San Francisco': 21, 'Brisbane': 11, 'Visitacion Valley': 24, 'Noe Valley': 98, 'Mission District': 5824, 'San Francisco': 20089, 'Hillsborough': 1, 'Highlands-Baywood Park': 2, 'Emerald Lake Hills': 1, 'West Menlo Park': 1, 'Ladera': 1, 'Los Altos Hills': 1, 'Loyola': 2, 'Cupertino': 1, 'Cambrian Park': 2, 'Seven Trees': 4, 'Morgan Hill': 9, 'San Martin': 20, 'Gilroy': 29, 'San Juan Bautista': 1, 'Hollister': 8, 'Gustine': 18, 'South Dos Palos': 9, 'Los Banos': 11, 'Firebaugh': 3, 'Mendota': 10, 'Coalinga': 10, 'Huron': 7, 'Avenal': 8, 'Kettleman City': 29, 'Lost Hills': 50, 'Buttonwillow': 19, 'Shafter': 1, 'Weedpatch': 3, 'Frazier Park': 19, 'Lebec': 12, 'Stevenson Ranch': 7, 'Santa Clarita': 1, 'San Fernando': 11, 'North Hollywood': 3, 'Universal City': 2, 'Hollywood': 1163, 'Koreatown': 1, 'Silver Lake': 19, 'Echo Park': 8, 'Los Angeles': 239, 'West Hollywood': 127, 'Beverly Hills': 30, 'Boyle Heights': 1, 'Glendale': 1, 'North Glendale': 1, 'Burbank': 15, 'Taft': 2, 'San Joaquin': 1, 'Union City': 2, 'San Leandro': 274, 'Nowthen': 36, 'Hornsby Bend': 385, 'Garfield': 1, 'Austin': 41119, 'Barton Creek': 117, 'Bee Cave': 42, 'Briarcliff': 272, 'Buda': 8, 'Geronimo': 21, 'Cibolo': 10, 'Garden Ridge': 1, 'Alamo Heights': 219, 'Castle Hills': 18, 'Reading': 4, 'Brushy Creek': 46, 'Anderson Mill': 27, 'Cedar Park': 20, 'Hudson Bend': 25, 'Colma': 10, 'Broadmoor': 3, 'El Segundo': 117, 'Del Aire': 5, 'Alvarado': 2, 'Grand Prairie': 1, 'Grapevine': 69, 'Coppell': 12, 'Kensington': 45, 'Foster City': 3, 'North Fair Oaks': 3, 'East Palo Alto': 4, 'Mountain View': 153, 'Los Altos': 4, 'San Carlos': 3}

world_mask = np.array(Image.open("mask.png"))
wc = WordCloud(background_color="white", max_words=1000, mask=world_mask)

wc.generate_from_frequencies(hardCoded)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
