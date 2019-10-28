class dataArranger():
    def inputFile(self, file_name):
        self.fn = file_name.split('.')[0]
        f = open(file_name, 'r')
        self.s = f.readlines()
        f.close()

    def printer(self, start_line):
        sender = open(self.fn + '_result.txt', 'w')
        i = 0
        counter = 0.
        for string in self.s:
            if i == 3:
                self.dt = float(string.split()[3])
                #print(self.dt)
            if i >= start_line:
                for word in string.split():
                    print('%.2f  %s' % (counter, word))
                    sender.write('%.2f  %s\n' % (counter, word))
                    counter += self.dt
            i+=1
        sender.close()

a = dataArranger()
a.inputFile('sample.AT2')
a.printer(4)
