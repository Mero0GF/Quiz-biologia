import random
import time
# funções
def quiz(x):
    print(x)
def quiz1(y):
    print(y*20)
# lista dos exercicios
p1 = """Qual a característica que diferencia por definitivo cobras peçonhentas e não peçonhentas?

a) Um pequeno orifício entre a narina e os olhos desta. 
b) O formato da cabeça.
c) O padrão das escamas na cauda da cobra.
d) O padrão de cores.
e) A maneira em que está se levanta para se mostrar dominante.
"""
p2 = """A estrutura do exoesqueleto dos insetos é composta por:

a) Proteínas.
b) Queratina.
c) Quitina.  
d) Osso.
e) Polissacarídeos em geral.
"""
p3 = """Qual a função dos “pelos” das conhecidas aranhas caranguejeiras?

a) Servem para manter sua temperatura corporal.
b) Tem a função de ajudar na produção de teia.
c) Define apenas o visual desta, ajudando-a a encontrar um parceiro para a reprodução.
d) Estes pelos possuem uma característica defensiva, causando irritação e sensação de queimadura à pele humana.  
e) Fazem importante papel na produção de peçonha.
"""
p4 = """A dentição humana se encaixa em qual das alternativas a seguir?

a) Carnívora.
b) Onívora. 
c) Herbívora.
d) Dentição mista.
e) Nenhuma das alternativas anteriores.
"""
p5 = """Qual dos métodos representa a característica que a cobra coral falsa usa para se “fantasiar” da verdadeira?

a) Coloração acidental.
b) Coloração por pigmentos.
c) Coloração publicitária.
d) Bioluminescência.
e) Mimetismo. 
"""
p6 = """Qual a importância da bioluminescência para os vaga-lumes?

a) Iluminação, por normalmente estar ativo à noite.
b) Defesa, criando uma imagem de algo “maior” ao seu predador.
c) Reprodução, chamando uma maior atenção de seus parceiros reprodutivos. 
d) Comunicação, pois esta característica permite a transmissão de ondas magnéticas com outros da mesma espécie.
e) Localização, possibilitando uma maior noção de espaço ao seu redor.
"""
p7 = """Aves, principalmente os patos, têm o costume de colocar o bico perto de sua cauda várias vezes quando está caminhando, porque eles fazem isso?

a) Estes animais fazem isso para se coçar, como nós também costumamos.
b) Este movimento é comum pois eles estão retirando partículas que os incomodam do corpo.
c) É uma maneira das aves se comunicarem com os seus filhotes, por isso que é comumente visto em patos/galinhas.
d) Pois eles possuem uma glândula neste lugar que produz uma espécie de muco, responsável por impermeabilizar suas penas. 
e) Porque estão se alimentando de pequenos parasitas em seus corpos, como carrapatos.
"""
p8 = """Os cachorros pertencem a qual gênero animal?

a) Canis. 
b) Cordados.
c) Felis.
d) Mamíferos.
e) Panthera.
"""
p9 = """Atualmente, nós conseguimos desenvolver uma relação de afeto com cães com naturalidade, mas porque isso é possível?

a) A espécie dos cachorros sempre existiu desde o início da humanidade, inclusive com sua característica de ser dócil e desenvolver afeto.
b) Isto foi possível pela enorme transformação genética do lobo e adaptação dos seres humanos em uma relação de interesse e benéfica para ambos os lados, que demorou cerca de 20.000 anos. 
c) Se trata de uma espécie domesticável pelas suas características puramente genéticas, que foram se desenvolvendo a partir de mutações genéticas e sendo repassadas às próximas gerações sem intervenção do ser humano.
d) Os cães são agressivos até os dias atuais, os humanos apenas aprenderam a lidar com isso para sua domesticação.
e) Nenhuma das alternativas anteriores.
"""
p10 = """Um curioso e lindo animal possui o nome específico de “lagosta-boxeadora”, porque ela é chamada assim?

a) Pela maneira em que se move.
b) Pelo formato de suas patas.
c) Pelas suas cores chamativas.
d) Pela sua capacidade de caçar suas presas com chutes.
e) Pela sua capacidade de socar seus predadores e presas com uma enorme força. 
"""
p11 = """A espécie das arraias possui uma característica muito importante para sua defesa, qual das alternativas representa essa característica?

a) A cauda, que possui um ferrão onde contém veneno. 
b) A boca, pois a sua mordida transmite o veneno por meio de seus dentes.
c) A pele, que apresenta um muco paralisante que incapacita o predador que mordê-la.
d) A pele, pois esta é altamente resistente e consegue resistir a grandes pressões.
e) A cauda, que possui uma força consideravelmente grande e que pode se comparar até a um coice de um cavalo.
"""
p12 = """Qual o único mamífero que, diferentemente de todos os outros, coloca ovo?

a) A galinha.
b) O ornitorrinco.
c) O rinoceronte.
d) O avestruz.
e) O lagarto.
"""
p13 = """As águas-vivas, quando entram em contato com a nossa pele, causa uma queimação que varia a potência de acordo com a espécie. Qual a célula responsável por esta sensação?

a) As hemácias.
b) Os estatoblastos.
c) Os cnidócitos. 
d) Os glóbulos brancos.
e) As células somáticas.
"""
p14 = """Os pavões possuem uma cauda com uma aparência extravagante e muito chamativa, qual das alternativas melhor representa a função dessa característica?

a) Reprodução, pois estes chamam mais atenção das fêmeas com as diferentes cores e padrões das suas penas.
b) Defesa, pois cria uma ilusão ao predador de imponência perante a ele, dando a impressão que o pavão cresceu de tamanho.
c) Caça, por impor medo às suas presas.
d) Reprodução e defesa, pois além de possuir lindos padrões de penas em sua cauda para chamar mais atenção de seus perceiros, também pode causar a impressão ao predador que ele “cresceu de tamanho” quando expõe suas penas. 
e) Para o voo, possibilita uma melhor aerodinâmica ao animal.
"""
p15 = """Qual dos animais a seguir é capaz de mudar de cor de acordo com o seu ambiente?

a) Iguana.
b) Lula.
c) Polvo.
d) Macaco.
e) Jacaré.
"""
# Funcionamento do programa
quiz1("-")
quiz("QUIZ SOBRE BIOLOGIA")
quiz1("-")
print("Observação: deve-se responder este quiz com as alternativas a, b, c, d ou e, de acordo com qual você acha que esteja certa.\nDigite qualquer coisa caso você queira iniciar o quiz")
input("")
while True:
    nota = 0
    listaex = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]
    for x in range(0,10,1):
        z = random.choice(listaex)
        quiz(z)
        y = input("").upper()
        if p1 in z:
            if "A" in y:
                nota += 1
            else:
                print("A resposta correta é A, pois as serpentes peçonhentas apresentam uma importante glândula produtora de peçonha entre os olhos e as narinas que normalmente são necessárias para a sobrevivência do animal.")
                print("")
                time.sleep(5)
        if p2 in z:
            if "C" in y:
                nota += 1
            else:
                print("A resposta correta é C, pois a quitina é o polissacarídeo responsável pela formação do exoesqueleto. A quitina inclusive tem o potencial de substituir o plástico futuramente, porque este é biodegradável, diferentemente do plástico, que demora cerca de 300 anos para se decompor.")
                print("")
                time.sleep(5)
        if p3 in z:
            if "D" in y:
                nota += 1
            else:
                print("A resposta correta é a D, pois as aranhas tendem a usar seus 'pelos' como defesa antes que usem sua mordida com a peçonha.")
                print("")
                time.sleep(5)
        if p4 in z:
            if "B" in y:
                nota += 1
            else:
                print("A resposta correta é a B, pois nossa arcada dentária não se encaixa em nenhuma das outras.")
                print("")
                time.sleep(5)
        if p5 in z:
            if "E" in y:
                nota += 1
            else:
                print("A resposta correta é a E. Estas cobras são facilmente confundidas com as cobras corais verdadeiras, pois sua coloração é extremamente semelhante a estas, porém isso não acontece por coincidência. Esta é uma característica que foi levada adiante justamente pela sua vantagem de se parecer com uma espécie temida na natureza.")
                print("")
                time.sleep(5)
        if p6 in z:
            if "C" in y:
                nota += 1
            else:
                print("A resposta correta é a C. Os vagalumes são insetos que facilmente notamos à noite, mas você já se perguntou qual a função desta luz que ele emite? A luz se trata de uma característica mais focada na reprodução, porém existe um estudo que indica uma possibilidade de ajudar na caça de suas presas também, o que traz um maior significado para esta luz que nós vemos.")
                print("")
                time.sleep(5)
        if p7 in z:
            if "D" in y:
                nota += 1
            else: 
                print("A resposta correta é a D. Você provavelmente ja viu um pato posicionando o seu bico perto de sua cauda. Neste lugar, ele possui uma glândula extremamente importante para este poder nadar sem sequer se molhar, pois esta produz um muco que impermeabiliza suas penas, assim permitindo este feito.")
                print("")
                time.sleep(5)
        if p8 in z:
            if "A" in y:
                nota += 1
            else:
                print("A resposta correta é a A. A classificação biológica é organizada respectivamente por dominio, reino, filo, classe, ordem, familia, genero e especie. Adentrando ao gênero, este é responsável por classificar espécies que são consideradas 'primas' e que ainda possuem capacidade de reproduzir entre si, mesmo sendo de outra espécie.")
                print("")
                time.sleep(5)
        if p9 in z:
            if "B" in y:
                nota += 1
            else: 
                print("A resposta correta é a B, pois construir uma relação com um animal silvestre sem que ambos tenham algum tipo de benefício é praticamente impossível.")
                print("")
                time.sleep(5)
        if p10 in z:
            if "E" in y:
                nota += 1
            else:
                print("A resposta correta é a E. Este curioso animal é uma espécie que possui patas parecidas com luvas de boxe, e além disso possuindo uma força considerável para tanto de defender, quanto caçar.")
                print("")
                time.sleep(5)
        if p11 in z:
            if "A" in y:
                nota += 1
            else:
                print("A resposta correta é a A. Na cauda deste animal, é possível nós percebermos a presença de uma ferrão. Este ferrão é serrilhado como um punhal, sendo assim, abrindo uma abertura à entrada do veneno desta ao organismo da vítima.")
                print("")
                time.sleep(5)
        if p12 in z:
            if "B" in y:
                nota += 1
            else:
                print("A resposta correta é B. Os ornitorrincos, por mais que sejam mamíferos, são os únicos mamíferos que botam ovo. Além disso, eles possuem a característica de serem venenosos ainda, o que é consideravelmente raro para mamíferos.")
                print("")
                time.sleep(5)
        if p13 in z:
            if "C" in y:
                nota += 1
            else:
                print("A resposta correta é a C. Os cnidoblastos ou cnidócitos são células urticantes presentes nos celenterados ou cnidários, principalmente nos tentáculos. Essa importante característica também é essencial para a caça de presas e defesa de predadores do animal.")
                print("")
                time.sleep(5)
        if p14 in z:
            if "D" in y:
                nota += 1
            else:
                print("A resposta correta é a D. Além desta característica ser importante para a reprodução, muitos animais buscam se defender 'aumentando de tamanho', pois assim os predadores ficam um pouco mais recuados em relação a se aproximarem da presa. ")
                print("")
                time.sleep(5)
        if p15 in z:
            if "C" in y:
                nota += 1
            else:
                print("A resposta correta é a C. Segundo especialistas, alguns disparos neuronais do lobo óptico dos polvos fazem com que seus cromatóforos, que são as células que contêm pigmentos, se tornem ativos durante o período de descanso. Assim, os animais mudam de cores e padrões como se estivessem acordados, reagindo a algo que sentem, por exemplo.")
                print("")
                time.sleep(5)
        listaex.remove(z)
    if nota == 10:
        print("Sua nota total foi de", nota,"pontos. Pontuação perfeita, parabéns!")    
    elif nota>=8:
        print("Sua nota total foi de", nota,"pontos. Ótimo desempenho em geral!")
    elif nota>=5:
        print("Sua nota total foi de", nota,"pontos. Uma pontuação mediana, porém sempre existe espaço para melhora!")
    else:
        print("Sua nota total foi de", nota,"pontos.")
    tentativa = input("Deseja tentar novamente? (s/n)")
    if "s" in tentativa:
        continue
    else:
        break


    



    
