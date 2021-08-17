# liyeplimal simulator.


packs = {
    'pack_01': 200,
    'pack_02': 400,
    'pack_03': 800,
    'pack_04': 1600,
    'pack_05': 3200,
    'pack_06': 6400,
    'pack_07': 12800,
    'pack_08': 25600,
    'pack_09': 51200,
    'pack_10': 100000,
    'pack_11': 500000,
    'pack_12': 1000000}

packs_1 = sorted(packs.keys(), reverse=True)
packs_2 = sorted(packs.values(), reverse=True)
packs_0 = dict(zip(packs_1, packs_2))

packs_list = list(packs.keys())
interest = list(packs.values())

totaux = dict(A=1.7 * packs['pack_01'], B=1.8 * packs['pack_02'], C=1.9 * packs['pack_03'], D=2 * packs['pack_04'],
              E=2.05 * packs['pack_05'], F=2.10078125 * packs['pack_06'], G=2.15 * packs['pack_07'],
              H=2.2 * packs['pack_08'], J=2.24 * packs['pack_09'], K=2.25 * packs['pack_10'],
              L=2.26666 * packs['pack_11'], M=2.28332 * packs['pack_12'])
