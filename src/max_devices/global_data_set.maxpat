{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 7,
			"minor" : 2,
			"revision" : 2,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"rect" : [ 173.0, 218.0, 697.0, 518.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-64",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "int" ],
					"patching_rect" : [ 204.083313, 137.0, 140.0, 23.0 ],
					"style" : "",
					"text" : "conformpath max boot"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial Bold",
					"fontsize" : 10.0,
					"id" : "obj-60",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 204.083313, 170.5, 183.0, 20.0 ],
					"style" : "",
					"text" : "sprintf read %s"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial Bold",
					"fontsize" : 10.0,
					"id" : "obj-11",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 204.083313, 252.0, 58.0, 18.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 245.0, 37.75, 52.0, 18.0 ],
					"style" : "",
					"text" : "set path",
					"textcolor" : [ 0.301961, 0.337255, 0.403922, 1.0 ],
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-12",
					"maxclass" : "outlet",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 204.083313, 215.0, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-6",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 31.333313, 69.0, 54.0, 23.0 ],
					"style" : "",
					"text" : "depth 2"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.439216, 0.74902, 0.254902, 0.0 ],
					"fontname" : "Arial Bold",
					"fontsize" : 10.0,
					"id" : "obj-62",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 31.333313, 11.0, 45.0, 18.0 ],
					"presentation" : 1,
					"presentation_linecount" : 2,
					"presentation_rect" : [ 335.25, 157.5, 38.0, 29.0 ],
					"style" : "",
					"text" : "buttom "
				}

			}
