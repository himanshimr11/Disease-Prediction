from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd

l1 = ['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
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

# Disease list
disease = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
           'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
           'Migraine','Cervical spondylosis',
           'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
           'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
           'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
           'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
           'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
           'Impetigo']

# Initialize symptom list
l2 = [0] * len(l1)

# TESTING DATA df -------------------------------------------------------------------------------------
df = pd.read_csv(r"C:\Users\hp\Downloads\Training.csv")
df.replace({'prognosis': {d: idx for idx, d in enumerate(disease)}}, inplace=True)
X = df[l1]
y = df[["prognosis"]]
np.ravel(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr = pd.read_csv(r"C:\Users\hp\Downloads\Testing.csv")
tr.replace({'prognosis': {d: idx for idx, d in enumerate(disease)}}, inplace=True)
X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X, np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if predicted == a:
            h = 'yes'
            break

    # Patient name and age retrieval
    patient_name = Name.get()
    patient_age = Age.get()

    if h == 'yes':
        t2.delete("1.0", END)
        t2.insert(END, f"{disease[a]} (Patient: {patient_name}, Age: {patient_age})")
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")

# Function to filter symptom list based on user input
def filter_symptoms(event, combobox, all_symptoms):
    search_term = combobox.get().lower()
    filtered_symptoms = [symptom for symptom in all_symptoms if symptom.lower().startswith(search_term)]
    combobox['values'] = filtered_symptoms
    if search_term == "":
        combobox['values'] = all_symptoms

# GUI setup
root = Tk()
root.configure(background='#D8BFD8')

# Entry variables
Symptom1 = StringVar()
Symptom2 = StringVar()
Symptom3 = StringVar()
Symptom4 = StringVar()
Symptom5 = StringVar()
Name = StringVar()
Age = StringVar()

# Heading
w2 = Label(root, justify=LEFT, text="Disease Predictor using Machine Learning", fg="black")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

# Labels
NameLb = Label(root, text="Name of the Patient-", fg="white", bg="#191970")
NameLb.grid(row=6, column=0, pady=16, sticky=W)

AgeLb = Label(root, text="Age of the Patient-", fg="white", bg="#191970")  # Age Label
AgeLb.grid(row=7, column=0, pady=10, sticky=W)

S1Lb = Label(root, text="Symptom 1", fg="black", bg="#87CEEB")
S1Lb.grid(row=8, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="black", bg="#87CEEB")
S2Lb.grid(row=9, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="black", bg="#87CEEB")
S3Lb.grid(row=10, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="black", bg="#87CEEB")
S4Lb.grid(row=11, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="black", bg="#87CEEB")
S5Lb.grid(row=12, column=0, pady=10, sticky=W)

destreeLb = Label(root, text="You are detected with : ", fg="white", bg="#191970")
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

# Entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

AgeEn = Entry(root, textvariable=Age)  # Age Entry
AgeEn.grid(row=7, column=1)

# Use ttk.Combobox with filter for symptoms
Symptom1En = ttk.Combobox(root, textvariable=Symptom1, values=OPTIONS, state="normal")
Symptom1En.grid(row=8, column=1)
Symptom1En.bind('<KeyRelease>', lambda event: filter_symptoms(event, Symptom1En, OPTIONS))

Symptom2En = ttk.Combobox(root, textvariable=Symptom2, values=OPTIONS, state="normal")
Symptom2En.grid(row=9, column=1)
Symptom2En.bind('<KeyRelease>', lambda event: filter_symptoms(event, Symptom2En, OPTIONS))

Symptom3En = ttk.Combobox(root, textvariable=Symptom3, values=OPTIONS, state="normal")
Symptom3En.grid(row=10, column=1)
Symptom3En.bind('<KeyRelease>', lambda event: filter_symptoms(event, Symptom3En, OPTIONS))

Symptom4En = ttk.Combobox(root, textvariable=Symptom4, values=OPTIONS, state="normal")
Symptom4En.grid(row=11, column=1)
Symptom4En.bind('<KeyRelease>', lambda event: filter_symptoms(event, Symptom4En, OPTIONS))

Symptom5En = ttk.Combobox(root, textvariable=Symptom5, values=OPTIONS, state="normal")
Symptom5En.grid(row=12, column=1)
Symptom5En.bind('<KeyRelease>', lambda event: filter_symptoms(event, Symptom5En, OPTIONS))

# Search Button
rnf = Button(root, text="SEARCH", command=randomforest, bg="#483D8B", fg="white")
rnf.grid(row=13, column=3, padx=10)

# Text area for result
t2 = Text(root, height=2, width=40, bg="lavender", fg="black")
t2.grid(row=17, column=1, padx=10)

root.mainloop()
