from os import walk,remove,removedirs,system
import datetime
import time 


def generarInforme(texto):
    print('[+] Terminado. Deseas guardar un informe ? (s/n)::',end=" ")
    while True:
            dec = str(input(''))
            if dec == 's' or dec =='S':
                fecha = str(datetime.datetime.now()).split()
                hora = fecha[1].split('.')[0].replace(':','_')              
                with open(f'informe_{fecha[0]}_{hora}.txt','w') as informe:
                    informe.write(texto)
                    informe.close()
                
                print('Informe Guardado')
                system('pause')
                break
            elif dec == 'n' or dec == 'N':
                break     
            print('Porfavor ingrese una opcion correcta.. ')    
            
def eliminarCarpetas():
    cnt_vacias = 0
    text = '---------------CARPETAAS--ELIMINADAS-------------------' +'\n'  
    print(f'[-] Eliminando....')
    for dirpath,dirname,file in walk('./'):      
        if len(file) ==0 and len(dirname)==0:   
            text += dirpath + '\n'  
            removedirs(dirpath)          
            cnt_vacias+=1
    system('cls')
    print(f'Total Carpetas eliminadas:{cnt_vacias}')       
    generarInforme(text)           
                             
if __name__ == '__main__':
    eliminarCarpetas()
        