, 			{
				"box" : 				{
					"comment" : "",
					"id" : "obj-1",
					"maxclass" : "inlet",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 31.333313, 34.0, 30.0, 30.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"annotation" : "Drop folder here !",
					"applycolors" : 1,
					"autopopulate" : 1,
					"depth" : 2,
					"fontsize" : 10.0,
					"hint" : "here !",
					"id" : "obj-28",
					"items" : [ "audiens", ",", "audiens/audiens_effectifis_2010.tsv", ",", "France_solo", ",", "France_solo/France_solo.tsv", ",", "France_solo/France_solo_ocde_educ.tsv", ",", "France_solo/France_solo_ocde_inventrices.tsv", ",", "France_solo/France_solo_ocde_politique.tsv", ",", "France_solo/France_solo_ocde_travail.tsv", ",", "insee", ",", "insee/insee_educ", ",", "insee/insee_educ/cond-educ-dip-eleve-age-sexe-2.tsv", ",", "insee/insee_educ/femmes-hommes-18-indicateurs-regionaux_enseignement_education.tsv", ",", "insee/insee_educ/pa_inf_65_donnees_figures.tsv", ",", "insee/insee_societe", ",", "insee/insee_societe/cond-vie-soc-temps-sociaux-sexe-2.tsv", ",", "insee/insee_societe/femmes-hommes-18-indicateurs-regionaux_revenus_Salaires_france.tsv", ",", "insee/insee_societe/marc-salair-ecart-h-f-2.tsv", ",", "insee/insee_societe/reve-pauv-taux-age-sexe-2.tsv", ",", "insee/insee_societe/reve-protec-montant-retraite-age-sexe-2.tsv", ",", "insee/insee_travail", ",", "insee/insee_travail/femmes-hommes-18-indicateurs-regionaux_revenus_Salaires.tsv", ",", "insee/insee_travail/marc-cho-nbr-taux-sexe-age-2.tsv", ",", "insee/insee_travail/marc-empl-csp-sexe-age-2.tsv", ",", "insee/insee_travail/marc-empl-nbr-taux-activ-sexe-age-2.tsv", ",", "insee/insee_travail/marc-empl-temps-trav-sexe-age-2.tsv", ",", "insee/insee_travail/marc-salair-net-mens-sexe-csp-2-sal.tsv", ",", "insee/rp2014_td_img2B.tsv", ",", "minist_dossier", ",", "minist_dossier/ministere_art_medias.tsv", ",", "minist_dossier/ministere_politique.tsv", ",", "minist_dossier/ministere_tout.tsv", ",", "minist_dossier/ministere_travail.tsv", ",", "minist_educ", ",", "minist_educ/repartition.tsv", ",", "nanterre", ",", "nanterre/societe.tsv", ",", "nanterre/travail.tsv", ",", "oced_francais", ",", "oced_francais/developpement", ",", "oced_francais/developpement/Mariage_precoce.tsv", ",", "oced_francais/developpement/Mutilations_genitales_feminines_(MGF)_.tsv", ",", "oced_francais/developpement/pourcentage_de_femmes_parmi_les_cadres_et_techniciens.tsv", ",", "oced_francais/developpement/pourcentage_de_femmes_parmi_les_parlementaires_hauts_fonctionnaires_et_directeurs.tsv", ",", "oced_francais/developpement/Ratio_femmes_hommes_de_scolarisation_dans_le_primaire.tsv", ",", "oced_francais/developpement/Ratio_femmes_hommes_de_scolarisation_dans_le_secondaire.tsv", ",", "oced_francais/developpement/Ratio_femmes_hommes_de_scolarisation_dans_le_superieur.tsv", ",", "oced_francais/developpement/Taux_d_alphabetisation.tsv", ",", "oced_francais/developpement/Taux_d_alphabetisation_des_jeunes.tsv", ",", "oced_francais/education", ",", "oced_francais/education/Low-achieving_students_Mathematics.tsv", ",", "oced_francais/education/Low-achieving_students_Reading.tsv", ",", "oced_francais/education/Low-achieving_students_Science.tsv", ",", "oced_francais/education/Top_performers_Mathematics.tsv", ",", "oced_francais/education/Top_performers_Reading.tsv", ",", "oced_francais/education/Top_performers_Science.tsv", ",", "oced_francais/emploi", ",", "oced_francais/emploi/Ecart_salarial_entre_femmes_et_hommes.tsv", ",", "oced_francais/emploi/Part_de_l_emploi_dans_l_agriculture_par_sexe_.tsv", ",", "oced_francais/emploi/Part_de_l_emploi_dans_l_industrie_par_sexe.tsv", ",", "oced_francais/emploi/Part_de_l_emploi_dans_les_services_par_sexe.tsv", ",", "oced_francais/emploi/Part_des_employes_a_temps_partiel_par_sexe_et_groupe_d_age.tsv", ",", "oced_francais/emploi/Part_des_employes_cadres_superieurs_par_sexe.tsv", ",", "oced_francais/emploi/Part_des_employes_temporaires_par_sexe.tsv", ",", "oced_francais/emploi/Part_des_femmes_dans_l_emploi_public.tsv", ",", "oced_francais/emploi/Part_des_femmes_dans_l_emploi_total.tsv", ",", "oced_francais/emploi/Part_des_sieges_occupes_par_des_femmes_dans_les_parlements_nationaux.tsv", ",", "oced_francais/emploi/Taux_d_activite_par_sexe_et_groupe_d_age.tsv", ",", "oced_francais/emploi/Taux_de_chomage_par_sexe_et_groupe_d_age.tsv", ",", "oced_francais/entreprenariat", ",", "oced_francais/entreprenariat/Attitude_envers_le_risque_entrepreneurial.tsv", ",", "oced_francais/entreprenariat/L_acces_a_l_argent_pour_demarrer_une_entreprise.tsv", ",", "oced_francais/entreprenariat/L_acces_a_la_formation_a_la_creation_d_entreprise_.tsv", ",", "oced_francais/entreprenariat/Part_de_femmes_inventrices.tsv", ",", "oced_francais/entreprenariat/Part_de_la_population_avec_un_compte_dans_une_institution_financiere.tsv", ",", "oced_francais/entreprenariat/Part_de_la_population_qui_declare_emprunter_de_l_argent_pour_demarrer_une_entreprise.tsv", ",", "oced_francais/entreprenariat/Part_des_entreprises_a_proprietaire_unique_appartenant_a_des_femmes.tsv", ",", "oced_francais/entreprenariat/Part_des_personnes_en_emploi_etant_employeurs.tsv", ",", "oced_francais/entreprenariat/Part_des_personnes_en_emploi_travaillant_a_leur_compte.tsv", ",", "oced_francais/entreprenariat/Part_des_travailleurs_independants_ayant_moins_de_30_ans.tsv", ",", "oced_francais/entreprenariat/Part_des_travailleurs_independants_dans_le_secteur_manufacturier_ou_la_construction.tsv", ",", "oced_francais/entreprenariat/Part_des_travailleurs_independants_dans_les_services.tsv", ",", "oced_francais/entreprenariat/Part_des_travailleurs_independants_parmi_les_diplomes_de_l_enseignement_tertiaire_ayant_un_emploi.tsv", ",", "oced_francais/entreprenariat/Part_des_travailleurs_independants_parmi_les_personnes__de_moins_de_30_ans_ayant_un_emploi.tsv", ",", "oced_francais/entreprenariat/Part_des_travailleurs_independants_parmi_les_personnes_de_nationalite_etrangere_ayant_un_emploi.tsv", ",", "oced_francais/entreprenariat/Preferences_pour_le_travail_independant.tsv" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 31.333313, 98.0, 364.5, 20.0 ],
					"pattrmode" : 1,
					"prefix" : "Macintosh HD:/Users/JRLetelier/perso/agora/data/m4l/",
					"presentation" : 1,
					"presentation_rect" : [ 8.875, 37.75, 364.0, 20.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "umenu",
							"parameter_shortname" : "umenu",
							"parameter_type" : 3,
							"parameter_initial" : [ "audiens/audiens_effectifis_2010.tsv" ],
							"parameter_invisible" : 1,
							"parameter_annotation_name" : "menu"
						}

					}
,
					"style" : "",
					"truncate" : 2,
					"varname" : "umenu"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-64", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-28", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-64", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-28" : [ "umenu", "umenu", 0 ]
		}
,
		"dependency_cache" : [  ],
		"autosave" : 0
	}

}
