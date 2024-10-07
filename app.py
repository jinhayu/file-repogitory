def main():
    class TV:
        def __init__(self):
            self.channel=1
            self.volume=1
            self.on="on"
        def turnon(self):
            return self.on
        def turnoff(self):
             self.on="off"
             return self.on
        def setchannel(self,channel):
            self.channel=channel
            return f"Tv의 채널:{self.channel}"
        def setVolume(self,volume):
            self.volume=volume
            return f"TV의 음량:{self.volume}"
    a=TV()
    print(a.setchannel(11))
    print(a.setVolume(6))
main()
        