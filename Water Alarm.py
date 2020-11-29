import datetime
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
print("select what you want:\n1 for making changes in your water drinking timings\n2 for playing your previous water alarm timings")
a = int(input())
if a==1:
    print("how many timings you want to give(note- you can give only 5 timings in a day)")
    d = int(input())
    d1 = str(d)
    with open("imp.txt" , "w") as adi:
        adi.write(d1)
        
    if d>7 or d<1:
        exit()
    else:
        if d==1:
            print("*first timings*\nenter the hour")
            b = int(input())
            b1 = str(b)
            
            print("*first timings*\nenter the minute")
            c = int(input())
            c1 = str(c)
            
            
        
            with open("a1.txt" , "w") as bb2:
                bb2.write(b1)
            with open("a2.txt" , "w") as cc2:
                cc2.write(c1)
            print("ok your data have been stored")
            print("press 1 to exit")
            ala = int(input())
            if ala == 1:
                exit()
            else:
                print("press 1 to exit")
                alaa = int(input())
                if alaa == 1:
                    exit()
                
        elif d==2:
         
            print("*first timings*\nenter the hour")
            bb = int(input())
            bb1 = str(bb)
            
            print("*first timings*\nenter the minute")
            cc = int(input())
            cc1 = str(cc)
            
            
        
            with open("a3.txt" , "w") as bb2:
                bb2.write(bb1)
            with open("a4.txt" , "w") as cc2:
                cc2.write(cc1)
            
            print("*second timings*\nenter the hour")
            bbb = int(input())
            bbb1 = str(bbb)
            
            print("*second timings*\nenter the minute")
            ccc = int(input())
            ccc1 = str(ccc)
            
            
        
            with open("aa3.txt" , "w") as bbu2:
                bbu2.write(bbb1)
            with open("aa4.txt" , "w") as ccu2:
                ccu2.write(ccc1)
            print("ok your data have been stored")
            print("press enter to exit")
            print("press 1 to exit")
            ala = int(input())
            if ala == 1:
                exit()
            else:
                print("press 1 to exit")
                alaa = int(input())
                if alaa == 1:
                    exit()
                
        elif d == 3:
            print("*first timings*\nenter the hour")
            bbuu = int(input())
            bbuu1 = str(bbuu)
            
            print("*first timings*\nenter the minute")
            ccuu = int(input())
            ccuu1 = str(ccuu)
            
            
        
            with open("auu3.txt" , "w") as bbuu2:
                bbuu2.write(bbuu1)
            with open("auu4.txt" , "w") as ccuu2:
                ccuu2.write(ccuu1)
            
            print("*second timings*\nenter the hour")
            bbbuu = int(input())
            bbbuu1 = str(bbbuu)
            
            print("*second timings*\nenter the minute")
            cccuu = int(input())
            cccuu1 = str(cccuu)
            
            
        
            with open("aauu3.txt" , "w") as bbuuu2:
                bbuuu2.write(bbbuu1)
            with open("aauu4.txt" , "w") as ccuuu2:
                ccuuu2.write(cccuu1)
            print("*third timings*\nenter the hour")
            bbbuuaa = int(input())
            bbbuuaa1 = str(bbbuuaa)
            
            print("*third timings*\nenter the minute")
            cccuuaa = int(input())
            cccuuaa1 = str(cccuuaa)
            with open("aauuaa3.txt" , "w") as bbuuuaa2:
                bbuuuaa2.write(bbbuuaa1)
            with open("aauuaa4.txt" , "w") as ccuuuaa2:
                ccuuuaa2.write(cccuuaa1)
            
            print("ok your data have been stored")
            
            print("press 1 to exit")
            ala = int(input())
            if ala == 1:
                exit()
            else:
                print("press 1 to exit")
                alaa = int(input())
                if alaa == 1:
                    exit()
        elif d == 4:
            print("*first timings*\nenter the hour")
            bbuu = int(input())
            bbuu1 = str(bbuu)
            
            print("*first timings*\nenter the minute")
            ccuu = int(input())
            ccuu1 = str(ccuu)
            
            
        
            with open("auu31.txt" , "w") as bbuu2:
                bbuu2.write(bbuu1)
            with open("auu41.txt" , "w") as ccuu2:
                ccuu2.write(ccuu1)
            
            print("*second timings*\nenter the hour")
            bbbuu = int(input())
            bbbuu1 = str(bbbuu)
            
            print("*second timings*\nenter the minute")
            cccuu = int(input())
            cccuu1 = str(cccuu)
            
            
        
            with open("aauu31.txt" , "w") as bbuuu2:
                bbuuu2.write(bbbuu1)
            with open("aauu41.txt" , "w") as ccuuu2:
                ccuuu2.write(cccuu1)
            print("*third timings*\nenter the hour")
            bbbuuaa = int(input())
            bbbuuaa1 = str(bbbuuaa)
            
            print("*third timings*\nenter the minute")
            cccuuaa = int(input())
            cccuuaa1 = str(cccuuaa)
            with open("aauuaa31.txt" , "w") as bbuuuaa2:
                bbuuuaa2.write(bbbuuaa1)
            with open("aauuaa41.txt" , "w") as ccuuuaa2:
                ccuuuaa2.write(cccuuaa1)
            print("*fourth timings*\nenter the hour")
            bbbuuaa1t = int(input())
            bbbuuaa1t1 = str(bbbuuaa)
            
            print("*fourth timings*\nenter the minute")
            cccuuaa1 = int(input())
            cccuuaa11 = str(cccuuaa)
            with open("aauuaa311.txt" , "w") as bbuuuaat2:
                bbuuuaat2.write(bbbuuaa1t1)
            with open("aauuaa411.txt" , "w") as ccuuuaat2:
                ccuuuaat2.write(cccuuaa11)
            
            print("ok your data have been stored")
            
            print("press 1 to exit")
            ala = int(input())
            if ala == 1:
                exit()
            else:
                print("press 1 to exit")
                alaa = int(input())
                if alaa == 1:
                    exit()
        elif d == 5:
            print("*first timings*\nenter the hour")
            bbuu = int(input())
            bbuu1 = str(bbuu)
            
            print("*first timings*\nenter the minute")
            ccuu = int(input())
            ccuu1 = str(ccuu)
            
            
        
            with open("auu311.txt" , "w") as bbuu2:
                bbuu2.write(bbuu1)
            with open("auu411.txt" , "w") as ccuu2:
                ccuu2.write(ccuu1)
            
            print("*second timings*\nenter the hour")
            bbbuu = int(input())
            bbbuu1 = str(bbbuu)
            
            print("*second timings*\nenter the minute")
            cccuu = int(input())
            cccuu1 = str(cccuu)
            
            
        
            with open("aauu311.txt" , "w") as bbuuu2:
                bbuuu2.write(bbbuu1)
            with open("aauu411.txt" , "w") as ccuuu2:
                ccuuu2.write(cccuu1)
            print("*third timings*\nenter the hour")
            bbbuuaa = int(input())
            bbbuuaa1 = str(bbbuuaa)
            
            print("*third timings*\nenter the minute")
            cccuuaa = int(input())
            cccuuaa1 = str(cccuuaa)
            with open("aauuaa311.txt" , "w") as bbuuuaa2:
                bbuuuaa2.write(bbbuuaa1)
            with open("aauuaa411.txt" , "w") as ccuuuaa2:
                ccuuuaa2.write(cccuuaa1)
            print("*fourth timings*\nenter the hour")
            bbbuuaa1 = int(input())
            bbbuuaa11 = str(bbbuuaa)
            
            print("*fourth timings*\nenter the minute")
            cccuuaa1 = int(input())
            cccuuaa11 = str(cccuuaa)
            with open("aauuaa3111.txt" , "w") as bbuuuaa21:
                bbuuuaa21.write(bbbuuaa11)
            with open("aauuaa4111.txt" , "w") as ccuuuaa21:
                ccuuuaa21.write(cccuuaa11)
            print("*fifth timings*\nenter the hour")
            bbbuuaa1aa = int(input())
            bbbuuaa11aa = str(bbbuuaa1aa)
            
            print("*fifth timings*\nenter the minute")
            cccuuaa1111 = int(input())
            cccuuaa11111 = str(cccuuaa1111)
            with open("aauuaa31111.txt" , "w") as bbuuuaa12:
                bbuuuaa12.write(bbbuuaa11aa)
            with open("aauuaa41111.txt" , "w") as ccuuuaa12:
                ccuuuaa12.write(cccuuaa11111)
            print("ok your data have been stored")
            
            print("press 1 to exit")
            ala = int(input())
            if ala == 1:
                exit()
            else:
                while(True):
                    print("press 1 to exit")
                    alaa = int(input())
                    if alaa == 1:
                        exit()
                    else:
                        print("enter 1 to exit")
                        alaa = int(input())
                        continue


