import json

greece_data = {
    "metadata": {
        "title": "Yunanistan Özel Seyahat Rehberi - Kavala, Selanik, Halkidiki, Vergina, Meteora ve İskeçe",
        "shortTitle": "Yunanistan Rotası",
        "planStatus": "approved_current_plan",
        "version": "2.0",
        "createdAt": "2026-10-19",
        "updatedAt": "2026-10-19",
        "language": "tr-TR",
        "timezone": "Europe/Athens",
        "distanceAndTimeDisclaimer": "Mesafeler ve sürüş süreleri yaklaşık değerlerdir. İpsala sınır kapısındaki kuyruk yoğunluğu, otoyol gişeleri ve yol çalışmaları süreleri değiştirebilir.",
        "bookingStatus": "Tüm otel rezervasyonları yapılmıştır; detaylar günlük programda ve konaklama bölümünde yer almaktadır."
    },
    "tripSummary": {
        "travelers": 2,
        "specialDietaryNotes": "Eşi çölyak hastasıdır (%100 glutensiz ve çapraz bulaşmasız mutfak zorunludur). Dini sebeplerle domuz eti/yağı kesinlikle tüketilmemektedir.",
        "startDate": "2026-10-24",
        "endDate": "2026-10-29",
        "durationDays": 6,
        "durationNights": 5,
        "startLocation": "İstanbul, Türkiye",
        "endLocation": "İstanbul, Türkiye",
        "arrival": {
            "date": "2026-10-24",
            "borderName": "İpsala / Kipi Sınır Kapısı",
            "country": "Yunanistan",
            "note": "İstanbul çıkışlı şahsi araçla İpsala üzerinden Yunanistan girişi"
        },
        "departure": {
            "date": "2026-10-29",
            "borderName": "Kipi / İpsala Sınır Kapısı",
            "destination": "İstanbul, Türkiye",
            "note": "Porto Lagos ve Gümülcine üzerinden A2 otoyoluyla Türkiye'ye dönüş"
        },
        "routeType": "circular_self_drive",
        "vehicleType": "Şahsi Araç (İlk Yurt Dışı Sürüşü)",
        "estimatedTotalDistanceKm": {
            "min": 1850,
            "max": 1950,
            "exact": 1895
        },
        "estimatedTotalDrivingHoursIncludingNormalBorders": {
            "min": 22,
            "max": 25
        },
        "countries": [
            "Türkiye",
            "Yunanistan"
        ],
        "primaryHighways": [
            "A2 (Egnatia Odos - Bölünmüş Ücretli Otoyol)",
            "A1 (Selanik - Atina Bölünmüş Otoyolu)",
            "A24 (Selanik - Kassandra Bölünmüş Otoyolu)"
        ],
        "excludedCountries": [
            {
                "country": "Kuzey Makedonya / Bulgaristan",
                "reason": "Bu tur 6 günlük doğrudan Ege ve Kuzey Yunanistan odaklı planlanmıştır; transit geçiş ve fazladan sınır kapısı yoğunluğu oluşturmamak için rota dışı bırakılmıştır."
            }
        ]
    },
    "approvedRoute": {
        "orderedStops": [
            "İstanbul",
            "İpsala Sınır Kapısı",
            "Kavala (Panagia & Liman)",
            "Selanik (Ano Poli / Yedikule)",
            "Nea Elvetia Metro (Park & Ride)",
            "Perea (Sahil)",
            "Afytos (Halkidiki - Kassandra)",
            "Vergina (Aigai Kraliyet Mezarları)",
            "Kalambaka (Meteora Manastırları)",
            "Dion Arkeolojik Parkı (Olimpos)",
            "İskeçe (Xanthi Eski Şehir)",
            "Mandra (Avdira)",
            "Porto Lagos (Aziz Nikolaos)",
            "İpsala Sınır Kapısı",
            "İstanbul"
        ],
        "routeText": "İstanbul → İpsala → Kavala → Selanik → Perea → Afytos → Vergina → Meteora (Kalambaka) → Dion → İskeçe → Mandra → Porto Lagos → İpsala → İstanbul",
        "googleMapsUrl": "https://www.google.com/maps/dir/%C4%B0stanbul,+T%C3%BCrkiye/%C4%B0psala+S%C4%B1n%C4%B1r+Kap%C4%B1s%C4%B1,+K%C3%B6pr%C3%BC,+%C4%B0psala%2FEdirne,+T%C3%BCrkiye/Atlas+Boutique+Suites,+%CE%9A%CE%B1%CF%81%CE%AC%CE%BD%CE%BF%CF%85+1,+%CE%9A%CE%B1%CE%B2%CE%AC%CE%BB%CE%B1,+%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1/(%CE%BC)+Metro+Station+%22Nea+Elvetia%22,+Michail+Psellou,+Thessaloniki,+Greece/Atlantis+''pleasure+By+The+Sea'',+Pavlou+Kountouriotou+51,+Perea,+Yunanistan/Free+Parking+1+Afytos,+4C3M%2B76,+Kassandra,+Greece/Aigai+Kraliyet+Mezarlar%C4%B1+M%C3%BCzesi,+Vergina,+Yunanistan/Hotel+Kaikis,+Trikalon+146,+Kalampaka,+Yunanistan/Archaeological+Site+of+Dion,+Eparchiaki+Odos+Katerinis+-+Limena+Litochoriou+910,+Dion,+Greece/Petrinos+Lofos,+Mandra,+Mandra,+67061,+Avdira,+Greece/%CE%99%CE%B5%CF%81%CE%AC+%CE%9C%CE%BF%CE%BD%CE%AE+%CE%91%CE%B3%CE%AF%CE%BF%CF%85+%CE%9D%CE%B9%CE%BA%CE%BF%CE%BB%CE%AC%CE%BF%CF%85,+Porto+Lagos,+Yunanistan/%C4%B0stanbul,+T%C3%BCrkiye"
    },
    "routeDecisions": {
        "safetyStrategy": {
            "status": "safe_motorways_only",
            "title": "Güvenli Otoyol Tercihi",
            "explanation": "İlk kez yurt dışına kendi aracınızla çıkacağınız için rotadaki tüm tehlikeli, dar dağ ve köy yolları elenmiştir. Ana geçişler tamamen A2 (Egnatia Odos) ve A1 bölünmüş ücretli otoyolları üzerinden planlanmıştır. Gişe ücretleri 1,50 € – 3,00 € arasındadır; hem kredi kartı hem nakit geçer."
        },
        "thessalonikiStrategy": {
            "status": "park_and_ride_metro",
            "title": "Selanik Metro Park & Ride",
            "explanation": "Selanik merkezine araçla kesinlikle girilmeyecektir. Önce çevre yolundan tepe mahalle Ano Poli gezilecek, ardından doğu uçtaki Nea Elvetia Metro İstasyonu otoparkına (650 araçlık) bırakılarak merkeze metroyla inilip yürüyüş yokuş aşağı yapılacaktır."
        },
        "placesIntentionallyNotIncluded": [
            {
                "place": "Olimpos Dağı Zirve Sürüşü (Prionia)",
                "reason": "Dar, dik ve virajlı dağ yolu ilk yurt dışı sürüşü için riskli görüldüğünden Olimpos Dağı eteklerindeki düz ayak Dion Arkeolojik Parkı tercih edilmiştir."
            },
            {
                "place": "Büyük Meteoron Manastırı (İç Gezi)",
                "reason": "Büyük Meteoron Salı günleri ziyarete kapalıdır. Bu nedenle Salı günü açık olan Varlaam (16:00) ve Roussanou (16:30) manastırları iç gezisi yapılıp Büyük Meteoron dışarıdan seyredilecektir."
            },
            {
                "place": "Atina ve Mora Yarımadası",
                "reason": "6 günlük sürede sürüş yorgunluğunu önlemek ve Kuzey Yunanistan kültür mirasına odaklanmak için ayrı bir geziye bırakılmıştır."
            }
        ]
    },
    "greekSosCard": {
        "title": "Restoranlarda Garsona Gösterilecek Yunanca Çölyak & Domuz Eti Kartı",
        "description": "Restorana oturduğunuzda sipariş vermeden önce bu ekranı doğrudan garsona veya mutfak şefine okutun. Hem Çölyak hastalığını (çapraz bulaşma dahil) hem de domuz eti/yağı tüketmediğinizi eksiksiz ve resmi bir dille açıklar.",
        "greekText": "Γεια σας! Η σύζυγός μου πάσχει από κοιλιοκάκη (σοβαρή αλλεργία στη γλουτένη). Δεν μπορεί να καταναλώσει απολύτως τίποτα που να περιέχει σιτάρι, κριθάρι, σίκαλη ή αλεύρι (ούτε σε σάλτσες, ούτε σε μαρινάδες). Επίσης, το φαγητό της δεν πρέπει να έρθει σε επαφή (επιμόλυνση) με λάδι φριτέζας όπου τηγανίστηκαν τρόφιμα με αλεύρι, ή με επιφάνειες/σκεύη που έχουν γλουτένη.\n\nΕπιπλέον, για θρησκευτικούς λόγους, δεν τρώμε καθόλου χοιρινό κρέας, μπέικον, ζαμπόν ή ζωικό λίπος χοιρινού.\n\nΜπορείτε σας παρακαλώ να μας προτείνετε ασφαλή πιάτα (π.χ. φρέσκο ψάρι ή θαλασσινά στη σχάρα, ψητό κοτόπουλο/αρνί ή καθαρά λαχανικά με ελαιόλαδο και λεμόνι); Σας ευχαριστούμε πολύ!",
        "turkishTranslation": "Merhaba! Eşim çölyak hastasıdır (ciddi gluten alerjisi). Buğday, arpa, çavdar veya un içeren hiçbir şeyi (soslarda veya marinasyonlarda dahi) tüketemez. Ayrıca yemeği, unlu gıdaların kızartıldığı fritöz yağıyla veya glutenli yüzey/ekipmanlarla temas etmemelidir (çapraz bulaşma olmamalıdır). Ek olarak, dini sebeplerle hiçbir şekilde domuz eti, pastırması, jambonu veya domuz yağı yemiyoruz. Bize güvenli tabaklar (örneğin ızgara taze balık/deniz ürünleri, ızgara tavuk/kuzu veya sadece zeytinyağı ve limonlu sebzeler) önerebilir misiniz? Çok teşekkür ederiz!",
        "safeFoods": [
            {
                "name": "Psari Skaras (Ψάρι Σχάρας)",
                "desc": "Izgara taze balık (sadece zeytinyağı ve limon sosu = Ladolemono ile)."
            },
            {
                "name": "Htapodi Skaras (Χταπόδι Σχάρας)",
                "desc": "Izgara ahtapot (unlanmadığından emin olun, ızgara olanı tamamen doğaldır)."
            },
            {
                "name": "Kalamari Skaras (Καλαμάρι Σχάρας)",
                "desc": "Izgara kalamar (tava/tiganita unlu olduğu için yasaktır; mutlaka 'Skaras' isteyin)."
            },
            {
                "name": "Horiatiki Salata (Χωριάτικη)",
                "desc": "Klasik Yunan salatası (domates, salatalık, zeytin, saf zeytinyağı ve feta peyniri). Üzerine paximadi (peksimet) konulmamasını söyleyin."
            },
            {
                "name": "Fava & Melitzanosalata",
                "desc": "Sarı mercimek püresi (fava) ve köz patlıcan salatası (ekmeksiz tüketildiğinde doğal glutensizdir)."
            }
        ],
        "hiddenTraps": [
            {
                "name": "Tiganita (Τηγανητά - Kızartmalar)",
                "desc": "Kabak kızartması, kalamar tava ve patates kızartması genellikle unlanır veya aynı fritözde pişer; kesinlikle kaçının!"
            },
            {
                "name": "Keftedes / Soutzoukakia (Köfteler)",
                "desc": "Yunan köftelerinde hem ekmek içi (gluten) hem de %50 dana - %50 domuz kıyması karışımı sıkça kullanılır."
            },
            {
                "name": "Gyros / Souvlaki",
                "desc": "Tavuk (Kotopoulo) olsa dahi domuz döneriyle aynı ızgarada pişebilir veya soslarında gluten bulunabilir."
            },
            {
                "name": "Kavala Kurabiyesi (Kourabiedes)",
                "desc": "Geleneksel Kavala kurabiyelerinde bazen domuz yağı (lard) kullanılabilir ('Me voutyro galaktos, horis hoirino lipos' teyit edilmeli). Buğday unu içerdiği için eşiniz kesinlikle tüketmemelidir."
            }
        ]
    },
    "dailyItinerary": [
        {
            "day": 1,
            "date": "2026-10-24",
            "weekday": "Cumartesi",
            "title": "İstanbul – İpsala – Kavala",
            "start": "İstanbul",
            "end": "Kavala",
            "overnight": "Kavala",
            "hotel": {
                "name": "Atlas Boutique Suites",
                "reservationCode": "6917068317",
                "location": "Karanou 1, Kavala",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Atlas+Boutique+Suites+Kavala&query_place_id=ChIJaw0ige67rhQRDajTgxkIakM"
            },
            "estimatedDistanceKm": {
                "min": 440,
                "max": 460,
                "exact": 450
            },
            "estimatedDrivingHoursIncludingNormalBorders": {
                "min": 5.5,
                "max": 6.5
            },
            "criticalAlert": "Kavalalı Mehmet Ali Paşa Evi Müzesi Cumartesi günleri saat 14:30'da kapanmaktadır. Kavala'ya varır varmaz aracınızı limana park edip ilk iş olarak yarımadanın ucundaki müzeye yürüyün!",
            "parking": [
                {
                    "title": "Πάρκινγκ Τελωνείου (Gümrük/Liman Otoparkı)",
                    "type": "Ana Öneri",
                    "description": "Dar sokaklara hiç girmeden sahil yolundan doğrudan girilen, 24 saat açık, düz ayak güvenli otopark. Otelinize ve Eski Şehir girişine 5 dk yürüme mesafesinde.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Parking+Teloneiou+Kavala&query_place_id=ChIJbQpGQAC7rhQRmvMbtsMH1dc"
                },
                {
                    "title": "Liman Ücretsiz Otopark Alanı",
                    "type": "Alternatif",
                    "description": "Liman sahasında açık ücretsiz park alanı.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Free+Parking+Kavala&query_place_id=ChIJrZ_1_Qe7rhQRphd5tu4RJVg"
                }
            ],
            "timeBlocks": [
                {
                    "startTime": "06:30",
                    "endTime": "10:00",
                    "activity": "İstanbul'dan hareket, Tekirdağ ve Keşan üzerinden İpsala Sınır Kapısı'na varış"
                },
                {
                    "startTime": "10:00",
                    "endTime": "11:30",
                    "activity": "İpsala / Kipi sınır geçişi, pasaport, gümrük ve yeşil sigorta kontrolleri"
                },
                {
                    "startTime": "11:30",
                    "endTime": "12:45",
                    "activity": "A2 (Egnatia Odos) otoyolu üzerinden Dedeağaç ve Gümülcine'yi geçerek Kavala'ya varış"
                },
                {
                    "startTime": "12:45",
                    "endTime": "13:15",
                    "activity": "Atlas Boutique Suites'e varış, aracın Liman Otoparkı'na (Parking Teloneiou) bırakılması",
                    "historyInfo": "Liman otoparkı Panagia yarımadasının tam eteğinde yer alır; aracınızı güvenle bırakıp yürüyüşe başlayabilirsiniz."
                },
                {
                    "startTime": "13:15",
                    "endTime": "14:15",
                    "activity": "Kavalalı Mehmet Ali Paşa Evi ve Heykeli (Panagia)",
                    "historyInfo": "1769'da Kavala'da doğan ve Mısır Valisi olarak Osmanlı tarihinde derin izler bırakan Kavalalı Mehmet Ali Paşa'nın doğduğu konaktır (18. yüzyıl). Döneminin en zengin sivil Osmanlı mimarisi örneklerinden biri olan yapı, haremlik ve selamlık bölümleri ile denize nazır muazzam bir avluya sahiptir. Önündeki bronz atlı heykel 1934 yılında Mısır halkının hediyesi olarak dikilmiştir."
                },
                {
                    "startTime": "14:15",
                    "endTime": "15:15",
                    "activity": "İmarethane (İmaret) & Halil Bey Külliyesi",
                    "historyInfo": "Mehmet Ali Paşa Evi'nden yokuş aşağı inerken sağda yer alan İmarethane, 1817–1821 yılları arasında Mehmet Ali Paşa tarafından memleketine vakıf olarak yaptırılmış; içerisinde iki medrese, iki mescit, aşevi ve mektep barındıran 18 kubbeli devasa bir Osmanlı külliyesidir. Hemen üst sokağındaki Halil Bey Camii ve Medresesi (Παλαιά Μουσική) ise 16. yüzyıl yapısı olup, caminin tabanındaki cam bölmeden altında yer alan erken Hristiyanlık bazilikası kalıntıları görülür."
                },
                {
                    "startTime": "15:30",
                    "endTime": "16:30",
                    "activity": "Kavala Su Kemeri (Kamares)",
                    "historyInfo": "Yarımadadan şehir düzlüğüne indiğinizde tam karşınıza çıkan 270 metre uzunluğundaki ve 25 metre yüksekliğindeki çift katlı kemer, Roma ve Bizans temelleri üzerine 1530 yılında Kanuni Sultan Süleyman tarafından onartılıp yükseltilerek Panagia yarımadasına su taşımak amacıyla inşa edilmiştir."
                },
                {
                    "startTime": "18:00",
                    "endTime": "20:30",
                    "activity": "Kavala limanında akşam yürüyüşü ve Savvas Seafood Restaurant'ta akşam yemeği"
                }
            ],
            "attractions": [
                "Kavalalı Mehmet Ali Paşa Evi ve Heykeli",
                "İmarethane (İmaret)",
                "Halil Bey Camii ve Külliyesi",
                "Kavala Su Kemeri (Kamares)",
                "Panagia Tarihi Yarımadası",
                "Kavala Limanı ve Kordon Boyu"
            ],
            "roadSequence": [
                "İstanbul",
                "Keşan",
                "İpsala Sınır Kapısı",
                "Kipi",
                "Dedeağaç (Alexandroupoli)",
                "Gümülcine (Komotini)",
                "Kavala"
            ],
            "routeNotes": [
                "İpsala Sınır Kapısı'na girmeden hemen önce Türkiye tarafında deponuzu tamamen doldurun (Yunanistan'da benzin daha pahalıdır).",
                "Yeşil Sigorta (Green Card), yeni tip çipli ehliyet ve ruhsatı torpido gözünde hazır bulundurun.",
                "Kavala içinde araba kullanmayın; yollar çok dar ve dik yokuşludur. Liman otoparkına park edip yürümek en konforlu yoldur."
            ],
            "mealPlan": [
                {
                    "mealType": "Akşam yemeği",
                    "timeRange": "18:30-20:30",
                    "location": "Kavala Limanı",
                    "strategy": "Taze ızgara deniz ürünleri ve zeytinyağlı güvenli akşam yemeği",
                    "recommendedFoods": [
                        "Psari Skaras (Izgara taze balık)",
                        "Htapodi Skaras (Izgara ahtapot)",
                        "Horiatiki (Yunan salatası - peksimetsiz)",
                        "Fava"
                    ],
                    "primaryOption": {
                        "venueName": "Savvas Seafood Restaurant",
                        "type": "Liman Deniz Ürünleri Restoranı",
                        "verificationStatus": "Verified",
                        "reason": "Liman sonunda marina manzaralı, taze ızgara balık ve ahtapotuyla ünlü, çölyak bilinci yüksek nezih restoran.",
                        "phone": "+30 251 022 4192",
                        "mapUrl": "https://www.google.com/maps/search/?api=1&query=Savvas+Kavala&query_place_id=ChIJofdIEWG7rhQRLZmr6bCsNwc"
                    },
                    "dietaryWarnings": [
                        "Garsona mutlaka SOS kartını gösterin ve balığın sadece ızgara (Skaras) olup una bulanmadığını teyit edin.",
                        "Kavala Kurabiyesi (Kourabiedes): Domuz yağı içermeyen 'Me voutyro galaktos' olanı tercih edilmeli; buğday unu içerdiğinden çölyaklı eş kesinlikle yememelidir."
                    ],
                    "sourceUrls": [
                        "https://www.google.com/maps/search/?api=1&query=Savvas+Kavala&query_place_id=ChIJofdIEWG7rhQRLZmr6bCsNwc"
                    ]
                }
            ],
            "dailyPaymentNotes": {
                "currenciesNeeded": ["EUR"],
                "cashRecommended": True,
                "expectedPayments": [
                    "A2 Otoyol gişe ücretleri (yaklaşık 4–6 €)",
                    "Liman otopark ücreti",
                    "Mehmet Ali Paşa Evi müze girişi",
                    "Akşam yemeği (kredi kartı geçer)"
                ],
                "warnings": [
                    "Otoyol gişelerinde kredi kartı temassız çalışır ancak hızlı geçiş için yanınızda 1–2 Euro bozukluk bulundurmak pratiktir."
                ]
            },
            "mapUrl": "https://www.google.com/maps/dir/%C4%B0stanbul,+T%C3%BCrkiye/%C4%B0psala+S%C4%B1n%C4%B1r+Kap%C4%B1s%C4%B1,+K%C3%B6pr%C3%BC,+%C4%B0psala%2FEdirne,+T%C3%BCrkiye/Atlas+Boutique+Suites,+%CE%9A%CE%B1%CF%81%CE%AC%CE%BD%CE%BF%CF%85+1,+%CE%9A%CE%B1%CE%B2%CE%AC%CE%BB%CE%B1,+%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1"
        },
        {
            "day": 2,
            "date": "2026-10-25",
            "weekday": "Pazar",
            "title": "Kavala – Selanik (Metro Turu) – Perea",
            "start": "Kavala",
            "end": "Perea",
            "overnight": "Perea",
            "hotel": {
                "name": "Atlantis ''Pleasure by the Sea''",
                "reservationCode": "6741250915",
                "location": "Pavlou Kountouriotou 51, Perea",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Atlantis+Pleasure+By+The+Sea+Perea&query_place_id=ChIJv7lV5ewVqBQRp1rKJ-32kgw"
            },
            "estimatedDistanceKm": {
                "min": 170,
                "max": 185,
                "exact": 175
            },
            "estimatedDrivingHoursIncludingNormalBorders": {
                "min": 2.0,
                "max": 2.5
            },
            "criticalAlert": "Selanik şehir merkezine aracınızla kesinlikle girmeyin. Çevre yolundan önce tepedeki Ano Poli (Yedikule) kalesine uğrayın, ardından Nea Elvetia Metro İstasyonu otoparkına aracınızı bırakıp merkeze metroyla inin. Yürüyüş Sintrivani'den başlayıp yokuş aşağı akacak ve Venizelou durağından metroyla otoparka dönülecektir.",
            "parking": [
                {
                    "title": "(μ) Metro Station 'Nea Elvetia' (Park & Ride)",
                    "type": "Ana Park & Ride",
                    "description": "Ana metro hattının doğu başlangıç istasyonu ve 650 araçlık modern otopark alanı. Aracınızı buraya bırakıp metroya binin.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Metro+Station+Nea+Elvetia+Thessaloniki&query_place_id=ChIJ99sJPwA5qBQRm18YA2tev9c"
                },
                {
                    "title": "Sintrivani Metro İstasyonu (İniş Durağı)",
                    "type": "Metro İniş",
                    "description": "Atatürk Evi'ne 7 dakika yürüme mesafesinde olan iniş durağınız.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Sintrivani+Metro+Thessaloniki&query_place_id=ChIJlYF4z_84qBQRCBbDsGE5U0w"
                },
                {
                    "title": "Venizelou Metro İstasyonu (Antik Müze - Dönüş Durağı)",
                    "type": "Metro Dönüş",
                    "description": "Aristotelous Meydanı'nın yukarısında, 1.600 yıllık Roma caddesini sergileyen metro istasyonu ve araca dönüş noktası.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Venizelou+Metro+Thessaloniki&query_place_id=ChIJC2532Kc5qBQRKQxVlUy42Uw"
                }
            ],
            "timeBlocks": [
                {
                    "startTime": "08:30",
                    "endTime": "10:15",
                    "activity": "Kavala'dan çıkış, A2 otoyolu ile Selanik çevre yoluna varış"
                },
                {
                    "startTime": "10:15",
                    "endTime": "11:15",
                    "activity": "Ano Poli (Yukarı Şehir) & Yedikule (Heptapyrgion / Επταπύργιο)",
                    "historyInfo": "1917 Büyük Selanik Yangını'ndan kurtulan tek tarihi Osmanlı-Bizans mahallesi olan Ano Poli'nin zirvesinde yer alır. Bizans döneminde akropol kalesi olarak inşa edilmiş, 1430'da II. Murad tarafından Selanik'in fethinden sonra İstanbul'daki Yedikule örnek alınarak 7 kuleli bir Osmanlı garnizonuna dönüştürülmüştür."
                },
                {
                    "startTime": "11:15",
                    "endTime": "11:45",
                    "activity": "Çevre yolundan Nea Elvetia Metro İstasyonu otoparkına geçiş ve metroya biniş",
                    "historyInfo": "Selanik şehir merkezinin dar sokakları ve yoğun trafiği bypass edilerek Sintrivani durağına hızlı ve konforlu ulaşım."
                },
                {
                    "startTime": "12:00",
                    "endTime": "13:00",
                    "activity": "Mustafa Kemal Atatürk Evi Müzesi (Sintrivani Metrodan 7 Dk Yürüyüş)",
                    "historyInfo": "1870 yılında Rodoslu Hacı Mehmet Vakfı tarafından inşa edilen üç katlı pembe köşk, Ali Rıza Efendi ve Zübeyde Hanım tarafından kiralanmış ve Gazi Mustafa Kemal Atatürk 1881 yılında bu evin ikinci katındaki ocaklı odada dünyaya gelmiştir. Türkiye Cumhuriyeti Selanik Başkonsolosluğu yerleşkesi içindedir ve giriş ücretsizdir."
                },
                {
                    "startTime": "13:10",
                    "endTime": "14:15",
                    "activity": "Galerius Rotundası ve Galerius Kemeri (Kamara)",
                    "historyInfo": "Atatürk Evi'nden yokuş aşağı 6 dakika yürüyüşle ulaşılan Rotunda, MS 306 yılında Roma İmparatoru Galerius tarafından anıt mezar veya Zeus tapınağı olarak Roma'daki Pantheon'a benzer biçimde (6,3 m duvar kalınlığıyla) inşa edilmiştir. 1590'da Sultan Hortacî Süleyman Efendi Camii'ne çevrilmiş olup bahçesindeki minare Selanik'te ayakta kalan tek Osmanlı minaresidir. Kemeri (Kamara) ise Sasanilere karşı zaferi anlatan mermer kabartmalarla bezelidir."
                },
                {
                    "startTime": "14:30",
                    "endTime": "15:45",
                    "activity": "Beyaz Kule (Λευκός Πύργος / Lefkos Pyrgos)",
                    "historyInfo": "Kemerden sahile doğru inildiğinde karşılayan 34 metre yüksekliğindeki silindirik kule, 1535 yılında Kanuni Sultan Süleyman döneminde Osmanlı liman savunmasının doğu burcu olarak (Mimar Sinan ekolüyle) inşa edilmiştir. Osmanlı döneminde 'Kanlı Kule' olarak anılan yapı, 1890'da beyaza boyanmasından sonra Beyaz Kule adını almıştır."
                },
                {
                    "startTime": "16:00",
                    "endTime": "18:00",
                    "activity": "Aristotelous Meydanı & Venizelou Metro Açık Hava Müzesi",
                    "historyInfo": "Beyaz Kule'den kordon boyu yürünerek ulaşılan Aristotelous Meydanı, 1917 yangınından sonra Ernest Hébrard tarafından Bizans ve Neoklasik senteziyle tasarlanmıştır. Meydanın üstündeki Venizelou Metro İstasyonu ise metro kazılarında ortaya çıkarılan 1.600 yıllık Roma mermer ana caddesini (Decumanus Maximus) yerinde koruyan eşsiz bir açık hava müzesidir."
                },
                {
                    "startTime": "18:00",
                    "endTime": "19:00",
                    "activity": "Venizelou'dan metro ile Nea Elvetia'ya dönüş, aracı alıp Perea sahilindeki Atlantis Hotel'e geçiş"
                }
            ],
            "attractions": [
                "Ano Poli (Tarihi Yukarı Şehir)",
                "Heptapyrgion (Yedikule Kalesi)",
                "Mustafa Kemal Atatürk Evi Müzesi",
                "Galerius Rotundası (Sultan Hortacı Camii)",
                "Galerius Zafer Kemeri (Kamara)",
                "Beyaz Kule (Lefkos Pyrgos)",
                "Nikis Sahil Kordonu",
                "Aristotelous Meydanı",
                "Venizelou Metro Arkeoloji Müzesi (Decumanus Maximus)"
            ],
            "roadSequence": [
                "Kavala",
                "A2 Egnatia Odos",
                "Selanik Çevre Yolu",
                "Ano Poli",
                "Nea Elvetia Metro",
                "Perea Sahili"
            ],
            "routeNotes": [
                "Ano Poli tepe bir mahalledir; kaleye çıkış yolu geniştir ancak kaleden sonra şehir merkezine inen dik sokaklara girmeyip çevre yolundan Nea Elvetia metrosuna geçilmelidir.",
                "Selanik metrosunda bilet otomatları temassız kredi kartı ve nakit kabul etmektedir.",
                "Perea, Selanik havalimanı ve sahil aksında huzurlu bir sayfiye kasabasıdır; otelinizin hemen önünde sahil yürüyüş yolu vardır."
            ],
            "mealPlan": [
                {
                    "mealType": "Öğle yemeği",
                    "timeRange": "13:30-15:00",
                    "location": "Selanik Merkez (Aristotelous / Kordon)",
                    "strategy": "Merkezde güvenli glutensiz deniz ürünleri veya glutensiz pizza",
                    "recommendedFoods": [
                        "Psari Skaras (Taze ızgara balık)",
                        "Deniz mahsullü glutensiz tabaklar",
                        "Glutensiz pizza"
                    ],
                    "primaryOption": {
                        "venueName": "7 Thalasses",
                        "type": "Prestijli Deniz Ürünleri Restoranı",
                        "verificationStatus": "Verified",
                        "reason": "Aristotelous Meydanı'na yürüme mesafesinde, Selanik'in en seçkin deniz ürünleri restoranı. Çölyak konusunda eğitimli mutfağı ve taze balıklarıyla en güvenli öğle yemeği adresi.",
                        "mapUrl": "https://www.google.com/maps/search/?api=1&query=7+Thalasses+Thessaloniki&query_place_id=ChIJQ1mkAwk5qBQRZ2YDo3HUhJQ"
                    },
                    "alternativeOptions": [
                        {
                            "venueName": "Basilico",
                            "type": "Sahil Kordonu - Nikis Bulvarı",
                            "verificationStatus": "Verified",
                            "reason": "Beyaz Kule ile Aristotelous arasında sahil kordonunda özel glutensiz pizza ve deniz ürünlü makarna alternatifleri sunar.",
                            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Basilico+Thessaloniki&query_place_id=ChIJK1zTLAQ5qBQR8b-rPi8co3M"
                        }
                    ]
                },
                {
                    "mealType": "Akşam yemeği",
                    "timeRange": "19:30-21:30",
                    "location": "Perea Sahili veya Kalamaria",
                    "strategy": "Sahilde taze balık tavernası veya çölyak odaklı Akdeniz mutfağı",
                    "recommendedFoods": [
                        "Izgara ahtapot",
                        "Çipura / levrek ızgara",
                        "Mantar ve sebze tabakları"
                    ],
                    "primaryOption": {
                        "venueName": "To Manitari",
                        "type": "Akdeniz & Çölyak Dostu Restoran (Kalamaria)",
                        "verificationStatus": "Verified",
                        "reason": "Perea yolunda Kalamaria mevkiinde, Selanik'te çölyak hastalarının 1 numaralı favorisi olan gurme Akdeniz restoranı.",
                        "mapUrl": "https://www.google.com/maps/search/?api=1&query=To+Manitari+Thessaloniki&query_place_id=ChIJ4YlzWdQ-qBQRu1cFq0ey4rg"
                    },
                    "alternativeOptions": [
                        {
                            "venueName": "Taverna Thalassopoulia",
                            "type": "Perea Sahili Taverna",
                            "verificationStatus": "Verified",
                            "reason": "Perea'daki otelinizle aynı cadde üzerinde (No: 51), denize sıfır taze balık tavernası; yürüme mesafesindedir.",
                            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Taverna+Thalassopoulia+Perea&query_place_id=ChIJ58tmIukVqBQRsaCsDIMrUXs"
                        }
                    ]
                }
            ],
            "dailyPaymentNotes": {
                "currenciesNeeded": ["EUR"],
                "cashRecommended": False,
                "expectedPayments": [
                    "A2 gişeleri (yaklaşık 2–4 €)",
                    "Nea Elvetia metro otoparkı & metro biletleri (kişi başı ~0.90–1.20 €)",
                    "Yeme içme (kart geçer)"
                ],
                "warnings": [
                    "Selanik metrosunda temassız kredi kartı doğrudan turnikelerde de kullanılabilmektedir."
                ]
            },
            "mapUrl": "https://www.google.com/maps/dir/Atlas+Boutique+Suites,+%CE%9A%CE%B1%CF%81%CE%AC%CE%BD%CE%BF%CF%85+1,+%CE%9A%CE%B1%CE%B2%CE%AC%CE%BB%CE%B1,+%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1/(%CE%BC)+Metro+Station+%22Nea+Elvetia%22,+Michail+Psellou,+Thessaloniki,+Greece/Atlantis+''pleasure+By+The+Sea'',+Pavlou+Kountouriotou+51,+Perea,+Yunanistan"
        },
        {
            "day": 3,
            "date": "2026-10-26",
            "weekday": "Pazartesi",
            "title": "Perea – Afytos (Halkidiki) – Perea",
            "start": "Perea",
            "end": "Perea",
            "overnight": "Perea",
            "hotel": {
                "name": "Atlantis ''Pleasure by the Sea''",
                "reservationCode": "6741250915",
                "location": "Pavlou Kountouriotou 51, Perea",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Atlantis+Pleasure+By+The+Sea+Perea&query_place_id=ChIJv7lV5ewVqBQRp1rKJ-32kgw"
            },
            "estimatedDistanceKm": {
                "min": 140,
                "max": 160,
                "exact": 150
            },
            "estimatedDrivingHoursIncludingNormalBorders": {
                "min": 1.5,
                "max": 2.0
            },
            "criticalAlert": "Foodie's Art Gluten Free Bakery Selanik'te Pazartesi günleri 08:30–13:00 arası açıktır (Pazar kapalıdır). Sabah Afytos'a geçmeden önce eşiniz için glutensiz bougatsa, ekmek ve atıştırmalık stoklamak için mükemmel fırsattır!",
            "parking": [
                {
                    "title": "Free Parking 1 Afytos",
                    "type": "Ana Ücretsiz Otopark",
                    "description": "Afytos taş sokaklarına araçla girilmez; köyün hemen girişindeki geniş ve düz ücretsiz otoparka bırakıp köye yürüyün.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Free+Parking+1+Afytos&query_place_id=ChIJxUz6KgArphQRvB6CX4_D8Bg"
                }
            ],
            "timeBlocks": [
                {
                    "startTime": "08:45",
                    "endTime": "09:45",
                    "activity": "Foodie's Art Gluten Free Bakery Ziyareti",
                    "historyInfo": "Selanik'te çölyak sertifikalı %100 glutensiz fırın. Eşiniz için geleneksel Yunan böreği (bougatsa), taze glutensiz ekmek ve kurabiye stoğu temin edilir."
                },
                {
                    "startTime": "09:45",
                    "endTime": "10:45",
                    "activity": "A24 bölünmüş otoyolu üzerinden Kassandra yarımadasına konforlu sürüş ve Afytos'a varış"
                },
                {
                    "startTime": "10:45",
                    "endTime": "16:00",
                    "activity": "Afytos Taş Meydanı, Folklor Müzesi (Aletras Konağı) ve Falez Yürüyüşü",
                    "historyInfo": "MÖ 3000'den beri yerleşim gören antik Aphytis kenti üzerine kurulu olan Afytos, Aristo'nun da yazılarında bahsettiği zengin bir Makedon limanıydı. Köyün tamamı yerel gözenekli kireçtaşından (porolithos) inşa edilmiş 19. yüzyıl taş konaklarından oluşur. Meydandaki 1859 tarihli Agios Dimitrios Kilisesi ve 1889 yapımı Aletras Konağı mimarisiyle dikkat çeker. Köyün deniz tarafındaki sarp kayalık yürüyüş yolu ('Vrachos'), Ege Denizi'ni ve Toroneos Körfezi'ni kuşbakışı izleyen doğal terastır."
                },
                {
                    "startTime": "16:00",
                    "endTime": "17:00",
                    "activity": "Afytos'tan Perea'ya dönüş, sahilde dinlenme ve otel çevresinde akşam programı"
                }
            ],
            "attractions": [
                "Foodie's Art Gluten Free Bakery",
                "Afytos Tarihi Taş Köyü",
                "Agios Dimitrios Kilisesi (1859)",
                "Afytos Folklor Müzesi (Aletras Konağı)",
                "Vrachos Falez Yürüyüş Yolu (Halkidiki'nin Balkonu)",
                "Kassandra Sahil Manzaraları"
            ],
            "roadSequence": [
                "Perea",
                "Selanik Doğu Aksı",
                "A24 Otoyolu",
                "Nea Moudania",
                "Kassandra Köprüsü",
                "Afytos",
                "Perea"
            ],
            "routeNotes": [
                "Perea'da konakladığınız için Selanik şehir merkezine girmeden A24 otoyoluna direkt bağlanırsınız.",
                "A24 otoyolu bölünmüş ve ücretsizdir (gişe bulunmaz).",
                "Afytos sokakları Arnavut kaldırımı taştır; rahat yürüyüş ayakkabısı giyilmesi önerilir."
            ],
            "mealPlan": [
                {
                    "mealType": "Öğle yemeği / Kafe",
                    "timeRange": "12:30-14:30",
                    "location": "Afytos Falezleri",
                    "strategy": "Uçurum kenarında muazzam deniz manzaralı ızgara deniz ürünleri",
                    "recommendedFoods": [
                        "Izgara çipura / levrek",
                        "Ladolemono soslu ahtapot",
                        "Yunan salatası (ekmeksiz)"
                    ],
                    "primaryOption": {
                        "venueName": "Thea Thalassa",
                        "type": "Falez Restoranı",
                        "verificationStatus": "Verified",
                        "reason": "Afytos'un ünlü falezleri üzerinde, Toroneos Körfezi'ne tepeden bakan, taze balık ve ahtapot servisi sunan manzaralı restoran.",
                        "mapUrl": "https://www.google.com/maps/search/?api=1&query=Thea+Thalassa+Afytos&query_place_id=ChIJHdf333sqphQRhgFyGidQpdc"
                    }
                }
            ],
            "dailyPaymentNotes": {
                "currenciesNeeded": ["EUR"],
                "cashRecommended": False,
                "expectedPayments": [
                    "Fırın alışverişi (kart geçer)",
                    "Folklor müzesi girişi (sembolik ~2–3 € nakit)",
                    "Öğle yemeği (kart geçer)"
                ],
                "warnings": [
                    "A24 otoyolunda gişe ücreti yoktur."
                ]
            },
            "mapUrl": "https://www.google.com/maps/dir/Atlantis+''pleasure+By+The+Sea'',+Pavlou+Kountouriotou+51,+Perea,+Yunanistan/Foodies+Art+Gluten+Free+Bakery,+Thessaloniki/Free+Parking+1+Afytos,+4C3M%2B76,+Kassandra,+Greece/Atlantis+''pleasure+By+The+Sea'',+Pavlou+Kountouriotou+51,+Perea,+Yunanistan"
        },
        {
            "day": 4,
            "date": "2026-10-27",
            "weekday": "Salı",
            "title": "Perea – Vergina (Aigai) – Kalambaka (Meteora)",
            "start": "Perea",
            "end": "Kalambaka",
            "overnight": "Kalambaka",
            "hotel": {
                "name": "Hotel Kaikis",
                "reservationCode": "5738903346",
                "location": "Trikalon 146, Kalampaka",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hotel+Kaikis+Kalambaka&query_place_id=ChIJM0O5fsgPWRMRdonAkG5b5-A"
            },
            "estimatedDistanceKm": {
                "min": 240,
                "max": 260,
                "exact": 250
            },
            "estimatedDrivingHoursIncludingNormalBorders": {
                "min": 3.0,
                "max": 3.5
            },
            "criticalAlert": "27 Ekim Salı günü Vergina Kraliyet Mezarları Müzesi saat 12:00'de açılır (Perea'dan 10:00'da çıkış tam açılış saatinde kapıda olmanızı sağlar). Meteora'da ise en büyük manastır olan Büyük Meteoron Salı günleri kapalıdır; bu nedenle öğleden sonra açık olan Varlaam (16:00'ya kadar) ve Roussanou (16:30'a kadar) manastırlarını gezeceğiz.",
            "parking": [
                {
                    "title": "Aigai Kraliyet Mezarları Müzesi Otoparkı",
                    "type": "Müze Otoparkı",
                    "description": "Müze girişinde düz, geniş ve ücretsiz açık otopark alanı mevcuttur.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Museum+of+the+Royal+Tombs+of+Aigai&query_place_id=ChIJKStsygjyVxMRtxRoIGBCgJI"
                },
                {
                    "title": "Meteora Manastır Otoparkları (Varlaam & Roussanou)",
                    "type": "Manastır Cepleri",
                    "description": "Dağ yolu geniş ve yeni asfalttır. Varlaam ve Roussanou manastırlarının kapı önlerinde ücretsiz park cepleri bulunmaktadır.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Monastery+of+Varlaam+Meteora&query_place_id=ChIJmUP3fK8PWRMRyF8qX4Npg9Q"
                }
            ],
            "timeBlocks": [
                {
                    "startTime": "10:00",
                    "endTime": "11:45",
                    "activity": "Perea'dan hareket, A1 ve A2 otoyolları üzerinden Vergina'ya sürüş"
                },
                {
                    "startTime": "12:00",
                    "endTime": "13:30",
                    "activity": "Vergina (Aigai) Kraliyet Mezarları Müzesi",
                    "historyInfo": "UNESCO Dünya Mirası Listesi'nde yer alan Aigai, Antik Makedonya Krallığı'nın ilk başkentiydi. 1977 yılında arkeolog Manolis Andronikos tarafından keşfedilen dev toprak tümülüsün altında, Büyük İskender'in babası Kral II. Filip'in (MÖ 336) hiç soyulmamış anıt mezarı ve IV. İskender'in mezarı bulunmuştur. Müze bizzat yer altı mezarlarının içine inşa edilmiştir; II. Filip'in saf altından meşe yapraklı kraliyet çelengi ve 16 ışınlı Vergina Güneşi işlemeli altın kemik kutusu (larnaks) dünya arkeoloji tarihinin en büyük şaheserlerindendir."
                },
                {
                    "startTime": "13:30",
                    "endTime": "15:00",
                    "activity": "A2 Egnatia Odos üzerinden Grevena dağ geçişi ile Kalambaka'ya varış (yeni otoyol)"
                },
                {
                    "startTime": "15:15",
                    "endTime": "16:45",
                    "activity": "Meteora: Varlaam Manastırı & Roussanou Manastırı Gezisi",
                    "historyInfo": "60 milyon yıl önce iç denizin çekilmesiyle oluşan 400 metrelik devasa kumtaşı sütunların tepesine, 14. yüzyılda inzivaya çekilen keşişler tarafından manastırlar inşa edilmiştir. 1517'de kurulan Varlaam Manastırı'na yüzyıllarca sadece 373 metrelik uçurumdan sarkıtılan ağlar ve halat merdivenlerle çıkılabilmiştir; içerisindeki eski halat vinç kulesi ve 1548 tarihli Bizans freskleri bugün hala görülebilir. Roussanou Manastırı ise daracık kaya sütununun zirvesine oturtulmuş en fotojenik yapıdır."
                },
                {
                    "startTime": "16:45",
                    "endTime": "17:30",
                    "activity": "Büyük Meteoron Manastırı dış seyir ve panoramik kayalık fotoğraf molası"
                },
                {
                    "startTime": "18:00",
                    "endTime": "19:00",
                    "activity": "Kalambaka merkezindeki Hotel Kaikis'e yerleşme ve akşam yemeği hazırlığı"
                }
            ],
            "attractions": [
                "Vergina (Aigai) Kraliyet Mezarları Müzesi (Kral II. Filip Mezarı)",
                "Altın Larnaks ve Vergina Güneşi Çelengi",
                "Meteora Dev Kumtaşı Kayalıkları",
                "Varlaam Manastırı",
                "Roussanou Manastırı",
                "Büyük Meteoron (Dış Seyir Noktası)",
                "Kalambaka Kasaba Merkezi"
            ],
            "roadSequence": [
                "Perea",
                "A1 Otoyolu",
                "Veria",
                "Vergina (Aigai)",
                "A2 Otoyolu (Grevena)",
                "Kalambaka (Meteora)"
            ],
            "routeNotes": [
                "Vergina'dan Kalambaka'ya giderken dağ yollarına girmeyin; A2 Egnatia Odos üzerinden Grevena ayrımını takip eden bölünmüş otoyol en güvenli ve hızlı güzergahtır.",
                "Meteora manastırlarında diz ve omuzları örten kıyafet zorunluluğu vardır (girişte hanımlara şal/etek verilmektedir).",
                "Manastır giriş ücretleri kişi başı 3 €'dur ve nakit ödeme tercih edilir."
            ],
            "mealPlan": [
                {
                    "mealType": "Akşam yemeği",
                    "timeRange": "19:00-21:00",
                    "location": "Kalambaka (Meteora Kayalıkları Eteği)",
                    "strategy": "Geleneksel fırın kuzu, ızgara tavuk ve zeytinyağlı tencere yemekleri",
                    "recommendedFoods": [
                        "Fırında kuzu (Arni sto fourno)",
                        "Izgara tavuk şiş",
                        "Fava ve zeytinyağlı taze fasulye / sebzeler"
                    ],
                    "primaryOption": {
                        "venueName": "Yamas Taverna Restaurant",
                        "type": "Geleneksel Taverna",
                        "verificationStatus": "Verified",
                        "reason": "Meteora kayalıklarının tam altında, uluslararası çölyak rehberlerinde (Atly vb.) glutensiz seçenekleriyle öne çıkan aile tavernası. Fırında kuzu, ızgara tavuk ve zeytinyağlı sebze yemekleri mevcuttur.",
                        "mapUrl": "https://www.google.com/maps/search/?api=1&query=Yamas+Taverna+Kalambaka&query_place_id=ChIJV9cn9MwPWRMRwtel3BLde8M"
                    },
                    "alternativeOptions": [
                        {
                            "venueName": "Restaurant Meteora Gkertsou Family",
                            "type": "Tarihi Aile Restoranı",
                            "verificationStatus": "Verified",
                            "reason": "1925'ten beri hizmet veren tarihi aile restoranı; ayrı bir zeytinyağlı sebze/vegan menüsü ve taze et/tavuk yemekleri bulunur.",
                            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Restaurant+Meteora+Gkertsou+Family&query_place_id=ChIJZ-YdJcwPWRMRAIJBG8I77UI"
                        }
                    ]
                }
            ],
            "dailyPaymentNotes": {
                "currenciesNeeded": ["EUR"],
                "cashRecommended": True,
                "expectedPayments": [
                    "A2 gişe ücretleri (yaklaşık 3–5 €)",
                    "Vergina Kraliyet Mezarları girişi (~15 € kişi başı, kart geçer)",
                    "Meteora manastır girişleri (manastır başı 3 € nakit)",
                    "Akşam yemeği"
                ],
                "warnings": [
                    "Meteora manastır gişelerinde nakit para bulundurmak işlem süresini kısaltır."
                ]
            },
            "mapUrl": "https://www.google.com/maps/dir/Atlantis+''pleasure+By+The+Sea'',+Pavlou+Kountouriotou+51,+Perea,+Yunanistan/Aigai+Kraliyet+Mezarlar%C4%B1+M%C3%BCzesi,+Vergina,+Yunanistan/Hotel+Kaikis,+Trikalon+146,+Kalampaka,+Yunanistan"
        },
        {
            "day": 5,
            "date": "2026-10-28",
            "weekday": "Çarşamba",
            "title": "Kalambaka – Dion – İskeçe – Mandra (Ohi Günü)",
            "start": "Kalambaka",
            "end": "Mandra",
            "overnight": "Mandra (Avdira)",
            "hotel": {
                "name": "Petrinos Lofos",
                "reservationCode": "6266974331",
                "location": "Mandra, 67061 Avdira",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Petrinos+Lofos+Mandra&query_place_id=ChIJ149suc_WrRQRN1pR7S3R3qM"
            },
            "estimatedDistanceKm": {
                "min": 380,
                "max": 410,
                "exact": 395
            },
            "estimatedDrivingHoursIncludingNormalBorders": {
                "min": 4.0,
                "max": 4.5
            },
            "criticalAlert": "Kalambaka'dan Dion'a giderken Olimpos Dağı arkasındaki dar dağ yollarına girmeyin; Larissa üzerinden A1 otoyolunu kullanın. 28 Ekim 'Ohi Günü' (Yunanistan Ulusal Bayramı) olduğu için İskeçe'ye öğleden sonra (15:30 gibi) vardığınızda sabahki geçit törenleri bitmiş ve caddeler trafiğe açılmış olacaktır.",
            "parking": [
                {
                    "title": "Dion Arkeolojik Parkı Otoparkı",
                    "type": "Müze Otoparkı",
                    "description": "Girişinde ücretsiz, ferah açık otopark mevcuttur.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Archaeological+Site+of+Dion&query_place_id=ChIJa2hneLAFWBMRAjRX_zXWlYA"
                },
                {
                    "title": "Otopark Roloi (Saat Kulesi Yanı - İskeçe)",
                    "type": "Merkez Otopark",
                    "description": "Eski Şehir'in dar sokaklarına girmeden, Osmanlı Saat Kulesi'nin hemen yanında yer alan en merkezi ve güvenli otopark.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Otopark+Roloi+Xanthi&query_place_id=ChIJxzfLVjktrBQRGF3PzE2xdz0"
                }
            ],
            "timeBlocks": [
                {
                    "startTime": "08:15",
                    "endTime": "10:15",
                    "activity": "Kalambaka'dan hareket, Larissa üzerinden A1 otoyolu ile Dion'a varış"
                },
                {
                    "startTime": "10:15",
                    "endTime": "12:00",
                    "activity": "Dion Arkeolojik Parkı (Olimpos Dağı Etekleri)",
                    "historyInfo": "Yunan mitolojisinde 12 tanrının evi kabul edilen Olimpos Dağı'nın tam eteklerinde kurulu olan Dion, adını baş tanrı Zeus'tan ('Dios') alır ve Makedonların en kutsal dini merkeziydi. Büyük İskender, MÖ 334 yılında Asya seferine çıkmadan hemen önce ordusunu burada toplamış ve Zeus tapınağında 9 gün boyunca kurbanlar sunmuştur. Sulak ormanlık alanda İsis Tapınağı (su içinde yükselen sütunlar), antik tiyatro ve Roma hamamları düz bir yürüyüş parkuruyla gezilir."
                },
                {
                    "startTime": "12:00",
                    "endTime": "15:30",
                    "activity": "A1 ve A2 otoyolları üzerinden Selanik ve Kavala aksını geçerek İskeçe'ye (Xanthi) sürüş"
                },
                {
                    "startTime": "15:30",
                    "endTime": "18:30",
                    "activity": "İskeçe (Xanthi) Eski Şehir (Palaia Poli) & Osmanlı Saat Kulesi Yürüyüşü",
                    "historyInfo": "'Binbir Rengin Şehri' olarak anılan İskeçe, 18. ve 19. yüzyıllarda Osmanlı İmparatorluğu'nun en değerli tütün üretim merkeziydi ('Yenice tütünü'). 1829 depreminden sonra zengin tüccarlar tarafından yamaç boyunca inşa edilen 1.200'den fazla cumbalı ahşap ve neoklasik taş konak, Yunanistan'ın en iyi korunan tarihi dokularından biridir. Meydandaki Osmanlı Saat Kulesi ise 1859 yılında Hacı Emin Ağa tarafından yaptırılmıştır."
                },
                {
                    "startTime": "18:30",
                    "endTime": "19:00",
                    "activity": "İskeçe'den Mandra köyündeki Petrinos Lofos otele geçiş, yerleşme ve dinlenme"
                }
            ],
            "attractions": [
                "Dion Arkeolojik Parkı (Zeus & İsis Kutsal Alanları)",
                "Olimpos Dağı Panoraması",
                "İskeçe Eski Şehir (Palaia Poli)",
                "Hacı Emin Ağa Osmanlı Saat Kulesi (1859)",
                "Tarihi Tütün Tüccarları Konakları",
                "Mandra Taş Köyü Yerleşimi"
            ],
            "roadSequence": [
                "Kalambaka",
                "Larissa",
                "A1 Otoyolu",
                "Dion",
                "Katerini",
                "A2 Egnatia Odos",
                "Kavala Çevre Yolu",
                "İskeçe (Xanthi)",
                "Mandra (Avdira)"
            ],
            "routeNotes": [
                "Kalambaka'dan ayrılırken Larissa yönündeki düz otoyol bağlantısı tercih edilmelidir; GPS kestirme köy yolları önerirse uymayın.",
                "İskeçe'de Türkçe konuşan esnaf ve garsonlar oldukça yaygındır; sipariş verirken rahatça Türkçe iletişim kurabilirsiniz.",
                "Petrinos Lofos, Mandra mevkiinde huzurlu bir taş konaktır ve geniş otoparkı mevcuttur."
            ],
            "mealPlan": [
                {
                    "mealType": "Akşam yemeği",
                    "timeRange": "16:30-18:30",
                    "location": "İskeçe Eski Şehir",
                    "strategy": "Tarihi taş konakta kuzu / tavuk ızgara ve zeytinyağlı lezzetler",
                    "recommendedFoods": [
                        "Izgara kuzu pirzola",
                        "Izgara tavuk göğsü",
                        "Zeytinyağlı taze salata",
                        "Köz patlıcan"
                    ],
                    "primaryOption": {
                        "venueName": "Παλαιά Πόλις (Palaia Polis)",
                        "type": "Tarihi Konak Restoranı",
                        "verificationStatus": "Verified",
                        "reason": "İskeçe Eski Şehir'de tarihi taş konakta hizmet veren seçkin restoran. Garsona SOS kartı gösterilerek ızgara etler güvenle tüketilebilir; Türkçe bilen personel yaygındır.",
                        "mapUrl": "https://www.google.com/maps/search/?api=1&query=Palaia+Polis+Xanthi&query_place_id=ChIJVeig0zgtrBQRisNkdn1IB4c"
                    },
                    "alternativeOptions": [
                        {
                            "venueName": "Ελιά (Elia)",
                            "type": "Geleneksel Restoran",
                            "verificationStatus": "Verified",
                            "reason": "Eski Şehir girişinde yüksek puanlı zeytinyağlı ve et alternatifi.",
                            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Elia+Xanthi&query_place_id=ChIJjXc4a4MtrBQRaiTZRKMrG4I"
                        },
                        {
                            "venueName": "Αμάλθεια (Amaltheia)",
                            "type": "Geleneksel Meydan Lokantası",
                            "verificationStatus": "Verified",
                            "reason": "Eski Şehir ara sokaklarında samimi aile işletmesi.",
                            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Amaltheia+Xanthi&query_place_id=ChIJ2ZNJxjgtrBQRpKwWycUo5q8"
                        }
                    ]
                }
            ],
            "dailyPaymentNotes": {
                "currenciesNeeded": ["EUR"],
                "cashRecommended": True,
                "expectedPayments": [
                    "A1 & A2 otoyol gişeleri (toplam ~8–10 €)",
                    "Dion Arkeolojik Parkı girişi (~8 €)",
                    "Otopark Roloi ücreti (~3–4 €)",
                    "İskeçe akşam yemeği"
                ],
                "warnings": [
                    "28 Ekim resmi tatil olduğu için bankalar ve bazı devlet daireleri kapalıdır; otoyol gişeleri ve restoranlar normal hizmet verir."
                ]
            },
            "mapUrl": "https://www.google.com/maps/dir/Hotel+Kaikis,+Trikalon+146,+Kalampaka,+Yunanistan/Archaeological+Site+of+Dion,+Eparchiaki+Odos+Katerinis+-+Limena+Litochoriou+910,+Dion,+Greece/Petrinos+Lofos,+Mandra,+Mandra,+67061,+Avdira,+Greece"
        },
        {
            "day": 6,
            "date": "2026-10-29",
            "weekday": "Perşembe",
            "title": "Mandra – Porto Lagos – İpsala – İstanbul",
            "start": "Mandra",
            "end": "İstanbul",
            "overnight": "İstanbul (Ev)",
            "hotel": None,
            "estimatedDistanceKm": {
                "min": 460,
                "max": 490,
                "exact": 475
            },
            "estimatedDrivingHoursIncludingNormalBorders": {
                "min": 5.5,
                "max": 6.5
            },
            "criticalAlert": "Porto Lagos'ta göl üzerinde flamingoları fotoğrafladıktan sonra doğrudan A2 otoyoluna bağlanarak İpsala Sınır Kapısı'na yönelin. Sınır öncesi son Yunan otoyol gişelerinden sonra Kipi'de gümrük sahasına girilir.",
            "parking": [
                {
                    "title": "Porto Lagos Ahşap Köprü Başı Otoparkı",
                    "type": "Manastır Otoparkı",
                    "description": "Vistonida Gölü lagününe bağlanan ahşap köprünün hemen girişinde geniş, güvenli ve ücretsiz park alanı.",
                    "mapUrl": "https://www.google.com/maps/search/?api=1&query=Monastery+of+Saint+Nicholas+Porto+Lagos&query_place_id=ChIJnfy003TZrRQRGjYuof1qWkM"
                }
            ],
            "timeBlocks": [
                {
                    "startTime": "09:00",
                    "endTime": "09:45",
                    "activity": "Mandra'dan çıkış ve Vistonida Lagünü boyunca Porto Lagos'a sürüş"
                },
                {
                    "startTime": "09:45",
                    "endTime": "10:45",
                    "activity": "Porto Lagos – Aziz Nikolaos Manastırı (Ιερά Μονή Αγίου Νικολάου) & Flamingolar",
                    "historyInfo": "Vistonida Gölü ile Ege Denizi'nin birleştiği sığ lagün üzerinde yer alan iki küçük adacık üzerine kurulmuş ve karaya uzun ahşap yaya köprüleriyle bağlanmış eşsiz bir manastırdır. Efsaneye göre Osmanlı döneminde bölgede yaşayan bir bey, kızının hastalığının buradaki şifalı suyla iyileşmesi üzerine araziyi Aynoroz'daki (Athos Dağı) Vatopedi Manastırı'na vakfetmiştir. Ekim ayında göl çevresinde konaklayan pembe flamingoları ve pelikanları izlemek için muazzam bir doğa durağıdır."
                },
                {
                    "startTime": "10:45",
                    "endTime": "12:30",
                    "activity": "A2 Egnatia Odos ile Gümülcine ve Dedeağaç üzerinden Kipi / İpsala Sınır Kapısı'na varış"
                },
                {
                    "startTime": "12:30",
                    "endTime": "14:00",
                    "activity": "Kipi / İpsala sınır geçişi, pasaport, gümrük ve freeshop molası"
                },
                {
                    "startTime": "14:00",
                    "endTime": "17:30",
                    "activity": "Keşan ve Tekirdağ üzerinden İstanbul'a varış ve tur tamamlama"
                }
            ],
            "attractions": [
                "Vistonida Gölü ve Lagün Doğa Parkı",
                "Aziz Nikolaos Manastırı (Göl Üstü Ahşap Köprüler)",
                "Ekim Ayı Pembe Flamingo Kolonileri",
                "A2 Egnatia Odos Trakya Manzaraları",
                "İpsala Sınır Kapısı & Meriç Nehri Köprüsü"
            ],
            "roadSequence": [
                "Mandra",
                "Porto Lagos",
                "Gümülcine (Komotini)",
                "Dedeağaç (Alexandroupoli)",
                "Kipi",
                "İpsala Sınır Kapısı",
                "Keşan",
                "Tekirdağ",
                "İstanbul"
            ],
            "routeNotes": [
                "Porto Lagos'ta ahşap köprülerde yürürken göl esintisine karşı rüzgarlık bulundurmanız önerilir.",
                "İpsala sınırında gümrüksüz satış mağazasından (Duty Free) alışveriş yapacaksanız pasaportunuzu yanınızda bulundurun.",
                "Türkiye'ye giriş yaptıktan sonra Keşan veya Tekirdağ'da yemek molası verilebilir."
            ],
            "mealPlan": [
                {
                    "mealType": "Yol atıştırmalığı & Öğle yemeği",
                    "timeRange": "13:00-14:30",
                    "location": "İpsala / Keşan",
                    "strategy": "Sınır geçişi sonrası Türkiye tarafında rahat yemek",
                    "recommendedFoods": [
                        "Keşan satır et",
                        "Izgara köfte / tavuk",
                        "Mevsim salata"
                    ],
                    "primaryOption": {
                        "venueName": "Keşan veya Tekirdağ Dinlenme Tesisleri",
                        "type": "Yol Üstü Izgara Restoranı",
                        "verificationStatus": "Flexible",
                        "reason": "Sınırı geçtikten sonra Türkiye tarafında tamamen güvenli ve helal ızgara et seçenekleri."
                    }
                }
            ],
            "dailyPaymentNotes": {
                "currenciesNeeded": ["EUR", "TRY"],
                "cashRecommended": False,
                "expectedPayments": [
                    "A2 son gişe ödemesi (~2–3 €)",
                    "Duty Free alışverişi",
                    "Türkiye tarafı yakıt ve yol harcamaları"
                ],
                "warnings": [
                    "Yunanistan'da kalan bozuk Euro'larınızı gişelerde veya Duty Free'de değerlendirebilirsiniz."
                ]
            },
            "mapUrl": "https://www.google.com/maps/dir/Petrinos+Lofos,+Mandra,+Mandra,+67061,+Avdira,+Greece/%CE%99%CE%B5%CF%81%CE%AC+%CE%9C%CE%BF%CE%BD%CE%AE+%CE%91%CE%B3%CE%AF%CE%BF%CF%85+%CE%9D%CE%B9%CE%BA%CE%BF%CE%BB%CE%AC%CE%BF%CF%85,+Porto+Lagos,+Yunanistan/%C4%B0psala+S%C4%B1n%C4%B1r+Kap%C4%B1s%C4%B1,+K%C3%B6pr%C3%BC,+%C4%B0psala%2FEdirne,+T%C3%BCrkiye/%C4%B0stanbul,+T%C3%BCrkiye"
        }
    ],
    "borderCrossings": [
        {
            "sequence": 1,
            "date": "2026-10-24",
            "fromCountry": "Türkiye",
            "toCountry": "Yunanistan",
            "crossingNames": [
                "İpsala Sınır Kapısı",
                "Kipi Border Checkpoint"
            ],
            "notes": "Türkiye çıkışında araç tescil ve yeşil sigorta kontrolü yapılır. Yunanistan tarafında Schengen pasaport kontrolü ve araç bagaj kontrolü uygulanır. Sabah 09:30–10:30 arası varış kuyruk yoğunluğunu azaltır."
        },
        {
            "sequence": 2,
            "date": "2026-10-29",
            "fromCountry": "Yunanistan",
            "toCountry": "Türkiye",
            "crossingNames": [
                "Kipi Border Checkpoint",
                "İpsala Sınır Kapısı"
            ],
            "notes": "Yunanistan çıkışında pasaport çıkış damgası vurulur. Türkiye girişinde pasaport kontrolü, gümrük tescil ve duty-free geçişi yapılır."
        }
    ],
    "vehicleRequirements": {
        "vehicleType": "Şahsi Türk Plakalı Otomobil",
        "pickupLocation": "İstanbul (Şahsi Araç)",
        "returnLocation": "İstanbul (Şahsi Araç)",
        "requiredCrossBorderCountries": ["Yunanistan"],
        "importantNote": "İlk yurt dışı sürüşünüz olduğundan A2 (Egnatia Odos) ve A1 bölünmüş otoyolları tercih edilmiştir. Dağ yollarından ve Selanik şehir içi trafiğinden kaçınılmıştır.",
        "checksBeforeDeparture": [
            "Uluslararası Yeşilkart Sigortası (Green Card) geçerlilik tarihi kontrol edildi.",
            "Yeni tip çipli sürücü belgesi kontrol edildi (Eski tip ehliyetler yurt dışında geçmez).",
            "Araç ruhsatı aslı araçta ve araç sürücünün adına tescilli (Değilse noter onaylı yurt dışı vekaletnamesi şarttır).",
            "Araç periyodik bakımı, lastik hava basınçları ve silecek suları kontrol edildi.",
            "Yurt dışı çıkışından önce İpsala sınır kapısı öncesinde Türkiye tarafında tam depo yakıt alındı."
        ],
        "borderInspectionChecklist": [
            "Torpido gözünde ruhsat, yeşil sigorta ve kasko poliçesi hazır.",
            "Yurt dışı çıkış harç pulları online veya gişeden ödendi.",
            "Pasaportlar ve Schengen vizeleri sürücü ve yolcu için hazır.",
            "Araç içinde reflektör, ilk yardım çantası ve yangın tüpü mevcut."
        ]
    },
    "documentsChecklist": [
        "Pasaportlar (En az 6 ay geçerlilik süreli)",
        "Çok girişli (Multi) Schengen Vizesi",
        "Yeni Tip Çipli Türkiye Cumhuriyeti Sürücü Belgesi",
        "Araç Tescil Belgesi (Ruhsat Aslı)",
        "Yeşilkart (Green Card) Uluslararası Motorlu Taşıt Sigortası",
        "Yurt Dışı Çıkış Harç Pulu (Dijital veya fiziki makbuz)",
        "Seyahat Sağlık Sigortası poliçe çıktıları",
        "Otel Rezervasyon belgeleri ve rezervasyon kodları (Atlas, Atlantis, Kaikis, Petrinos Lofos)",
        "Çölyak & Helal Yunanca Garson SOS Kartı çıktısı veya telefonda ekran görüntüsü"
    ],
    "accommodationPlan": [
        {
            "checkIn": "2026-10-24",
            "checkOut": "2026-10-25",
            "nights": 1,
            "city": "Kavala",
            "hotelName": "Atlas Boutique Suites",
            "reservationCode": "6917068317",
            "recommendedAreas": ["Panagia Yarımadası Eteği", "Liman Caddesi"],
            "requirements": ["Sahil otoparkına yakınlık", "Düz ayak giriş", "Eski Şehir yürüme mesafesi"],
            "avoid": ["Panagia içi araçla dar sokaklara giriş"],
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Atlas+Boutique+Suites+Kavala&query_place_id=ChIJaw0ige67rhQRDajTgxkIakM"
        },
        {
            "checkIn": "2026-10-25",
            "checkOut": "2026-10-27",
            "nights": 2,
            "city": "Perea (Selanik Sahili)",
            "hotelName": "Atlantis ''Pleasure by the Sea''",
            "reservationCode": "6741250915",
            "recommendedAreas": ["Perea Sahil Kordonu"],
            "requirements": ["Ücretsiz otopark", "Şehir trafiğinden uzaklık", "A24 otoyolu bağlantısı", "Denize sıfır konum"],
            "avoid": ["Selanik merkez otelleri (park ve trafik kabusu)"],
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Atlantis+Pleasure+By+The+Sea+Perea&query_place_id=ChIJv7lV5ewVqBQRp1rKJ-32kgw"
        },
        {
            "checkIn": "2026-10-27",
            "checkOut": "2026-10-28",
            "nights": 1,
            "city": "Kalambaka (Meteora)",
            "hotelName": "Hotel Kaikis",
            "reservationCode": "5738903346",
            "recommendedAreas": ["Kalambaka Kasaba Merkezi", "Trikalon Caddesi"],
            "requirements": ["Otel otoparkı", "Meteora kayalıklarına 10 dk sürüş mesafesi", "Glutensiz restoranlara yakınlık"],
            "avoid": ["Kastraki içi aşırı dar yokuşlar"],
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Hotel+Kaikis+Kalambaka&query_place_id=ChIJM0O5fsgPWRMRdonAkG5b5-A"
        },
        {
            "checkIn": "2026-10-28",
            "checkOut": "2026-10-29",
            "nights": 1,
            "city": "Mandra (Avdira / İskeçe)",
            "hotelName": "Petrinos Lofos",
            "reservationCode": "6266974331",
            "recommendedAreas": ["Mandra Köyü", "Porto Lagos Yolu"],
            "requirements": ["Geniş açık otopark", "Tarihi taş konak atmosferi", "A2 otoyolu ve Porto Lagos'a yakınlık"],
            "avoid": ["İskeçe merkezi park yeri kısıtı"],
            "mapUrl": "https://www.google.com/maps/search/?api=1&query=Petrinos+Lofos+Mandra&query_place_id=ChIJ149suc_WrRQRN1pR7S3R3qM"
        }
    ],
    "foodGuide": {
        "preferencesToConfirm": {
            "porkAllowed": False,
            "porkRestriction": "Strict",
            "porkRestrictionNote": "Domuz eti, pastırması, jambonu veya domuz yağı içeren hiçbir gıda kesinlikle tüketilmeyecektir; dini gerekçelerle SOS kartında açıkça belirtilmiştir.",
            "alcoholInFoodAllowed": True,
            "alcoholInFoodNote": "Şarap ve sirke ile pişirilen balık sosları tüketilebilir; ancak una bulanmamış olması şarttır.",
            "seafoodPreferred": True,
            "seafoodPreferenceNote": "Taze ızgara balık, ızgara ahtapot, ızgara kalamar (unsuz) ve kabuklu deniz ürünleri birinci öncelikli tercihtir.",
            "celiacDiseaseStrict": True,
            "celiacDiseaseNote": "Eşi çölyak hastasıdır; buğday, un, arpa, çavdar ve ortak fritöz yağından kaynaklanan çapraz bulaşma kesinlikle önlenmelidir.",
            "targetMealBudgetPerPerson": "30–50 €",
            "budgetPolicy": "Deniz kenarı kaliteli balık restoranları ve geleneksel güvenli tavernalar tercih edilmiştir."
        },
        "verificationLegend": {
            "Verified": "Resmi menü, glütensiz seçenek ve adres doğrulanmıştır.",
            "VerifiedByTravelSource": "Güvenilir uluslararası çölyak toplulukları (Atly vb.) tarafından onaylanmıştır.",
            "Provisional": "Seçkin adrestir; sipariş öncesi SOS kartı gösterilmelidir.",
            "Flexible": "Esnek yerel yemek seçeneğidir."
        },
        "usefulDietaryPhrases": [
            {
                "language": "Yunanca",
                "phrase": "Horis glouteni (Χωρίς γλουτένη)",
                "meaning": "Glutensiz"
            },
            {
                "language": "Yunanca",
                "phrase": "Horis hoirino (Χωρίς χοιρινό)",
                "meaning": "Domuz eti olmasın"
            },
            {
                "language": "Yunanca",
                "phrase": "Psari Skaras (Ψάρι Σχάρας)",
                "meaning": "Izgara balık (unsuz, sadece zeytinyağı-limon)"
            },
            {
                "language": "Yunanca",
                "phrase": "Horiatiki horis paximadi (Χωριάτικη χωρίς παξιμάδι)",
                "meaning": "Yunan salatası (üzerinde peksimet/ekmek olmadan)"
            },
            {
                "language": "Yunanca",
                "phrase": "Ohi tiganita (Όχι τηγανητά)",
                "meaning": "Kızartma olmasın (fritöz çapraz bulaşması riski)"
            }
        ],
        "generalOrderingNotes": [
            "Restorana oturduğunuzda menüye bakmadan önce SOS Garson Kartını garsona okutun.",
            "Kalamar sipariş ederken mutlaka 'Kalamari Skaras' (Izgara) vurgusu yapın; aksi halde unlanıp kızartılan 'Kalamari Tiganita' gelir.",
            "Köfte (Keftedes) ve sucuklarda ekmek içi ve domuz kıyması kullanıldığından daima parça et (kuzu pirzola, tavuk şiş vb.) tercih edin.",
            "Kavala Kurabiyesi alırken sadece kendiniz için 'Me voutyro galaktos' (Süt tereyağlı) olanı sorun; eşiniz kesinlikle yememelidir.",
            "Pazartesi sabahı Selanik'teki Foodie's Art fırınından glutensiz bougatsa ve ekmek alarak sonraki günler için güvenli kahvaltı stoğu yapın."
        ],
        "certifiedBakeries": [
            {
                "name": "Foodie's Art Gluten Free Bakery",
                "city": "Selanik",
                "address": "Selanik Doğu Aksı",
                "workingHours": "Pazartesi 08:30–13:00 (Pazar Kapalı)",
                "specialties": "Glutensiz Bougatsa (Yunan böreği), taze ekmek, kurabiye, pizza tabanı",
                "mapUrl": "https://www.google.com/maps/search/?api=1&query=Foodies+Art+Gluten+Free+Bakery+Thessaloniki&query_place_id=ChIJUR0tSQA5qBQRHQH2BC0YAUI"
            }
        ],
        "finalVerificationWindow": "Restoranların çalışma saatleri ve masa rezervasyonları seyahatten 2–3 gün önce Google Maps üzerinden kontrol edilmelidir."
    },
    "currencies": [
        {
            "country": "Yunanistan",
            "currency": "Euro",
            "code": "EUR",
            "cardAcceptance": "Mükemmel (Restoranlar, gişeler, süpermarketler, müzeler)",
            "euroUsage": "Resmi ve tek yasal para birimi",
            "cashRecommended": True,
            "primaryPaymentCurrencyForTravel": True,
            "planningCashBandForTwo": {
                "min": 150,
                "max": 250,
                "currency": "EUR",
                "scope": "Meteora manastır girişleri (3€), bahşişler, küçük köy kafeleri ve otoparklar"
            }
        }
    ],
    "moneyAndPayments": {
        "mainReferenceCurrency": "EUR",
        "lastVerified": "2026-10-19",
        "exchangeRatePolicy": {
            "reason": "Yunanistan resmi para birimi Euro'dur.",
            "recommendedAction": "Harcamaların tamamına yakınında yurt dışı komisyonsuz veya düşük komisyonlu kredi kartı kullanılmalıdır.",
            "hardcodedRatesIncluded": False
        },
        "cashStrategy": {
            "euroEmergencyReserveForTwo": {
                "min": 200,
                "max": 300,
                "currency": "EUR",
                "note": "Manastır girişleri (nakit 3€ zorunluluğu olabilen yerler), otopark otomatları ve acil durumlar için nakit olarak torpido/cüzdanda bulundurulmalıdır."
            },
            "localCurrencyRules": [
                "Otoyol gişelerinde temassız kredi kartı doğrudan geçer; 1–2 Euro bozukluk bulundurmak geçişi hızlandırır.",
                "Meteora manastırlarında kişi başı 3 € bilet ücreti çoğu zaman nakit toplanır.",
                "Restoranlarda bahşiş hesaba dahil değildir; servis memnuniyetine göre %5–10 nakit bırakılabilir."
            ]
        },
        "cardAndAtmChecklist": [
            "Kredi kartlarının yurt dışı kullanımına açık olduğu banka uygulamasından kontrol edildi.",
            "Döviz ekstreli kart varsa varsayılan hesap döviz olarak ayarlandı.",
            "POS cihazlarında para birimi sorulduğunda daima 'EUR' (yerel para) seçilmeli (DCC komisyon tuzağından kaçının)."
        ],
        "roadPaymentPlan": [
            {
                "country": "Yunanistan (A2 Egnatia Odos & A1)",
                "verificationStatus": "Verified",
                "possiblePayments": [
                    "Kavala Gişeleri (~2.40 €)",
                    "Selanik Çevre Yolu Gişeleri (~1.20–1.80 €)",
                    "Larissa / Dion Gişeleri (~1.50–2.50 €)",
                    "İskeçe Gişeleri (~1.90 €)"
                ],
                "recommendedPaymentBackup": [
                    "Temassız Kredi Kartı",
                    "Nakit Bozuk Euro"
                ],
                "note": "Gişelerde 'Card' (kart) veya 'Coins/Cash' (nakit) simgeli şeritlere girilmelidir."
            }
        ],
        "rentalCarMoneyChecks": [
            "Yakıt alımlarında benzin istasyonlarında kart geçerlidir.",
            "Otopark fişleri araca dönene kadar cüzdanda saklanmalıdır."
        ],
        "budgetDisclaimer": "Otoyol gişe ücretleri ve müze girişleri mevsimsel olarak küçük değişiklikler gösterebilir.",
        "finalVerificationDates": [
            "2026-10-20",
            "2026-10-23"
        ]
    },
    "navigationAndDrivingNotes": [
        "A2 (Egnatia Odos) ve A1 bölünmüş ücretli otoyollardır; hız limiti 130 km/s'dir.",
        "Şehir içi hız limiti 50 km/s, bölünmüş yollarda 110 km/s, otoyollarda 130 km/s'dir.",
        "Farlar gündüz ve gece sürekli açık tutulmalıdır.",
        "Emniyet kemeri hem ön hem arka koltuklarda zorunludur.",
        "Direksiyon başında cep telefonu kullanımı kesinlikle yasaktır ve cezası yüksektir.",
        "Selanik şehir merkezine araba ile girilmeyip Nea Elvetia Metro otoparkına bırakılmalıdır.",
        "Olimpos dağ yollarına girmeyip Larissa üzerinden A1 otoyoluyla Dion Arkeolojik Parkı'na gidilmelidir.",
        "Vergina'dan Kalambaka'ya giderken A2 Grevena otoyol kolu takip edilmelidir.",
        "Google Maps haritalarını çevrimdışı (offline) olarak telefonunuza indirin."
    ],
    "packingAndPracticalChecklist": [
        "Pasaportlar, vizeler, yeşil sigorta ve araç ruhsatı",
        "Tansiyon ve düzenli kullanılan kişisel ilaçlar",
        "Eşiniz için acil durum glütensiz paket atıştırmalıklar (fındık, badem, glütensiz kraker)",
        "Rahat yürüyüş ayakkabısı (Afytos arnavut kaldırımı ve Meteora basamakları için)",
        "Meteora manastırları için omuz ve dizleri örten kıyafet / şal",
        "Porto Lagos lagün rüzgarına karşı rüzgarlık mont",
        "Telefon araç tutacağı ve hızlı araç şarj cihazı",
        "Powerbank (taşınabilir şarj aleti)",
        "Güneş gözlüğü ve şapka",
        "SOS Garson Kartı renkli A4 çıktısı (yedek olarak)"
    ],
    "sourceReferences": [
        {
            "title": "Google Maps 1.895 KM Tam Sürüş Rotası",
            "url": "https://www.google.com/maps/dir/%C4%B0stanbul,+T%C3%BCrkiye/%C4%B0psala+S%C4%B1n%C4%B1r+Kap%C4%B1s%C4%B1,+K%C3%B6pr%C3%BC,+%C4%B0psala%2FEdirne,+T%C3%BCrkiye/Atlas+Boutique+Suites,+%CE%9A%CE%B1%CF%81%CE%AC%CE%BD%CE%BF%CF%85+1,+%CE%9A%CE%B1%CE%B2%CE%AC%CE%BB%CE%B1,+%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1/(%CE%BC)+Metro+Station+%22Nea+Elvetia%22,+Michail+Psellou,+Thessaloniki,+Greece/Atlantis+''pleasure+By+The+Sea'',+Pavlou+Kountouriotou+51,+Perea,+Yunanistan/Free+Parking+1+Afytos,+4C3M%2B76,+Kassandra,+Greece/Aigai+Kraliyet+Mezarlar%C4%B1+M%C3%BCzesi,+Vergina,+Yunanistan/Hotel+Kaikis,+Trikalon+146,+Kalampaka,+Yunanistan/Archaeological+Site+of+Dion,+Eparchiaki+Odos+Katerinis+-+Limena+Litochoriou+910,+Dion,+Greece/Petrinos+Lofos,+Mandra,+Mandra,+67061,+Avdira,+Greece/%CE%99%CE%B5%CF%81%CE%AC+%CE%9C%CE%BF%CE%BD%CE%AE+%CE%91%CE%B3%CE%AF%CE%BF%CF%85+%CE%9D%CE%B9%CE%BA%CE%BF%CE%BB%CE%AC%CE%BF%CF%85,+Porto+Lagos,+Yunanistan/%C4%B0stanbul,+T%C3%BCrkiye",
            "usedFor": "Tüm gezi duraklarının navigasyonu"
        },
        {
            "title": "Aigai Vergina Kraliyet Mezarları Müzesi",
            "url": "https://www.aigai.gr/",
            "usedFor": "Müze açılış saatleri ve II. Filip mezarı tarihi bilgileri"
        },
        {
            "title": "Meteora Manastırları Resmi Ziyaret Rehberi",
            "url": "https://visitmeteora.travel/",
            "usedFor": "Salı günü açık olan Varlaam ve Roussanou manastır çalışma saatleri"
        },
        {
            "title": "Selanik Metro İşletmesi",
            "url": "https://www.thessmetro.gr/",
            "usedFor": "Nea Elvetia Park & Ride, Sintrivani ve Venizelou hat bilgileri"
        },
        {
            "title": "Foodie's Art Gluten Free Bakery Selanik",
            "url": "https://www.google.com/maps/search/?api=1&query=Foodies+Art+Gluten+Free+Bakery+Thessaloniki",
            "usedFor": "Glutensiz sertifikalı fırın ve çalışma günleri"
        },
        {
            "title": "Egnatia Odos Otoyol İşletmesi",
            "url": "https://www.egnatia.eu/",
            "usedFor": "A2 gişe ücretleri ve yol durumu"
        }
    ]
}

with open('yunanistan-turu-24-29-ekim-2026.json', 'w', encoding='utf-8') as f:
    json.dump(greece_data, f, ensure_ascii=False, indent=2)

print('yunanistan-turu-24-29-ekim-2026.json successfully generated.')
