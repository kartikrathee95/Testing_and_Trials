class Commentary():
    commentary_observers  = []
    def __init__(self):
        pass
    
    def addobserver(self,observer):

        if "app" in observer:
            obj = AppCommentary()
        elif "web" in observer:
            obj= WebsiteCommentary()
        self.commentary_observers.append(obj)

    def notify(self):
        
        for observer in self.commentary_observers:
            observer.update()


                


class AppCommentary():
    def update(self):
        print("App Commentary is as followees = {}".format())



class WebsiteCommentary():
    def update(self):
        print("Website Commentary is as followees = {}".format())
