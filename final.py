#importing different libraries 
from tkinter import*
from PIL import Image,ImageTk

#Creating the root variable
#Displaying the root window
root=Tk()
#using some built in functions
root.title("Periodic Table")     

global label

# using different attributes
font_1=("Arial",12)              
current_label = None
current_symbol=None
photo=None

#creating some user defines functions 
def show_label(label_text):     
    global current_label
    if current_label:
        current_label.grid_forget()
    current_label =Label(root, text=label_text,font=myfont_1,borderwidth=1,relief=SOLID)  
    current_label.grid(row=1, column=3,columnspan=4,rowspan=3)
  

def show_symbol(symbol):
    global current_symbol
    if current_symbol:
        current_symbol.grid_forget()

    
    if(symbol=='H'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="limegreen")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Li'or symbol=='Na' or symbol=='K' or symbol=='Rb' or symbol=='Cs' or symbol=='Fr'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="Salmon")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Be'or symbol=='Mg' or symbol=='Ca' or symbol=='Sr' or symbol=='Ba' or symbol=='Ra'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="Sandy Brown")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Sc'or symbol=='Y' or symbol=='Ti' or symbol=='Zr' or symbol=='Hf' or symbol=='Rf' or symbol=='V' or symbol=='Nb' or symbol=='Ta' or symbol=='Db' or symbol=='Cr' or symbol=='Mo' or symbol=='W' or symbol=='Sg' or symbol=='Mn' or symbol=='Tc' or symbol=='Re' or symbol=='Bh' or symbol=='Fe' or symbol=='Ru' or symbol=='Os' or symbol=='Hs' or symbol=='Co' or symbol=='Rh' or symbol=='Ir' or symbol=='Ni' or symbol=='Pd' or symbol=='Pt' or symbol=='Cu' or symbol=='Ag' or symbol=='Au' or symbol=='Zn' or symbol=='Cd' or symbol=='Hg' or symbol=='Cn'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="light goldenrod")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Lu'or symbol=='Lr'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="royalblue2")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Mt'or symbol=='Ds' or symbol=='Rg' or symbol=='Nh' or symbol=='Mc' or symbol=='Lv' or symbol=='Ts' or symbol=='Og'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="light gray")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='B'or symbol=='Si' or symbol=='Ge' or symbol=='As' or symbol=='Sb' or symbol=='Te' or symbol=='At'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="lime green")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Al'or symbol=='Ga' or symbol=='In' or symbol=='Tl' or symbol=='Sn' or symbol=='Pb' or symbol=='Fl' or symbol=='Bi' or symbol=='Po'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="green yellow")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='C'or symbol=='N' or symbol=='O' or symbol=='P' or symbol=='S' or symbol=='Se'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="deep skyblue")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='F'or symbol=='Cl' or symbol=='Br' or symbol=='I'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="medium orchid")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='He'or symbol=='Ne' or symbol=='Ar' or symbol=='Kr' or symbol=='Xe' or symbol=='Rn'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="light slate gray")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='La'or symbol=='Ce' or symbol=='Pr' or symbol=='Nd' or symbol=='Pm' or symbol=='Sm'or symbol=='Eu'or symbol=='Gd' or symbol=='Tb' or symbol=='Dy' or symbol=='Ho' or symbol=='Er' or symbol=='Tm' or symbol=='Yb'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="aquamarine")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
    elif(symbol=='Ac'or symbol=='Th' or symbol=='Pa' or symbol=='U' or symbol=='Np' or symbol=='Pu'or symbol=='Am'or symbol=='Cm' or symbol=='Bk' or symbol=='Cf' or symbol=='Es' or symbol=='Fm' or symbol=='Md' or symbol=='No'):
                  current_symbol=Label(root,text=symbol,font=myfont_2,padx=15,pady=13,borderwidth=1,relief=SOLID,bg="hot pink")
                  current_symbol.grid(row=1,column=6,columnspan=3,rowspan=2)
def show_img(realimage):
        global photo
        photo=PhotoImage(file=realimage)
        image_label=Label(image=photo)
        image_label.grid(row=1,column=8,columnspan=3,rowspan=3)

# Created a function to search different molecules of an element
def show_molecules():
       search_text=entry.get()
        
       if (search_text=="Hydrogen"):
                global pop
                pop=Toplevel(root)
                pop.title("Molecules of the Hydrogen")

                mol_image_label=Label(pop,text="H2O molecule")
                mol_image_label.grid(row=1,column=1)

                image_label=Label(pop)
                image_label.configure(image=h_img)
                image_label.grid(row=2,column=1)

                mol_image_label1=Label(pop,text="H2O2 molecule")
                mol_image_label1.grid(row=1,column=2)

                image_label1=Label(pop)
                image_label1.configure(image=h2o2_img)
                image_label1.grid(row=2,column=2)

                mol_image_label2=Label(pop,text="H2SO4 molecule")
                mol_image_label2.grid(row=3,column=1)

                image_label2=Label(pop)
                image_label2.configure(image=h2so4_img)
                image_label2.grid(row=4,column=1)

                mol_image_label3=Label(pop,text="HCl molecule")
                mol_image_label3.grid(row=3,column=2)

                image_label3=Label(pop)
                image_label3.configure(image=hcl_img)
                image_label3.grid(row=4,column=2)

                mol_image_label4=Label(pop,text="HNO3 molecule")
                mol_image_label4.grid(row=5,column=1)

                image_label4=Label(pop)
                image_label4.configure(image=hno3_img)
                image_label4.grid(row=6,column=1)

                mol_image_label5=Label(pop,text="H2CO3 molecule")
                mol_image_label5.grid(row=5,column=2)

                image_label5=Label(pop)
                image_label5.configure(image=h2co3_img)
                image_label5.grid(row=6,column=2)
       elif (search_text=="Sodium"):
                global pop2
                pop2=Toplevel(root)
                pop2.title("Molecules of the Sodium")

                mol_image_label=Label(pop2,text="NaCl molecule")
                mol_image_label.grid(row=1,column=1)

                image_label=Label(pop2)
                image_label.configure(image=nacl_img)
                image_label.grid(row=2,column=1)

                mol_image_label1=Label(pop2,text="NaHCO3 molecule")
                mol_image_label1.grid(row=1,column=2)

                image_label1=Label(pop2)
                image_label1.configure(image=nahco3_img)
                image_label1.grid(row=2,column=2)

                mol_image_label2=Label(pop2,text="NaOCl molecule")
                mol_image_label2.grid(row=3,column=1)

                image_label2=Label(pop2)
                image_label2.configure(image=naocl_img)
                image_label2.grid(row=4,column=1)

                mol_image_label3=Label(pop2,text="NaOH molecule")
                mol_image_label3.grid(row=3,column=2)

                image_label3=Label(pop2)
                image_label3.configure(image=naoh_img)
                image_label3.grid(row=4,column=2)

                mol_image_label4=Label(pop2,text="NaNO3 molecule")
                mol_image_label4.grid(row=5,column=1)

                image_label4=Label(pop2)
                image_label4.configure(image=nano3_img)
                image_label4.grid(row=6,column=1)

                mol_image_label5=Label(pop2,text="NaNO2 molecule")
                mol_image_label5.grid(row=5,column=2)

                image_label5=Label(pop2)
                image_label5.configure(image=nano2_img)
                image_label5.grid(row=6,column=2)
                
