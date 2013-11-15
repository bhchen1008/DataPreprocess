#encoding:utf-8
'''
Created on 2012/12/25

@author: NetDB

IBM_Generator輸出格式如下
Customer_ID    Item_ID
此Translator要將IBM_Generator產出的格式轉換成
每一行是一個Transaction的格式，如下
Item_ID,Item_ID....=>一行為一個Customer所購買的物品
'''
import sys

#若輸入的參數不對，則無法繼續進行，輸入參數依序為input_file,output_file,seperated_string(分隔符號)
if(len(sys.argv)!=4): 
    print "please give 3 parameters(ex. input_file output_file seperated_string)"

else:
    input_f = open(sys.argv[1]);
    output_f = open(sys.argv[2],'w');
    Seperated_String = sys.argv[3]
    
    lines = input_f.readlines()             #讀取input_file的每一行
    line_current = int(lines[0].split()[0]) #目前正在編輯的那一行，一開始設為第一個Customer的ID    
    line_start = 1                          #分辨是否要插入分隔符號用，只有第一個Transaction需要辨認
    
    for line in lines:
        line_content = line.split();        #將每一行做個split方便取值 
        line_num = int(line_content[0])     #紀錄Customer_ID，也就是該行的Item應該屬於哪個Customer
        line_value = int(line_content[2])   #紀錄Item_ID
              
        if(line_current == line_num):       #如果目前編輯的line=讀取進來的line_num(也就是Customer_ID)，則繼續於同一行編輯            
            if(line_start != 1):
                output_f.write(Seperated_String + str(line_value))
            else:                
                output_f.write(str(line_value))
            line_start = 0                  #使得可以辨認接下來的不是第一個Item  
            
        else:                               #若目前編輯的這一行與line_num不一樣時，則要跳下一行繼續編輯
            line_current = line_num         #將目前編輯的這一行改為下一行            
            output_f.write("\n" + str(line_value)) #換行之後繼續從第一個開始印

