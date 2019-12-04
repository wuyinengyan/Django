class Dispatcher:
    def reg(self, cmd, fn):
        pass

    def run(self):
        while True:
            cmd = input(">>>").strip()
            if cmd == "quit":
                break
            getattr(self, cmd, self.defaultfn)()

    def defaultfn(self):
        print("Unknown command")


if __name__ == '__main__':
    d = Dispatcher()
    d.run()
