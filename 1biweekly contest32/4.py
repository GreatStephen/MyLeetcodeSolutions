# "0786040670823" 11
# "238187007967311348545668518776270294758495974175895437200545054212502777027738921097754437608288484588052457687344178027991884596129831961886908909399567483236734110180243037661297058943408018237058125578539505130591117710207466348526227937963661381315807774139921194973460744218951616231689162032427029291677387359015749379583626338404782919064007175363578033937454426775212729160790052604791861224399702108312549347531874804852493291792468927454022330714445990602893248361734241243836695104077082229171994945986867993"

class Solution:
    def longestAwesome(self, s: str) -> int:
#         cum = []
        
#         for c in s:
#             res = list((cum or [[set(),set()]])[-1])
#             if c in res[0]:
#                 res[0].remove(c)
#                 res[1].add(c)
#             elif c in res[1]:
#                 res[1].remove(c)
#                 res[0].add(c)
#             else:
#                 res[1].add(c)
#             cum.append(res)
        
#         print(cum)

        @lru_cache(None)
        def tempres(i,j):
            if i==j:
                return [set(),{s[i]}]
            else:
                lastres = tempres(i, j-1)
                lastres = [set(lastres[0]), set(lastres[1])]
                if s[j] in lastres[0]:
                    lastres[0].remove(s[j])
                    lastres[1].add(s[j])
                elif s[j] in lastres[1]:
                    lastres[1].remove(s[j])
                    lastres[0].add(s[j])
                else:
                    lastres[1].add(s[j])
            return lastres
        
        
        ans = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                res = tempres(i,j)
                if j-i==10: print(res)
                if len(res[1])<=1:
                    ans = max(ans, 2*len(res[0])+len(res[1]))
        return ans

