
import tkinter as tk
from tkinter import ttk, messagebox
import random
from PIL import Image, ImageTk
import pygame

def reda_muzica():
    pygame.mixer.init()
    pygame.mixer.music.load("C:\Proiect_Python\GYM_music.mp3")
    pygame.mixer.music.set_volume(0.5)  # Ajustează volumul
    pygame.mixer.music.play(-1)  # -1 înseamnă că melodia va fi redată în mod repetat

def opreste_muzica():
    pygame.mixer.music.stop()
# Inițializare profil utilizator cu valori implicite
profil_utilizator = {
    'nume': '',
    'varsta': 0,
    'inaltime': 0,
    'greutate': 0,
    'gen': 'barbat',
    'nivel_activitate': 1.5,
}
optiuni_nivel_activitate = ['1', '1.3', '1.5', '1.7', '2']

# Funcție pentru calculul BMI
def calculeaza_bmi(profil_utilizator):
    inaltime_in_metri = profil_utilizator['inaltime'] / 100
    bmi = profil_utilizator['greutate'] / (inaltime_in_metri ** 2)
    return round(bmi, 2)

# Funcție pentru calculul aportului caloric zilnic
def calculeaza_calorii(profil_utilizator):
    bmi = calculeaza_bmi(profil_utilizator)
    calorii = 0

    if profil_utilizator['gen'] == 'barbat':
        calorii = 88.362 + (13.397 * profil_utilizator['greutate']) + \
                    (4.799 * profil_utilizator['inaltime']) - (5.677 * bmi)
    else:
        calorii = 447.593 + (9.247 * profil_utilizator['greutate']) + \
                    (3.098 * profil_utilizator['inaltime']) - (4.330 * bmi)

    # Ține cont de nivelul de activitate
    calorii *= profil_utilizator['nivel_activitate']

    if gen1_var.get() == 'Doresc să slăbesc.':
        calorii -= 500  # Reducerea cu 500 de calorii zilnic pentru a slăbi în jur de 0.5 kg/săptămână
    elif gen1_var.get() == 'Doresc să îmi dezvolt masa musculară.':
        calorii += 300  # Adăugarea a 300 de calorii zilnic pentru creșterea masei musculare
    return round(calorii)

# Funcție pentru generarea unei rutine zilnice de antrenament
def genereaza_rutina_antrenament(tip_corp_ales, vreau_sa_slabesc):
    rutina_antrenament = []

    if vreau_sa_slabesc:
        rutina_antrenament.extend([
            'Cardio - 30 de minute de alergare',
            'Skipping - 3 seturi de 50 de repetări',
            'Plank - 3 seturi de 45 de secunde',
            'Yoga sau Pilates - 1 oră',
        ])
    else:
        if "athlete" in tip_corp_ales:
            rutina_antrenament.extend([
                'Flotări - 3 seturi de 12 repetări',
                'Squat-uri - 3 seturi de 12 repetări',
                'Jumping Jacks - 3 seturi de 30 de secunde',
                'Plank - 3 seturi de 60 de secunde',
            ])
        if "hero" in tip_corp_ales:
            rutina_antrenament.extend([
               'Deadlifts - 3 seturi de 10 repetări',
               'Bench Press - 3 seturi de 10 repetări',
               'Pull-ups - 3 seturi de 8 repetări',
               'Leg Press - 3 seturi de 12 repetări',
            ])
        if "bodybuilder" in tip_corp_ales:
            rutina_antrenament.extend([
               'Barbell Curls - 4 seturi de 8 repetări',
               'Triceps Dips - 4 seturi de 10 repetări',
               'Lateral Raises - 4 seturi de 12 repetări',
               'Hammer Curls - 4 seturi de 10 repetări',
            ])
    
    return rutina_antrenament




# Funcție pentru obținerea unui sfat de fitness zilnic
def obtine_sfat_fitness(tip_corp_ales, vreau_sa_slabesc):
    sfaturi = {
        "athlete": [
            'Bea multă apă pentru a rămâne hidratat.',
            'Găsește un partener de antrenament pentru a rămâne responsabil.',
        ],
        "hero": [
            'Folosește greutăți mai mari pentru progres.',
            'Odihnește-te suficient pentru recuperare.',
        ],
        "bodybuilder": [
            'Concentrează-te pe izolare și contracția musculară.',
            'Mănâncă suficient pentru a susține creșterea musculară.',
        ]
    }

    if vreau_sa_slabesc:
        return "Fă exerciții cardio regulate și urmează un regim alimentar echilibrat, de deficit caloric."
    elif "Doresc să îmi dezvolt masa musculară." in tip_corp_ales:
        return "Folosește greutăți progresiv mai mari pentru antrenamentele de forță și mănâncă în surplus caloric pentru creșterea musculară."
    else:
        return random.choice(sfaturi.get(tip_corp_ales, ["Fă exerciții regulate și mănâncă sănătos."]))


