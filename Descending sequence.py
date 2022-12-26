#test case : 123443213455443211
class Descending_sequence(object):
    '''class docstring'''
    seq = ''
    def check(self)->None:
        '''function docstring'''
        seq_list = list(map(lambda x :int(x),self.seq))
        exports = list()
        temp = ''
        for i in range(len(seq_list)):
            if i == len(seq_list)-1 :
                if any(temp) is True :
                    last = int(temp[-1])
                    if last>=seq_list[i] :
                        temp+=str(seq_list[i])
                        exports.append(temp)
            else :
                if seq_list[i]>=seq_list[i+1]:
                    temp += str(seq_list[i])
                else :
                    if any(temp) is True :
                        temp += str(seq_list[i]) 
                        exports.append(temp)
                        temp = ''
        lengths = [len(i) 
                   for i in exports]
        if any(lengths) is True :
            idx = lengths.index((max(lengths)))
            return exports[idx]
        else :
            return temp
    
ask = input('enter a numeric sequence :')
if ask.isnumeric() :
    sample = Descending_sequence()
    sample.seq = ask
    print(sample.check())
exit = input('enter any key to exit :')
