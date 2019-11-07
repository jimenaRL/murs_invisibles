#!/bin/bash
BASEPATH=$(dirname $0)

echo "> CNC-Audiens"
python $BASEPATH/data/sources/CNC-Audiens/tout/cnc-audiens-tout.py
python $BASEPATH/data/sources/CNC-Audiens/audiens/cnc-audiens.py
python $BASEPATH/data/sources/CNC-Audiens/cnc1/cnc-audiens.py
python $BASEPATH/data/sources/CNC-Audiens/cnc2/cnc-audiens.py

echo "> EESR"
echo ">> EESR-FR"
python data/sources/EESR/EESR-FR/data.py
echo ">> parite2019"
python data/sources/EESR/parite2019/parite2019.py


echo "> INSEE"
python $BASEPATH/data/sources/INSEE/insee.py

echo "> INSEE-95"
python $BASEPATH/data/sources/INSEE-95/insee-95.py

echo "> MINIST-CULT"
python $BASEPATH/data/sources/MINIST-CULT/miniscult.py


echo "> OECD"
echo ">> developpement"
python $BASEPATH/data/sources/oecd/developpement/developpement.py
echo ">> education"
python $BASEPATH/data/sources/oecd/education/education.py
echo ">> emploi"
python $BASEPATH/data/sources/oecd/emploi/emploi.py
echo ">> entrepreneuriat"
python $BASEPATH/data/sources/oecd/entrepreneuriat/entrepreneuriat.py
echo ">> gouvernance"
python $BASEPATH/data/sources/oecd/gouvernance/gouvernance.py


echo "> onu"
echo ">> genderstats"
python $BASEPATH/data/sources/onu/genderstats/genderstats.py
echo ">> dataunorg"
python $BASEPATH/data/sources/onu/dataunorg/dataunorg.py


echo "> secretariat_egalite_femmes_hommes"
python $BASEPATH/data/sources/secretariat_egalite_femmes_hommes/secret.py

echo "> VIOLENCES"
python $BASEPATH/data/sources/VIOLENCES/violences.py