# Funcție pentru obținerea unei provocări fitness zilnice
def obtine_provocare_fitness():
    provocari = [
        'Completează 10 burpees în fiecare dimineață.',
        'Mergi 10.000 de pași în fiecare zi.',
        'Încearcă o nouă clasă de fitness în această săptămână.',
        'Înoată timp de 30 de minute în fiecare zi.',
    ]
    return random.choice(provocari)

# Funcție pentru actualizarea afișajului cu informații de fitness zilnice
def actualizeaza_afisaj():
    profil_utilizator['nume'] = nume_intrare.get()
    
    profil_utilizator['varsta'] = int(varsta_intrare.get())
    profil_utilizator['inaltime'] = int(inaltime_intrare.get())
    profil_utilizator['greutate'] = int(greutate_intrare.get())
    profil_utilizator['gen'] = gen_var.get()
    profil_utilizator['nivel_activitate'] = float(nivel_activitate_var.get())
    tip_corp_ales = tip_corp_var.get()
    
    vreau_sa_slabesc = gen1_var.get() == 'Doresc să slăbesc.'
    sfat_fitness = obtine_sfat_fitness(tip_corp_ales, vreau_sa_slabesc)
     # Obține tipul de corp ales și dacă utilizatorul dorește să slăbească
    tip_corp_ales = tip_corp_var.get()
    vreau_sa_slabesc = gen1_var.get() == 'Doresc să slăbesc.'

    # Obține rutina de antrenament în funcție de tipul de corp și obiectivul utilizatorului
    rutina_antrenament = genereaza_rutina_antrenament(tip_corp_ales, vreau_sa_slabesc)
    rezultat = (
        f"Salut, {profil_utilizator['nume']}!\n\n"
        "🍽️ Aport Caloric Zilnic: {}\n\n"
        f"🏋️‍♂️ BMI: {calculeaza_bmi(profil_utilizator)}\n\n"
        "💪 Rutina de Antrenament:\n{rutina}\n\n"
        "💡 Sfat de Fitness Zilnic: {sfat}\n\n"
        "🏆 Provocare de Fitness Zilnică: {provocare}"
    ).format(
        calculeaza_calorii(profil_utilizator),
        rutina='\n'.join(rutina_antrenament),
        sfat=sfat_fitness,
        provocare=obtine_provocare_fitness()
    )
    rezultat_text.set(rezultat)
    
# Încarcă imaginea pentru background global
try:
    background_image_path = "C:\Proiect_Python\poza_proiectPy2.jpg"
    background_image = Image.open(background_image_path)
    background_image = background_image.resize((500, 650), Image.LANCZOS)
except Exception as e:
    print(f"Eroare încărcare imagine de fundal: {e}")
    background_image = None
    

# Crează fereastra principală
root = tk.Tk()
root.title("Aplicație Zilnică de Fitness")


# Adaugă aceste linii pentru a seta un stil mai atractiv
style = ttk.Style()
style.configure('TLabel', font=('Arial', 10), foreground='black')  # Setează font și culoare pentru etichete
style.configure('TButton', font=('Arial', 10), padding=5)          # Setează font și padding pentru butoane

# Setează dimensiunile ferestrei principale
root.geometry("500x650")

# Adaugă imaginea de fundal (verificăm dacă imaginea a fost încărcată corect)
if background_image:
    tk_background_image = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=tk_background_image)
    background_label.place(relwidth=1, relheight=1)

# Exemplu de utilizare în aplicație
buton_redare_muzica = ttk.Button(root, text="Redare Muzică", command=reda_muzica)
buton_redare_muzica.grid(row=10, column=0, padx=10, pady=10)

buton_oprire_muzica = ttk.Button(root, text="Oprire Muzică", command=opreste_muzica)
buton_oprire_muzica.grid(row=10, column=1, padx=10, pady=10)

nivel_activitate_combobox = ttk.Combobox(root, values=optiuni_nivel_activitate)
nivel_activitate_combobox.set('1.5')  # Setează valoarea implicită

# Buton pentru actualizarea informațiilor
actualizare_buton = ttk.Button(root, text="Actualizare Informații", command=actualizeaza_afisaj)
actualizare_buton.grid(row=9, column=0, columnspan=2, padx=10, pady=10)




# Creare câmpuri de intrare pentru informații despre utilizator
nume_label = ttk.Label(root, text="Nume:")
nume_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
nume_intrare = ttk.Entry(root)
nume_intrare.grid(row=0, column=1, padx=10, pady=5)

