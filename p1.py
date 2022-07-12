


import os
import json
from unicodedata import name
import urllib.request
# from selenium_stealth import stealth
import undetected_chromedriver.v2 as uc

from pydub import AudioSegment
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait #para ajax
from selenium.webdriver.support import expected_conditions as EC # para ajax
from selenium.webdriver.chrome.options import Options  # instalar extensiones


# chromeOptions = Options()
# chromeOptions.headless = True
# driver=webdriver.Chrome(options=chromeOptions)




tiempo1=1
tiempo2=1
tiempo3=.5
def cab():
    global driver

    # firefox_capabilities = webdriver.DesiredCapabilities.CHROME
    options=webdriver.ChromeOptions()

    #OCULTAR PANTALLA
    # options.headless=True

    # options.add_argument('start-maximized') # 

    # options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # options.add_experimental_option("useAutomationExtension", False)

    print("agregando opciones")
    options.add_argument('--no-sandbox') # Bypass OS security model # si va
    options.add_argument("--headless") # Runs Chrome in headless mode. #si va
    options.add_argument('--disable-gpu')  # applicable to windows os only # si va
    
    # options.add_argument('disable-infobars')
    # options.add_argument("--disable-extensions")
    # profile.add_argument("--kiosk")
    print("agregando extension")
    options.add_extension("./extension_0_0_0_2.crx")
                                                # profile.set_capability("host","134.209.188.111")
                                                # options.addArguments("load-extension=/path/to/extension"); # conjunto de extensiones
    # chrome_path = which("./chromedriver")
    print("Iniciando uc webdriver")

    driver=uc.Chrome(options=options, executable_path=r'./chromedriver.exe')
    print("se inicio driver")
    # driver=webdriver.Chrome(options=options, executable_path=r'./chromedriver.exe')
    time.sleep(3)
    # stealth(driver,
    #     languages=["en-US", "en"],
    #     vendor="Google Inc.",
    #     platform="Win32",
    #     webgl_vendor="Intel Inc.",
    #     renderer="Intel Iris OpenGL Engine",
    #     fix_hairline=True,
    #     )
                                                # driver.get("https://chrome.google.com/webstore/detail/im-not-robot-captcha-clic/ceipnlhmjohemhfpbjdgeigkababhmjc/related?hl=es-419")
                                                # time.sleep(3)
                                                # r=driver.find_element(By.CLASS_NAME,"g-c-R")
                                                # r.click()
                                                # time.sleep(2)
                                                # driver.find_element(By.XPATH,"//body").send_keys(Keys.RIGHT)

                                                # time.sleep(4)
                                                # webdriver.ActionChains(driver).send_keys(Keys.RIGHT)


    
    driver.get("https://sedeclave.dgt.gob.es/WEB_NCIT_CONSULTA/solicitarCita.faces")
    driver.implicitly_wait(5)
    
    
def oficinaDeSolicitud(ofiVar):
    
    grupoDeOficina={"A":1,"Á":2,"B":3,"C":4,"G":5,"H":6,"I":7,"J":8,"L":9,"M":10,"N":11,"O":12,"P":13,"R":14,"S":15,"T":16,"V":17,"Z":18}
    oficinasEnGeneral={"Badajoz":1,"Barcelona":2,"Barcelona-Sabadell":3,"Bizkaia":4, "Burgos":5, "Las Palmas-Lanzarote":3, "Las Palmas-Gran Canaria":2}
    # oficinaSeleccionado=str(input("Oficina donde desea solicitar la cita(*): "))
    oficinaSeleccionado=ofiVar
    var=ofiVar
    for i in range(1,3):
        if var[:i].isdigit():
            indiceOpt=var[:i]
            oficinaSeleccionado=var[i:]
    
    return [grupoDeOficina[oficinaSeleccionado[0]],indiceOpt]
def tipoDeTramite(tramiVar):
    listaDeTiposDeTramite={"Tramites de oficina":2, "Renovacion de permisos de conduccion (solo UE/EEE)":3, "Canjes de permiso de conduccion":4}
    # tipoDeTramiteSelecionado=str(input("Tipo de tramite: "))
    tipoDeTramiteSelecionado=tramiVar
    return listaDeTiposDeTramite[tipoDeTramiteSelecionado]
#BORRAR PORQUE YA NO ES NECESARIO
def paisDeTramite():
    listaDePaises={"Alemania":2,"Argelia":3,"Argentina":4}
    # paisSeleccionado=str(input("Ingrese el pais: "))
    paisSeleccionado="Alemania"
    return listaDePaises[paisSeleccionado]
def primerGo():
    time.sleep(tiempo2)
    # print("Lego aqui ")
    try:
        botonContinuar= driver.find_element(By.NAME,"publicacionesForm:j_id71")
        # print("valor del boton: ",botonContinuar.get_attribute("value"))
        # print("pero no paso")
        botonContinuar.click()
    except Exception as err:
        print("error en boton cotinuar: ", err)    
def instaladorDeHack():
    chrome_options = Options()
    chrome_options.add_extension('')
def descargarAudio():
    time.sleep(tiempo2)
    try:
        objectoDescargar=driver.find_element(By.CLASS_NAME,"rc-audiochallenge-tdownload-link")    
    
        linkDeDescarga=objectoDescargar.get_attribute("href")
        urllib.request.urlretrieve(linkDeDescarga, "voz.mp3")
        time.sleep(tiempo2)
        # files                                                                       
        src = "voz.mp3"
        dst = "comvert.wav"

        # convert wav to mp3                                                            
        audSeg = AudioSegment.from_mp3(src)
        audSeg.export(dst, format="wav")

    except Exception as err:
        print('error en descargar audio: ', err)
        
        return "noHayProceso"
