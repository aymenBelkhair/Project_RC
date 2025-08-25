#!/usr/bin/python
# -*- coding: latin-1 -*-

def inpute():
        messages = [
                    (
                        "system",
                        "Your role is to analyze the given texts (many paragraphs separate by //n) and then answer the question(s) based on the given text; answer directly without explaination. The answer should be in French, and if you can't find an answer, respond with 'je ne peux pas préciser'."
                        ),
                    ("human", "{question} ? chercher la reponse dans ce text : \n\n {text}"),
                ]
        
    
    
        questions_extract = [
        
        "appartient Représentant légal Acheteur",
        
        "Objet de la consultation ",
        
        #"Adresse du marche",
        
        #"La date limite de réception des candidatures et des offres ",
        
        "visites sur site obligatoires",
        
        "Métalleries Serrureries lot",
        
        #"la durée du marché Délai d'exécution Délai de livraison",
        
        #"critères de sélection , jugement des offres",
        
        #"documents inclus dossier de candidature Courriel : E-mail : ",
        
       # "exigencesn matière de qualifications certifications ",
        
        #"financement organisé paiements échelonnés  avance forfaitaire ",
        
        #"pénalités en cas de retard",
        
        #"des primes bonus livraison anticipée",
        
        #"La sous-traitance  autorisée les modalités"
        
        ]
        
        question_pdf =[
        
        "À qui appartient le projet, qui a lancer ce marche<>DC1.1",
        
        "Quel est l'objet du projet, ou de la consultation<>DC1.2",
        
        #" Quel est l'adresse du marche",
        
        #"Quel est la Date et l'heure limites réception offres ",
        
        "Les visites sur site sont-il obligatoires ? comment s'organisent-elles ? ",
        
        "Quel est le numéro du lot métallerie-serrurerie<>DC1.3",
        
        #"Quelle est la durée du marché ",
        
        #"Quels sont les critères de sélection et de jugement des offres",
        
        #"Quels documents spécifiques doivent être inclus dans le dossier de candidature ",
        
        #"Y a-t-il des exigences spécifiques en matière de qualifications ou de certifications pour soumissionner",
        
        #"Comment le financement est-il organisé pour ce projet (paiements échelonnés, avance forfaitaire)",
        
        #"Y a-t-il des pénalités en cas de retard",
        
        #"Le marché prévoit-il des primes ou des bonus en cas de livraison anticipée",
        
        #"La sous-traitance est-elle autorisée ? Si oui, quelles sont les modalités" 
        ]
        
        questions_gpt = [
        
            "Identifie l’acheteur qui a lancer le project avec son adreesse? Sans aucun autre information ou explication",
        
            "Quel est l objet du projet ? Sans débuter par 'l object de la consultation est',mais donner directement la réponse et sans beaucoup de detaille ", 
        
            #"reponde au 2 questions en une seul phrase compréhensible (Acheteur/nAdresse) 1-À qui appartient le projet, ou qui a lancé ce marché ? 2-Quelle est l'adresse du marché ?",
        
            #"À qui appartient le projet, ou qui a lancé ce marché ?",
        
            #"Quelle est l'adresse du marché ?",
        
            #"1-Quelle est la date et l'heure limite pour la réception des offres ? 2-Quelle est la durée prévue pour ce marché ?",
        
            "Les visites obligatoires sont-elles requises ? Répondre par 'oui' ou 'non'. Si 'oui', quelle est la date prévue pour cette visite et #comment s'organisent-elles ? (Chercher un contact : e-mail, téléphone ou lien d'inscription)",
        
            "Quel est le numéro du lot(s) concernant la métallerie serrurerie ? Releve tous les lots, analyse bien le text il se peux avoir une lot generale puis des sous lots comme 'Lot01 12 métallerie serrurerie' ? Votre reponse doit etre formuler comme suit LOT N°X {SERRURERIE} - {METALLERIE} - {autres information sur cette lot s'in exist par example (PORTES DE GARAGE)}, le text entre {} varie selon le text(s). Sans aucun autre information ou explication ",
        
            #"Quelle est la durée prévue pour ce marché ?",
        
            #"Quels sont les critères de sélection et de jugement des offres ?",
        
            #"Quels documents spécifiques doivent être inclus dans le dossier de candidature ? avec le lien ou email de postulation?",
        
            #"Y a-t-il des exigences spécifiques en matière de qualifications ou de certifications pour soumissionner ?",
        
            #"Comment le financement du projet est-il organisé (paiements échelonnés, avance forfaitaire, etc.) ?",
        
            #"Y a-t-il des pénalités prévues en cas de retard ?",
        
            #"Le marché prévoit-il des primes ou des bonus en cas de livraison anticipée ?",
        
            #"La sous-traitance est-elle autorisée ? Si oui, quelles sont les modalités prévues ?"
        
        ]


        return messages,questions_extract,question_pdf,questions_gpt
    
if __name__ == "__main__":
    inpute()