varsta_label = ttk.Label(root, text="Vârstă:")
varsta_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
varsta_intrare = ttk.Entry(root)
varsta_intrare.grid(row=1, column=1, padx=10, pady=5)

inaltime_label = ttk.Label(root, text="Înălțime (cm):")
inaltime_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
inaltime_intrare = ttk.Entry(root)
inaltime_intrare.grid(row=2, column=1, padx=10, pady=5)

greutate_label = ttk.Label(root, text="Greutate (kg):")
greutate_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
greutate_intrare = ttk.Entry(root)
greutate_intrare.grid(row=3, column=1, padx=10, pady=5)

gen_label = ttk.Label(root, text="Sex:")
gen_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
gen_var = tk.StringVar()
gen_var.set('barbat')
gen_barbat = ttk.Radiobutton(root, text='Bărbat', variable=gen_var, value='barbat')
gen_barbat.grid(row=4, column=1, padx=10, pady=5, sticky="w")
gen_femeie = ttk.Radiobutton(root, text='Femeie', variable=gen_var, value='femeie')
gen_femeie.grid(row=4, column=2, padx=10, pady=5, sticky="w")

nivel_activitate_label = ttk.Label(root, text="Nivel Activitate:")
nivel_activitate_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
nivel_activitate_var = tk.StringVar()
nivel_activitate_var.set('1.5')
nivel_activitate_intrare = ttk.Entry(root, textvariable=nivel_activitate_var)
nivel_activitate_combobox.grid(row=5, column=1, padx=10, pady=5)


# Adăugare câmp de bifare pentru opțiunea de a slăbi
gen1_var = tk.StringVar()
gen1_var.set('Doresc să slăbesc.')
scadere_greutate_checkbox = ttk.Radiobutton(root, text="Doresc să slăbesc.", variable=gen1_var, value='Doresc să slăbesc.')
scadere_greutate_checkbox.grid(row=6, column=0, padx=10, pady=5)
alege_masa_musculara_checkbox = ttk.Radiobutton(root, text="Doresc să îmi dezvolt masa musculară.", variable=gen1_var, value='Doresc să îmi dezvolt masa musculară.')
alege_masa_musculara_checkbox.grid(row=6, column=1, padx=10, pady=5)


# Campurile cu cele trei tipuri de corp (athlete, hero, bodybuilder)
tip_corp_label = ttk.Label(root, text="Alege tipul de corp:")
tip_corp_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

tip_corp_var = tk.StringVar()
tip_corp_dropdown = ttk.Combobox(root, textvariable=tip_corp_var, values=["athlete", "hero", "bodybuilder"])

def show_hide_tip_corp_dropdown():
    if gen1_var.get() == 'Doresc să îmi dezvolt masa musculară.':
        tip_corp_dropdown.grid(row=7, column=1, padx=10, pady=5)
    else:
        tip_corp_dropdown.grid_forget()  # Hide the dropdown

gen1_var.trace_add('write', lambda *args: show_hide_tip_corp_dropdown())

# Creare widget text pentru afișarea informațiilor
rezultat_text = tk.StringVar()
rezultat_label = ttk.Label(root, textvariable=rezultat_text, wraplength=400, justify="left")
rezultat_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


# Functie pentru afisarea notificarilor
def afiseaza_notificare(mesaj):
    root.attributes('-topmost', 1)
    root.attributes('-topmost', 0)
    root.after(5000, lambda: root.attributes('-topmost', 1))
    messagebox.showinfo("Notificare", mesaj)

# Functie pentru afisarea mesajelor motivationale
def afiseaza_mesaj_motivational():
    mesaje_motivationale = [
        "Fiecare antrenament este un pas înainte către obiectivele tale!",
        "Nu uita să te odihnești! Corpul tău are nevoie de timp pentru recuperare.",
        "Eșecul este doar o oportunitate de a încerca din nou cu mai multă înțelepciune.",
        "Străduiți-vă pentru progres, nu pentru perfecțiune.",
    ]
    afiseaza_notificare(random.choice(mesaje_motivationale))

# Functie pentru a afisa provocarea saptamanala
def afiseaza_provocare_saptamanala():
    messagebox.showinfo("Provocarea Săptămânală", "Concurează cu prietenii pentru a afla cine poate face cei mai mulți pași într-o săptămână.")


# Creare meniu pentru funcționalitățile noi
meniu_nou = tk.Menu(root)
root.config(menu=meniu_nou)

meniu_nou.add_command(label="Notificare Zilnică", command=lambda: afiseaza_notificare("Este timpul pentru antrenament!"))
meniu_nou.add_command(label="Mesaj Motivațional", command=afiseaza_mesaj_motivational)
meniu_nou.add_command(label="Provocarea Săptămânală", command=afiseaza_provocare_saptamanala)


# Rulare aplicație
root.mainloop()