def convertidoATexto():
    er=descargarAudio()
    if er=="noHayProceso":
        return "error123"
    else:
        audioParaProcesar="comvert.wav"
        audio_output="Prueba dato"
        try:
            recognizer = sr.Recognizer()
            vz=sr.AudioFile(audioParaProcesar)
            with vz as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.record(source) # read the entire audio file
            # recognize speech using Google Speech Recognition
            audio_output = recognizer.recognize_google(audio, language="es-ES")
            time.sleep(tiempo2)
            
        except Exception as err:
            print("Error speechh: ",err)
    
        os.remove("voz.mp3")
        os.remove("comvert.wav")
        
        print("----------------",audio_output,"----------------------------------")
        return audio_output
def Audifonos():
    try:
        time.sleep(tiempo2)
        driver.find_element(By.ID,"recaptcha-audio-button").click()# audifono en recaptcha
        
        # botonParaEscucharAudio=driver.find_element(By.CLASS_NAME,"rc-button-default").click()# play para el audio
    except Exception as err:
        
        return "error"
        
def provinciaResidenciaFun(proviVar):
    
    provincia={"A":1,"B":2,"C":3,"G":4,"H":5,"J":6,"L":7,"M":8,"N":9,"O":10,"P":11,"R":12,"S":13,"T":14,"V":15,"Z":16}
    # oficinaSeleccionado=str(input("Oficina donde desea solicitar la cita(*): "))
    
    var=proviVar
    for i in range(1,3):
        if var[:i].isdigit():
            indiceOpt=var[:i]
            provinciaSeleccionado=var[i:]
        else:
            break
    
    return [provincia[provinciaSeleccionado[0]],indiceOpt]
def paisUEEEE(id):
    provincia={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"L":10,"M":11,"N":12,"P":13,"R":14,"S":15}
    # oficinaSeleccionado=str(input("Oficina donde desea solicitar la cita(*): "))
    
    var=id
    for i in range(1,3):
        if var[:i].isdigit():
            indiceOpt=var[:i]
            provinciaSeleccionado=var[i:]
        else:
            break
    return [provincia[provinciaSeleccionado[0]],indiceOpt]
    
def main(id,ofiVar,tramiVar,paisVar):

    time.sleep(tiempo2)
    global c
    parte1=True
    paraRefresh=0
    while parte1:
        # driver.find_element(By.XPATH,"//div[@class='btnContinuarSolicitarCita']/input").submit()    
        
        GrupoDeOf,oficinaS=oficinaDeSolicitud(ofiVar)
        if len(driver.find_elements(By.ID,"publicacionesForm:oficina")) >0:
            try:
                print()
                time.sleep(tiempo2)    
                
                driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:oficina']/optgroup[{GrupoDeOf}]/option[{oficinaS}]").click()
            except Exception as err:
                # print("Elemento oficina no selecionado: ",err)
                time.sleep(tiempo3)
                driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:oficina']/optgroup[{GrupoDeOf}]/option[{oficinaS}]").click()
            time.sleep(tiempo2)

            tipoDeTramiteSeleccionado=int(tipoDeTramite(tramiVar))
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:tipoTramite']/option[{tipoDeTramiteSeleccionado}]").click()
            
            
            if tipoDeTramiteSeleccionado ==4:
                time.sleep(tiempo2)
                paisEnNumero=int(paisVar)+1
                
                driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:pais']/option[{paisEnNumero}]").click()
            elif tipoDeTramiteSeleccionado==3:
                #publicacionesForm:paiscee
                optG,optS=paisUEEEE(paisVar)
                driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:paiscee']/optgroup[{optG}]/option[{optS}]").click()
            else:
                pass
            
            # time.sleep(4)
            # Activar capcha de forma clasica
            frames = driver.find_elements(By.TAG_NAME, "iframe")
            driver.switch_to.frame(frames[0])
            
            
            # print(len(driver.find_elements(By.CLASS_NAME,"recaptcha-checkbox-border")))
            driver.find_element(By.CLASS_NAME,"recaptcha-checkbox-border").click()
            print("Picó el captcha")
            
            while True:
                try:
                    time.sleep(tiempo2)
                    reCaptcha= driver.find_element(By.ID,"recaptcha-anchor")
                    
                    time.sleep(tiempo2)
                    if "recaptcha-checkbox-focused" in reCaptcha.get_attribute("class"):
                        driver.find_element(By.ID,"recaptcha-anchor-label").click()
                    
                    # print("lista de clases: ",reCaptcha.get_attribute("class") )
                    time.sleep(tiempo2)
                    # print("Texto de verificacion: ",reCaptcha.get_attribute("textContent"))
                    estado=str(reCaptcha.get_attribute("aria-checked"))
                    print("estado checked: ", estado)
                    # print("Class de verificacion: ",reCaptcha.get_attribute("aria-checked"))
                    # if str(reCaptcha.get_attribute("textContent"))=="Se requiere la verificación de reCAPTCHA.." or str(reCaptcha.get_attribute("textContent"))=="Recaptcha requires verification." :
                except Exception as err:
                    driver.refresh()
                    # print("Error placa 2: ",err)
                    # if err=='Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="recaptcha-anchor"]"}':
                    #     estado=False
                    # else:
                    #     print("error en proceso de captcha: ", err)
                    #     estado="true"
                    
                if estado=="true":
                    # driver.refresh()
                    # print("Captcha verificado, todo esta marchando bien")
                    
                    # VUELVE AL ARCHIVO PRINCIPAL
                    driver.switch_to.default_content()
                    time.sleep(tiempo2)
                    primerGo()
                    time.sleep(tiempo1)
                    try:
                        msgErrorLog=driver.find_elements(By.XPATH,"//div[@id='publicacionesForm:j_id75']/ul/li") # lplplp
                        
                        if len(msgErrorLog)>0:
                            # print("Si hay datos", msgErrorLog[0].get_attribute("textContent"))
                            parte1=False                
                        else:
                            print("False alarma..................................")
                            os.popen("I_m_so_lonely_broken_angel_song_s_audio.mp3")
                            time.sleep(.2)
                            #   PASAR AL TERCER NIVEL >=
                            driver.find_element(By.NAME,"publicacionesForm:area:0:j_id109").click()
                            time.sleep(.5)
                            
                            paisURL=paisVar
                            if tramiVar=="Tramites de oficina":
                                datosTerceraFaceForm3(id, paisVar)
                            elif tramiVar=="Renovacion de permisos de conduccion (solo UE/EEE)":
                                datosTerceraFaceForm2(id, paisVar)
                            elif tramiVar=="Canjes de permiso de conduccion":
                                datosTerceraFaceForm1(id, paisVar)
                            
                            parte1=False
                            break
                    except Exception as exc:
                        print("Eroor nivel ultimo: ", exc)
                    break
                else:
                    # print("para audifonos ")
                    time.sleep(.4)
                    driver.switch_to.default_content()
                    frames2 = driver.find_elements(By.TAG_NAME, "iframe")
                    # print("Cantidad de frames: ",len(frames2))
                    driver.switch_to.frame(frames2[4])
                    htm=driver.find_element(By.TAG_NAME, "html")
                    # print("lasg de html: ",htm.get_attribute("lang"))
                    
                    # ctnDivBtn=driver.find_element(By.TAG_NAME,"input")
                    # print("Contenedor haver si existe: ", ctnDivBtn.get_attribute("id"))
                    time.sleep(.4)
                    ctnDivBtn=driver.find_elements(By.TAG_NAME,"div")
                    # print("Cantidad de div: ", len(ctnDivBtn))
                    time.sleep(.4)
                    est=Audifonos()
                    if est=="error":
                        parte1=False
                        break
                    time.sleep(tiempo2)
                    #descargarAudio()
                    for i in range(0,10):
                        try:
                            textoAIngresar=convertidoATexto()
                            if textoAIngresar=="error123":
                                break
                            inputDeAudioTraducido=driver.find_element(By.ID,"audio-response")
                            # print("Ingresando texto a captcha")
                            inputDeAudioTraducido.send_keys(textoAIngresar)
                            time.sleep(.2)
                            # print("verificando texto ")
                            driver.find_element(By.ID,"recaptcha-verify-button").click()
                            
                            time.sleep(.2)
                            
                            textoFalloSpeech=driver.find_element(By.CLASS_NAME,"rc-audiochallenge-error-message").get_attribute("textContent")
                            if len(textoFalloSpeech)>1:
                                pass
                            else:
                                time.sleep(.2)
                                driver.switch_to.default_content()
                                frames = driver.find_elements(By.TAG_NAME, "iframe")
                                driver.switch_to.frame(frames[0])
                                break
                        except Exception as err:
                            print("Error en el for: ",err)
                            break
            c+=1
            print("Cantidad de vuelta: ", c)
                        
        else:
            print("!!!![*] se metio aqui")
            # primerGo()
            # paraRefresh+=1
            # if paraRefresh==3:
            driver.refresh()
            # print("no hay oficina:",paraRefresh)
                        
                    
