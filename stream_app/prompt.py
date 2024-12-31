#!/usr/bin/python
# -*- coding: latin-1 -*-

def inpute():
        messages = [
                    (
                        "system",
                        "Your role is to analyze the given texts (many paragraphs separate by //n) and then answer the question(s) based on the given text; answer directly without explaination. The answer should be in French, and if you can't find an answer, respond with 'je ne peux pas pr�ciser'."
                        ),
                    ("human", "{question} ? chercher la reponse dans ce text : \n\n {text}"),
                ]
        
    
    
        questions_extract = [
        
        "appartient Repr�sentant l�gal Acheteur  ",
        
        "Objet de la consultation ",
        
        #"Adresse du marche",
        
        #"La date limite de r�ception des candidatures et des offres ",
        
        #"visites sur site obligatoires",
        
        "M�talleries Serrureries",
        
        #"la dur�e du march� D�lai d'ex�cution D�lai de livraison",
        
        #"crit�res de s�lection , jugement des offres",
        
        #"documents inclus dossier de candidature Courriel : E-mail : ",
        
       # "exigencesn mati�re de qualifications certifications ",
        
        #"financement organis� paiements �chelonn�s  avance forfaitaire ",
        
        #"p�nalit�s en cas de retard",
        
        #"des primes bonus livraison anticip�e",
        
        #"La sous-traitance  autoris�e les modalit�s"
        
        ]
        
        question_pdf =[
        
        "� qui appartient le projet, qui a lancer ce marche",
        
        "Quel est l'objet du projet, ou de la consultation ",
        
        #" Quel est l'adresse du marche",
        
        #"Quel est la Date et l'heure limites r�ception offres ",
        
        #"Les visites sur site sont-il obligatoires ? comment s'organisent-elles ? ",
        
        "Quel est le num�ro du lot m�tallerie-serrurerie ",
        
        #"Quelle est la dur�e du march� ",
        
        #"Quels sont les crit�res de s�lection et de jugement des offres",
        
        #"Quels documents sp�cifiques doivent �tre inclus dans le dossier de candidature ",
        
        #"Y a-t-il des exigences sp�cifiques en mati�re de qualifications ou de certifications pour soumissionner",
        
        #"Comment le financement est-il organis� pour ce projet (paiements �chelonn�s, avance forfaitaire)",
        
        #"Y a-t-il des p�nalit�s en cas de retard",
        
        #"Le march� pr�voit-il des primes ou des bonus en cas de livraison anticip�e",
        
        #"La sous-traitance est-elle autoris�e ? Si oui, quelles sont les modalit�s" 
        ]
        
        questions_gpt = [
        
            "Identification de l�acheteur qui a lancer le project, avec son adreesse",
        
            "Quel est l'objet du projet ou de la consultation ?", 
        
            #"reponde au 2 questions en une seul phrase compr�hensible (Acheteur/nAdresse) 1-� qui appartient le projet, ou qui a lanc� ce march� ? 2-Quelle est l'adresse du march� ?",
        
            #"� qui appartient le projet, ou qui a lanc� ce march� ?",
        
            #"Quelle est l'adresse du march� ?",
        
            #"1-Quelle est la date et l'heure limite pour la r�ception des offres ? 2-Quelle est la dur�e pr�vue pour ce march� ?",
        
            #"Les visites obligatoires sont-elles requises ? R�pondre par 'oui' ou 'non'. Si 'oui', quelle est la date pr�vue pour cette visite et #comment s'organisent-elles ? (Chercher un contact : e-mail, t�l�phone ou lien d'inscription)",
        
            "Quel est le num�ro du lot(s) concernant la m�tallerie serrurerie ? releve tous les lots, analyse bien le text il se peux avoir une lot generale puis des sous lots comme 'Lot01 12 m�tallerie serrurerie, Lot11 21 m�tallerie serrurerie ' ?",
        
            #"Quelle est la dur�e pr�vue pour ce march� ?",
        
            #"Quels sont les crit�res de s�lection et de jugement des offres ?",
        
            #"Quels documents sp�cifiques doivent �tre inclus dans le dossier de candidature ? avec le lien ou email de postulation?",
        
            #"Y a-t-il des exigences sp�cifiques en mati�re de qualifications ou de certifications pour soumissionner ?",
        
            #"Comment le financement du projet est-il organis� (paiements �chelonn�s, avance forfaitaire, etc.) ?",
        
            #"Y a-t-il des p�nalit�s pr�vues en cas de retard ?",
        
            #"Le march� pr�voit-il des primes ou des bonus en cas de livraison anticip�e ?",
        
            #"La sous-traitance est-elle autoris�e ? Si oui, quelles sont les modalit�s pr�vues ?"
        
        ]


        return messages,questions_extract,question_pdf,questions_gpt
    
if __name__ == "__main__":
    inpute()