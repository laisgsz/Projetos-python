vlc = int(input('digite sua velocidade: '))
vlc_max = 70

if vlc <= vlc_max :
     print('Nao tomou multa')
elif vlc > vlc_max and vlc <= vlc_max + 10: 
     print('Tomou multa leve')
elif vlc > vlc_max and vlc <= vlc_max + 20: 
    print('tomou multa grave')
elif vlc > vlc_max + 20:
      print('Tomou multa gravissima')