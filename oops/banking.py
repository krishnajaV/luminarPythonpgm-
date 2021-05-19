class Bank:
    bank_name="SBI Palakkad"
    def registration(self,name,id,phone,gender,age,address,city,minbal):
        self.name=name
        self.id=id
        self.phone=phone
        self.gender=gender
        self.age=age
        self.address=address
        self.city=city
        self.minbal=minbal
        print("name=",self.name)
        print("id=", self.id)
        print("phone=",self.phone)
        print("gender=", self.gender)
        print("age=", self.age)
        print("address", self.address)
        print("city=", self.city)
        print("bank_name=", Bank.bank_name)
        print("minimumbalance",self.minbal)
    def deposit(self,depamount):
        self.depamount=depamount
        print("depositamount=",self.depamount)
        self.total_amount=self.minbal+self.depamount
        print("current amountis=",self.total_amount)
    def withdrowal(self,withamt):
        self.withamt=withamt
        if(self.total_amount>self.minbal):
            print("inefficient Balance")
        else:
            print("enter amount you want",self.withamt)
            self.total_amount=self.total_amount-self.withamt
            print("current balance=",self.total_amount)


ob=Bank()
ob.registration("krishna",45,"905545125","female",25,"vachakkara house","palakkad",5000)
ob.deposit(5000)
ob.withdrowal(1000)
ob1=Bank()
ob1.registration("krishnajith",46,"905545125","male",25,"vachakkara house","palakkad",5000)
ob1.deposit(50000)
ob1.withdrowal(6000)







