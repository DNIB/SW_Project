import time

class dataArranger():
    def inputFile(self, file_name):
        self.fn = file_name.split('.')[0]
        f = open(file_name, 'r')
        self.s = f.readlines()
        f.close()
    
    def printer(self, start_line):
        sender = open(self.fn + '_result.txt', 'w')
        i = 0
        counter = 1
        for string in self.s:
            if i >= start_line:
                for word in string.split():
                    #print('%.2f  %s' % (counter/100, word))
                    sender.write('%.2f  %s\n' % (counter/100, word))
                    counter += 1
            i+=1
        sender.close()
        print("檔案輸出成功，輸出檔名為", self.fn + '_result.txt\n')

sample = dataArranger()
print("注意：處理的檔案應與本程式於同資料夾")
print("若要結束程式，檔名處輸入 end \n")
while True:
    fn = input('請輸入檔名：')
    print(fn)
    if fn == 'end':
        break
        
    try:
        sample.inputFile(fn)
    except:
        print('執行錯誤：檔案不存在？')
        print('提醒：副檔名須一並輸入 如：sample.AT2\n')
        continue
        
    try:
        sample.printer(4)
    except:
        print('執行錯誤 錯誤碼 A01 請回報編寫者\n')
        continue

print("程式執行結束，五秒後關閉")
time.sleep(5)