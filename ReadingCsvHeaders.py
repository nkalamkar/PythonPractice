import csv,fileinput,sys
import os
import shutil
import glob
import datetime

class E65_Filehandling:
    
    global JUP_ETL_Files_Dir,TML_LIST_Files_Dir,GW_LIST_Files_Dir,E65_Scripts_Dir
    global file_folder,total_fields,file_type
    
    JUP_ETL_Files_Dir = 'C:\\Users\\nidhi\\Documents\\Test'
    TML_LIST_Files_Dir= 'C:\\Users\\nidhi\\Documents'
    GW_LIST_Files_Dir= 'C:\\Users\\nidhi\\Documents\\Test'
    E65_Scripts_Dir= 'C:\\Users\\nidhi\\Documents\\Test'
    file_folder = 'TerminalInforView'
    total_fields =3
    file_type= 'csv'
        
    def createFileList():
        if (file_folder == 'TerminalInforView'):
            #print(glob.glob(JUP_ETL_Files_Dir + "/tinfor*/TerminalInfoView_*.csv"))
            file_count = len(glob.glob(JUP_ETL_Files_Dir +"/tinfor*/TerminalInfoView_*.csv"))
            print(file_count)
            tinfor_file = TML_LIST_Files_Dir + "\\Test.lst"
            if file_count > 0 :
                E65_Filehandling.record_Log(E65_Scripts_Dir,file_count,file_folder)
                f = open(tinfor_file,"w+")
                print("file opened")
                for name in glob.glob(JUP_ETL_Files_Dir +"/tinfor*/TerminalInfoView_*.csv"):
                    f.write("%s\n" % name)
                    #print(s.path.isfile(name))
                f.close()
                print("Completed the file list")
                E65_Filehandling.validate(tinfor_file,total_fields,file_folder,'csv')
            else:
                E65_Filehandling.record_Log(E65_Scripts_Dir,file_count,file_folder)
                exit(1)            
        else:
            file_type = "gwstats"
            file_count = len(glob.glob(JUP_ETL_Files_Dir +"/gwstats_*/" +"*" +file_type + "_*.csv"))
            #print(file_count)
            tinfor_file = GW_LIST_Files_Dir + "\\Test.lst"
            if file_count > 0 :
                E65_Filehandling.record_Log(E65_Scripts_Dir,file_count,file_folder)
                f = open(tinfor_file,"w+")
                #print("file opened")
                for name in glob.glob(JUP_ETL_Files_Dir +"/gwstats_*/" +"*" +file_type + "_*.csv"):
                    f.write("%s\n" % name)
                    #print(name)
                f.close()
                #print("Completed the file list")
                E65_Filehandling.validate(tinfor_file,total_fields,file_folder,file_type)

            else:
                E65_Filehandling.record_Log(E65_Scripts_Dir,file_count,file_folder)
                exit(1)
            
    def record_Log(path,count,file_folder):
        if file_folder == 'TerminalInforView':
            f= open(path +"\\Test.log","a+")
        else:
            f= open(path +"\\Test1.log","a+")
        f.write("------------------------------------------------------------ \n %s : Pre Script Logs \n"% str(datetime.datetime.now())
                    + '---------------------------------------------------------- \n'
                    +'%s : Total : %d files found \n'% (str(datetime.datetime.now()),count))
        if count == 0 :
            f.write (" Hence the task failed.")
        
        f.close()
        
    def validate(tinfor_file,total_fields,file_folder,file_type):
        d = ','
        bad_file_count = 0
        flag = 0
        print(tinfor_file.strip())
        with open(tinfor_file.strip(),"r") as f:
           for line in f:
               new_file_name = line.strip() + '.tmp'
               bad_file_name = line.strip() + '.bad'
               if (os.path.isfile(bad_file_name)== True):
                    os.remove(bad_file_name)
                    os.remove(new_file_name)
                    print('file removed')
               f1 = open(line.strip(),"r")
               print('file opened to read:'+line.strip())
               reader = csv.reader(f1,skipinitialspace=True,delimiter=d,quoting=csv.QUOTE_NONE)
               header = next(reader)
               print("header:" + str(header))
               ncol= len(header)
               if ncol < total_fields:
                   f1.close()
                   os.rename(line.strip(), bad_file_name+'.hdr')
                   break
                
               f2 = open(new_file_name,"a+")
               f3 = open(bad_file_name,"w+")
               
               for row in reader:
                   if flag ==0:
                       csv.writer(f3).writerow( [x.strip() for x in header])
                       csv.writer(f2).writerow([x.strip() for x in header])
                       flag+=1
                       
                   elif len(row)< ncol:
                       csv.writer(f3).writerow(row)
                       
                   else:
                       csv.writer(f2).writerow([x.strip() for x in row])

               f3.seek(0)        
                   
               for x in csv.reader(f3,delimiter=d):
                   if not x:
                       print(x)   
                       f3.close()
                       print('file is empty')
                       os.remove(bad_file_name)
                       print('empty bad file removed')
                       break
                   else:
                       bad_file_count = +bad_file_count
                       print('bad_file_count: ' + str(bad_file_count))

               f1.close()
               f2.close()
               os.remove(line.strip())
               os.rename(new_file_name,line.strip())
               
E65_Filehandling.createFileList()
