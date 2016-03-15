#!/usr/bin/python

# Written by Anubis
# Just a small script to remove duplicate words from wordlist, etc
# Anyway I got 5 minutes so I wrote this thing.
# Codes are too simple, therefore no comment marked


def filter(file):
    print"\n[+] Duplicate Words Remover"
    print"[=] Written by Anubis"
    print"[=] www.mmsecurity.net/forum"
    print"[=] Please be patient, it will take time depending on wordlist size"

    try:
        x = open(file).readlines()
        print"\n[+] Original : [%s] Lines" % len(x)
        y = []
        for i in x:
            y.append(i)
            x.remove(i)

        print"[+] Duplicates : [%d] Lines" % int(len(x)-len(y))

        if int(len(x)-len(y)) == 0:
            print"\n[+] No Duplicate Words"
            #print"[+] New File not written"
            endtime = time.time()
            duration = endtime - starttime
            print"[+] Action Completed in [%.3f] Seconds" % duration

        elif int(len(x)-len(y)) != 0:
            z = open(file,'w')
            for i in y:
                if i != '\n': z.write(i)
            z.close()
            endtime = time.time()
            duration = endtime - starttime

            print"[+] New File : [%s] Lines" % len(y)
            print"[+] Duplicate Words Removed!"
            print"[+] Action Completed in [%.3f] Seconds" % duration

    except IOError:
        print"[!] File Not Found!"
        print"[!] Check if the file name is correct or not"
    except KeyboardInterrupt:
        print"[!] Ctrl^C detected!"
        print"[!] Program Terminated"

if __name__ == '__main__':
    import sys, time
    from os.path import basename
    if len(sys.argv) == 1:
        print"\n\n\t[!] %s wordlist.txt" % basename(sys.argv[0])
        print"\n[=] Written by Anubis"
        print"[=] www.4sectors.com/forum"
    elif len(sys.argv) == 2:
        global starttime
        starttime = time.time()
        filter(sys.argv[1])

