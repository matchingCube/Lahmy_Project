from PyPDF2 import PdfReader, PdfWriter
import uuid

def toPercent(value):
    return str(round(float(value) * 100,2))

def myPdfs(kupotData,myData,kupaType):

    reader = PdfReader("application/pdf/Gemeltech_PDF.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)
    writer.update_page_form_field_values(
        writer.pages[0],
        {"sugKupa": kupaType,
        "milatHipos": myData["search"],
        "menayotLimit": myData["menayot"],
        "matachLimit": myData["matach"],
        "checkDate": myData["date"]}
    )
    index=0
    for kupa in kupotData:
        index+=1
        writer.update_page_form_field_values(
                writer.pages[0],
                {"netunimDate": kupa.AD_TKUFAT_DIVUACH.strftime("%d/%m/%Y"),
                f"kupa{index}_shemGoof": kupa.ShemMenahel[0:11],
                f"kupa{index}_maslul": kupa.shemKupa[0:21],
                f"kupa{index}_number": int(kupa.IdKupa),
                f"kupa{index}_mainHitmahut": kupa.HITMAHUT_RASHIT,
                f"kupa{index}_tsua1": f"{toPercent(kupa.TSUA_MITZT_MI_THILAT_SHANA)}%",
                f"kupa{index}_tsua2": f"{toPercent(kupa.TSUA_MITZTABERET_LETKUFA)}%",
                f"kupa{index}_tsua3": f"{toPercent(kupa.TSUA_MITZTABERET_36_HODASHIM)}%",
                f"kupa{index}_tsua4": f"{toPercent(kupa.TSUA_MITZTABERET_60_HODASHIM)}%",
                f"kupa{index}_sharp": round(kupa.Sharp,2),
                f"kupa{index}_stiyatTeken": f"{toPercent(kupa.StiatTeken)}%",
                f"kupa{index}_hasifaLemenayot": f"{toPercent(kupa.ChassifaLeMenayot)}%",
                f"kupa{index}_hasifaLematach": f"{toPercent(kupa.ChassifaLeMatach)}%",
                f"kupa{index}_beta": round(kupa.Beta,2),
                f"kupa{index}_mezumanim": f"{toPercent(kupa.ACHUZ_SUG_NECHES4708_)}%",
                f"kupa{index}_agachMeyoadot": f"{toPercent(kupa.ACHUZ_SUG_NECHES4712_)}%",
                f"kupa{index}_agachMemshaltiot": f"{toPercent(kupa.ACHUZ_SUG_NECHES4701_)}%",
                f"kupa{index}_pikdonot": f"{toPercent(kupa.ACHUZ_SUG_NECHES4706_)}%",
                f"kupa{index}_konzernySachir": f"{toPercent(kupa.ACHUZ_SUG_NECHES4703_)}%",
                f"kupa{index}_konzernyLoSachir": f"{toPercent(kupa.ACHUZ_SUG_NECHES4704_)}%",
                f"kupa{index}_halvaot": f"{toPercent(kupa.ACHUZ_SUG_NECHES4707_)}%",
                f"kupa{index}_kranotNemanoot": f"{toPercent(kupa.ACHUZ_SUG_NECHES4709_)}%",
                f"kupa{index}_menayot": f"{toPercent(kupa.ACHUZ_SUG_NECHES4705_)}%",
                f"kupa{index}_nechasimAcherim": f"{toPercent(kupa.ACHUZ_SUG_NECHES4710_)}%",
                f"kupa{index}_dmiNihool": f"{toPercent(kupa.dnBp)}%",
                f"kupa{index}_LoSachir": f"{toPercent(kupa.ACHUZ_LoSachir)}%",
                f"kupa{index}_odefActuary": f"{toPercent(kupa.ODEF_GIRAON_ACTUARI_LETKUFA)}%"
                }
        )

    # make a random UUID
    name = uuid.uuid4().hex
    
    with open(f"application/pdf/res_{name}.pdf", "wb") as output_stream:
        return writer.write(output_stream)
