import string
from turtle import color
from fpdf import FPDF

#Temps d'échéance pour la facture
from TimeFunc import *
MoisDelais = 0
debut = StartDate(MoisDelais)
fin = EndDate(MoisDelais)
PremierDateLocation = '11/2021'

# A Remplir
#Entreprise qui effectue la facture

#mail à envoyer
NomEntreprise = 'XXXXX'
NomFAmilleEntre = 'XXXX'
PrenomFamilleEntre = 'XXXXXX'
AdresseEntreprise = 'XXXXX'
CodePostaleEntreprise = 'XXXX'
VilleEntreprise = 'XXXXXX'
PortableEntreprise1 = 'XXXXXXXXXX'
PortableEntreprise2 = 'XXXXXXX'
MailEntreprise = 'XXXXXXXXXXXXXXXXXXXXx'
CompteIBANEntreprise = 'xXXXXXXXXXXXXXX'
PrixLocation1 = '750.00'
PrixCharges = '200.00'
MontantTotal = '950.00'
MontantTotalEnLettre = 'La somme de neuf cent cinquante euros et zéros centimes'
MontantIndemnite = '40.00'
ObjetLocation = 'Location non meublée'
ModePaiement = ''
LogoEntreprise = 'ImageLoyerPython/kiatou.png'
# LogoSignature = 'ImageLoyerPython/signature.jpg'

#Particulier qui reçoit la facture
NomFamillePart = 'XXXXXXX'
PrenomFamillePart = 'XXXXXXXXXX'
AdressePart ='XXXXXXXXX'
CodePostalePart ='XXXXXXXXXXX'
VillePart = 'XXXXXX'
PaysPart = 'XXXXXXXXX'


#Front End Python
#dateActuelle en int pour trouver le numero de contrat
annee = int (debut[6]+debut[7]+debut[8]+debut[9])
mois = int (debut[3]+debut[4])
anneeArrive =  int (PremierDateLocation[3]+ PremierDateLocation[4]+ PremierDateLocation[5] +PremierDateLocation[6])
moisArrive = int (PremierDateLocation[0] + PremierDateLocation[1])

calcul = (annee - anneeArrive)*12 + mois-moisArrive+1
numerobis = str(calcul)

class PDF(FPDF):
    def header(self):
        # Logo
        self.image(LogoEntreprise, 163, 10,28)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        # Title
        self.cell(0, 0, NomEntreprise)
        self.set_font('Arial', '', 10)
        self.ln(8)
        self.cell(0,0,NomFAmilleEntre+' '+PrenomFamilleEntre)
        self.ln(4)
        self.cell(0,0,AdresseEntreprise)
        self.ln(4)
        self.cell(0,0,CodePostaleEntreprise+' '+ VilleEntreprise)
        self.ln(4)
        self.cell(0,0,'Portable: '+PortableEntreprise1 +'  ' + PortableEntreprise2)
        self.ln(4)
        self.cell(0,0,'Mail: '+MailEntreprise)
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instanciation des paramètres généraux
pdf = PDF('P','mm','A4')
pdf.set_margins(20,15, 20)
pdf.alias_nb_pages()
pdf.add_page()

#Pour l'entête du contrat
pdf.set_font('Arial','', 10)
pdf.cell(139,4,'Contrat:     C'+ debut[6]+debut[7]+debut[8]+debut[9]+debut[3]+debut[4]+debut[0]+debut[1],0,0)
pdf.cell(31,4,'Quittance de loyer',1,1)
pdf.cell(139,4,'Locataire:   '+NomFamillePart + ' ' + PrenomFamillePart,0,0)
pdf.cell(31,4,'Contrat N° '+numerobis,1,1)
pdf.cell(139,4,'Période:         '+debut,0,0)
pdf.cell(31,4,debut,1,1)
pdf.ln(4)
pdf.cell(0,4,NomFamillePart+' '+ PrenomFamillePart,0,1)
pdf.cell(0,4,AdressePart,0,1)
pdf.cell(0,4,CodePostalePart+' '+VillePart,0,1)
pdf.cell(0,4,PaysPart,0,1)
pdf.ln(4)

#Le corps du contrat

pdf.set_fill_color(0,180,180) #fill with yellow color
pdf.cell(0,4,'AVIS D\'ECHEANCE',1,1,"C",fill=1)
pdf.cell(0,26,"Période du "+ debut + " au " + fin,1,0)
pdf.cell(-30,26,PrixLocation1 +' euros',1,0,"C")
pdf.ln(8)
pdf.cell(0,2,ObjetLocation,0,1)
pdf.ln(5)
pdf.cell(0,4,'Adresse : '+AdressePart + ' ' + CodePostalePart + ' ' + VillePart,0,1)
pdf.ln(7)
pdf.cell(0,26,"Charges Comprises",1,0)
pdf.cell(-30,26,PrixCharges + ' euros',1,1,"C")
pdf.ln(7)
pdf.set_font('Arial','I', 10)
pdf.cell(0,4,'Reçu de M/Mme '+ NomFamillePart + ' ' + PrenomFamillePart,0,1)
pdf.cell(0,4,MontantTotalEnLettre,0,1)
pdf.cell(0,4,"Au titre du paiement du loyer et des charges du logement/local sis:",0,1)
pdf.cell(0,4,AdressePart + ' ' + CodePostalePart + ' ' + VillePart,0,1)
pdf.cell(0,4,"Pour la période de location du "+debut +" au " + fin +"",0,1)



pdf.ln(40)
pdf.set_font('Arial','B', 10)
pdf.cell(40,4,"Mode de Paiement:",0,0)
pdf.set_font('Arial','', 10)
pdf.cell(80,4,ModePaiement,0,0)
pdf.set_fill_color(0,180,180) #fill with yellow colorv
pdf.set_font('Arial','B', 10)
pdf.cell(30,4,"Montant à régler",1,0,fill =1)
pdf.cell(23,4,MontantTotal+' euros',1,1,fill =1)
pdf.cell(40,4,"",0,0)
pdf.set_font('Arial','', 10)
pdf.cell(40,4,CompteIBANEntreprise,0,1)
pdf.cell(63,4,"",0,0)
pdf.set_fill_color(220,50,50)
pdf.cell(110,4,MontantTotal + ' euros payé le '+ debut + ' ' + ModePaiement,1,1, fill =1)
pdf.ln(2)
pdf.cell(40,4,'Le non paiement à échéance entrainera la',0,1)
pdf.cell(40,4,'facturation d\'une indemnité égale à '+ MontantIndemnite +' euros',0,1)
# pdf.image(LogoSignature, 35, 230,28)

pdf.ln(40)

pdf.output("QuittanceLoyer/quittance_loyer.pdf", 'F')
