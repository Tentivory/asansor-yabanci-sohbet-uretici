#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansör Yabancı Sohbet Üretici
Bu kod, asansörde karşılaşan iki yabancının olası saçma sohbetlerini üretir.
Gerçekten çalışır, denemeden inanmayın.
"""

import random

sohbetler = [
    "A: 'Hava nasıl?'\nB: 'Asansörün içinde, dışarıdan haberim yok. Sen?'\nA: 'Ben de öyle.'",
    "A: 'Bu asansör çok yavaş.'\nB: 'Evet, belki de zaman durmuştur. Felsefe yapalım mı?'\nA: 'Olur, ama önce hangi katta iniyoruz?'",
    "A: 'Kedin var mı?'\nB: 'Hayır, ama asansörde bir kedi gördüm. Kaçtı.'\nA: 'Asansör kedisi mi? Efsane.'",
    "A: 'Kahve içelim mi?'\nB: 'Asansörde mi? Riskli. Ama cesurum.'\nA: 'Tamam, 3. katta bekliyorum.'",
    "A: 'Bugün ne yaptın?'\nB: 'Asansöre bindim. Sen?'\nA: 'Ben de. Aynı hikaye.'",
    "A: 'Müzik çalalım mı?'\nB: 'Asansör müziği zaten çalıyor. Daha kötü mü olsun?'\nA: 'Haklısın, susalım.'"
]

def uret_sohbet():
    return random.choice(sohbetler)

if __name__ == "__main__":
    print("=== ASANSÖR SOHBETİ ===")
    print(uret_sohbet())
    print("\nNot: Gerçek hayatta denemeyin, asansör sıkışabilir ve sohbet uzayabilir.")

# Gizli saklı mesaj (base64 decode edin): ZGVtb2tyYXNpIGl5aWRpci4gQW1hIGFzYW5zb3IgZGFoYSBpeWku
# Ciddiyetle saçmalık.
