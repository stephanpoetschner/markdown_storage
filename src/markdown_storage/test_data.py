SAMPLE_TEXT = """title: FH Technikum Wien
subline: Elektronische Informationsdienste
externalurl: http://technikum-wien.at
duration: "abgeschlossen: 2006"
date: 2006-12-30 12:00
---
* Leistungsstipendium mehrmals erhalten: wird pro Studiengang (ca. 240 Studenten) an 6 Studenten pro Jahr vergeben.
* Teammitglied der [Austrian Cubes](http://www.austriancubes.at/) (Roboter Fussball): Teilnahme an [WM in Osaka (Japan) 2005](http://www.robocup2005.org/)"""


SAMPLE_TEXT_SPLIT = (
    """title: FH Technikum Wien\nsubline: Elektronische Informationsdienste\nexternalurl: http://technikum-wien.at\nduration: "abgeschlossen: 2006"\ndate: 2006-12-30 12:00""",
    """* Leistungsstipendium mehrmals erhalten: wird pro Studiengang (ca. 240 Studenten) an 6 Studenten pro Jahr vergeben.\n* Teammitglied der [Austrian Cubes](http://www.austriancubes.at/) (Roboter Fussball): Teilnahme an [WM in Osaka (Japan) 2005](http://www.robocup2005.org/)"""
)

SAMPLE_METADATA = {
    'date': '2006-12-30 12:00',
    'duration': 'abgeschlossen: 2006',
    'subline': 'Elektronische Informationsdienste',
    'title': 'FH Technikum Wien',
    'externalurl': 'http://technikum-wien.at',
}