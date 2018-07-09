while  True:
        c=self.ser.read()
        if int(c)>0:
        	print ("greter than zero")
        	from accesgrntd import access
        	self.q=access()
        	self.q.show()
        	self.close()
        	break
        else:
        	print("its zero")