def datosTerceraFaceForm1(id, paisV):
    time.sleep(1)
    with open("./static/data.json", "r") as dataR:
        content=json.load(dataR)
    if content[0][id]:
        nifNIE=content[0][id]["nifnie"]
        NOMBRE=content[0][id]["nombre"]
        primerApellido=content[0][id]["primerApellido"]
        segundoApellido=content[0][id]["segundoApellido"]
        telefono=content[0][id]["telefono"]
        fechaNacimiento=content[0][id]["fechaNacimiento"]
        if paisV=="1" or paisV=='4'or paisV=='5'or paisV=='8' or paisV=='10' or paisV=='13' or paisV=='14' or paisV=='17' or paisV=='18'or paisV=='19'or paisV=='21'or paisV=='22'or paisV=='23'or paisV=='25'or paisV=='26'or paisV=='27'or paisV=='28'or paisV=='29'or paisV=='30'or paisV=='31'or paisV=='32'or paisV=='34'or paisV=='37'or paisV=='38'or paisV=='42'or paisV=='43'or paisV=='44'or paisV=='46'or paisV=='48':
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            correoE=content[0][id]["correoElectronico"]
            emailAviso=content[0][id]["emailAviso"]
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id123:0:CEEminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id127:3:nombreCEE").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id132:1:primerApellidoCEE").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id136:2:segundoApellidoCEE").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.ID, "publicacionesForm:j_id148:4:CEEelsalvador6").send_keys(telefono)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id152:5:CEEelsalvador7").send_keys(fechaNacimiento)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id159:11:mypermisocond").send_keys(numPermisoConduccion)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id164:12:myemail").send_keys(correoE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:CEEmiemailsavi").send_keys(emailAviso)
            
            #PERMISOS A SOLICITAR
            for checkOn in content[0][id]["chekeados"]:
                if checkOn =="on1":permisoAM=driver.find_element(By.ID,"publicacionesForm:j_id186:13:AM").click()
                if checkOn =="on2":permisoA1=driver.find_element(By.ID,"publicacionesForm:j_id190:6:A1").click()
                if checkOn =="on3":permisoA2=driver.find_element(By.ID,"publicacionesForm:j_id193:7:A2").click()
                if checkOn =="on4":permisoA=driver.find_element(By.ID,"publicacionesForm:j_id196:14:A").click()
                if checkOn =="on5":permisoB=driver.find_element(By.ID,"publicacionesForm:j_id199:8:B").click()
                if checkOn =="on6":permisoBE=driver.find_element(By.ID,"publicacionesForm:j_id202:15:BE").click()
                if checkOn =="on7":permisoC1=driver.find_element(By.ID,"publicacionesForm:j_id205:9:C1").click()
                if checkOn =="on8":permisoC1E=driver.find_element(By.ID,"publicacionesForm:j_id208:16:C1E").click()
                if checkOn =="on9":permisoC=driver.find_element(By.ID,"publicacionesForm:j_id211:17:C").click()
                if checkOn =="on10":permisoCE=driver.find_element(By.ID,"publicacionesForm:j_id214:18:CE").click()
                if checkOn =="on11":permisoD1=driver.find_element(By.ID,"publicacionesForm:j_id217:19:D1").click()
                if checkOn =="on12":permisoD1E=driver.find_element(By.ID,"publicacionesForm:j_id220:20:D1E").click()
                if checkOn =="on13":permisoD=driver.find_element(By.ID,"publicacionesForm:j_id223:10:D").click()
                if checkOn =="on14":permisoDE=driver.find_element(By.ID,"publicacionesForm:j_id226:21:DE").click()
            
            #AUTORIZACION
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()    
        elif paisV=="2":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            
            fechaExpedicion=content[0][id]["fechaExpedicion"]
            lugarDeNacimiento=content[0][id]["lugarDeNacimiento"]
            # CHEKEADOS------------------->
            #PERMISOS A SOLICITAR
            for checkOn in content[0][id]["chekeados"]:
                if checkOn =="on1":permisoA1=driver.find_element(By.ID,"publicacionesForm:j_id1860:10:A1").click()
                if checkOn =="on2":permisoA2=driver.find_element(By.ID,"publicacionesForm:j_id1863:11:A2").click()
                if checkOn =="on3":permisoB=driver.find_element(By.ID,"publicacionesForm:j_id1866:12:B").click()
                if checkOn =="on4":permisoC1=driver.find_element(By.ID,"publicacionesForm:j_id1869:13:C1").click()
                if checkOn =="on5":permisoC2=driver.find_element(By.ID,"publicacionesForm:j_id1872:14:C2").click()
                if checkOn =="on6":permisoD=driver.find_element(By.ID,"publicacionesForm:j_id1875:15:D").click()
                if checkOn =="on6":permisoD=driver.find_element(By.ID,"publicacionesForm:j_id1878:16:E").click()
                
            numPermisoConduccionAr=content[0][id]["numPermisoConduccionAr"]
            wilayaExpedicion=content[0][id]["wilayaExpedicion"]
            dairaExpedicion=content[0][id]["dairaExpedicion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1806:0:DZminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1810:4:nombreDZ").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1815:2:primerApellidoDZ").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1819:3:segundoApellidoDZ").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1824:1:residenciaDZ']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1831:5:DZelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1835:6:DZelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1842:8:mifechaexp").send_keys(fechaExpedicion)# fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1849:9:lugarNacArgArgelia").send_keys(lugarDeNacimiento)# lugar nacimiento Argelia
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1881:17:minumpermisoarg").send_keys(numPermisoConduccionAr)# num permiso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1886:18:miwilaya").send_keys(wilayaExpedicion)# wilaya expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1890:19:midaira").send_keys(dairaExpedicion)# daira expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:DZmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1908:7:DZobservaciones").send_keys(observaciones) # observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        elif paisV=="3" or paisV=="41" or paisV=='52':
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id268:0:PaisAcuerdominif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id272:4:nombrePaisAcuerdo").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id277:2:primerApellidoPaisAcuerdo").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id281:3:segundoApellidoPaisAcuerdo").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id286:1:residenciaPaisAcuerdo']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id293:5:PaisAcuerdoelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id297:6:PaisAcuerdoelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:PaisAcuerdomiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id318:7:PaisAcuerdoobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        elif paisV=="33":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1117:0:MKminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1121:4:nombreMK").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1126:2:primerApellidoMK").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1130:3:segundoApellidoMK").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1135:1:residenciaMK']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1142:5:MKelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1146:6:MKelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1153:8:macedonia23").send_keys(numPermisoConduccion)# num permiso conduccion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:MKmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1172:7:MKobservaciones").send_keys(observaciones)# obvservaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        elif paisV=="51":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            certificadoConductor=content[0][id]["certificadoConductor"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id410:0:UAminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id414:4:nombreUA").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id419:2:primerApellidoUA").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id423:3:segundoApellidoUA").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id428:1:residenciaUA']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id435:5:UAelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id439:6:UAelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id446:8:ucrania74").send_keys(certificadoConductor)# certificado conductor
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:UAmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id465:7:UAobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        elif paisV=="6":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"]
            numCartaIdentificacion=content[0][id]["numCartaIdentificacion"]
            lugarExpedicion=int(content[0][id]["lugarExpedicion"])
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1715:0:BOminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1719:4:nombreBO").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1724:2:primerApellidoBO").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1728:3:segundoApellidoBO").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1733:1:residenciaBO']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1740:5:BOelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1744:6:BOelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1751:8:bolivia9").send_keys(fechaExpedicion) # fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1758:10:bolivia22").send_keys(numCartaIdentificacion) # carta identificacion
            time.sleep(.4)
            driver.find_element(By.XPATH,f"//select[@id='publicacionesForm:j_id1762:9:bolivia21']/option[{lugarExpedicion}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1777:11:bolivia23").send_keys(numPermisoConduccion) # permiso conduccion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:BOmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1795:7:BOobservaciones").send_keys(observaciones) # observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        elif paisV=="7": # publicacionesForm:area:0:j_id109  
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            numRegistroConductor=content[0][id]["numRegistroConductor"]
            nombreMadre=content[0][id]["nombreMadre"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1644:0:BRminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1648:4:nombreBR").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1653:2:primerApellidoBR").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1657:3:segundoApellidoBR").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1662:1:residenciaBR']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1669:5:BRelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1673:6:BRelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1680:9:brasil24").send_keys(numRegistroConductor)# registro de conductor
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1685:10:deLaMadreBrasil").send_keys(nombreMadre)# nombre madre
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:BRmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1704:7:BRobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="9":# publicacionesForm:area:0:j_id109
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            lugarExpedicion=content[0][id]["lugarExpedicion"]
            numIdentidadChileno=content[0][id]["numIdentidadChileno"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1574:0:RCHminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1578:4:nombreRCH").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1583:2:primerApellidoRCH").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1587:3:segundoApellidoRCH").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1592:1:residenciaRCH']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1599:5:RCHelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1603:6:RCHelsalvador7").send_keys(fechaNacimiento) # fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1610:8:chile21").send_keys(lugarExpedicion)# lugar expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1615:9:chile50").send_keys(numIdentidadChileno)# num identidad chileno
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:RCHmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1633:7:RCHobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="11":# publicacionesForm:area:0:j_id109
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            licenciaConduccion01A1=content[0][id]["licenciaConduccion01A1"]
            licenciaConduccion02A2=content[0][id]["licenciaConduccion02A2"]
            licenciaConduccion03B1=content[0][id]["licenciaConduccion03B1"]
            licenciaConduccion04C1=content[0][id]["licenciaConduccion04C1"]
            licenciaConduccion05B2C2=content[0][id]["licenciaConduccion05B2C2"]
            licenciaConduccion06B3C3=content[0][id]["licenciaConduccion06B3C3"]
            documentoIdentidad=content[0][id]["documentoIdentidad"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1481:0:COminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1485:4:nombreCO").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1490:2:primerApellidoCO").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1494:3:segundoApellidoCO").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1499:1:residenciaCO']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1506:5:COelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1510:6:COelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1517:8:colombia51").send_keys(licenciaConduccion01A1)# lic1
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1522:9:colombia52").send_keys(licenciaConduccion02A2) # lic2
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1526:10:colombia53").send_keys(licenciaConduccion03B1)# lic3
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1531:11:colombia54").send_keys(licenciaConduccion04C1)# lic4
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1535:12:colombia55").send_keys(licenciaConduccion05B2C2)# lic5
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1540:13:colombia56").send_keys(licenciaConduccion06B3C3)# lic6
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1544:14:colombia59").send_keys(documentoIdentidad)# documento identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:COmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1563:7:COobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="12":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            #PERMISOS A SOLICITAR
            for checkOn in content[0][id]["chekeados"]:
                if checkOn =="on1": driver.find_element(By.ID,"publicacionesForm:j_id1960:9:generico").click()
                if checkOn =="on2": driver.find_element(By.ID,"publicacionesForm:j_id1963:10:generico").click()
                if checkOn =="on3": driver.find_element(By.ID,"publicacionesForm:j_id1966:42:generico").click()
                if checkOn =="on4": driver.find_element(By.ID,"publicacionesForm:j_id1969:43:generico").click()
                if checkOn =="on5": driver.find_element(By.ID,"publicacionesForm:j_id1972:44:generico").click()
                if checkOn =="on6": driver.find_element(By.ID,"publicacionesForm:j_id1975:45:generico").click()
                if checkOn =="on7": driver.find_element(By.ID,"publicacionesForm:j_id1978:50:generico").click()
                if checkOn =="on8": driver.find_element(By.ID,"publicacionesForm:j_id1981:12:generico").click()
                if checkOn =="on9": driver.find_element(By.ID,"publicacionesForm:j_id1984:48:generico").click()
                if checkOn =="on10": driver.find_element(By.ID,"publicacionesForm:j_id1987:49:generico").click()
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1919:1:CRIminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1923:5:nombreCRI").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1928:3:primerApellidoCRI").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1932:4:segundoApellidoCRI").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1937:2:residenciaCRI']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1944:6:CRIelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1948:7:CRIelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id2000:41:numpermisocond").send_keys(numPermisoConduccion)# permiso conduccion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:CRImiemailsavi").send_keys(emailAviso) # email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id2020:8:CRIobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="15":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            cedulaIdentificacion=content[0][id]["cedulaIdentificacion"]
            fechaPrimeraExpedicion=content[0][id]["fechaPrimeraExpedicion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1409:0:ECminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1413:4:nombreEC").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1418:2:primerApellidoEC").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1422:3:segundoApellidoEC").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1427:1:residenciaEC']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1434:5:ECelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1438:6:ECelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1445:8:ecuador58").send_keys(cedulaIdentificacion)# cedula identificacion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1450:9:ecuador59").send_keys(fechaPrimeraExpedicion)# fecha primera expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:ECmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1470:7:ECobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="16":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"]
            documentoUnicoIdentidad=content[0][id]["documentoUnicoIdentidad"]
            numLicencia=content[0][id]["numLicencia"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1332:0:ESminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1336:4:nombreES").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1341:2:primerApellidoES").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1345:3:segundoApellidoES").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1350:1:residenciaES']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1357:5:ESelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1361:6:ESelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1368:8:elsalvador9").send_keys(fechaExpedicion)# fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1375:9:elsalvador60").send_keys(documentoUnicoIdentidad)# documento unico de identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1379:10:elsalvador61").send_keys(numLicencia) # num licencia
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:ESmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1398:7:ESobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="20":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            numLicencia=content[0][id]["numLicencia"]
            numPasaporte=content[0][id]["numPasaporte"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1262:0:ECminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1266:4:nombreEC").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1271:2:primerApellidoEC").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1275:3:segundoApellidoEC").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1280:1:residenciaEC']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1287:5:ECelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1291:6:ECelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1298:8:filipinas61").send_keys(numLicencia)# num licencia
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1303:9:filipinas62").send_keys(numPasaporte)# num pasaporte
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:RPmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1321:7:FPobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="24":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"]
            numLicencia=content[0][id]["numLicencia"]
            fechaVencimiento=content[0][id]["fechaVencimiento"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1183:0:GCAminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1187:4:nombreGCA").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1192:2:primerApellidoGCA").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1196:3:segundoApellidoGCA").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1201:1:residenciaGCA']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1208:5:GCAelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1212:6:GCAelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1219:8:guatemala9").send_keys(fechaExpedicion)# fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1226:9:guatemala61").send_keys(numLicencia)# num licencia
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1230:10:guatemala63").send_keys(fechaVencimiento)# fecha vencimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:GCAmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1251:7:GCAobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="35":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"]
            lugarExpedicion=content[0][id]["lugarExpedicion"]
            numCartaIdentidad=content[0][id]["numCartaIdentidad"]
            numPermisoMarroqui=content[0][id]["numPermisoMarroqui"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            
            driver.find_element(By.ID,"publicacionesForm:j_id1036:0:MAminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1040:4:nombreMA").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1045:2:primerApellidoMA").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1049:3:segundoApellidoMA").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id1054:1:residenciaMA']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1061:5:MAelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1065:6:MAelsalvador7").send_keys(fechaNacimiento)# fecha nacimeinto
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1072:8:marruecos9").send_keys(fechaExpedicion)#fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1079:9:marruecos21").send_keys(lugarExpedicion)# lugar expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1083:10:marruecos64").send_keys(numCartaIdentidad)# num carta identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1088:11:marruecos65").send_keys(numPermisoMarroqui)# permiso conducir
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:MAmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1106:7:MAobservaciones").send_keys(observaciones)# observaciones 
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            time.sleep(.5)
            driver.find_element(By.NAME,"publicacionesForm:j_id2059").click()
            time.sleep(10)
        elif paisV=="36":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            lugarExpedicion=content[0][id]["lugarExpedicion"]
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            numCartaIdentidad=content[0][id]["numCartaIdentidad"]
            fechaUltimaExpedicion=content[0][id]["fechaUltimaExpedicion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id955:0:NICminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id959:4:nombreNIC").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id964:2:primerApellidoNIC").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id968:3:segundoApellidoNIC").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id973:1:residenciaNIC']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id980:5:NICelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id984:6:NICelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id991:8:nicaragua21").send_keys(lugarExpedicion)# lugar expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id996:9:nicaragua23").send_keys(numPermisoConduccion)# num permiso conduccion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1000:10:nicaragua64").send_keys(numCartaIdentidad)# num carta identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1005:11:nicaragua66").send_keys(fechaUltimaExpedicion)# fecha ultima expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:NICmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id1025:7:NICobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        elif paisV=="39":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"]            
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id878:0:PAminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id882:4:nombrePA").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id887:2:primerApellidoPA").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id891:3:segundoApellidoPA").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id896:1:residenciaPA']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id903:5:PAelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id907:6:PAelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id914:8:panama9").send_keys(fechaExpedicion)# fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id923:9:panama23").send_keys(numPermisoConduccion)# num permiso conduccion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:PAmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id944:7:COobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="40":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"] 
            lugarExpedicion=content[0][id]["lugarExpedicion"]
            numCartaIdentificacion=content[0][id]["numCartaIdentificacion"]
            numPermisoConduccion=content[0][id]["numPermisoConduccion"]
            categoriaLicencia=int(content[0][id]["categoriaLicencia"])
            numComputacion=content[0][id]["numComputacion"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id779:0:PYminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id783:4:nombrePY").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id788:2:primerApellidoPY").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id792:3:segundoApellidoPY").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id797:1:residenciaPY']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id804:5:PYelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id808:6:PYelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id815:8:paraguay9").send_keys(fechaExpedicion)# fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id822:9:paraguay21").send_keys(lugarExpedicion)# lugar expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id826:10:paraguay22").send_keys(numCartaIdentificacion)# num carta identificacion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id831:11:paraguay23").send_keys(numPermisoConduccion)# num permiso conduccion
            time.sleep(.4)
            driver.find_element(By.XPATH,f"//select[@id='publicacionesForm:j_id835:12:paraguay67']/option[{categoriaLicencia}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id848:13:paraguay68").send_keys(numComputacion)# num de computacion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:PYmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id867:7:PYobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
            
        elif paisV=="45":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            fechaExpedicion=content[0][id]["fechaExpedicion"] 
            lugarExpedicion=content[0][id]["lugarExpedicion"]
            numCartaIdentidad=content[0][id]["numCartaIdentidad"]
            numPermisoDominicano=content[0][id]["numPermisoDominicano"]
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id698:0:DOMminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id702:4:nombreDOM").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id707:2:primerApellidoDOM").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id711:3:segundoApellidoDOM").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id716:1:residenciaDOM']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id723:5:DOMelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id727:6:DOMelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id734:8:repdominicana9").send_keys(fechaExpedicion)# fecha expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id741:9:repdominicana21").send_keys(lugarExpedicion)# lugar expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id745:10:repdominicana64").send_keys(numCartaIdentidad)# num carta identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id750:11:repdominicana69").send_keys(numPermisoDominicano)# num permiso conduccion 
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:DOMmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id768:7:DOMobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
            
        elif paisV=="47":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            organoEmisor=content[0][id]["organoEmisor"] 
            numDocumentoIdentidad=content[0][id]["numDocumentoIdentidad"] 
            numRegCondLic=content[0][id]["numRegCondLic"]
            numSerieCarnetConducir=content[0][id]["numSerieCarnetConducir"]                        
            emailAviso=content[0][id]["emailAviso"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id621:0:SRBminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id625:4:nombreSRB").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id630:2:primerApellidoSRB").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id634:3:segundoApellidoSRB").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id639:1:residenciaSRB']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id646:5:SRBelsalvador6").send_keys(telefono)# telefono 
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id650:6:SRBelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id657:9:serbia71").send_keys(organoEmisor)# organo emisor
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id664:8:serbia70").send_keys(numDocumentoIdentidad)# num documento identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id670:11:serbia76").send_keys(numRegCondLic)# num registro conductor
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id675:10:serbia73").send_keys(numSerieCarnetConducir)# num de serie carnet
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:SRBmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="49":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            numCartaIdentidad=content[0][id]["numCartaIdentidad"] 
            numPermisoConduccion=content[0][id]["numPermisoConduccion"] 
            lugarNacimiento=content[0][id]["lugarNacimiento"]                    
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id546:0:TNminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id550:4:nombreTN").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id555:2:primerApellidoTN").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id559:3:segundoApellidoTN").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id564:1:residenciaTN']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id571:5:TNelsalvador6").send_keys(telefono)# telefono
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id575:6:TNelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id582:10:tunez64").send_keys(numCartaIdentidad)# num carta identidad
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id587:9:tunez23").send_keys(numPermisoConduccion)# num permiso conduccion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id591:8:lugarNac10").send_keys(lugarNacimiento)# lugar nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:TNmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id610:7:TNobservaciones").send_keys(observaciones)# observaciones
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
            
        elif paisV=="50":
            provinciaResidencia=content[0][id]["provinciaResidencia"]
            optGroup,option=provinciaResidenciaFun(provinciaResidencia)
            
            numLicencia=content[0][id]["numLicencia"] 
            lugarExpedicion=content[0][id]["lugarExpedicion"] 
            emailAviso=content[0][id]["emailAviso"]
            observaciones=content[0][id]["observaciones"]
            #COMPLETAR FORMULARIO AQUI
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id476:0:TRminif").send_keys(nifNIE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id480:4:nombreTR").send_keys(NOMBRE)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id485:2:primerApellidoTR").send_keys(primerApellido)
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id489:3:segundoApellidoTR").send_keys(segundoApellido)
            time.sleep(.4)
            driver.find_element(By.XPATH, f"//select[@id='publicacionesForm:j_id494:1:residenciaTR']/optgroup[{optGroup}]/option[{option}]").click()
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id501:5:TRelsalvador6").send_keys(telefono)# telefono 
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id505:6:TRelsalvador7").send_keys(fechaNacimiento)# fecha nacimiento
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id512:9:turquia61").send_keys(numLicencia)# num licencia
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id517:8:turquia21").send_keys(lugarExpedicion)# lugar de expedicion
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:TRmiemailsavi").send_keys(emailAviso)# email aviso
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:j_id535:7:TRobservaciones").send_keys(observaciones)# observaciones 
            time.sleep(.4)
            driver.find_element(By.ID,"publicacionesForm:autorizacion").click()
        with open("./static/data.json", "r") as file:
            dataRead=json.load(file)
            dataRead[0].pop(id)
        with open("./static/data.json","w") as fileW:
            json.dump(dataRead, fileW, indent=4)
        
        time.sleep(.4)
        driver.get("https://sedeclave.dgt.gob.es/WEB_NCIT_CONSULTA/solicitarCita.faces")

