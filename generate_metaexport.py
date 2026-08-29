import json

# Define the basic services structure based on the traditional Wix/Squarespace "Products & Services" paradigm
# Wix Headless Drop allows defining meta exports for data ingestion

meta_export = {
    "version": "1.0",
    "entities": {
        "services": [
            {
                "id": "srv-ortodoncia",
                "name": "Ortodoncia (Brackets y Alineadores)",
                "description": "Tratamientos de ortodoncia especializada incluyendo brackets metálicos, estéticos y alineadores invisibles.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"  # To be defined, or custom consultation
                },
                "category": "Service",
                "duration": 45,
                "url": "/servicio-ortodoncia"
            },
            {
                "id": "srv-cirugia",
                "name": "Cirugía Maxilofacial y Muelas del Juicio",
                "description": "Extracciones complejas y cirugía oral.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"
                },
                "category": "Service",
                "duration": 60,
                "url": "/servicio-cirugia"
            },
            {
                "id": "srv-implantes",
                "name": "Implantes Dentales",
                "description": "Recupera la función y estética de tu sonrisa con implantes dentales.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"
                },
                "category": "Service",
                "duration": 60,
                "url": "/servicio-implantes"
            },
            {
                "id": "srv-endodoncia",
                "name": "Endodoncia",
                "description": "Tratamiento de conductos para salvar dientes dañados o infectados.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"
                },
                "category": "Service",
                "duration": 60,
                "url": "/servicio-endodoncia"
            },
            {
                "id": "srv-periodoncia",
                "name": "Periodoncia",
                "description": "Tratamiento de las enfermedades de las encías y tejidos de soporte.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"
                },
                "category": "Service",
                "duration": 45,
                "url": "/servicio-periodoncia"
            },
            {
                "id": "srv-odontopediatria",
                "name": "Odontopediatría",
                "description": "Atención dental especializada para bebés, niños y adolescentes.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"
                },
                "category": "Service",
                "duration": 45,
                "url": "/servicio-odontopediatria"
            },
            {
                "id": "srv-integral",
                "name": "Odontología Integral y Limpiezas",
                "description": "Prevención, diagnóstico y tratamiento de problemas dentales comunes.",
                "price": {
                    "currency": "MXN",
                    "amount": "0"
                },
                "category": "Service",
                "duration": 45,
                "url": "/servicio-integral"
            }
        ],
        "products": [
             # Leaving empty but ready for physical products or other items if needed in future
        ]
    }
}

with open("export_zip/metaexport.json", "w", encoding="utf-8") as f:
    json.dump(meta_export, f, indent=2, ensure_ascii=False)

print("Generated metaexport.json successfully.")