elif a==2:
    ad1 = open("imp.txt" , "r")
    add1 = int(ad1.read())
    if add1 == 1:
        print("ok!! your previous alarm has started")
        var1 = open("a1.txt" , "r")
        var2 = int(var1.read())
        var3 = open("a2.txt" , "r")
        var4 = int(var3.read())
        while(1 == 1):

            if(var2 == datetime.datetime.now().hour and var4 == datetime.datetime.now().minute):
                speak("its time you should drink 1 glass water")
                speak("honestly press enter if you have drank")
                input()

                speak("well done you completed your target of drinking 1 glass water, bye")
                exit()
    if add1 == 2:
        print("ok!! your previous alarm has started")
        var1 = open("a3.txt" , "r")
        var2 = int(var1.read())
        var3 = open("a4.txt" , "r")
        var4 = int(var3.read())
        while(1 == 1):

            if(var2 == datetime.datetime.now().hour and var4 == datetime.datetime.now().minute):
                speak("its time you should drink 1 glass water")
                speak("honestly press enter if you have drank")
                input()
                speak("ok your next alarm is started!!")
                var111 = open("aa3.txt" , "r")
                var112 = int(var111.read())
                var113 = open("aa4.txt" , "r")
                var114 = int(var113.read())
                while(1 == 1):

                    if(var112 == datetime.datetime.now().hour and var114 == datetime.datetime.now().minute):
                        speak("its time you should drink 1 glass water")
                        speak("honestly press enter if you have drank")
                        input()
                        speak("well done you completed your target of drinking 2 glass water, bye")
                        exit()
    if add1 == 3:
        print("ok!! your previous alarm has started")
        var1 = open("auu3.txt" , "r")
        var2 = int(var1.read())
        var3 = open("auu4.txt" , "r")
        var4 = int(var3.read())
        while(1 == 1):

            if(var2 == datetime.datetime.now().hour and var4 == datetime.datetime.now().minute):
                speak("its time you should drink 1 glass water")
                speak("honestly press enter if you have drank")
                input()
                speak("ok your next alarm is started!!")
                var11u1 = open("aauu3.txt" , "r")
                var11u2 = int(var11u1.read())
                var11u3 = open("aauu4.txt" , "r")
                var11u4 = int(var11u3.read())
                while(1 == 1):

                    if(var11u2 == datetime.datetime.now().hour and var11u4 == datetime.datetime.now().minute):
                        speak("its time you should drink 1 glass water")
                        speak("honestly press enter if you have drank")
                        input()
                        speak("ok your next alarm is started!!")
                        var111 = open("aauuaa3.txt" , "r")
                        var112 = int(var111.read())
                        var113 = open("aauuaa4.txt" , "r")
                        var114 = int(var113.read())
                        while(1 == 1):

                            if(var112 == datetime.datetime.now().hour and var114 == datetime.datetime.now().minute):
                                speak("its time you should drink 1 glass water")
                                speak("honestly press enter if you have drank")
                                input()
                                speak("well done you completed your target of drinking 3 glass water, bye")
                                exit()
    elif add1 == 4:
        print("ok!! your previous alarm has started")
        vara1 = open("auu31.txt" , "r")
        vara2 = int(vara1.read())
        vara3 = open("auu41.txt" , "r")
        vara4 = int(vara3.read())
        while(1 == 1):

            if(vara2 == datetime.datetime.now().hour and vara4 == datetime.datetime.now().minute):
                speak("its time you should drink 1 glass water")
                speak("honestly press enter if you have drank")
                input()
                speak("ok your next alarm is started!!")
                var11au1 = open("aauu31.txt" , "r")
                var11au2 = int(var11au1.read())
                var11au3 = open("aauu41.txt" , "r")
                var11au4 = int(var11au3.read())
                while(1 == 1):

                    if(var11au2 == datetime.datetime.now().hour and var11au4 == datetime.datetime.now().minute):
                        speak("its time you should drink 1 glass water")
                        speak("honestly press enter if you have drank")
                        input()
                        speak("ok your next alarm is started!!")
                        var11aa1 = open("aauuaa31.txt" , "r")
                        var11aa2 = int(var11aa1.read())
                        var11aa3 = open("aauuaa41.txt" , "r")
                        var11aa4 = int(var11aa3.read())
                        while(1 == 1):

                            if(var11aa2 == datetime.datetime.now().hour and var11aa4 == datetime.datetime.now().minute):
                                speak("its time you should drink 1 glass water")
                                speak("honestly press enter if you have drank")
                                input()
                                speak("ok your next alarm is started!!")
                                var11aaa1 = open("aauuaa311.txt" , "r")
                                var11aaa2 = int(var11aaa1.read())
                                var11aaa3 = open("aauuaa411.txt" , "r")
                                var11aaa4 = int(var11aaa3.read())
                                while(1 == 1):

                                    if(var112 == datetime.datetime.now().hour and var114 == datetime.datetime.now().minute):
                                        speak("its time you should drink 1 glass water")
                                        speak("honestly press enter if you have drank")
                                        input()
                                        speak("well done you completed your target of drinking 4 glass water, bye")
                                        exit()
    elif add1 == 5:
        print("ok!! your previous alarm has started")
        var1f = open("auu311.txt" , "r")
        var2f = int(var1f.read())
        var3f = open("auu411.txt" , "r")
        var4f = int(var3f.read())
        while(1 == 1):

            if(var2f == datetime.datetime.now().hour and var4f == datetime.datetime.now().minute):
                speak("its time you should drink 1 glass water")
                speak("honestly press enter if you have drank")
                input()
                speak("ok your next alarm is started!!")
                var111u1fu = open("aauu311.txt" , "r")
                var111u2fu = int(var111u1fu.read())
                var111u3fu = open("aauu411.txt" , "r")
                var111u4fu = int(var111u3fu.read())
                while(1 == 1):

                    if(var111u2fu == datetime.datetime.now().hour and var111u4fu == datetime.datetime.now().minute):
                        speak("its time you should drink 1 glass water")
                        speak("honestly press enter if you have drank")
                        input()
                        speak("ok your next alarm is started!!")
                        var1111fuw = open("aauuaa311.txt" , "r")
                        var1112fuw = int(var1111fuw.read())
                        var1113fuw = open("aauuaa411.txt" , "r")
                        var1114fuw = int(var1113fuw.read())
                        while(1 == 1):

                            if(var1112fuw == datetime.datetime.now().hour and var1114fuw == datetime.datetime.now().minute):
                                speak("its time you should drink 1 glass water")
                                speak("honestly press enter if you have drank")
                                input()
                                speak("ok your next alarm is started!!")
                                var11111as = open("aauuaa3111.txt" , "r")
                                var11112as = int(var11111as.read())
                                var11113as = open("aauuaa4111.txt" , "r")
                                var11114as = int(var11113as.read())
                                while(1 == 1):

                                    if(var11112as == datetime.datetime.now().hour and var11114as == datetime.datetime.now().minute):
                                        speak("its time you should drink 1 glass water")
                                        speak("honestly press enter if you have drank")
                                        input()
                                        speak("ok your next alarm is started!!")
                                        var111111asa = open("aauuaa31111.txt" , "r")
                                        var111112asa = int(var111111.read())
                                        var111113asa = open("aauuaa41111.txt" , "r")
                                        var111114asa = int(var111113.read())
                                        while(1 == 1):

                                            if(var111112asa == datetime.datetime.now().hour and var111114asa == datetime.datetime.now().minute):
                                                speak("its time you should drink 1 glass water")
                                                speak("honestly press enter if you have drank")
                                                input()
                                        
                                
    
                
        
    
    
