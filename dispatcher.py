class Dispatcher:
    cmds = {}

    def reg(self, cmd, fn):
        self.cmds[cmd] = fn

    def run(self):
        pass

    def defaultfn(self):
        print("Unknown Command")
