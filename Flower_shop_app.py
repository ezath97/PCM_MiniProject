import json
import random
class Flower:
    def __init__(self):
        self.Flower_detail={1:{'Name':'Rose','Price':0,'Stock':0},
                            2:{'Name':'Lilly','Price':0,'Stock':0},
                            3:{'Name':'Orchid','Price':0,'Stock':0},
                            4:{'Name':'Gerberas','Price':0,'Stock':0},
                            5:{'Name':'carnations','Price':0,'Stock':0}}


    def Update_flower(self,Flower_ID):
        self.Flower_ID=Flower_ID
        self.name=self.Flower_detail[self.Flower_ID]['Name']
        print(self.name)
        self.Price=input('Enter Price:')
        self.Stock=input('Enter Stock:')
        self.details={'Name':self.name,'Price':self.Price,'Stock':self.Stock}
        self.Flower_detail[self.Flower_ID]=self.details
        return self.Flower_detail
        
    def view_flowers_list(self):
        with open ('Flower_List.json','w') as f:
            json.dump(self.Flower_detail,f,indent=4)
        print('-------------------List of Flower Items--------------------')
        for self.i,self.j in self.Flower_detail.items():
            print('Flower ID:',self.i)
            print('Flower name:',self.j['Name'],'---','Price:',self.j['Price'],'---','Quantity:',self.j['Stock'])
            print('*'*40)
    

class bouquet(Flower):
    def __init__(self):
        super().__init__()

    def bouquet_type(self):
        print('-------------------List of Bouquet catogories----------------------')
        print('-------------------------------------------------------------------')
        print('---------Catagory : Small ---Number_of_Flowers : 4-8---------------')
        print('---------Catagory : Medium---Number_of_Flowers : 8-12--------------')
        print('---------Catagory : Large ---Number_of_Flowers : 12-18-------------')
        print('-------------------------------------------------------------------')
        self.Bouquet_detail={'small':{'Catagory':'small','Flowers':0,'price':0},
                            'medium':{'Catagory':'medium','Flowers':0,'price':0},
                            'large':{'Catagory':'large','Flowers':0,'price':0}}
        self.B_catagory=input('Please Enter Catagory:').lower()
        return self.B_catagory
    
    def view_flowers(self):
        with open ('Flower_List.json','r') as f:
            self.Flower_detail=json.load(f)
        print('-------------------List of Flower Items--------------------')
        for self.i,self.j in self.Flower_detail.items():
            print('Flower ID:',self.i)
            print('Flower name:',self.j['Name'],'---','Price:',self.j['Price'],'---','Quantity:',self.j['Stock'])
            print('*'*40)
        
        
    def select_flowers(self):
        self.id=int(input('Please enter Flower ID: '))
        self.price=0
        if self.id not in [1,2,3,4,5]:
            print('Please enter Correct ID')
            return bouquet.select_flowers(self)
        self.num=int(input('Please enter Number of Flowers:'))
        stk=int(self.Flower_detail[(str(self.id))]['Stock'])
        prc=int(self.Flower_detail[(str(self.id))]['Price'])
        if self.num <= stk:
            self.price = self.price + (self.num * prc)
        else:
            print('Flower out of stock')
            bouquet.select_flowers(self)
        return self.id,self.price,self.num

    def purchase(self):
        self.Hist={}
        self.keys=random.randint(0,100)
        opt=input('Please confirm purchase by typing "YES": ')
        if opt.lower() == 'yes':
            self.Hist[self.keys]={'Bouquet':self.B_catagory,'Flowers':self.Flower_detail[(str(self.id))]['Name'], 'Price':self.price,'number':self.num}
        return self.Hist


    def view_history(self):
        print('-------------------List of Purchase History--------------------')
        for self.i,self.j in self.Hist.items():
            print('ID:',self.i,' -- Bouquet:',self.j['Bouquet'],' -- Flowers:',self.j['Flowers'],' -- Price:',self.j['Price'],' -- number:',self.j['number'])
            print('*'*40)


c=Flower()
c.Update_flower(1)
c.Update_flower(2)
c.Update_flower(3)
c.Update_flower(4)
c.Update_flower(5)
c.view_flowers_list()
b=bouquet()
b.bouquet_type()
b.view_flowers()
b.select_flowers()
b.purchase()
b.view_history()

