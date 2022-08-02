import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import AKING
    AKING.Main()
if bit == '32bit':
    import AKING32
    AKING32.Main()
