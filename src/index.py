from varasto import Varasto

def print_varasto_info(mehu_varasto, olut_varasto):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu_varasto}")
    print(f"Olutvarasto: {olut_varasto}")

def print_olut_getters(olut_varasto):
    print("Olut getterit:")
    print(f"saldo = {olut_varasto.saldo}")
    print(f"tilavuus = {olut_varasto.tilavuus}")
    print(f"paljonko_mahtuu = {olut_varasto.paljonko_mahtuu()}")

def test_mehu_setters(mehu_varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu_varasto.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu_varasto}")
    print("Otetaan 3.14")
    mehu_varasto.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu_varasto}")

def test_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def test_ylitaytto(olut_varasto, mehu_varasto):
    print(f"Olutvarasto: {olut_varasto}")
    print("olutta.lisaa_varastoon(1000.0)")
    olut_varasto.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olut_varasto}")

    print(f"Mehuvarasto: {mehu_varasto}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehu_varasto.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehu_varasto}")

def test_ottaminen(olut_varasto, mehu_varasto):
    print(f"Olutvarasto: {olut_varasto}")
    saatiin = olut_varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olut_varasto}")

    print(f"Mehuvarasto: {mehu_varasto}")
    saatiin = mehu_varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehu_varasto}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print_varasto_info(mehua, olutta)
    print_olut_getters(olutta)
    test_mehu_setters(mehua)
    test_virhetilanteet()
    test_ylitaytto(olutta, mehua)
    test_ottaminen(olutta, mehua)

if __name__ == "__main__":
    main()
