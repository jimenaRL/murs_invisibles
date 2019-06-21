#!/bin/bash
BASEPATH=$(dirname $0)

echo "> onu"

echo ">> genderstats"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/onu/genderstats/genderstats.py
echo ">> dataunorg"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/onu/dataunorg/dataunorg.py


echo "> oecd"

echo ">> developpement"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/oecd/developpement/developpement.py

echo ">> gouvernance"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/oecd/gouvernance/gouvernance.py

echo ">> emploi"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/oecd/emploi/emploi.py

echo ">> education"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/oecd/education/education.py

echo ">> entrepreneuriat"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/oecd/entrepreneuriat/entrepreneuriat.py


echo "> CNC-Audiens"
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/CNC-Audiens/audiens/cnc-audiens.py
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/CNC-Audiens/cnc1/cnc-audiens.py
PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/CNC-Audiens/cnc2/cnc-audiens.py

echo "> EESR"

echo ">> EESR-FR"
PYTHONIOENCODING=UTF-8 python data/sources/EESR/EESR-FR/data.py

echo ">> parite2019"
PYTHONIOENCODING=UTF-8 python data/sources/EESR/EESR-FR/data.py

echo "> secretariat_egalite_femmes_hommes_2"

PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/secretariat_egalite_femmes_hommes_2/secret.py


echo "> secretariat_egalite_femmes_hommes"

PYTHONIOENCODING=UTF-8 python $BASEPATH/data/sources/secretariat_egalite_femmes_hommes/minist_dossier.py