# Photoimage is a built in function which is used to display the images by passing that image as a parameter
h_img=PhotoImage(file="molh.png")
h2o2_img=PhotoImage(file="h2o2.png")
h2so4_img=PhotoImage(file="h2so4.png")
hcl_img=PhotoImage(file="hcl.png")
hno3_img=PhotoImage(file="hno3.png")
h2co3_img=PhotoImage(file="h2co3.png")

nacl_img=PhotoImage(file="nacl.png")
nahco3_img=PhotoImage(file="nahco3.png")
naocl_img=PhotoImage(file="naocl.png")
naoh_img=PhotoImage(file="naoh.png")
nano3_img=PhotoImage(file="nano3.png")
nano2_img=PhotoImage(file="nano2.png")
               
entry=Entry(root)
entry.grid(row=1,column=12,columnspan=2,padx=10,pady=15)

font=("Arial",12)

#created different widgets like buttons and labels
molbutton=Button(root,padx=10,pady=10,text="Search the molecules",command=show_molecules)
molbutton.grid(row=1,column=14,columnspan=2)
newlabel=Label(root,text="Enter the name of the molecule",font=font)
newlabel.grid(row=0,column=11,columnspan=4)
   
def poph(img,imgec):
        global pop

        #Toplevel is a built in function which is used to display the pop up window of that basic root window
        pop=Toplevel(root)
        pop.title("Hydrogen")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Hydrogen:",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Hydrogen:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)

#To show the information about the molecules
def show_infoH():
                infolabel=Label(pop,text="Some uses molecules of the Hydrogen",font=myfont)
                infolabel.grid(row=4,column=1,columnspan=4)
                infolabel1=Label(pop,text="Hydrogen can be used in fuel cells to generate electricity, or power and heat.\n Today, hydrogen is most commonly used in petroleum refining and fertilizer production,\n while transportation and utilities are emerging markets.\nHydrogen is a clean fuel that, when consumed in a fuel cell, produces only water, electricity,\n and heat.\n Hydrogen and fuel cells can play an important role in our national energy strategy,with the\n potential for use in a broad range of applications,across virtually all sectors—transportation, \ncommercial, industrial, residential, and  portable.\n Hydrogen and fuel cells can provide energy for use in diverse applications,\n including distributed or combined-heat-and-power; backup power; \nsystems for storing and enabling renewable energy; portable power;\n auxiliary power for trucks, aircraft, rail, and ships;\n specialty vehicles such as forklifts; and passenger and freight vehicles\n including cars, trucks, and buses.\n",font=myfont,justify="left")
                infolabel1.grid(row=5,column=1,columnspan=4)