def datosTerceraFaceForm2(id, paisVar):
    time.sleep(1)
    with open("./static/data.json", "r") as dataR:
        content=json.load(dataR)
    if content[0][id]:
        nifnieI=content[0][id]["nifnieI"]
        numPermisoConduccionI=content[0][id]["numPermisoConduccionI"]
        nombreI=content[0][id]["nombreI"]
        primerApellidoI=content[0][id]["primerApellidoI"]
        segundoApellidoI=content[0][id]["segundoApellidoI"]
        generoSexoI=content[0][id]["generoSexoI"]
        fechaNacimientoI=content[0][id]["fechaNacimientoI"]
        correoElectronicoI=content[0][id]["correoElectronicoI"]
        
        nifnieR=content[0][id]["nifnieR"]
        nombreR=content[0][id]["nombreR"]
        primerApellidoR=content[0][id]["primerApellidoR"]
        segundoApellidoR=content[0][id]["segundoApellidoR"]
        correoElectronicoR=content[0][id]["correoElectronicoR"]
        
        telefonoO=content[0][id]["telefonoO"]
        numExpedienteO=content[0][id]["numExpedienteO"]
        matriculaDelBastidorO=content[0][id]["matriculaDelBastidorO"]
        
        #LLENADO DE DATOS A LA PAGINA
        
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:NIFNIERDO").send_keys(nifnieI)# nifNie
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:NUMPERMRDO").send_keys(numPermisoConduccionI)# num permiso
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:nombreRDO2").send_keys(nombreI)# nombre
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape1RDO2").send_keys(primerApellidoI)# primerApellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape2RDO").send_keys(segundoApellidoI)# segundo apellido
        time.sleep(.4)
        #=>publicacionesForm:sexoRDO
        if generoSexoI=="masculino":
            opt="1"
            driver.find_element(By.XPATH,f"//select[@id='publicacionesForm:sexoRDO']/option[{opt}]").click()
        elif generoSexoI=="femenino":
            opt="2"
            driver.find_element(By.XPATH,f"//select[@id='publicacionesForm:sexoRDO']/option[{opt}]").click()
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:fechaNacRDO").send_keys(fechaNacimientoI)# fecha nacimiento
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:emailRDO").send_keys(correoElectronicoI)# correo electronico
        time.sleep(.4)
        
        driver.find_element(By.ID,"publicacionesForm:NIFNIERNTE").send_keys(nifnieR)# nifNie
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:nombreRNTE").send_keys(nombreR)# nombre
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape1RNTE").send_keys(primerApellidoR)# primer apellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape2RNTE").send_keys(segundoApellidoR)# segundo apellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:emailRNTE").send_keys(correoElectronicoR)# correo electronico
        time.sleep(.4)
        
        driver.find_element(By.ID,"publicacionesForm:telcto").send_keys(telefonoO)# tel comunicacion
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:expediente").send_keys(numExpedienteO)# num expediente
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:matricula").send_keys(matriculaDelBastidorO)# matricula bastidor
        
        #SOLICITAR CITA
        #driver.find_element(By.NAME,"publicacionesForm:j_id2059").click()
        with open("./static/data.json", "r") as file:
            dataRead=json.load(file)
            dataRead[0].pop(id)
        with open("./static/data.json","w") as fileW:
            json.dump(dataRead, fileW, indent=4)
        
        time.sleep(.4)
        driver.get("https://sedeclave.dgt.gob.es/WEB_NCIT_CONSULTA/solicitarCita.faces")

