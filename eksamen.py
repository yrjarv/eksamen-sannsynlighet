"""
Beregner sannsynligheten for å komme opp i ulike eksamensfag paa ulike trinn
"""
# Endres av bruker
TRINN = 3
skriftlige_fag = ["IT 2", "Fysikk 2", "Sidemål"]
muntlige_fag = ["IT 2", "Fysikk 2", "Historie", "Religion", "Norsk muntlig"]

# Konstanter, kan variere mellom læreplanversjoner og år
fag_samme_dag = [
    ["MAT1019", "MAT1021"],
    ["REA3056", "REA3060", "MAT1023"],
    ["SAM3068", "FSP6219", "FSP6239"],
    ["FSP6152", "FSP6222", "FSP6242"],
    ["SAM3046", "SAM3073", "SPR3036", "REA3039"],
    ["SAM3046", "SAM3073", "SPR3036"],
    ["SAM3055", "SAM3070", "REA3036"],
    ["SAM3051", "SAM3058", "SAM3061", "FSP6226", "REA3046"],
    ["REA3049", "SAM3051", "SAM3058", "SAM3061"],
    ["SPR3031", "REA3049"]
]
oppslag_fag = {
    "Sidemål"           : "NOR1268",
    "Hovedmål"          : "NOR1267",
    "Norsk muntlig"     : "NOR1269",
    "1P"                : "MAT1019",
    "1T"                : "MAT1021",
    "Engelsk 1"         : "SPR3029",
    "Markedsføring 2"   : "SAM3046",
    "Psykologi 2"       : "SAM3073",
    "KK 3"              : "SPR3036",
    "Fysikk 2"          : "REA3039",
    "R1"                : "REA3056",
    "S1"                : "REA3060",
    "2P"                : "MAT1021",
    "Økstyr"            : "SAM3068",
    "Spansk 1"          : "FSP6219",
    "Tysk 1"            : "FSP6239",
    "Politikk"          : "SAM3055",
    "Økled"             : "SAM3070",
    "S2"                : "REA3062",
    "R2"                : "REA3058",
    "Biologi 2"         : "REA3036",
    "Engelsk"           : "ENG1007",
    "Sosialkunnskap"    : "SAM3051",
    "Rettslære 2"       : "SAM3058",
    "Samfunnsøkonomi 2" : "SAM3061",
    "Spansk I+II"       : "FSP6226",
    "Kjemi 2"           : "REA3046",
    "Engelsk 2"         : "SPR3031",
    "IT 2"              : "REA3049"
}

# Oversetting mellom fagnavn og fagkode
for i, fag in enumerate(skriftlige_fag):
    if fag in oppslag_fag:
        skriftlige_fag[i] = oppslag_fag[fag]
for i, fag in enumerate(muntlige_fag):
    if fag in oppslag_fag:
        muntlige_fag[i] = oppslag_fag[fag]

# Beregning av alle mulige kombinasjoner
antall_pr_fag: dict[str, float] = {}
muligheter: list = []
if TRINN == 1:
    for fag in skriftlige_fag:
        antall_pr_fag[fag] = 0.2
        muligheter.append(fag)
    for fag in muntlige_fag:
        if fag in antall_pr_fag:
            antall_pr_fag[fag] += 0.2
        else:
            antall_pr_fag[fag] = 0.2
        muligheter.append(fag)

elif TRINN == 2:
    for fag in skriftlige_fag:
        antall_pr_fag[fag] = 1
        muligheter.append(fag)
    for fag in muntlige_fag:
        if fag in antall_pr_fag:
            antall_pr_fag[fag] += 1
        else:
            antall_pr_fag[fag] = 1
        muligheter.append(fag)

elif TRINN == 3:
    muligheter = []
    for s1 in skriftlige_fag:
        for s2 in skriftlige_fag:
            if s2 == s1: # Ikke mulig at begge skriftlige er i samme fag
                continue
            for dag in fag_samme_dag: # Sjekk om dager kolliderer
                if s1 in dag and s2 in dag:
                    break
            else:
                for m in muntlige_fag:
                    if m in (s1, s2): # Ikke samme muntlig og skriftlig
                        continue
                    if [s2, s1, m] in muligheter: # Allerede funnet
                        continue
                    muligheter.append([s1, s2, m])

    for mulighet in muligheter: # Teller opp
        for fag in mulighet:
            if fag in antall_pr_fag:
                antall_pr_fag[fag] += 1
            else:
                antall_pr_fag[fag] = 1

# Utregning og printing av prosent sannsynlighet
for fag, antall in antall_pr_fag.items():
    if fag in oppslag_fag.values():
        fag = next(k for k, v in oppslag_fag.items() if v == fag)
    print(f"{fag.ljust(20, '.')}{100*antall/len(muligheter):.0f}%")
