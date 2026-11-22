# Escreva uma função/programa que compare o que foi bipado com o que o pedido pede e mostre, para
#cada item do pedido, se está OK, FALTANDO n ou SOBRANDO n. Também mostre os SKUs bipados que não
#pertencem ao pedido.

pedido = [
    { "sku": "SSD-1TB-KG", "qtd": 2 },
    { "sku": "MEM-16-DDR5", "qtd": 2 },
    { "sku": "FNT-650W", "qtd": 1 },
    { "sku": "GAB-AIR-01", "qtd": 1 },
]

bipados = [
    "SSD-1TB-KG", "MEM-16-DDR5", "SSD-1TB-KG", "FNT-650W",
    "BRD-MOUSEPAD", "FNT-650W", "CBL-HDMI-2M", "ssd-1tb-kg"
]

bipados = [sku.upper()for sku in bipados ]

print("\nItem no pedido:")
for item in pedido:
    sku = item["sku"]
    qtd_pedida = item["qtd"]
    qtd_bipada = bipados.count(sku)
    
    
    if qtd_bipada == qtd_pedida:
        print(f"{sku}: OK")
    elif qtd_bipada < qtd_pedida:
        print(f"{sku}: FALTANDO {qtd_pedida - qtd_bipada}")
    else:
        print(f"{sku}: SOBRANDO {qtd_bipada - qtd_pedida}")


skus_do_pedido = [item["sku"] for item in pedido]
print("\nFora do pedido:")
for sku in set(bipados): 
    if sku not in skus_do_pedido:
        print(f"{sku}: Não pertence ao pedido (Bipado {bipados.count(sku)}x)")
        


        
total = len(bipados)
    
print(f"Total de intem bipados:{total}")