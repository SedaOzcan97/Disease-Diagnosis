from tkinter import *
import numpy as np
import pandas as pd
from PIL import ImageTk,Image
from tkinter import filedialog

AGE= ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70']

GENDER= ['MALE','FEMALE']

SYMPTOMPS=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len( SYMPTOMPS)):
    l2.append(0)




# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Symptom_Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[SYMPTOMPS]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------





# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Symptom_Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)



X= df[SYMPTOMPS]

y = df[["prognosis"]]
np.ravel(y)

# DECISION TREE ALGORITHM (PREDICTION1)
def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   
    clf3 = clf3.fit(X,y)

   
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
   

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(SYMPTOMPS)):
        
        for z in psymptoms:
            if(z==SYMPTOMPS[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
#RANDOM FOREST (PREDICTION2)

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(SYMPTOMPS)):
        for z in psymptoms:
            if(z== SYMPTOMPS[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")

#NAIVES BAYES (PREDICTION3)
def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
   

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(SYMPTOMPS)):
        for z in psymptoms:
            if(z==SYMPTOMPS[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

#main gui------------------------------------------------------------------------------------

root = Tk()

def open_img(): 
        x=openfn()

        img = Image.open(x)  
        img = img.resize((250, 250), Image.ANTIALIAS) 
        img = ImageTk.PhotoImage(img) 
        print(img)
   
        panel = Label(root, image = img)  
        panel.image = img 
        panel.grid(row = 3) 

def openfn():
    filename = filedialog.askopenfilename(title ='open')
    return filename

def openNewWindow(): 
      
    newWindow = Toplevel(root) 
    root.resizable(width = True, height = True)
    newWindow.title("Image Disease Prediction") 
    newWindow.geometry("500x300") 
    Label(newWindow,  text ="Please Upload Patient Image").pack()
   
    btn = Button(newWindow, text ='open image', command = open_img ).pack()
    btn.grid(row = 1, column=3) 
    root.mainloop()

    

   


     


Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name_Surname = StringVar()
Height= IntVar()
Weight = IntVar()
Gender = StringVar()
Gender.set(None)
Age = IntVar()
Age.set(None)




w2 = Label(root, justify=LEFT, text="PATIENT", fg="red")
w2.config(font=("Elephant", 12))
w2.grid(row=1, column=0, columnspan=1, padx=100)


w2 = Label(root, justify=LEFT, text="Name Surname:", fg="black")
w2.config(font=("Elephant", 12))
w2.grid(row=2, column=0, columnspan=2, padx=100)

t1 = Text(root, height=1, width=20,fg="black")
t1.grid(row=2, column=1, padx=10)



w2 = Label(root, justify=LEFT, text="Height:", fg="black")
w2.config(font=("Elephant", 12))
w2.grid(row=3, column=0, columnspan=2, padx=100)

t1 = Text(root, height=1, width=20,fg="black")
t1.grid(row=3, column=1, padx=10)

w2 = Label(root, justify=LEFT, text="Weight:", fg="black")
w2.config(font=("Elephant", 12))
w2.grid(row=4, column=0, columnspan=2, padx=100)

t1 = Text(root, height=1, width=20,fg="black")
t1.grid(row=4, column=1, padx=10)



S1Lb = Label(root,  text="     Big/Small Tension:", fg="black")
S1Lb.grid(row=11, column=1, padx=10, sticky=W)

t1 = Text(root, height=1, width=10,fg="black")
t1.grid(row=11, column=1, padx=10)

S2Lb = Label(root, text="      Pulsation:", fg="black",)
S2Lb.grid(row=12, column=1, pady=10, sticky=W)

t1 = Text(root, height=1, width=10,fg="black")
t1.grid(row=12, column=1, padx=10)

S2Lb = Label(root, text="     Temperature:", fg="black",)
S2Lb.grid(row=13, column=1, pady=10, sticky=W)

t1 = Text(root, height=1, width=10,fg="black")
t1.grid(row=13, column=1, padx=10)

S2Lb = Label(root, text="     Respiration Rate", fg="black",)
S2Lb.grid(row=14, column=1, pady=10, sticky=W)

t1 = Text(root, height=1, width=10,fg="black")
t1.grid(row=14, column=1, padx=10)

S2Lb = Label(root, text="     Cholestrol:", fg="black",)
S2Lb.grid(row=15, column=1, pady=10, sticky=W)

t1 = Text(root, height=1, width=10,fg="black")
t1.grid(row=15, column=1, padx=10)

OPTIONS3= sorted(AGE)
OPTIONS2= sorted(GENDER)
OPTIONS = sorted(SYMPTOMPS)

GLb = Label(root, text="Gender:", fg="black")
GLb.config(font=("Elephant", 12))
GLb.grid(row=5, column=1, pady=10, sticky=W)

GEn = OptionMenu(root, Gender,*OPTIONS2)
GEn.grid(row=5, column=1, columnspan=2)

ALb = Label(root, text="Age:", fg="black")
ALb.config(font=("Elephant", 12))
ALb.grid(row=6, column=1, pady=10, sticky=W)

S0En = OptionMenu(root, Age,*OPTIONS3)
S0En.grid(row=6, column=1, columnspan=2)

S1Lb = Label(root, text="Symptom 1:", fg="black")
S1Lb.grid(row=6, column=0, pady=10, sticky=W)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=0)

S2Lb = Label(root, text="Symptom 2:", fg="black",)
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=9, column=0)

S3Lb = Label(root, text="Symptom 3:", fg="black")
S3Lb.grid(row=10, column=0, pady=10, sticky=W)
S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=11, column=0)

S4Lb = Label(root, text="Symptom 4:", fg="black")
S4Lb.grid(row=12, column=0, pady=10, sticky=W)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=13, column=0)

S5Lb = Label(root, text="Symptom 5:", fg="black")
S5Lb.grid(row=14, column=0, pady=10, sticky=W)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=15, column=0)




lrLb = Label(root, text="                                                      Predction1:", fg="white", bg="red")
lrLb.grid(row=16, column=0, pady=10,sticky=W)


dst = Button(root, text="Prediction1", command=DecisionTree,fg="blue")
dst.grid(row=16, column=3,padx=10)

t1 = Text(root, height=1, width=40,fg="black")
t1.grid(row=16, column=1, padx=10)

destreeLb = Label(root, text="                                                     Prediction2:", fg="white", bg="red")
destreeLb.grid(row=17, column=0, pady=10, sticky=W)


rnf = Button(root, text="Prediction2", command=randomforest,fg="blue")
rnf.grid(row=17, column=3,padx=10)

t2 = Text(root, height=1, width=40,fg="black")
t2.grid(row=17, column=1 , padx=10)

ranfLb = Label(root, text="                                                     Prediction3:", fg="white", bg="red")
ranfLb.grid(row=18, column=0, pady=5, sticky=W)

lr = Button(root, text="Prediction3", command=NaiveBayes,fg="blue")
lr.grid(row=18, column=3,padx=10)

t3 = Text(root, height=1, width=40,fg="black")
t3.grid(row=18, column=1 , padx=10)

rnf = Button(root, text="GO TO IMAGE DISEASE PREDICTION PAGE", command= openNewWindow ,fg="blue")
rnf.grid(row=1, column=3,padx=10)

rnf = Button(root, text="PREDICT FOR IMAGE",fg="blue")
rnf.grid(row=5, column=3,padx=10)



rnf1 = Button(root, text="SAVE",fg="blue")
rnf1.grid(row=7, column=3,padx=10)
root.mainloop()
