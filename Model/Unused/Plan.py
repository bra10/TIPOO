'''
catalogo de plan de estudio
'''
class Plan():
    
    subjects_ch1=["Principios de la orientacion a objetos",
                  "Elementos basicos  de un lenguaje orientado a objetos",
                  "Introduccion al lenguaje Java"]
    subjects_ch2=["Miembros de una clase",
                  "Manejo de metodos",
                  "Modificadores para los miembros de una clase",
                  "Diseno y creacion de objetos"]
    subjects_ch3=["Tipos de clases",
                  "Clases envoltura",
                  "Manejo de paquetes"]
    subjects_ch4=["Herencia simple",
                  "Herencia multiple",
                  "Composicion de clases"]
    chapters={
    "Unidad 1":subjects_ch1,
    "Unidad 2":subjects_ch2,
    "Unidad 3":subjects_ch3,
    "Unidad 4":subjects_ch4
    }
    
    def get_all_chapters(self):
        return self.get_chapters("uni").itervalues()
    
    def get_lang_chapter(self,lang,name):
        chp = self.get_chapters("uni").keys().index(name)
        return self.get_chapters(lang).keys()[int(chp)]
    
    def get_lang_subject(self,lang,chapter,name):
        sbj = self.get_chapters("uni")[chapter].index(name)
        chp = self.get_chapters("uni").keys().index(chapter)
        tmp = self.get_chapters(lang).keys()[int(chp)]
        return self.get_chapters(lang)[tmp][sbj]
    
    def get_lang_only_subject(self,lang,name):
        #return self.get_chapters("uni").values()
        sbjs=self.get_chapters("uni").values()
        for i in range(len(sbjs)):
            try:
                idx=sbjs[i].index(name)
            except:
                idx=None
            if idx:
                break
        sbj=self.get_chapters("spanish").values()[i][idx]
        #sbj = self.get_chapters("uni").values().index(name)
        return sbj
        #return self.get_chapters(lang).values()[sbj]
    
    def get_uni_chapter(self,lang,name):
        chp = self.get_chapters(lang).keys().index(name)
        return self.get_chapters("uni").keys()[int(chp)]
    
    def get_uni_subject(self,lang,chapter,name):
        sbj = self.get_chapters(lang)[chapter].index(name)
        chp = self.get_chapters(lang).keys().index(chapter)
        tmp = self.get_chapters("uni").keys()[int(chp)]
        return self.get_chapters("uni")[tmp][sbj]
    
    def get_chapters(self,lang):
        
        def spanish():
            subjects_ch1=["Principios de la orientaci&oacute;n a objetos",
                      "Elementos basicos  de un lenguaje orientado a objetos",
                      "Introduccion al lenguaje Java"]
            subjects_ch2=["Miembros de una clase",
                          "Manejo de metodos",
                          "Modificadores para los miembros de una clase",
                          "Diseno y creacion de objetos"]
            subjects_ch3=["Tipos de clases",
                          "Clases envoltura",
                          "Manejo de paquetes"]
            subjects_ch4=["Herencia simple",
                          "Herencia multiple",
                          "Composicion de clases"]
            chapters={
                "Unidad 1":subjects_ch1,
                "Unidad 2":subjects_ch2,
                "Unidad 3":subjects_ch3,
                "Unidad 4":subjects_ch4
                }
            return chapters
            
        def uni():             
            subjects_ch1=["1-1",
                          "1-2",
                          "1-3"]
            subjects_ch2=["2-1",
                          "2-2",
                          "2-3",
                          "2-4"]
            subjects_ch3=["3-1",
                          "3-2",
                          "3-3"]
            subjects_ch4=["4-1",
                          "4-2",
                          "4-3"]
            chapters={
            "1":subjects_ch1,
            "2":subjects_ch2,
            "3":subjects_ch3,
            "4":subjects_ch4
            }
            return chapters
        
        chapters_lang={"spanish":spanish,
                       "uni":uni
                       }
        
        return chapters_lang[lang]()
   
    #===========================================================================
    # subjects_ch1=["Abstracci&oacute;n ",
    #               "Encapsulamiento",
    #               "Herencia",
    #               "Poliformismo",
    #               "Clase",
    #               "Herencia",
    #               "Instancia",
    #               "Mensajes",
    #               "Modularidad",
    #               "Excepciones",
    #               "Java",
    #               "Estructura de programa Java",
    #               "Int&eacute;rprete y M&aacute;quina Virtual",
    #               "Compilaci&oacute;n y ejecuci&oacute;n de programa Java",
    #               "Depuraci&oacute;n programa Java",
    #               "Palabras reservadas en Java",
    #               "Tipos de datos primitivos y Manejo de arreglos",
    #               "Manejo de cadenas: la clase String",
    #               "Arquitectura del API de Java"]
    # subjects_ch2=["Declaracin de atributos o datos y su uso",
    #               
    #               ]
    #===========================================================================