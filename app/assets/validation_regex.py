
telefono_reg = r'^(\d{3} ?){2}\d{4} *$'

nome_reg = r'^([A-ZÀÈÉÌÒÙ][a-zàéèòùì]+ )*([A-Z][a-zàéèòùì]+) *$'

cognome_reg = r'^([A-ZÀÈÉÌÒÙ](\'[A-ZÀÈÉÌÒÙ])?[a-zàéèòùì]+(-| ))*([A-ZÀÈÉÌÒÙ](\'[A-ZÀÈÉÌÒÙ])?[a-zàéèòùì]+) *$'

urbe_reg = r'^[A-ZÀÈÉÌÒÙ][a-zàéèòùì]*(( |\')[A-ZÀÈÉÌÒÙ]?[a-zàéèòùì]+)* *$'

indirizzo_reg = r'^(Viale|Via|Corso|Piazza|Piazzale) [A-ZÀÈÉÌÒÙ]?[a-zàéèòùì]+(( |\')[A-ZÀÈÉÌÒÙ]?[a-zàéèòùì]+)* \d+ *$'

password_reg = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'