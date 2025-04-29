from django.shortcuts import render

def formulario_view(request):
    if request.method == 'POST':
        # Pega todos os campos normalmente...
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        link = request.POST.get('link')
        zona = request.POST.get('zona')
        frente = request.POST.get('frente')
        profundidade = request.POST.get('profundidade')
        area = request.POST.get('area')
        ca_basico = request.POST.get('ca_basico')
        ca_maximo = request.POST.get('ca_maximo')
        taxa_ocupacao = request.POST.get('taxa_ocupacao')
        recuo_frontal = request.POST.get('recuo_frontal')
        recuo_lateral = request.POST.get('recuo_lateral')
        recuo_fundos = request.POST.get('recuo_fundos')
        altura_maxima = request.POST.get('altura_maxima')
        studio = request.POST.get('studio_m2')
        dois_dorms = request.POST.get('dois_dorm_m2')
        tres_dorms = request.POST.get('tres_dorm_m2')
        percentual_area_comum = request.POST.get('percentual_area_comum')
        vagas_unidade = request.POST.get('vagas_minimas_unidade')
        comercio_terreo = request.POST.get('comercio_obrigatorio')

        responseText = f"""Você é um assistente especialista em planejamento urbano e viabilidade imobiliária.

Com base nas informações abaixo, calcule:<br><br>
1. A área máxima construída permitida (com e sem outorga onerosa);<br>
2. A área útil (descontando % de áreas comuns);<br>
3. A quantidade máxima de unidades por tipo (studios, 2 dorms, 3 dorms);<br>
4. A taxa de ocupação e os recuos obrigatórios aplicáveis ao terreno;<br>
5. O número máximo de pavimentos permitidos (assuma 3 m por pavimento);<br>
6. O total mínimo de vagas de garagem exigidas;<br>
7. Um resumo executivo com os principais números.<br><br><br>

---

📌 *Dados do Projeto:*<br><br>

Cidade: {cidade} - {estado}  <br>
Link do Plano Diretor: {link}  <br>
Zona urbana: {zona}<br>
Frente do terreno (m): {frente}<br>
Profundidade do terreno (m): {profundidade}<br>
Área do terreno (m²): {area} <br>
Coeficiente de Aproveitamento básico (CA): {ca_basico}  <br>
CA máximo com outorga onerosa: {ca_maximo}  <br>
Taxa de ocupação permitida (%): {taxa_ocupacao} <br>
Recuos obrigatórios (m):<br>
- Frontal: {recuo_frontal}  <br>
- Lateral: {recuo_lateral}<br>
- Fundos: {recuo_fundos}  <br>
Altura máxima permitida (m): {altura_maxima}  <br><br>

🏠 *Tipos de unidades residenciais e áreas médias (m²):*  <br>
- Studio: {studio}<br>
- 2 dormitórios: {dois_dorms} <br>
- 3 dormitórios: {tres_dorms}<br><br>

📦 % de área comum a descontar: {percentual_area_comum}<br>
🚗 Vagas mínimas por unidade: {vagas_unidade} <br>
🏪 Comércio no térreo é obrigatório? {comercio_terreo}
"""

        return render(request, 'formulario.html', {'resposta': responseText})

    return render(request, 'formulario.html')
