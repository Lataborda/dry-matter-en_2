import streamlit as st
from PIL import Image


image = Image.open('Logos2.png')
st.image(image)



#Titulo
st.write("""
# Tool for measuring the dry matter and starch content of fresh cassava roots  

This tool calculates the percentage of dry matter and starch content in fresh cassava roots, based on measurement of their density. To do this, it is necessary to record the exact weight of a sample of cassava roots in air (approximately 5 kg), then the weight of this same sample submerged in water. The following video illlustrates the procedure:
""")


#insert video


st.video('DrymatterEn.mp4')


#insert variables


st.subheader('Please input the weights:')

PS = st.number_input('Weight of cassava in the air (g)', 4500,6000)
PA = st.number_input('Weight of cassava submerged in water (g)', 200,800)

#Inicio de ecuación

#Gravedad específica (parte de abajo de la ecuacuación)

GEd = int(PS) - int(PA)

#resultado de gravedad específica

RG = int(PS) / int(GEd)


# Ecuaciación de materia seca 

MS1 = 158.26 * float(RG) - 142.05

st.write('* **According to the equation from CIAT 1976 (Kawano et al. 1987), the percentage of dry matter for this sample is:**')
#st.subheader(round(MS1,1))
st.subheader(f"Dry matter content: {round(MS1)}%")

if float(MS1)<27:
	st.error('**Percentage of dry matter is low**')

elif 27.01 <= float(MS1) <= 31.99:
	st.warning('**Percentage of dry matter is average**')

elif float(MS1)>= 32:
	st.success('**Percentage of dry matter is high**')


#Porcentaje de almidón
Alm= float(MS1)*0.875

st.write('* *Starch in cassava usually represents between 80 and 90% of the dry matter, with an average of 87.5%. Therefore the approximate percentage of (pure) starch in this sample would be around:*')
#st.subheader(round(Alm,1))
st.subheader(f"Percentage of starch: {round(Alm)}%")

#Porcentaje de almidón recuperable
AlmRe= float(MS1)*0.64

st.write('* *For industrial use, only part of the starch contained in cassava roots is extractable. According to Hansupalak et al. (2016), recoverable starch represents 64% of the dry matter. Therefore the percentage of recoverable starch (at 13% moisture) of this sample would be around:*')
#st.subheader(round(AlmRe,1))
st.subheader(f"Percentage of extractable starch: {round(AlmRe,1)}%")


st.write('**NOTE**: The values calculated on this page with the CIAT 1976 equation (Kawano et al. 1987; Keating et al. 1981) are indicative. For more precise values, other methods are recommended, such as oven drying (105°C for 24 hours) for dry matter content, and enzymatic starch determination (Holm et al. 1986) for starch content. This tool is made available without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability or fitness for a particular purpose. No warranties are made either regarding any damages, loss of data, loss of profits, liabilities and/or injuries caused by the use of this tool.')

st.write('**References:**')
st.write('-Hansupalak N., Piromkraipak P., Tamthirat P., Manitsorasak A., Sriroth K., Tran T. (2016). Biogas reduces the carbon footprint of cassava starch: A comparative assessment with fuel oil. Journal of Cleaner Production 134 part B, 539-546.') 
st.write('-Holm J., Björck I., Drews A., Asp N.G. (1986). A rapid method for the analysis of starch. Starch‐Stärke, 38(7), 224-226.') 
st.write('-Kawano K., Goncalves Fukuda W.M., Cenpukdee U. (1987). Genetic and environmental effects on dry matter content of cassava root. Crop Science 27, 69-74.') 
st.write('-Keating B.A., Breen A.R., Evenson J.P. (1981). Estimation of Starch and Total Fermentables Content in Storage Roots of Cassava (Manihot esculenta Crantz. Journal of the Science of Food and Agriculture 32, 997-1004.')
	 
st.markdown('*Copyright (C) 2022 CIRAD & CIAT*')
st.markdown('**Authors: Luis Alejandro Taborda Andrade (latabordaa@unal.edu.co), Katia Contreras (kcontreras@agrosavia.co), Thierry Tran (thierry.tran@cirad.fr)**')
