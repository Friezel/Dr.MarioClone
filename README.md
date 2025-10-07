# Dr. mario clone

**Inhoudstafel**

- [[#Projectteam|Projectteam]]
- [[#Beschrijving van het project|Beschrijving van het project]]
	- [[#Beschrijving van het project#Wat willen we doen?|Wat willen we doen?]]
	- [[#Beschrijving van het project#Wat is Dr.Mario|Wat is Dr.Mario]]
	- [[#Beschrijving van het project#Doelstellingen|Doelstellingen]]
	- [[#Beschrijving van het project#Uitbreidingsmogelijkheden|Uitbreidingsmogelijkheden]]
- [[#Gebruikte libraries|Gebruikte libraries]]
- [[#Bron van ons idee|Bron van ons idee]]


# Projectteam
- Dries Schreurs
- Lander Geerts
# Beschrijving van het project
## Wat willen we doen?
In dit voorstel willen we een Python-implementatie ontwikkelen van het klassieke puzzelspel Dr. Mario[^1], oorspronkelijk uitgebracht in 1990 voor de NES. Dit project zal worden geïmplementeerd met behulp van de Pygame[^3]-bibliotheek. Ons doel is om een functionele en speelbare versie van het spel te maken.
## Wat is Dr.Mario
Dr. Mario[^1] is een puzzelspel dat sterk lijkt op Tetris[^2]. In plaats van tetromino's, gebruikt het spel "pillen" die bestaan uit twee gekleurde blokken. Deze pillen vallen van bovenaan het scherm, en de speler moet ze zo plaatsen dat er horizontale of verticale rijen van vier of meer blokken van dezelfde kleur ontstaan. Deze rijen worden vervolgens verwijderd. Het doel is om alle virussen op het speelveld te elimineren door ze te laten verdwijnen in combinatie met de pillen.
## Doelstellingen
Wij willen een speelbare versie van Dr. Mario[^1] ontwikkelen in Python. Het spel zal bestaan uit de volgende kernfunctionaliteiten:
- Een speelveld met virussen die verwijderd moeten worden.
- Pillen die van bovenaan het scherm vallen en door de speler kunnen worden geroteerd en verplaatst.
- Het verwijderen van rijen van vier of meer blokken van dezelfde kleur.
- Een scoringsysteem dat punten toekent op basis van het verwijderen van blokken en virussen.
- Een win- en verliesconditie: de speler wint als alle virussen zijn verwijderd en verliest als de pillen het speelveld volledig vullen.
## Uitbreidingsmogelijkheden
Indien de klassieke implementatie van Dr. Mario[^1] niet voldoende is kunnen we ook ons eigen puzzelspel ontwerpen. Dit zou kunnen bestaan uit:
- Een aangepaste versie van Dr. Mario[^1] met een eigen gebruikersinterface en spelmechanica.
- Een geheel nieuw puzzelspel met eigen regels, maar wel in de stijl van Tetris[^2], Dr.Mario[^1] of PuyoPuyo[^4]
# Gebruikte libraries
- Python
- Pygame[^3]
# Bron van ons idee
Ons project is geïnspireerd op de volgende bronnen:
- Dr. Mario[^1]: Het originele spel dat als basis dient voor ons project.
- Tetris[^2]: Een klassiek puzzelspel dat vergelijkbare mechanica gebruikt

[^1]: _Dr. Mario - Wikiwand_. (z.d.). https://www.wikiwand.com/nl/articles/Dr._Mario
[^2]: _Tetris - Wikiwand_. (z.d.). https://www.wikiwand.com/nl/articles/Tetris
[^3]: _pygame news_. (z.d.). https://www.pygame.org/news
[^4]: _Puyo puyo - Wikiwand_. (z.d.). https://www.wikiwand.com/en/articles/Puyo_Puyo