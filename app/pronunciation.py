#from dialect_enums import *
# I still don't get what I'm supposed to do with these enums, and they
# aren't importing for some reason anyway. Let's just nuke this feature for now
class Pronunciation:
        def __init__(self,
                     transcription: str,):
                     #dialect: Dialect):


            if not isinstance(transcription, str):
                self.transcription = None
            else:
                self.transcription = transcription

            #if not isinstance(dialect, Dialect):
                    #self.dialect = None
            #else:
                    #self.dialect = dialect
