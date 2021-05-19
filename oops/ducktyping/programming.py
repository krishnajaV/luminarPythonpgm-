class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execution using pycharm")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("execution using vscode")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p=Programmer()
pyc=Pycharm()
p.coding(pyc)