def datosTerceraFaceForm3(id, paisVar):
    time.sleep(1)
    with open("./static/data.json", "r") as dataR:
        content=json.load(dataR)
    if content[0][id]:
        nifnieI=content[0][id]["nifnieI"]
        nombreI=content[0][id]["nombreI"]
        primerApellidoI=content[0][id]["primerApellidoI"]
        segundoApellidoI=content[0][id]["segundoApellidoI"]
        correoElectronicoI=content[0][id]["correoElectronicoI"]
        
        nifnieR=content[0][id]["nifnieR"]
        nombreR=content[0][id]["nombreR"]
        primerApellidoR=content[0][id]["primerApellidoR"]
        segundoApellidoR=content[0][id]["segundoApellidoR"]
        correoElectronicoR=content[0][id]["correoElectronicoR"]
        
        telefonoO=content[0][id]["telefonoO"]
        numExpedienteO=content[0][id]["numExpedienteO"]
        matriculaDelBastidorO=content[0][id]["matriculaDelBastidorO"]
        
        #LLENADO DE DATOS A LA PAGINA
        
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:NIFNIERDO").send_keys(nifnieI)# nifNie        
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:nombreRDO1").send_keys(nombreI)# nombre
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape1RDO1").send_keys(primerApellidoI)# primerApellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape2RDO").send_keys(segundoApellidoI)# segundo apellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:emailRDO").send_keys(correoElectronicoI)# correo electronico
        time.sleep(.4)
        
        driver.find_element(By.ID,"publicacionesForm:NIFNIERNTE").send_keys(nifnieR)# nifNie
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:nombreRNTE").send_keys(nombreR)# nombre
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape1RNTE").send_keys(primerApellidoR)# primer apellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:ape2RNTE").send_keys(segundoApellidoR)# segundo apellido
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:emailRNTE").send_keys(correoElectronicoR)# correo electronico
        time.sleep(.4)
        
        driver.find_element(By.ID,"publicacionesForm:telcto").send_keys(telefonoO)# tel comunicacion
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:expediente").send_keys(numExpedienteO)# num expediente
        time.sleep(.4)
        driver.find_element(By.ID,"publicacionesForm:matricula").send_keys(matriculaDelBastidorO)# matricula bastidor
        
        #SOLICITAR CITA
        #driver.find_element(By.NAME,"publicacionesForm:j_id2059").click()
        with open("./static/data.json", "r") as file:
            dataRead=json.load(file)
            dataRead[0].pop(id)
        with open("./static/data.json","w") as fileW:
            json.dump(dataRead, fileW, indent=4)
        
        time.sleep(.4)
        driver.get("https://sedeclave.dgt.gob.es/WEB_NCIT_CONSULTA/solicitarCita.faces")
        
        
