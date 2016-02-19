class Mobile(object) :
    def __init__(self,manufacturer,operating_system,model,cost):
        "Here is my docstring"
        self._manufacturer = manufacturer
        self._operating_system = operating_system
        self._model = model
        self._cost = cost

    def getModel(self):
        return self._model

class Android(Mobile):
    def __init__(self,man,os,model,cost):
	    super(Android, self).__init__(man,os,model,cost)

    def getModel(self):
        return "This is Android Mobile-"	+	self._model

class Blackberry(Mobile):
    def __init__(self,man,os,model,cost):
	    super(Blackberry, self).__init__(man,os,model,cost)

    def getModel(self):
        return "This is Blackberry-"	+	self._model

if __name__ == '__main__':
    mobile = Mobile("Nokia","Win8","Lumia",10000)
    print mobile.getModel()
    android = Android("Samsung","Android","Grand",30000) 
    print android.getModel()
    blackberry = Blackberry("BlackB","RIM","Curve",20000)
    print blackberry.getModel()
	
		