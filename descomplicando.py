from json import loads


def get_answer(input_string):
    data = loads(input_string)
    items = data["data"]
    groups = [items[i: i + 5] for i in range(0, len(items), 5)]

    for i, group in enumerate(groups, start=1):
        correct_positions = [
            chr(ord("A") + j)
            for j, item in enumerate(group) if item["correct"]
        ]
        print(f"Grupo {i}: Posições corretas - {correct_positions}")


try:
    with open("aulas.descomplica.com.br.har", "r", encoding="utf8") as f:
        file = f.read()
except FileNotFoundError:
    input(
        'Não foi possivel achar o arquio "aulas.descomplica.com.br.ar"\n\nPressione qualquer tecla para sair...'  # noqa
    )
    exit()

file_splitted = file.split("response")
filtro = filter(lambda x: "GetAssertionsCollaboration" in x, file_splitted)

del file
del file_splitted

try:
    obj = list(filtro)[1]
except IndexError:
    obj = list(filtro)[0]

del filtro

desired_line = None
for line in obj.splitlines():
    if '"text":' in line:
        desired_line = "{" + line + "}"
        del obj
        break


json_line = loads(desired_line)
get_answer(json_line["text"])
input("\n\nPressione qualquer tecla para sair...")