#VARIABLES GLOBALES NO TOCAR

def datoJson():
    
    while True:
        time.sleep(1)    
        with open("./static/data.json", "r") as dataJ:
            try:
                dataP=json.load(dataJ)
            except Exception as err:
                pass
        if len(dataP[0].keys())>0:
            for data in range(0,len(dataP[0].keys())):
                numeroDeDatos=list(dataP[0].keys())[data]# NOMBRE DE CADA DATOS SUBMIT 
                
                oficina=dataP[0][numeroDeDatos]["oficinaSeleccionado"]
                tramite=dataP[0][numeroDeDatos]["tipoTramite"]
                try:
                    pais=dataP[0][numeroDeDatos]["paisSeleccionado"]
                except Exception as exc:
                    pais=""
                main(numeroDeDatos,oficina,tramite, pais)
        else:
            time.sleep(2)
            print("vacio")
        
# LLAMA A LA FUNCION PARA LLENAR DATOS
def inicializarPrograma():
    
    try:
        
        cab() 
        time.sleep(4)
        datoJson()
    except Exception as err:
        print("ERROR GEERAL INICIANDO NUEVAMENTE..................", err)
        driver.quit()
        if err !="'Connection aborted.', ConnectionResetError(10054, 'Se ha forzado la interrupción de una conexión existente por el host remoto', None, 10054, None))":
            inicializarPrograma()
        
c=1
# os.popen("I_m_so_lonely_broken_angel_song_s_audio.mp3")
if __name__=="__main__":
    inicializarPrograma()
#
#BTN PARTE2 => name= publicacionesForm:area:0:j_id109-publicacionesForm:area:0:j_id109-publicacionesForm:area:0:j_id109

#NIFNIE=> publicacionesForm:NIFNIERDO - publicacionesForm:NIFNIERDO -
#NUM permisoc conduccion=> publicacionesForm:NUMPERMRDO - publicacionesForm:NUMPERMRDO
# nombre=> publicacionesForm:nombreRDO2 - publicacionesForm:nombreRDO2

#NIFNIE=> publicacionesForm:NIFNIERNTE - publicacionesForm:NIFNIERNTE
#NOMBRE=> publicacionesForm:nombreRNTE - publicacionesForm:nombreRNTE
#primer=> publicacionesForm:ape1RNTE - publicacionesForm:ape1RNTE

# TRAMITES DE OFICNINA
# PARTE 2=> publicacionesForm:area:0:j_id109