# "0570916750571583751736943052407926373575133557333309079506960246457324359395232029691777405362165161021864623857537792425676901941424404525423075736128717521783918768167795620951217044803041491676279004903722659623519377196880733573035707285267530874123716493139733140990791489524629139665706045266028626473817789830692122313261610120920850115430121705769031172576202088258411187011587549541221908817829568992978543148951046594225056061140008535734854344804847015495500369535294423195704346990484119055483604640075253998712242775726986304386702996560780081911432646776146243028360843841763613964905137253945732498199829139270276202762299713986282655095535695913682642173566550465213294251168052660112706427853855983481431046266541624306713629637017064305766270113064949775468042662078969458251246241433707735349526044178411812843292032063739331990922394363065764209203156015641354830357309904696306105420837833353476147439740995767782887239703881582095503263929075691170109044901001835673533827929318469527890754112050817722208354698743717787524897633088091982421183425424521808245832538296816948936338954546841283445480479986161857962362419745625776240290720594392485469718677139576997791561967904561229002681941195505287534175278841034869528309942529080903012946536242609900943534614298441627613677469548358055137200641299845381817816689005840741174149797473386001954280287045271653659964911082074364831568967167518027269768232248618824315504146035181127910642466412112767622787242623918331497535527297489723619204454046937915491469003601878453054259583360785390719878178676398565752407304677166946361532161249030490919307125900670612215956541992234883804307018211945389851923307259873473221518481089463972230684817995255298249805294928735921348226421785633684590656173881187729251633336622834843027963033751963163001323036982785070378857893994135005454141546948019686164556027425430989577394653067523539618745662079079839218640959780651677855486921792353269850544311920129385406065359951797417427981793887974223884165070783823085320857901020692021508489105727215305212209613161558014599619308733465555841899600305229069651096366729119037314739146878348968009164679012269318048290828531066918354490602279216969043786698352511846539922526078757265389812732734882244507261173908395444926734342573364362599006768464618589578327612626691740110518228908586496456840626687195268899675998357454465163564551113802324413509302170937094715651336884128201316350141079552380812060777658328074701868804559899427013734464740877570678185756719982621143527144668519223185793861753179291651400307984599994076660409715664545403361469660491335576829433534734260931988306523456570212506176790635794275517087747626545624204449119466881986010564704532521819054706226368952258574210027857537520623297631022752355506633622098742311342343511252547431701445670735952979414257675428227719844082257908999300215152141600310070606030086122868990726848819466974061663605064856656438828871465091082554375380782982508963513528050410116143038166547316329134701864487454327301148231029563882061395209101961843667164733097510091145939459320885364047212925895572282386273928617259540196625925184504017957107796789138205815019363974575100335856619890838321136252335839413465010598561065053471083626629766684517222997314940820996222216032737951242637827184966694284508143735592223933112497744682311754253751016474545622163003280551077413649079100204443858250893581221829570088557140883331043540367013314282322795719609945558812186775629390315201105325729336811977168669851246629630420223560385456892795306837743763984122344346425992792487207261504593806919019568796431462868127185196226416670573791777534797834054281291113055006793890596952560086062731495763562796183173668581069006931722704935451275774167867791144364173427951483297465469589218861194063117545356690303417980780731363703647615502540323067951313132872870612488345059464350640782820506527742230709260485897087713290738501821794983951010732957625300414247057242314786100674286464978508293923906191158481432616967722986852980148772421383415806094017607060309601107595677023914041406517717481383504312183185703558108061972771764790235219765307872813744212398248978097064350259928535556074127437467680123889372497499882142425747352656245982674131300680329318707180896693592980440161754252129289041418067958925352156578984524649350524067433746465977510827839761320679444943975021413659771574965020516443215530621057079099152383671494895037102452146174133708801409921388527198524851738094288882039379594443484415627159222185861681813002034442823458593870215954312903331573625155416459110453556990902688313930454176743632636552151985394500173557152993531937363509111658575345506231122366853292918812412913074596479746300366667070727218590642581048355630707732386369773214175340558251409757093696185398006012830919156360240869590823266631310830108253919861365746967589725351117137052083134602939372378732254870799338834129949410129233545125209074637557463756312116488904095742637509550495583644174287311000617541975134962709994555132174705882451811629896248212576625632192732469176536026547802700928311023880886271206188563244160094804502455738743342451386081623261881045571548746666617060896123374069880529672725629558657793251171278137938084939084786045146220209313674008297282012411757523826896295927244841781319511245120765109370909266672911972969937024170865974491380845995576710005174458416616039426067363573138319545575624266237937174956151401362179168198725172654129565715581826485652114463844727350936000962980144434395887973686002916049164055667559487683937054713682105714053356597809131610457471343043616507029673840167909680325957399296753054090587458856499277210542032243266682861797444781568991589435390465394755439599231761669068139271830201940732069972509752052091032119610752465118501077574663747563868064458000397611989729570069315099024316152078490602295234760102684104350783962600739051834081930408511959746446119012351857944959824327059179683140490403598592049717944090819733721651929235669597593695654859993768278017944496605054690111236495983179778121472352499186823419502732075320210755321824335649758688984714232790361490149570188281604222110512392999566680544014478899612291943898960120597207109961788131840977505193201912030366002789569033700306925667560731753615588831115466899082047028480612758503826230629024398818013314322647685615392785286924724997917948346493300694790873131422979311230171080522351006547364491506395418473802177963438567788167720306668633909622826048356781173345508948910471953177820322883114794763199252876236917400318281944704664959459811901194530914718854655059717191269454563307756752229183271493530251997347717044354275139037290815922370185127119050942557976570351532527262109583621282244938238973770034938644310672187039603932603548407934786121651165838375059976109659792754307186188221603404969585535706975405453426105329465789303910852761340893174189060250883155245869222075073150973578245345857545313189761951522778530418823365437268651338171762040992268784344691207924854668611173230227801733170266212112651489160540785947559650500547551477310868810910734830841337727701508126930638551378080962382676346271307063362162796666715662972796448022031725550018582416516822761179648514358723894554618668317412523412969844246790012301756598796245114314143162656819943797362571109855"                 
                    