import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import BD
    BD.Main()
if bit == '32bit':
    print('[•] Wait 32 Bit Soon')
