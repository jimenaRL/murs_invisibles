echo "> onu"

echo ">> genderstats"
PYTHONIOENCODING=UTF-8 python data_tmp/sources/onu/genderstats/genderstats.py
echo ">> dataunorg"
PYTHONIOENCODING=UTF-8 python data_tmp/sources/onu/dataunorg/dataunorg.py


echo "> oecd"

echo ">> developpement"
PYTHONIOENCODING=UTF-8 python data_tmp/sources/oecd/developpement/developpement.py

echo ">> gouvernance"
PYTHONIOENCODING=UTF-8 python data_tmp/sources/oecd/gouvernance/gouvernance.py

echo ">> emploi"
PYTHONIOENCODING=UTF-8 python data_tmp/sources/oecd/emploi/emploi.py

echo "> secretariat_egalite_femmes_hommes"

PYTHONIOENCODING=UTF-8 python data_tmp/sources/secretariat_egalite_femmes_hommes/minist_dossier.py