def pophe(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Helium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Helium:",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the helium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)

def popli(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Lithium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Lithium:",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Lithium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoli():
                infolabel=Label(pop,text="Some important uses of the Lithium",font=myfont)
                infolabel.grid(row=4,column=1,columnspan=4)
                infolabel1=Label(pop,text="Bromine and lithium chloride together form concentrated brine which absorbs the humidity under high temperature.\n Brine is used in the manufacturing of air conditioning systems.\nAlloys of the metal with manganese, cadmium, copper, and aluminium are used to make aircraft’s parts.\nThe carbonate is used in medicine as an antidepressant and pottery industry.\n",font=myfont,justify="left")
                infolabel1.grid(row=5,column=1,columnspan=4)
#passed two arguments
def popna(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Sodium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Sodium:",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Sodium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoNa():
                infolabel=Label(pop,text="Some important uses of the Sodium",font=myfont)
                infolabel.grid(row=4,column=1,columnspan=4)
                infolabel1=Label(pop,text="It is also used in improving the structure of certain alloys; soaps,\n the purification of molten metals and sodium vapour lamps.\nSodium is a component of sodium chloride, which is a very important \ncompound found in the living environment.\nSodium is important in the manufacturing of organic compounds and in making esters.\nSolid sodium carbonate is required in making glass.\n",font=myfont,justify="left")
                infolabel1.grid(row=5,column=1,columnspan=4)


def popk(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Potassium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Potassium:",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Potassium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infok():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Potassium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="It can be used as a medium of heat exchange and used in nuclear power plants \nbecause of this reason.People use potassium salts as a constituent of fertiliser.\nIt is one of the essential nutrients of the human body.Potassium chloride is also used in injections.\nPotash can be used to make glass and soap etc\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popRb(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Rubidium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Rubidium:",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Rubidium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoRb():
        global infolabel
        infolabel=Label(pop,text="Some important molecules of the Rubidium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Rubidium finds its major application in speciality glasses which are utilized in fibre optics telecommunications \nsystems and in night-vision devices.\n The carbonate of  Rubidium (Rb2CO3) is used as an additive to these types of glass,\n where it reduces electrical conductivity and improves stability and durability. \nRubidium-cesium-antimony coating is commonly applied to the photo-cathodes of photo-multiplier tubes,\n which are used in radiation detection devices,\n medical imaging equipment, and night-vision devices.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popCs(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Caesium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Caesium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Caesium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoCs():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Rubidium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Cesium formate-based drilling fluids are extensively used in extractive oil industry.\nIt is used in thermionic generators which convert heat energy into electrical energy.As the density of cesium is very high, cesium chloride,\n cesium sulphate are widely used in molecular biology.Cesium is used in manufacturing optical glasses\n and other optical instruments.\n It is used to remove oxygen from light bulbs and vacuum tubes.A special application of cesium is that it is used in the manufacturing \nof most accurate atomic clock.\n It is also called as cesium clock.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popFr(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Francium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Francium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Francium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoFr():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Francium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Since francium is produced in tiny quantities in nature,\n it does show any much commercial applications.Francium has been used in the field of research,\n chemistry and also in the atomic structure.\nIt is used for diagnostics for curing cancers.\nIt is also used in many spectroscopic experiments.\nFrancium is a highly radioactive metal, and since it exhibits a short half-life,\n it does not have more impact on the environment.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popBe(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Beryllium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Beryllium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Beryllium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoBe():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the beryllium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Beryllium is used in gears and cogs particularly in the aviation industry.\n Beryllium is a silvery-white metal.\n It is relatively soft and has a low density.\n Beryllium is used in alloys with copper or nickel to make gyroscopes, \nsprings, electrical contacts, spot-welding electrodes and non-sparking tools.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popMg(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Magnesium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Magnesium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Magnesium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoMg():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Magnesium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Magnesium is used in products that benefit from being lightweight,\n such as car seats, luggage, laptops, cameras and power tools.\n It is also added to molten iron and steel to remove sulfur.\n As magnesium ignites easily in air and burns with a bright light, \nit's used in flares, fireworks and sparklers.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popCa(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Calcium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Calcium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Calcium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoCa():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Calcium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Calcium is one of the most important minerals for the human body. \nIt helps form and maintain healthy teeth and bones.\n A proper level of calcium in the body over a lifetime can help prevent osteoporosis.\nCalcium helps your body with: Building strong bones and teeth,\n Clotting blood, Sending and receiving nerve signals, Squeezing and relaxing muscles,\n Releasing hormones and other chemicals ,Keeping a normal heartbeat\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popSr(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Strontium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Strontium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Strontium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoSr():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Strontium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Strontium is best known for the brilliant reds its \nsalts give to fireworks and flares. \nIt is also used in producing ferrite magnets and refining zinc.\n Modern 'glow-in-the-dark' paints and plastics contain strontium aluminate.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popBa(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Barium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Barium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Barium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoBa():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the barium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Barium is not an extensively used element.\n Most is used in drilling fluids for oil and gas wells.\n It is also used in paint and in glassmaking.\n All barium compounds are toxic; \nhowever, barium sulfate is insoluble and so can be safely swallowed.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popRa(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Radium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Radium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Radium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoRa():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Radium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Some of the practical uses of radium are due to its radioactive properties.\n Radium was previously used in the self-luminous paints for watches,\n aircraft switches, nuclear panels clocks, and instrument dials.\n Ra was earlier used as an additive in the products \nlike hair cream, toothpaste, and even food items.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popSc(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Scandium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Scandium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Scandium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoSc():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Scandium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Scandium is mainly used for research purposes.\n It has, however, great potential because it has almost as low a density as aluminium and a much higher melting point.\n An aluminium-scandium alloy has been used in Russian MIG fighter planes, \nhigh-end bicycle frames and baseball bats.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popY(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Yittrium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Yittrium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the yittrium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoY():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Yittrium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Yttrium is often used as an additive in alloys. \nIt increases the strength of aluminium and magnesium alloys.\n It is also used in the making of microwave filters for radar and has been used as a catalyst \nin ethene polymerisation.\n Yttrium-aluminium garnet (YAG) is used in lasers\n that can cut through metals.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popLu(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Lutetium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Lutesium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Lutesium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoLu():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Lutesium:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Yttrium is often used as an additive in alloys.\n It increases the strength of aluminium and magnesium alloys.\n It is also used in the making of microwave filters for radar and has been \nused as a catalyst in ethene polymerisation. \nYttrium-aluminium garnet (YAG) is used in lasers that can cut through metals.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

def popLr(img,imgec):
        global pop
        pop=Toplevel(root)
        pop.title("Lawrencium")
        global labelhec
        labelec=Label(pop,text="Electronic Configuration of the Lawrencium",font=myfont)
        labelec.grid(row=0,column=1)
        global imag
        imag=PhotoImage(file=imgec)
        pic1=Label(pop,image=imag)
        pic1.grid(row=1,column=1)

        global labelh
        labelh=Label(pop,text="Reactions of the Lawrencium:",font=myfont)
        labelh.grid(row=0,column=2)
        global image
        image=PhotoImage(file=img)
        pic=Label(pop,image=image)
        pic.grid(row=1,column=2)
def show_infoLr():
        global infolabel
        infolabel=Label(pop,text="Some important uses of the Lawrenciums:",font=myfont)
        infolabel.grid(row=4,column=1,columnspan=4)
        infolabel1=Label(pop,text="Only a few atoms of lawrencium have ever been made.\n Because of this, there is no commercial use for this element.\n Its only use is for research within a laboratory.\n Most actinides are used for their radioactive properties.\n",font=myfont,justify="left")
        infolabel1.grid(row=5,column=1,columnspan=4)

myfont_2=("Arial",20) 

myfont_1=("Arial",16)
myfont=("Arial",12)

#Created different buttons to display all elements from the periodic table

button_H=Button(root,text="H",padx=19,pady=20,command=lambda:(show_label("Hydrogen\nAtomic No.=1\nAtomic Mass No. =1.00784\nAlkali metal\nPosition='s'Block"),show_symbol("H"),poph('h.png','hec.png'),show_img('realh.png'),show_infoH()),font=myfont,bg="limegreen")
button_Li=Button(root,text="Li",padx=18,pady=20,command=lambda:(show_label("Lithium\nAtomic No.=3\nAtomic mass=6.941\nAlkali metal\nPosition='s'Block"),show_symbol("Li"),popli('li.png','liec.png'),show_img('realli.png'),show_infoli()),font=myfont,bg="salmon")
button_Na=Button(root,text="Na",padx=15,pady=20,command=lambda:(show_label("Sodium\nAtomic No.=11\nAtomic mass=22.98977\nAlkali metal\nPosition='s'Block"),show_symbol("Na"),popna('Na.png','naec.png'),show_img('realna.png'),show_infoNa()),font=myfont,bg="salmon")
button_K=Button(root,text="K",padx=19,pady=20,font=myfont,command=lambda:(show_label("Potassium\nAtomic No.=19\nAtomic mass=39.0983\nAlkali metal\nPosition='s'Block"),show_symbol("K"),popk('k.png','kec.png'),show_img('realk.png'),show_infok()),bg="salmon")
button_Rb=Button(root,text="Rb",padx=14,pady=20,font=myfont,command=lambda:(show_label("Rubidium\nAtomic No.=37\nAtomic mass=85.4678\nAlkali metal\nPosition='s'Block"),show_symbol("Rb"),popRb('Rb.png','Rbec.png'),show_img('realRb.png'),show_infoRb()),bg="salmon")
button_Cs=Button(root,text="Cs",padx=14,pady=20,font=myfont,command=lambda:(show_label("Cesium\nAtomic No.=55\nAtomic mass=132.9045\nAlkali metal\nPosition='s'Block"),show_symbol("Cs"),popCs('Cs.png','Csec.png'),show_img('realCs.png'),show_infoCs()),bg="salmon")
button_Fr=Button(root,text="Fr",padx=17,pady=20,font=myfont,command=lambda:(show_label("Francium\nAtomic No.=87\nAtomic mass=223\nAlkali metal\nPosition='s'Block"),show_symbol("Fr"),popFr('Fr.png','Frec.png'),show_img('realFr.png'),show_infoFr()),bg="salmon")

button_Be=Button(root,text="Be",padx=18,pady=20,font=myfont,command=lambda:(show_label("Beryllium\nAtomic No.=4\nAtomic mass=9.01218\nAlkaline Earth Metal\nPosition-'s'Block"),show_symbol("Be"),popBe('be.png','Beec.png'),show_img('realBe.png'),show_infoBe()),bg="sandy brown")
button_Mg=Button(root,text="Mg",padx=17,pady=20,font=myfont,command=lambda:(show_label("Magnesium\nAtomic No.=12\nAtomic mass=24.305\nAlkaline Earth Metal\nPosition-'s'Block"),show_symbol("Mg"),popMg('Mg.png','Mgec.png'),show_img('realMg.png'),show_infoMg()),bg="sandy brown")
button_Ca=Button(root,text="Ca",padx=18,pady=20,font=myfont,command=lambda:(show_label("Calcium\nAtomic No.=20\nAtomic mass=40.08\nAlkaline Earth Metal\nPosition-'s'Block"),show_symbol("Ca"),popCa('Ca.png','Caec.png'),show_img('realCa.png'),show_infoCa()),bg="sandy brown")
button_Sr=Button(root,text="Sr",padx=21,pady=20,font=myfont,command=lambda:(show_label("Strontuim\nAtomic No.=38\nAtomic mass=87.62\nAlkaline Earth Metal\nPosition-'s'Block"),show_symbol("Sr"),popSr('Sr.png','Srec.png'),show_img('realSr.png'),show_infoSr()),bg="sandy brown")
button_Ba=Button(root,text="Ba",padx=19,pady=20,font=myfont,command=lambda:(show_label("Barium\nAtomic No.=56\nAtomic mass=137.33\nAlkaline Earth Metal\nPosition-'s'Block"),show_symbol("Ba"),popBa('Ba.png','Baec.png'),show_img('realBa.png'),show_infoBa()),bg="sandy brown")
button_Ra=Button(root,text="Ra",padx=19,pady=20,font=myfont,command=lambda:(show_label("Radium\nAtomic No.=88\nAtomic mass=226.0254\nAlkaline Earth Metal\nPosition-'s'Block"),show_symbol("Ra"),popRa('Ra.png','Raec.png'),show_img('realRa.png'),show_infoRa()),bg="sandy brown")

button_Sc=Button(root,text="Sc",padx=20,pady=20,font=myfont,command=lambda:(show_label("Scandium\nAtomic No.=21\nAtomic mass=44.9559\nTransition Metal\nPosition-'d'Block"),show_symbol("Sc"),popSc('Scec.png','Sc.png'),show_img('realSc.png'),show_infoSc()),bg="light goldenrod")
button_Y=Button(root,text="Y",padx=25,pady=20,font=myfont,command=lambda:(show_label("Yitrium\nAtomic No.=39\nAtomic mass=88.9059\nTransition Metal\nPosition-'d'Block"),show_symbol("Y"),popY('Yec.png','Y.png'),show_img('realY.png'),show_infoY()),bg="light goldenrod")
button_Lu1=Button(root,text="Lu",padx=21,pady=20,font=myfont,command=lambda:(show_label("Lutetium\nAtomic No.=71\nAtomic mass=174.967\nTransition Metal\nPosition-'d'Block"),show_symbol("Lu"),popLu('Luec.png','Lu.png'),show_img('realLu.png'),show_infoLu()),bg="royalblue2")
button_Lr1=Button(root,text="Lr",padx=23,pady=20,font=myfont,command=lambda:(show_label("Lawrencium\nAtomic No.=103\nAtomic mass=260\nTransition Metal\nPosition-'d'Block"),show_symbol("Lr"),popLr('Lr.png','Lrec.png'),show_img('realLr.png'),show_infoLr()),bg="royalblue2")

button_Ti=Button(root,text="Ti",padx=23,pady=20,font=myfont,command=lambda:(show_label("Titanium\nAtomic No.=22\nAtomic mass=47.90\nTransition Metal\nPosition-'d'Block"),show_symbol("Ti"),show_img('realTi.png')),bg="light goldenrod")
button_Zr=Button(root,text="Zr",padx=23,pady=20,font=myfont,command=lambda:(show_label("Zirconium\nAtomic No.=40\nAtomic mass=91.22\nTransition Metal\nPosition-'d'Block"),show_symbol("Zr"),show_img('realZr.png')),bg="light goldenrod")
button_Hf=Button(root,text="Hf",padx=22,pady=20,font=myfont,command=lambda:(show_label("Hafnium\nAtomic No.=72\nAtomic mass=178.49\nTransition Metal\nPosition-'d'Block"),show_symbol("Hf"),show_img('realHf.png')),bg="light goldenrod")
button_Rf=Button(root,text="Rf",padx=22,pady=20,font=myfont,command=lambda:(show_label("Rutherfordium\nAtomic No.=104\nAtomic mass=261\nTransition Metal\nPosition-'d'Block"),show_symbol("Rf"),show_img('realRf.png')),bg="light goldenrod")

button_V=Button(root,text="V",padx=24,pady=20,font=myfont,command=lambda:(show_label("Vanadium\nAtomic No.=23\nAtomic mass=50.9415\nTransition Metal\nPosition-'d'Block"),show_symbol("V"),show_img('realV.png')),bg="light goldenrod")
button_Nb=Button(root,text="Nb",padx=19,pady=20,font=myfont,command=lambda:(show_label("Niobium\nAtomic No.=41\nAtomic mass=92.9064\nTransition Metal\nPosition-'d'Block"),show_symbol("Nb"),show_img('realNb.png')),bg="light goldenrod")
button_Ta=Button(root,text="Ta",padx=20,pady=20,font=myfont,command=lambda:(show_label("Tantalum\nAtomic No.=73\nAtomic mass=180.9479\nTransition Metal\nPosition-'d'Block"),show_symbol("Ta"),show_img('realTa.png')),bg="light goldenrod")
button_Db=Button(root,text="Db",padx=19,pady=20,font=myfont,command=lambda:(show_label("Dubnium\nAtomic No.=105\nAtomic mass=262\nTransition Metal\nPosition-'d'Block"),show_symbol("Db"),show_img('realDb.png')),bg="light goldenrod")

button_Cr=Button(root,text="Cr",padx=21,pady=20,font=myfont,command=lambda:(show_label("Chromium\nAtomic No.=24\nAtomic mass=51.996\nTransition Metal\nPosition-'d'Block"),show_symbol("Cr"),show_img('realCr.png')),bg="light goldenrod")
button_Mo=Button(root,text="Mo",padx=18,pady=20,font=myfont,command=lambda:(show_label("Molybdenum\nAtomic No.=42\nAtomic mass=95.94\nTransition Metal\nPosition-'d'Block"),show_symbol("Mo"),show_img('realMo.png')),bg="light goldenrod")
button_W=Button(root,text="W",padx=22,pady=20,font=myfont,command=lambda:(show_label("Tunsten\nAtomic No.=74\nAtomic mass=183.85\nTransition Metal\nPosition-'d'Block"),show_symbol("W"),show_img('realW.png')),bg="light goldenrod")
button_Sg=Button(root,text="Sg",padx=19,pady=20,font=myfont,command=lambda:(show_label("Seaborgium\nAtomic No.=106\nAtomic mass=263\nTransition Metal\nPosition-'d'Block"),show_symbol("Sg"),show_img('realSg.png')),bg="light goldenrod")

button_Mn=Button(root,text="Mn",padx=21,pady=20,font=myfont,command=lambda:(show_label("Manganese\nAtomic No.=25\nAtomic mass=54.938\nTransition Metal\nPosition-'d'Block"),show_symbol("Mn"),show_img('realMn.png')),bg="light goldenrod")
button_Tc=Button(root,text="Tc",padx=23,pady=20,font=myfont,command=lambda:(show_label("Techneium\nAtomic No.=43\nAtomic mass=98\nTransition Metal\nPosition-'d'Block"),show_symbol("Tc"),show_img('realTc.png')),bg="light goldenrod")
button_Re=Button(root,text="Re",padx=21,pady=20,font=myfont,command=lambda:(show_label("Rhenium\nAtomic No.=75\nAtomic mass=186.207\nTransition Metal\nPosition-'d'Block"),show_symbol("Re"),show_img('realRe.png')),bg="light goldenrod")
button_Bh=Button(root,text="Bh",padx=22,pady=20,font=myfont,command=lambda:(show_label("Bohrium\nAtomic No.=107\nAtomic mass=262\nTransition Metal\nPosition-'d'Block"),show_symbol("Bh"),show_img('realBh.png')),bg="light goldenrod")

button_Fe=Button(root,text="Fe",padx=22,pady=20,font=myfont,command=lambda:(show_label("Iron\nAtomic No.=26\nAtomic mass=55.847\nTransition Metal\nPosition-'d'Block"),show_symbol("Fe"),show_img('realFe.png')),bg="light goldenrod")
button_Ru=Button(root,text="Ru",padx=22,pady=20,font=myfont,command=lambda:(show_label("Ruthenium\nAtomic No.=44\nAtomic mass=101.07\nTransition Metal\nPosition-'d'Block"),show_symbol("Ru"),show_img('realRu.png')),bg="light goldenrod")
button_Os=Button(root,text="Os",padx=21,pady=20,font=myfont,command=lambda:(show_label("Osmium\nAtomic No.=76\nAtomic mass=190.2\nTransition Metal\nPosition-'d'Block"),show_symbol("Os"),show_img('realOs.png')),bg="light goldenrod")
button_Hs=Button(root,text="Hs",padx=22,pady=20,font=myfont,command=lambda:(show_label("Hassium\nAtomic No.=108\nAtomic mass=255\nTransition Metal\nPosition-'d'Block"),show_symbol("Hs"),show_img('realHs.png')),bg="light goldenrod")

button_Co=Button(root,text="Co",padx=22,pady=20,font=myfont,command=lambda:(show_label("Cobalt\nAtomic No.=27\nAtomic mass=58.9332\nTransition Metal\nPosition-'d'Block"),show_symbol("Co"),show_img('realCo.png')),bg="light goldenrod")
button_Rh=Button(root,text="Rh",padx=23,pady=20,font=myfont,command=lambda:(show_label("Rhodium\nAtomic No.=45\nAtomic mass=102.9055\nTransition Metal\nPosition-'d'Block"),show_symbol("Rh"),show_img('realRh.png')),bg="light goldenrod")
button_Ir=Button(root,text="Ir",padx=28,pady=20,font=myfont,command=lambda:(show_label("Iridium\nAtomic No.=77\nAtomic mass=192.22\nTransition Metal\nPosition-'d'Block"),show_symbol("Ir"),show_img('realIr.png')),bg="light goldenrod")
button_Mt=Button(root,text="Mt",padx=24,pady=20,font=myfont,command=lambda:(show_label("Meitnerium\nAtomic No.=109\nAtomic mass=256\nTransition Metal\nPosition-'d'Block"),show_symbol("Mt"),show_img('realMt.png')),bg="light gray")

button_Ni=Button(root,text="Ni",padx=23,pady=20,font=myfont,command=lambda:(show_label("Nickel\nAtomic No.=28\nAtomic mass=58.70\nTransition Metal\nPosition-'d'Block"),show_symbol("Ni"),show_img('realNi.png')),bg="light goldenrod")
button_Pd=Button(root,text="Pd",padx=21,pady=20,font=myfont,command=lambda:(show_label("Palladium\nAtomic No.=46\nAtomic mass=106.4\nTransition Metal\nPosition-'d'Block"),show_symbol("Pd"),show_img('realPd.png')),bg="light goldenrod")
button_Pt=Button(root,text="Pt",padx=24,pady=20,font=myfont,command=lambda:(show_label("Platinum\nAtomic No.=78\nAtomic mass=195.09\nTransition Metal\nPosition-'d'Block"),show_symbol("Pt"),show_img('realPt.png')),bg="light goldenrod")
button_Ds=Button(root,text="Ds",padx=21,pady=20,font=myfont,command=lambda:(show_label("Darmstadtium\nAtomic No.=110\nAtomic mass=281\nTransition Metal\nPosition-'d'Block"),show_symbol("Ds"),show_img('realDs.png')),bg="light gray")

button_Cu=Button(root,text="Cu",padx=22,pady=20,font=myfont,command=lambda:(show_label("Copper\nAtomic No.=29\nAtomic mass=63.546\nTransition Metal\nPosition-'d'Block"),show_symbol("Cu"),show_img('realCu.png')),bg="light goldenrod")
button_Ag=Button(root,text="Ag",padx=22,pady=20,font=myfont,command=lambda:(show_label("Silver\nAtomic No.=47\nAtomic mass=107.868\nTransition Metal\nPosition-'d'Block"),show_symbol("Ag"),show_img('realAg.png')),bg="light goldenrod")
button_Au=Button(root,text="Au",padx=22,pady=20,font=myfont,command=lambda:(show_label("Gold\nAtomic No.=79\nAtomic mass=196.9665\nTransition Metal\nPosition-'d'Block"),show_symbol("Au"),show_img('realAu.png')),bg="light goldenrod")
button_Rg=Button(root,text="Rg",padx=22,pady=20,font=myfont,command=lambda:(show_label("Roentgenium\nAtomic No.=111\nAtomic mass=272\nTransition Metal\nPosition-'d'Block"),show_symbol("Rg"),show_img('realRg.png')),bg="light gray")

button_Zn=Button(root,text="Zn",padx=22,pady=20,font=myfont,command=lambda:(show_label("Zinc\nAtomic No.=30\nAtomic mass=65.38\nTransition Metal\nPosition-'d'Block"),show_symbol("Zn"),show_img('realZn.png')),bg="light goldenrod")
button_Cd=Button(root,text="Cd",padx=20,pady=20,font=myfont,command=lambda:(show_label("Cadmium\nAtomic No.=48\nAtomic mass=112.41\nTransition Metal\nPosition-'d'Block"),show_symbol("Cd"),show_img('realCd.png')),bg="light goldenrod")
button_Hg=Button(root,text="Hg",padx=21,pady=20,font=myfont,command=lambda:(show_label("Mercury\nAtomic No.=80\nAtomic mass=200.59\nTransition Metal\nPosition-'d'Block"),show_symbol("Hg"),show_img('realHg.png')),bg="light goldenrod")
button_Cn=Button(root,text="Cn",padx=21,pady=20,font=myfont,command=lambda:(show_label("Copernicium\nAtomic No.=112\nAtomic mass=277\nTransition Metal\nPosition-'d'Block"),show_symbol("Cn"),show_img('realHg.png')),bg="light goldenrod")

button_B=Button(root,text="B",padx=24,pady=20,font=myfont,command=lambda:(show_label("Boron\nAtomic No.=5\nAtomic mass=10.81\nMetelloid\nposition-'p'Block"),show_symbol("B"),show_img('realB.png')),bg="lime green")
button_Al=Button(root,text="Al",padx=22,pady=20,font=myfont,command=lambda:(show_label("Aluminium\nAtomic No.=13\nAtomic mass=132.9045\nMetal\n'P'Block"),show_symbol("Al"),show_img('realAl.png')),bg="green yellow")
button_Ga=Button(root,text="Ga",padx=19,pady=20,font=myfont,command=lambda:(show_label("Gallium\nAtomic No.=31\nAtomic mass=69.72\nMetal\n'p'Block"),show_symbol("Ga"),show_img('realGa.png')),bg="green yellow")
button_In=Button(root,text="In",padx=24,pady=20,font=myfont,command=lambda:(show_label("Indium\nAtomic No.=49\nAtomic mass=114.82\nMetal\n'p'Block"),show_symbol("In"),show_img('realIn.png')),bg="green yellow")
button_Tl=Button(root,text="Tl",padx=23,pady=20,font=myfont,command=lambda:(show_label("Thallium\nAtomic No.=81\nAtomic mass=204.37\nMetal\n'p'Block"),show_symbol("Tl"),show_img('realTl.png')),bg="green yellow")
button_Nh=Button(root,text="Nh",padx=20,pady=20,font=myfont,command=lambda:(show_label("Nihonium\nAtomic No.=113\nAtomic mass=286\nRadioactive\nPosition-'p'Block"),show_symbol("Nh"),show_img('realNh.png')),bg="light gray")

button_C=Button(root,text="C",padx=25,pady=20,font=myfont,command=lambda:(show_label("Carbon\nAtomic No.=6\nAtomic mass=12.011"),show_symbol("C"),show_img('realC.png')),bg="deep skyblue")
button_Si=Button(root,text="Si",padx=23,pady=20,font=myfont,command=lambda:(show_label("Silicon\nAtomic No.=14\nAtomic mass=28.0855\nMetelloid\n'p'Block"),show_symbol("Si"),show_img('realSi.png')),bg="lime green")
button_Ge=Button(root,text="Ge",padx=20,pady=20,font=myfont,command=lambda:(show_label("Germanium\nAtomic No.=32\nAtomic mass=72.59\nMetelloid\n'p'Block"),show_symbol("Ge"),show_img('realGe.png')),bg="lime green")
button_Sn=Button(root,text="Sn",padx=21,pady=20,font=myfont,command=lambda:(show_label("Tin\nAtomic No.=50\nAtomic mass=118.69\nMetal\n'p'Block"),show_symbol("Sn"),show_img('realSn.png')),bg="green yellow")
button_Pb=Button(root,text="Pb",padx=21,pady=20,font=myfont,command=lambda:(show_label("Lead\nAtomic No.=82\nAtomic mass=207.2\nMetal\n'p'Block"),show_symbol("Pb"),show_img('realPb.png')),bg="green yellow")
button_Fl=Button(root,text="Fl",padx=24,pady=20,font=myfont,command=lambda:(show_label("Flerovium\nAtomic No.=114\nAtomic mass=289\nRadioactive\nPosition-'p'Block"),show_symbol("Fl"),show_img('realFl.png')),bg="green yellow")

button_N=Button(root,text="N",padx=24,pady=20,font=myfont,command=lambda:(show_label("Nitrogen\nAtomic No.=7\nAtomic mass=14.0067\nNon-Metal\nPosition-'p'Block"),show_symbol("N"),show_img('realN.png')),bg="deep skyblue")
button_P=Button(root,text="P",padx=24,pady=20,font=myfont,command=lambda:(show_label("Phosphorus\nAtomic No.=15\nAtomic mass=30.97376\nNon-Metal\nPosition-'p'Block"),show_symbol("P"),show_img('realP.png')),bg="deep skyblue")
button_As=Button(root,text="As",padx=20,pady=20,font=myfont,command=lambda:(show_label("Arsenic\nAtomic No.=33\nAtomic mass=74.9216\nMetelloid\nPosition-'p'Block"),show_symbol("As"),show_img('realAs.png')),bg="lime green")
button_Sb=Button(root,text="Sb",padx=19,pady=20,font=myfont,command=lambda:(show_label("Antimony\nAtomic No.=51\nAtomic mass=121.75\nMetelloid\nPosition-'p'Block"),show_symbol("Sb"),show_img('realSb.png')),bg="lime green")
button_Bi=Button(root,text="Bi",padx=22,pady=20,font=myfont,command=lambda:(show_label("Bismuth\nAtomic No.=83\nAtomic mass=208.9804\nMetal\n'p'Block"),show_symbol("Bi"),show_img('realBi.png')),bg="green yellow")
button_Mc=Button(root,text="Mc",padx=19,pady=20,font=myfont,command=lambda:(show_label("Moscovium\nAtomic No.=115\nAtomic mass=290\nRadioactive\nPosition-'p'Block"),show_symbol("Mc"),show_img('realMc.png')),bg="light gray")

button_O=Button(root,text="O",padx=24,pady=20,font=myfont,command=lambda:(show_label("Oxygen\nAtomic No.=8\nAtomic mass=15.9994\nNon-Metal\nPosition-'p'Block"),show_symbol("O"),show_img('realO.png')),bg="deep skyblue")
button_S=Button(root,text="S",padx=25,pady=20,font=myfont,command=lambda:(show_label("Sulphur\nAtomic No.=16\nAtomic mass=32.06\nNon-Metal\nPosition-'p'Block"),show_symbol("S"),show_img('realS.png')),bg="deep skyblue")
button_Se=Button(root,text="Se",padx=21,pady=20,font=myfont,command=lambda:(show_label("Selenium\nAtomic No.=34\nAtomic mass=78.96\nNon-Metal\nPosition-'p'Block"),show_symbol("Se"),show_img('realSe.png')),bg="deep skyblue")
button_Te=Button(root,text="Te",padx=22,pady=20,font=myfont,command=lambda:(show_label("Tellurium\nAtomic No.=52\nAtomic mass=127.60\nMetelloid\nPosition-'p'Block"),show_symbol("Te"),show_img('realTe.png')),bg="lime green")
button_Po=Button(root,text="Po",padx=21,pady=20,font=myfont,command=lambda:(show_label("Polonium\nAtomic No.=84\nAtomic mass=209\nMetal\nPosition-'p'Block"),show_symbol("Po"),show_img('realPo.png')),bg="green yellow")
button_Lv=Button(root,text="Lv",padx=23,pady=20,font=myfont,command=lambda:(show_label("Livermorum\nAtomic No.=116\nAtomic mass=293\nRadioactive\nPosition-'p'Block"),show_symbol("Lv"),show_img('realLv.png')),bg="light gray")

button_F=Button(root,text="F",padx=25.5,pady=20,font=myfont,command=lambda:(show_label("Flourine\nAtomic No.=9\nAtomic mass=18.998403\nHalogen\nPosition-'p'Block"),show_symbol("F"),show_img('realFl.png')),bg="medium orchid")
button_Cl=Button(root,text="Cl",padx=22.5,pady=20,font=myfont,command=lambda:(show_label("Clorine\nAtomic No.=17\nAtomic mass=35.453\nHalogen\nPosition-'p'Block"),show_symbol("Cl"),show_img('realCl.png')),bg="medium orchid")
button_Br=Button(root,text="Br",padx=22.5,pady=20,font=myfont,command=lambda:(show_label("Bromine\nAtomic No.=35\nAtomic mass=79.904\nHalogen\nPosition-'p'Block"),show_symbol("Br"),show_img('realBr.png')),bg="medium orchid")
button_I=Button(root,text="I",padx=29,pady=20,font=myfont,command=lambda:(show_label("Iodine\nAtomic No.=53\nAtomic mass=126.9045\nHalogen\nPosition-'p'Block"),show_symbol("I"),show_img('realI.png')),bg="medium orchid")
button_At=Button(root,text="At",padx=23,pady=20,font=myfont,command=lambda:(show_label("Astatine\nAtomic No.=85\nAtomic mass=210\nHalogen\nPosition-'p'Block"),show_symbol("At"),show_img('realAt.png')),bg="lime green")
button_Ts=Button(root,text="Ts",padx=22,pady=20,font=myfont,command=lambda:(show_label("Tennessine\nAtomic No.=117\nAtomic mass=294\nRadioactive\nPosition-'p'Block"),show_symbol("Ts"),show_img('realTs.png')),bg="light gray")

button_He=Button(root,text="He",padx=22,pady=20,font=myfont,command=lambda:(show_label("Helium\nAtomic No.=2\nAtomic mass=4.00260\nNobel Metal\nPosition-'p'Block"),show_symbol("He"),pophe('he.png','heec.png'),show_img('realHe.png')),bg="light slate gray")
button_Ne=Button(root,text="Ne",padx=22,pady=20,font=myfont,command=lambda:(show_label("Neon\nAtomic No.=10\nAtomic mass=20.179\nNobel Metal\nPosition-'p'Block"),show_symbol("Ne"),show_img('realNe.png')),bg="light slate gray")
button_Ar=Button(root,text="Ar",padx=24,pady=20,font=myfont,command=lambda:(show_label("Argon\nAtomic No.=18\nAtomic mass=39.948\nNobel Metal\nPosition-'p'Block"),show_symbol("Ar"),show_img('realAr.png')),bg="light slate gray")
button_Kr=Button(root,text="Kr",padx=24,pady=20,font=myfont,command=lambda:(show_label("Krypton\nAtomic No.=36\nAtomic mass=83.80\nNobel Metal\nPosition-'p'Block"),show_symbol("Kr"),show_img('realKr.png')),bg="light slate gray")
button_Xe=Button(root,text="Xe",padx=22,pady=20,font=myfont,command=lambda:(show_label("xenon\nAtomic No.=54\nAtomic mass=131.30\nNobel Metal\nPosition-'p'Block"),show_symbol("Xe"),show_img('realXe.png')),bg="light slate gray")
button_Rn=Button(root,text="Rn",padx=22,pady=20,font=myfont,command=lambda:(show_label("Radon\nAtomic No.=86\nAtomic mass=222\nNobel Metal\nPosition-'p'Block"),show_symbol("Rn"),show_img('realRn.png')),bg="light slate gray")
button_Og=Button(root,text="Og",padx=21,pady=20,font=myfont,command=lambda:(show_label("Oganesson\nAtomic No.=118\nAtomic mass=294\nRadioactive\nPosition-'p'Block"),show_symbol("Og"),show_img('realOg.png')),bg="light gray")

button_La=Button(root,text="La",padx=22,pady=20,font=myfont,command=lambda:(show_label("Lanthanum\nAtomic No.=57\nAtomic mass=138.91\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("La"),show_img('realLa.png')),bg="aquamarine")
button_Ac=Button(root,text="Ac",padx=22,pady=20,font=myfont,command=lambda:(show_label("Actnium\nAtomic No.=89\nAtomic mass=227\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Ac"),show_img('realAc.png')),bg="hot pink")

button_Ce=Button(root,text="Ce",padx=20,pady=20,font=myfont,command=lambda:(show_label("Cerium\nAtomic No.=58\nAtomic mass=140.116\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Ce"),show_img('realCe.png')),bg="aquamarine")
button_Th=Button(root,text="Th",padx=21,pady=20,font=myfont,command=lambda:(show_label("Thorium\nAtomic No.=90\nAtomic mass=232.038\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Th"),show_img('realTh.png')),bg="hot pink")

button_Pr=Button(root,text="Pr",padx=21,pady=20,font=myfont,command=lambda:(show_label("Praseodymium\nAtomic No.=59\nAtomic mass=140.908\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Pr"),show_img('realPr.png')),bg="aquamarine")
button_Pa=Button(root,text="Pa",padx=20,pady=20,font=myfont,command=lambda:(show_label("Protactinium\nAtomic No.=91\nAtomic mass=231.036\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Pa"),show_img('realPa.png')),bg="hot pink")

button_Nd=Button(root,text="Nd",padx=20,pady=20,font=myfont,command=lambda:(show_label("Neodymium\nAtomic No.=60\nAtomic mass=144.282\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Nd"),show_img('realNd.png')),bg="aquamarine")
button_U=Button(root,text="U",padx=25,pady=20,font=myfont,command=lambda:(show_label("Uranium\nAtomic No.=92\nAtomic mass=238.029\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("U"),show_img('realU.png')),bg="hot pink")

button_Pm=Button(root,text="Pm",padx=20,pady=20,font=myfont,command=lambda:(show_label("Promethium\nAtomic No.=61\nAtomic mass=145\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Ra"),show_img('realRa.png')),bg="aquamarine")
button_Np=Button(root,text="Np",padx=21,pady=20,font=myfont,command=lambda:(show_label("Neptunium\nAtomic No.=93\nAtomic mass=237\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Np"),show_img('realNp.png')),bg="hot pink")

button_Sm=Button(root,text="Sm",padx=19,pady=20,font=myfont,command=lambda:(show_label("Samarium\nAtomic No.=62\nAtomic mass=150.36\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Sm"),show_img('realSm.png')),bg="aquamarine")
button_Pu=Button(root,text="Pu",padx=22,pady=20,font=myfont,command=lambda:(show_label("Plutonium\nAtomic No.=94\nAtomic mass=244\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Pu"),show_img('realPu.png')),bg="hot pink")

button_Eu=Button(root,text="Eu",padx=22,pady=20,font=myfont,command=lambda:(show_label("Europium\nAtomic No.=63\nAtomic mass=151.964\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Eu"),show_img('realEu.png')),bg="aquamarine")
button_Am=Button(root,text="Am",padx=20,pady=20,font=myfont,command=lambda:(show_label("Americium\nAtomic No.=95\nAtomic mass=243\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Am"),show_img('realAm.png')),bg="hot pink")

button_Gd=Button(root,text="Gd",padx=20,pady=20,font=myfont,command=lambda:(show_label("Gadolinium\nAtomic No.=64\nAtomic mass=64\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Gd"),show_img('realGd.png')),bg="aquamarine")
button_Cm=Button(root,text="Cm",padx=18,pady=20,font=myfont,command=lambda:(show_label("Curium\nAtomic No.=96\nAtomic mass=247\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Cm"),show_img('realCm.png')),bg="hot pink")

button_Tb=Button(root,text="Tb",padx=22,pady=20,font=myfont,command=lambda:(show_label("Terbium\nAtomic No.=65\nAtomic mass=158.925\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Tb"),show_img('realTb.png')),bg="aquamarine")
button_Bk=Button(root,text="Bk",padx=22,pady=20,font=myfont,command=lambda:(show_label("Berkelium\nAtomic No.=97\nAtomic mass=247\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Bk"),show_img('realBk.png')),bg="hot pink")

button_Dy=Button(root,text="Dy",padx=21,pady=20,font=myfont,command=lambda:(show_label("Dysprocium\nAtomic No.=66\nAtomic mass=162.500\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Dy"),show_img('realDy.png')),bg="aquamarine")
button_Cf=Button(root,text="Cf",padx=22,pady=20,font=myfont,command=lambda:(show_label("Californium\nAtomic No.=98\nAtomic mass=247\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Cf"),show_img('realCf.png')),bg="hot pink")

button_Ho=Button(root,text="Ho",padx=20,pady=20,font=myfont,command=lambda:(show_label("Holmium\nAtomic No.=67\nAtomic mass=164.930\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Ho"),show_img('realHo.png')),bg="aquamarine")
button_Es=Button(root,text="Es",padx=20,pady=20,font=myfont,command=lambda:(show_label("Einsteinium\nAtomic No.=99\nAtomic mass=252\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Es"),show_img('realEs.png')),bg="hot pink")

button_Er=Button(root,text="Er",padx=23,pady=20,font=myfont,command=lambda:(show_label("Erbium\nAtomic No.=68\nAtomic mass=167.259\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Er"),show_img('realEr.png')),bg="aquamarine")
button_Fm=Button(root,text="Fm",padx=20,pady=20,font=myfont,command=lambda:(show_label("Fermium\nAtomic No.=100\nAtomic mass=257\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Fm"),show_img('realFm.png')),bg="hot pink")

button_Tm=Button(root,text="Tm",padx=19,pady=20,font=myfont,command=lambda:(show_label("Thulium\nAtomic No.=69\nAtomic mass=168.934\nIneer-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Tm"),show_img('realTm.png')),bg="aquamarine")
button_Md=Button(root,text="Md",padx=19,pady=20,font=myfont,command=lambda:(show_label("Mendelivium\nAtomic No.=101\nAtomic mass=258\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Md"),show_img('realMd.png')),bg="hot pink")

button_Yb=Button(root,text="Yb",padx=22,pady=20,font=myfont,command=lambda:(show_label("Ytterbium\nAtomic No.=70\nAtomic mass=173.045\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Yb"),show_img('realYb.png')),bg="aquamarine")
button_No=Button(root,text="No",padx=22,pady=20,font=myfont,command=lambda:(show_label("Nobelium\nAtomic No.=102\nAtomic mass=259\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("No"),show_img('realNo.png')),bg="hot pink")

button_Lu=Button(root,text="Lu",padx=22,pady=20,font=myfont,command=lambda:(show_label("Lutetium\nAtomic No.=71\nAtomic mass=174.967\nInner-Transition Element\nLanthanoid\nPosition-'f'Block"),show_symbol("Lu"),show_img('realLu.png')),bg="aquamarine")
button_Lr=Button(root,text="Lr",padx=23,pady=20,font=myfont,command=lambda:(show_label("Lawrencium\nAtomic No.=103\nAtomic mass=262\nInner-Transition Element\nActinoid\nPosition-'f'Block"),show_symbol("Lr"),show_img('realLr.png')),bg="hot pink")

#packed those buttons inside the grid
button_H.grid(row=1,column=0)
button_Li.grid(row=2,column=0)
button_Na.grid(row=3,column=0)
button_K.grid(row=4,column=0)
button_Rb.grid(row=5,column=0)
button_Cs.grid(row=6,column=0)
button_Fr.grid(row=7,column=0)

button_Be.grid(row=2,column=1)
button_Mg.grid(row=3,column=1)
button_Ca.grid(row=4,column=1)
button_Sr.grid(row=5,column=1)
button_Ba.grid(row=6,column=1)
button_Ra.grid(row=7,column=1)

button_Sc.grid(row=4,column=2)
button_Y.grid(row=5,column=2)
button_Lu1.grid(row=6,column=2)
button_Lr1.grid(row=7,column=2)

button_Ti.grid(row=4,column=3)
button_Zr.grid(row=5,column=3)
button_Hf.grid(row=6,column=3)
button_Rf.grid(row=7,column=3)

button_V.grid(row=4,column=4)
button_Nb.grid(row=5,column=4)
button_Ta.grid(row=6,column=4)
button_Db.grid(row=7,column=4)

button_Cr.grid(row=4,column=5)
button_Mo.grid(row=5,column=5)
button_W.grid(row=6,column=5)
button_Sg.grid(row=7,column=5)

button_Mn.grid(row=4,column=6)
button_Tc.grid(row=5,column=6)
button_Re.grid(row=6,column=6)
button_Bh.grid(row=7,column=6)

button_Fe.grid(row=4,column=7)
button_Ru.grid(row=5,column=7)
button_Os.grid(row=6,column=7)
button_Hs.grid(row=7,column=7)

button_Co.grid(row=4,column=8)
button_Rh.grid(row=5,column=8)
button_Ir.grid(row=6,column=8)
button_Mt.grid(row=7,column=8)

button_Ni.grid(row=4,column=9)
button_Pd.grid(row=5,column=9)
button_Pt.grid(row=6,column=9)
button_Ds.grid(row=7,column=9)

button_Cu.grid(row=4,column=10)
button_Ag.grid(row=5,column=10)
button_Au.grid(row=6,column=10)
button_Rg.grid(row=7,column=10)

button_Zn.grid(row=4,column=11)
button_Cd.grid(row=5,column=11)
button_Hg.grid(row=6,column=11)
button_Cn.grid(row=7,column=11)

button_B.grid(row=2,column=12)
button_Al.grid(row=3,column=12)
button_Ga.grid(row=4,column=12)
button_In.grid(row=5,column=12)
button_Tl.grid(row=6,column=12)
button_Nh.grid(row=7,column=12)

button_C.grid(row=2,column=13)
button_Si.grid(row=3,column=13)
button_Ge.grid(row=4,column=13)
button_Sn.grid(row=5,column=13)
button_Pb.grid(row=6,column=13)
button_Fl.grid(row=7,column=13)

button_N.grid(row=2,column=14)
button_P.grid(row=3,column=14)
button_As.grid(row=4,column=14)
button_Sb.grid(row=5,column=14)
button_Bi.grid(row=6,column=14)
button_Mc.grid(row=7,column=14)

button_O.grid(row=2,column=15)
button_S.grid(row=3,column=15)
button_Se.grid(row=4,column=15)
button_Te.grid(row=5,column=15)
button_Po.grid(row=6,column=15)
button_Lv.grid(row=7,column=15)

button_F.grid(row=2,column=16)
button_Cl.grid(row=3,column=16)
button_Br.grid(row=4,column=16)
button_I.grid(row=5,column=16)
button_At.grid(row=6,column=16)
button_Ts.grid(row=7,column=16)

button_He.grid(row=1,column=17)
button_Ne.grid(row=2,column=17)
button_Ar.grid(row=3,column=17)
button_Kr.grid(row=4,column=17)
button_Xe.grid(row=5,column=17)
button_Rn.grid(row=6,column=17)
button_Og.grid(row=7,column=17)

button_La.grid(row=10,column=2)
button_Ac.grid(row=11,column=2)

button_Ce.grid(row=10,column=3)
button_Th.grid(row=11,column=3)

button_Pr.grid(row=10,column=4)
button_Pa.grid(row=11,column=4)

button_Nd.grid(row=10,column=5)
button_U.grid(row=11,column=5)

button_Pm.grid(row=10,column=6)
button_Np.grid(row=11,column=6)

button_Sm.grid(row=10,column=7)
button_Pu.grid(row=11,column=7)

button_Eu.grid(row=10,column=8)
button_Am.grid(row=11,column=8)

button_Gd.grid(row=10,column=9)
button_Cm.grid(row=11,column=9)

button_Tb.grid(row=10,column=10)
button_Bk.grid(row=11,column=10)

button_Dy.grid(row=10,column=11)
button_Cf.grid(row=11,column=11)

button_Ho.grid(row=10,column=12)
button_Es.grid(row=11,column=12)

button_Er.grid(row=10,column=13)
button_Fm.grid(row=11,column=13)

button_Tm.grid(row=10,column=14)
button_Md.grid(row=11,column=14)

button_Yb.grid(row=10,column=15)
button_No.grid(row=11,column=15)

button_Lu.grid(row=10,column=16)
button_Lr.grid(row=11,column=16)

button_Ho.grid(row=10,column=12)
button_Es.grid(row=11,column=12)

button_Er.grid(row=10,column=13)
button_Fm.grid(row=11,column=13)

button_Tm.grid(row=10,column=14)
button_Md.grid(row=11,column=14)

button_Yb.grid(row=10,column=15)
button_No.grid(row=11,column=15)

button_Lu.grid(row=10,column=16)
button_Lr.grid(row=11,column=16)


root.mainloop()